import asyncio
import importlib

from pyrogram import idle
from pyrogram.types import BotCommand
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS

from VillainMusic import LOGGER, app, userbot
from VillainMusic.core.call import Nand
from VillainMusic.misc import sudo
from VillainMusic.plugins import ALL_MODULES
from VillainMusic.utils.database import (
    get_banned_users,
    get_gbanned,
)

COMMANDS = [
    BotCommand("start", "❖ sᴛᴀʀᴛ ʙᴏᴛ • ᴛᴏ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ"),
    BotCommand("help", "❖ ʜᴇʟᴘ ᴍᴇɴᴜ • ɢᴇᴛ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs"),
    BotCommand("ping", "❖ ᴘɪɴɢ ʙᴏᴛ • ᴄʜᴇᴄᴋ ᴘɪɴɢ"),
    BotCommand("play", "❖ ᴘʟᴀʏ ᴀᴜᴅɪᴏ ɪɴ ᴠᴄ"),
    BotCommand("vplay", "❖ ᴘʟᴀʏ ᴠɪᴅᴇᴏ ɪɴ ᴠᴄ"),
    BotCommand("pause", "❖ ᴘᴀᴜsᴇ sᴛʀᴇᴀᴍ"),
    BotCommand("resume", "❖ ʀᴇsᴜᴍᴇ sᴛʀᴇᴀᴍ"),
    BotCommand("skip", "❖ sᴋɪᴘ ᴛʀᴀᴄᴋ"),
    BotCommand("stop", "❖ sᴛᴏᴘ sᴛʀᴇᴀᴍ"),
    BotCommand("queue", "❖ sʜᴏᴡ ᴏ̨ᴜᴇᴜᴇ"),
    BotCommand("song", "❖ ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ"),
    BotCommand("tagall", "❖ ᴛᴀɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs"),
]


async def setup_bot_commands():
    try:
        await app.set_bot_commands(COMMANDS)
        LOGGER("VillainMusic").info(
            "Bot commands set successfully!"
        )

    except Exception as e:
        LOGGER("VillainMusic").error(
            f"Failed to set bot commands: {e}"
        )


async def init():

    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "Assistant client variables not defined."
        )
        return

    await sudo()

    try:
        users = await get_gbanned()

        for user_id in users:
            BANNED_USERS.add(user_id)

        users = await get_banned_users()

        for user_id in users:
            BANNED_USERS.add(user_id)

    except Exception as e:
        LOGGER("VillainMusic").error(
            f"Banned user load error: {e}"
        )

    await app.start()

    LOGGER("VillainMusic").info(
        "Bot Started Successfully!"
    )

    await setup_bot_commands()

    # Import Plugins Fix
    for all_module in ALL_MODULES:

        try:
            all_module = (
                all_module
                .replace("\\", ".")
                .replace("/", ".")
            )

            if not all_module.startswith("."):
                all_module = "." + all_module

            importlib.import_module(
                "VillainMusic.plugins" + all_module
            )

            LOGGER("VillainMusic.plugins").info(
                f"Imported => {all_module}"
            )

        except Exception as e:

            LOGGER("VillainMusic.plugins").error(
                f"Failed To Import {all_module} : {e}"
            )

    LOGGER("VillainMusic.plugins").info(
        "All Modules Imported!"
    )

    await userbot.start()

    LOGGER("VillainMusic").info(
        "Assistant Started!"
    )

    await Nand.start()

    LOGGER("VillainMusic").info(
        "Voice Client Started!"
    )

    try:
        await Nand.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )

    except NoActiveGroupCall:

        LOGGER("VillainMusic").error(
            "Turn on VC in LOG_GROUP_ID"
        )

    except Exception as e:

        LOGGER("VillainMusic").error(
            f"VC Error : {e}"
        )

    try:
        await Nand.decorators()

    except Exception as e:

        LOGGER("VillainMusic").error(
            f"Decorator Error : {e}"
        )

    LOGGER("VillainMusic").info(
        "Villain Music Started Successfully!"
    )

    await idle()

    await app.stop()
    await userbot.stop()

    LOGGER("VillainMusic").info(
        "Stopping Villain Music Bot..."
    )


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())