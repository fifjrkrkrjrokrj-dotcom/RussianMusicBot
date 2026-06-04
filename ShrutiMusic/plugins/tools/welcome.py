import os
from unidecode import unidecode
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import enums, filters
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, Message
from logging import getLogger
from ShrutiMusic import LOGGER
from ShrutiMusic.misc import SUDOERS
from ShrutiMusic import app
from ShrutiMusic.utils.database import welcomedb
from config import styled_button

LOGGER = getLogger(__name__)

# Create downloads folder if missing
os.makedirs("downloads", exist_ok=True)

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None

def circle(pfp, size=(450, 450)):
    # Use compatible resampling filter
    try:
        resample = Image.Resampling.LANCZOS
    except AttributeError:
        resample = Image.LANCZOS
    pfp = pfp.resize(size, resample).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, resample)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chat, uid, uname):
    background = Image.open("ShrutiMusic/assets/welcome.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize((450, 450))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('ShrutiMusic/assets/font.ttf', size=45)
    font2 = ImageFont.truetype('ShrutiMusic/assets/font.ttf', size=90)  # kept but unused
    draw.text((65, 250), f'NAME : {unidecode(user)}', fill="white", font=font)
    draw.text((65, 340), f'ID : {uid}', fill="white", font=font)
    draw.text((65, 430), f"USERNAME : {uname if uname else 'Not set'}", fill="white", font=font)
    pfp_position = (767, 133)
    background.paste(pfp, pfp_position, pfp)
    out_path = f"downloads/welcome#{uid}.png"
    background.save(out_path)
    return out_path

@app.on_message(filters.command("welcome") & ~filters.private)
async def auto_state(_, message):
    usage = "<b>❖ ᴜsᴀɢᴇ ➥</b> /welcome [on|off]"
    if len(message.command) == 1:
        return await message.reply_text(usage, parse_mode=enums.ParseMode.HTML)

    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)

    if user.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
        A = await welcomedb.find_one({"chat_id": chat_id})
        state = message.text.split(None, 1)[1].strip().lower()

        if state == "on":
            if A and not A.get("disabled", False):
                return await message.reply_text("✦ Special Welcome Already Enabled", parse_mode=enums.ParseMode.HTML)
            await welcomedb.update_one({"chat_id": chat_id}, {"$set": {"disabled": False}}, upsert=True)
            await message.reply_text(f"✦ Enabled Special Welcome in {message.chat.title}", parse_mode=enums.ParseMode.HTML)

        elif state == "off":
            if A and A.get("disabled", False):
                return await message.reply_text("✦ Special Welcome Already Disabled", parse_mode=enums.ParseMode.HTML)
            await welcomedb.update_one({"chat_id": chat_id}, {"$set": {"disabled": True}}, upsert=True)
            await message.reply_text(f"✦ Disabled Special Welcome in {message.chat.title}", parse_mode=enums.ParseMode.HTML)

        else:
            await message.reply_text(usage, parse_mode=enums.ParseMode.HTML)
    else:
        await message.reply("✦ Only Admins Can Use This Command", parse_mode=enums.ParseMode.HTML)

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    A = await welcomedb.find_one({"chat_id": chat_id})

    if A and A.get("disabled", False):
        return

    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return

    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        pic = await app.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except AttributeError:
        pic = "ShrutiMusic/assets/upic.png"

    # Delete previous welcome message for this chat
    old_msg_key = f"welcome-{member.chat.id}"
    if temp.MELCOW.get(old_msg_key) is not None:
        try:
            await temp.MELCOW[old_msg_key].delete()
        except Exception as e:
            LOGGER.error(e)

    try:
        username_display = user.username if user.username else "ɴᴏᴛ sᴇᴛ"
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, username_display
        )

        caption = f"""
<blockquote>🌟 <b>ᴡᴇʟᴄᴏᴍᴇ {user.mention}!</b></blockquote>

<blockquote>
📋 <b>ɢʀᴏᴜᴘ:</b> {member.chat.title}
🆔 <b>ʏᴏᴜʀ ɪᴅ:</b> <code>{user.id}</code>
👤 <b>ᴜsᴇʀɴᴀᴍᴇ:</b> @{username_display}
</blockquote>

<blockquote>
✨ ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴊᴏɪɴɪɴɢ <b>{member.chat.title}</b>!
🤝 ᴍᴀᴋᴇ ɴᴇᴡ ғʀɪᴇɴᴅs, ᴄʜᴀᴛ ᴡɪᴛʜ ᴏᴛʜᴇʀs, ᴀɴᴅ ᴇɴᴊᴏʏ ᴛʜᴇ ᴄᴏᴍᴍᴜɴɪᴛʏ.
</blockquote>

<blockquote>
📢 <b>ᴅᴏɴ'ᴛ ғᴏʀɢᴇᴛ ᴛᴏ ᴊᴏɪɴ @XTR_Net</b>

<blockquote>
💎 ʀᴇsᴘᴇᴄᴛ ᴛʜᴇ ʀᴜʟᴇs • sᴛᴀʏ ᴀᴄᴛɪᴠᴇ • ʜᴀᴠᴇ ғᴜɴ ❤️
</blockquote>
</blockquote>
"""

        reply_markup = InlineKeyboardMarkup([
            [styled_button("🎵 ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🎵", url=f"https://t.me/{app.username}?startgroup=True", style=enums.ButtonStyle.PRIMARY)],
            [styled_button("⟪ #𝗫𝗧𝗥 ⟫ 𝗡𝗘𝗧", url="https://t.me/xtrchannel", style=enums.ButtonStyle.SECONDARY),
             styled_button("⟪#𝗫𝗧𝗥⟫ 𝗕𝗢𝗧𝗦", url="https://t.me/XTRBots", style=enums.ButtonStyle.SECONDARY)]
        ])

        sent_msg = await app.send_photo(
            member.chat.id,
            photo=welcomeimg,
            caption=caption,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        temp.MELCOW[old_msg_key] = sent_msg

    except Exception as e:
        LOGGER.error(f"Failed to send welcome: {e}")

    # Cleanup files
    try:
        os.remove(f"downloads/welcome#{user.id}.png")
        os.remove(f"downloads/pp{user.id}.png")
    except Exception:
        pass
