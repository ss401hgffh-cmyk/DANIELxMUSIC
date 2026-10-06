# Saya Music
from pyrogram.types import InlineKeyboardButton

import config
from SayaMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Add me to your group",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Help",
                callback_data="open_help",
            )
        ],
        [
            InlineKeyboardButton(text="Support", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="Channel", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="Source", url=config.UPSTREAM_REPO),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Add me to your group",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Help",
                callback_data="open_help",
            )
        ],
        [
            InlineKeyboardButton(text="Support", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="Channel", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="Source", url=config.UPSTREAM_REPO),
        ],
    ]
    return buttons
