# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com

from pyrogram.types import InlineKeyboardButton
import config
from VillainMusic import app

from config import styled_button

from pyrogram import enums
def start_panel(_):
    buttons = [
        [
            styled_button(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true",
                style=enums.ButtonStyle.SUCCESS,
            ),
            styled_button(text=_["S_B_2"], url=config.SUPPORT_GROUP, style=enums.ButtonStyle.SUCCESS),
        ],
        [
            styled_button(text=_["S_B_11"], callback_data="about_page", style=enums.ButtonStyle.PRIMARY)  # About button
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            styled_button(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=enums.ButtonStyle.SUCCESS,
            )
        ],
        [
            styled_button(
                text=_["S_B_11"],
                callback_data="about_page",
                style=enums.ButtonStyle.PRIMARY,
            ),
            styled_button(
                text=_["S_B_12"],
                callback_data="owner_page",
                style=enums.ButtonStyle.PRIMARY,
            )
        ],
        [
            styled_button(
                text=_["E_X_1"],
                callback_data="fork_repo",
                style=enums.ButtonStyle.PRIMARY,
            ),
            styled_button(text=_["S_B_5"], url=f"https://t.me/{config.OWNER_USERNAME}" if config.OWNER_USERNAME else f"tg://openmessage?user_id={config.OWNER_ID}", style=enums.ButtonStyle.PRIMARY),
        ],
        [
            styled_button(text=_["S_B_4"], callback_data="help_page_1", style=enums.ButtonStyle.PRIMARY)
        ],
    ]
    return buttons

def about_panel(_):
    buttons = [
        [
            styled_button(text=_["S_B_6"], url=config.SUPPORT_CHANNEL, style=enums.ButtonStyle.PRIMARY),
            styled_button(text=_["S_B_2"], url=config.SUPPORT_GROUP, style=enums.ButtonStyle.SUCCESS),
        ],
        [
            styled_button(text="🎁 Blaze giveaway 🎁", url=config.BLAZE_GIVEAWAY, style=enums.ButtonStyle.PRIMARY),
        ],
        [
            styled_button(text=_["BACK_BUTTON"], callback_data="settingsback_helper", style=enums.ButtonStyle.PRIMARY)
        ]
    ]
    return buttons

def owner_panel(_):
    buttons = [
        [
            styled_button(text=_["S_H_1"], url=config.INSTAGRAM, style=enums.ButtonStyle.PRIMARY),
            styled_button(text=_["S_H_2"], url=config.YOUTUBE, style=enums.ButtonStyle.PRIMARY),
        ],
        [
            styled_button(text=_["S_H_3"], url=config.GITHUB, style=enums.ButtonStyle.PRIMARY),
            styled_button(text=_["S_H_4"], url=config.DONATE, style=enums.ButtonStyle.PRIMARY),
        ],
        [
            styled_button(text=_["BACK_BUTTON"], callback_data="settingsback_helper", style=enums.ButtonStyle.PRIMARY)
        ]
    ]
    return buttons


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/VillainMusic
# 📢 Telegram Channel : https://t.me/VillainBots
# ===========================================


# ❤️ Love From VillainBots 
