"""
░█▀█░█▀▄░█▀█░█▀█░█▀▄░▀█▀░█▀▀░▀█▀░█▀█░█▀▄░█░█░░░█░░░▀█▀░█▀▀░█▀▀░█▀█░█▀▀░█▀▀
░█▀▀░█▀▄░█░█░█▀▀░█▀▄░░█░░█▀▀░░█░░█▀█░█▀▄░░█░░░░█░░░░█░░█░░░█▀▀░█░█░▀▀█░█▀▀
░▀░░░▀░▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀▀▀░░▀░░▀░▀░▀░▀░░▀░░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀

Copyright (c) 2025 Nand Yaduwanshi (@NoxxOP)
Location: Supaul, Bihar
Email: badboy809075@gmail.com
GitHub: https://github.com/NoxxOP

All rights reserved.

This code is the intellectual property of Nand Yaduwanshi.
You are not allowed to copy, modify, redistribute, or use this
code for commercial or personal projects without explicit permission.

Allowed:
- Forking for personal learning
- Submitting improvements via pull requests

Not Allowed:
- Claiming this code as your own
- Re-uploading without credit or permission
- Selling or using commercially

Love From VillainBots
Telegram: https://t.me/VillainBots
"""

from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VillainMusic import app

from config import styled_button

from pyrogram import enums
def help_pannel_page1(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                styled_button(text=_["H_B_1"], callback_data="help_callback hb1", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_2"], callback_data="help_callback hb2", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text=_["H_B_3"], callback_data="help_callback hb3", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_4"], callback_data="help_callback hb4", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text=_["H_B_5"], callback_data="help_callback hb5", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_6"], callback_data="help_callback hb6", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_7"], callback_data="help_callback hb7", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text=_["H_B_8"], callback_data="help_callback hb8", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_9"], callback_data="help_callback hb9", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_10"], callback_data="help_callback hb10", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text="⏮", callback_data="help_page_4", style=enums.ButtonStyle.PRIMARY),
                styled_button(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                    style=enums.ButtonStyle.PRIMARY if START else enums.ButtonStyle.DANGER,
                ),
                styled_button(text="⏭", callback_data="help_page_2", style=enums.ButtonStyle.PRIMARY),
            ],
        ]
    )

def help_pannel_page2(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                styled_button(text=_["H_B_11"], callback_data="help_callback hb11", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_12"], callback_data="help_callback hb12", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text=_["H_B_13"], callback_data="help_callback hb13", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_14"], callback_data="help_callback hb14", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text=_["H_B_15"], callback_data="help_callback hb15", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_16"], callback_data="help_callback hb16", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_17"], callback_data="help_callback hb17", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text=_["H_B_18"], callback_data="help_callback hb18", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_19"], callback_data="help_callback hb19", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_20"], callback_data="help_callback hb20", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text="⏮", callback_data="help_page_1", style=enums.ButtonStyle.PRIMARY),
                styled_button(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                    style=enums.ButtonStyle.PRIMARY if START else enums.ButtonStyle.DANGER,
                ),
                styled_button(text="⏭", callback_data="help_page_3", style=enums.ButtonStyle.PRIMARY),
            ],
        ]
    )

def help_pannel_page3(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                styled_button(text=_["H_B_21"], callback_data="help_callback hb21", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_22"], callback_data="help_callback hb22", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text=_["H_B_23"], callback_data="help_callback hb23", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_24"], callback_data="help_callback hb24", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text=_["H_B_25"], callback_data="help_callback hb25", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_26"], callback_data="help_callback hb26", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_27"], callback_data="help_callback hb27", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text=_["H_B_28"], callback_data="help_callback hb28", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_29"], callback_data="help_callback hb29", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_30"], callback_data="help_callback hb30", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text="⏮", callback_data="help_page_2", style=enums.ButtonStyle.PRIMARY),
                styled_button(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                    style=enums.ButtonStyle.PRIMARY if START else enums.ButtonStyle.DANGER,
                ),
                styled_button(text="⏭", callback_data="help_page_4", style=enums.ButtonStyle.PRIMARY),
            ],
        ]
    )

def help_pannel_page4(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                styled_button(text=_["H_B_31"], callback_data="help_callback hb31", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_32"], callback_data="help_callback hb32", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text=_["H_B_33"], callback_data="help_callback hb33", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_34"], callback_data="help_callback hb34", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text=_["H_B_35"], callback_data="help_callback hb35", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_37"], callback_data="help_callback hb37", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text=_["H_B_38"], callback_data="help_callback hb38", style=enums.ButtonStyle.PRIMARY),
                styled_button(text=_["H_B_39"], callback_data="help_callback hb39", style=enums.ButtonStyle.PRIMARY),
            ],
            [
                styled_button(text=_["H_B_36"], callback_data="help_callback hb36", style=enums.ButtonStyle.PRIMARY),
            ],   
            [
                styled_button(text="⏮", callback_data="help_page_3", style=enums.ButtonStyle.PRIMARY),
                styled_button(
                    text=_["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                    style=enums.ButtonStyle.PRIMARY if START else enums.ButtonStyle.DANGER,
                ),
                styled_button(text="⏭", callback_data="help_page_1", style=enums.ButtonStyle.PRIMARY),
            ],
        ]
    )

def help_back_markup(_, page: int = 1):
    return InlineKeyboardMarkup(
        [
            [
                styled_button(
                    text=_["BACK_BUTTON"],
                    callback_data=f"help_page_{page}",
                    style=enums.ButtonStyle.PRIMARY,
                )
            ]
        ]
    )


def private_help_panel(_):
    return [
        [
            styled_button(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
                style=enums.ButtonStyle.PRIMARY,
            ),
        ]
    ]
