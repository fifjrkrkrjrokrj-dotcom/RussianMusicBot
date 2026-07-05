import time
import os
import requests
import asyncio

from pyrogram import filters, enums
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from py_yt import VideosSearch
import config
from VillainMusic import app
from VillainMusic.misc import _boot_
from VillainMusic.plugins.sudo.sudoers import sudoers_list
from VillainMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from VillainMusic.utils import bot_sys_stats
from VillainMusic.utils.decorators.language import LanguageStart
from VillainMusic.utils.formatters import get_readable_time
from VillainMusic.utils.inline import help_pannel_page1, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string

def download_video_sync(url, path):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        r = requests.get(url, headers=headers, stream=True, timeout=60)
        if r.status_code == 200:
            with open(path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
    except Exception as e:
        print(f"Error downloading start video: {e}")
    return False

START_VIDEO_FILE_ID = None
START_PHOTO_FILE_ID = None
DEFAULT_PHOTO = "https://files.catbox.moe/4v1tel.jpg"

@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    global START_VIDEO_FILE_ID, START_PHOTO_FILE_ID
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel_page1(_)
            try:
                return await message.reply_photo(
                    photo=DEFAULT_PHOTO,
                    caption=_["help_1"].format(config.SUPPORT_GROUP),
                    reply_markup=keyboard,
                    message_effect_id=5159385139981059251,
                )
            except:
                try:
                    return await message.reply_photo(
                        photo=DEFAULT_PHOTO,
                        caption=_["help_1"].format(config.SUPPORT_GROUP),
                        reply_markup=keyboard,
                    )
                except:
                    return await message.reply_text(
                        text=_["help_1"].format(config.SUPPORT_GROUP),
                        reply_markup=keyboard,
                        disable_web_page_preview=True,
                    )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOG_GROUP_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        styled_button(text=_["S_B_8"], url=link, style=enums.ButtonStyle.PRIMARY),
                        styled_button(text=_["S_B_9"], url=config.SUPPORT_GROUP, style=enums.ButtonStyle.PRIMARY),
                    ],
                ]
            )
            await m.delete()
            try:
                await app.send_photo(
                    chat_id=message.chat.id,
                    photo=thumbnail,
                    caption=searched_text,
                    reply_markup=key,
                    message_effect_id=5159385139981059251,
                )
            except:
                await app.send_photo(
                    chat_id=message.chat.id,
                    photo=thumbnail,
                    caption=searched_text,
                    reply_markup=key,
                )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOG_GROUP_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
        if name == "start":
            out = private_panel(_)
            UP, CPU, RAM, DISK = await bot_sys_stats()
            is_video = config.START_IMG_URL.endswith((".mp4", ".mkv", ".webm", ".mov", ".gif"))
            if is_video:
                local_video = "cache/start_video.mp4"
                if not os.path.exists("cache"):
                    os.makedirs("cache")
                if not START_VIDEO_FILE_ID and not os.path.exists(local_video):
                    await asyncio.to_thread(download_video_sync, config.START_IMG_URL, local_video)
                
                video_to_send = START_VIDEO_FILE_ID or (local_video if os.path.exists(local_video) else config.START_IMG_URL)
                try:
                    sent = await message.reply_video(
                        video=video_to_send,
                        caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM, message.from_user.username or "None"),
                        reply_markup=InlineKeyboardMarkup(out),
                        message_effect_id=5159385139981059251,
                        supports_streaming=True,
                    )
                    if sent and sent.video and not START_VIDEO_FILE_ID:
                        START_VIDEO_FILE_ID = sent.video.file_id
                except:
                    try:
                        sent = await message.reply_video(
                            video=video_to_send,
                            caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM, message.from_user.username or "None"),
                            reply_markup=InlineKeyboardMarkup(out),
                            supports_streaming=True,
                        )
                        if sent and sent.video and not START_VIDEO_FILE_ID:
                            START_VIDEO_FILE_ID = sent.video.file_id
                    except:
                        await message.reply_text(
                            text=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM, message.from_user.username or "None"),
                            reply_markup=InlineKeyboardMarkup(out),
                        )
            else:
                try:
                    sent = await message.reply_photo(
                        photo=START_PHOTO_FILE_ID or config.START_IMG_URL,
                        caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM, message.from_user.username or "None"),
                        reply_markup=InlineKeyboardMarkup(out),
                        message_effect_id=5159385139981059251,
                    )
                    if sent and sent.photo and not START_PHOTO_FILE_ID:
                        START_PHOTO_FILE_ID = sent.photo.file_id
                except:
                    try:
                        sent = await message.reply_photo(
                            photo=START_PHOTO_FILE_ID or config.START_IMG_URL,
                            caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM, message.from_user.username or "None"),
                            reply_markup=InlineKeyboardMarkup(out),
                        )
                        if sent and sent.photo and not START_PHOTO_FILE_ID:
                            START_PHOTO_FILE_ID = sent.photo.file_id
                    except:
                        await message.reply_text(
                            text=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM, message.from_user.username or "None"),
                            reply_markup=InlineKeyboardMarkup(out),
                        )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOG_GROUP_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
    else:
        out = private_panel(_)
        UP, CPU, RAM, DISK = await bot_sys_stats()
        is_video = config.START_IMG_URL.endswith((".mp4", ".mkv", ".webm", ".mov", ".gif"))
        if is_video:
            local_video = "cache/start_video.mp4"
            if not os.path.exists("cache"):
                os.makedirs("cache")
            if not START_VIDEO_FILE_ID and not os.path.exists(local_video):
                await asyncio.to_thread(download_video_sync, config.START_IMG_URL, local_video)
            
            video_to_send = START_VIDEO_FILE_ID or (local_video if os.path.exists(local_video) else config.START_IMG_URL)
            try:
                sent = await message.reply_video(
                    video=video_to_send,
                    caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM, message.from_user.username or "None"),
                    reply_markup=InlineKeyboardMarkup(out),
                    message_effect_id=5159385139981059251,
                    supports_streaming=True,
                )
                if sent and sent.video and not START_VIDEO_FILE_ID:
                    START_VIDEO_FILE_ID = sent.video.file_id
            except:
                try:
                    sent = await message.reply_video(
                        video=video_to_send,
                        caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM, message.from_user.username or "None"),
                        reply_markup=InlineKeyboardMarkup(out),
                        supports_streaming=True,
                    )
                    if sent and sent.video and not START_VIDEO_FILE_ID:
                        START_VIDEO_FILE_ID = sent.video.file_id
                except:
                    await message.reply_text(
                        text=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM, message.from_user.username or "None"),
                        reply_markup=InlineKeyboardMarkup(out),
                    )
        else:
            try:
                sent = await message.reply_photo(
                    photo=START_PHOTO_FILE_ID or config.START_IMG_URL,
                    caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM, message.from_user.username or "None"),
                    reply_markup=InlineKeyboardMarkup(out),
                    message_effect_id=5159385139981059251,
                )
                if sent and sent.photo and not START_PHOTO_FILE_ID:
                    START_PHOTO_FILE_ID = sent.photo.file_id
            except:
                try:
                    sent = await message.reply_photo(
                        photo=START_PHOTO_FILE_ID or config.START_IMG_URL,
                        caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM, message.from_user.username or "None"),
                        reply_markup=InlineKeyboardMarkup(out),
                    )
                    if sent and sent.photo and not START_PHOTO_FILE_ID:
                        START_PHOTO_FILE_ID = sent.photo.file_id
                except:
                    await message.reply_text(
                        text=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM, message.from_user.username or "None"),
                        reply_markup=InlineKeyboardMarkup(out),
                    )
        if await is_on_off(2):
            await app.send_message(
                chat_id=config.LOG_GROUP_ID,
                text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
            )

@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    try:
        await message.reply_photo(
            photo=DEFAULT_PHOTO,
            caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
            reply_markup=InlineKeyboardMarkup(out),
            message_effect_id=5159385139981059251,
        )
    except:
        try:
            await message.reply_photo(
                photo=DEFAULT_PHOTO,
                caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
                reply_markup=InlineKeyboardMarkup(out),
            )
        except:
            await message.reply_text(
                text=_["start_1"].format(app.mention, get_readable_time(uptime)),
                reply_markup=InlineKeyboardMarkup(out),
            )
    return await add_served_chat(message.chat.id)

@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_GROUP,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                try:
                    await message.reply_photo(
                        photo=DEFAULT_PHOTO,
                        caption=_["start_3"].format(
                            message.from_user.first_name,
                            app.mention,
                            message.chat.title,
                            app.mention,
                        ),
                        reply_markup=InlineKeyboardMarkup(out),
                        message_effect_id=5159385139981059251,
                    )
                except:
                    try:
                        await message.reply_photo(
                            photo=DEFAULT_PHOTO,
                            caption=_["start_3"].format(
                                message.from_user.first_name,
                                app.mention,
                                message.chat.title,
                                app.mention,
                            ),
                            reply_markup=InlineKeyboardMarkup(out),
                        )
                    except:
                        await message.reply_text(
                            text=_["start_3"].format(
                                message.from_user.first_name,
                                app.mention,
                                message.chat.title,
                                app.mention,
                            ),
                            reply_markup=InlineKeyboardMarkup(out),
                        )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
