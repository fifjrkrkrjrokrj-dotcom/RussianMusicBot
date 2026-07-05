from pyrogram import filters
from pyrogram import enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from VillainMusic import app
from VillainMusic.utils.database import get_lang, set_lang
from VillainMusic.utils.decorators import ActualAdminCB, language, languageCB
from config import BANNED_USERS
from strings import get_string, languages_present

from config import styled_button

def lanuages_keyboard(_):
    buttons = []
    temp = []
    for i in languages_present:
        temp.append(
            styled_button(
                text=languages_present[i],
                callback_data=f"languages:{i}",
                style=enums.ButtonStyle.PRIMARY,
            )
        )
        if len(temp) == 2:
            buttons.append(temp)
            temp = []
    if temp:
        buttons.append(temp)
        
    buttons.append(
        [
            styled_button(
                text=_["BACK_BUTTON"],
                callback_data=f"settingsback_helper",
                style=enums.ButtonStyle.PRIMARY,
            ),
            styled_button(
                text=_["CLOSE_BUTTON"],
                callback_data=f"close",
                style=enums.ButtonStyle.DANGER
            ),
        ]
    )
    return InlineKeyboardMarkup(buttons)

@app.on_message(filters.command(["lang", "setlang", "language"]) & ~BANNED_USERS)
@language
async def langs_command(client, message: Message, _):
    keyboard = lanuages_keyboard(_)
    await message.reply_text(
        _["lang_1"],
        reply_markup=keyboard,
    )

@app.on_callback_query(filters.regex("LG") & ~BANNED_USERS)
@languageCB
async def lanuagecb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)

@app.on_callback_query(filters.regex(r"languages:(.*?)") & ~BANNED_USERS)
@ActualAdminCB
async def language_markup(client, CallbackQuery, _):
    langauge = (CallbackQuery.data).split(":")[1]
    old = await get_lang(CallbackQuery.message.chat.id)
    if str(old) == str(langauge):
        return await CallbackQuery.answer(_["lang_4"], show_alert=True)
    try:
        _ = get_string(langauge)
        await CallbackQuery.answer(_["lang_2"], show_alert=True)
    except:
        _ = get_string(old)
        return await CallbackQuery.answer(
            _["lang_3"],
            show_alert=True,
        )
    await set_lang(CallbackQuery.message.chat.id, langauge)
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)
