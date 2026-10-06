# Saya Music
from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            InlineKeyboardButton(
                text="Queue List",
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text="Close",
                callback_data="close",
            ),
        ]
    ]
    dur = [
        [
            InlineKeyboardButton(
                text=f"{played} / {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="Queue List",
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text="Close",
                callback_data="close",
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Back",
                    callback_data=f"queue_back_timer {CPLAY}",
                ),
                InlineKeyboardButton(
                    text="Close",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl


def aq_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="Resume", callback_data=f"stream_admin Resume|{chat_id}"),
            InlineKeyboardButton(text="Pause", callback_data=f"stream_admin Pause|{chat_id}"),
            InlineKeyboardButton(text="Skip", callback_data=f"stream_admin Skip|{chat_id}"),
            InlineKeyboardButton(text="Stop", callback_data=f"stream_admin Stop|{chat_id}"),
        ],
        [InlineKeyboardButton(text="Close", callback_data="close")],
    ]
    return buttons
