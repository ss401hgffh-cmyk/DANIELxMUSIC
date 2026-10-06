# Saya Music
from typing import Union

from pyrogram.types import InlineKeyboardButton


def setting_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text="Auth Users", callback_data="AUTH_SETTINGS"),
            InlineKeyboardButton(text="Language", callback_data="LANGUAGE_SETTINGS"),
        ],
        [
            InlineKeyboardButton(text="Play Mode", callback_data="PLAYBACK_SETTINGS"),
        ],
        [
            InlineKeyboardButton(text="Voting Mode", callback_data="VOTE_SETTINGS"),
        ],
        [
            InlineKeyboardButton(text="Close", callback_data="close"),
        ],
    ]
    return buttons


def vote_mode_markup(_, current, mode: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(text="Voting Mode", callback_data="VOTE_MODE_INFO"),
            InlineKeyboardButton(
                text="ON" if mode == True else "OFF",
                callback_data="TOGGLE_VOTE_MODE",
            ),
        ],
        [
            InlineKeyboardButton(text="-2", callback_data="DECREASE_VOTE_COUNT"),
            InlineKeyboardButton(
                text=f"Current: {current}",
                callback_data="CURRENT_VOTE_INFO",
            ),
            InlineKeyboardButton(text="+2", callback_data="INCREASE_VOTE_COUNT"),
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="SETTINGS_BACK",
            ),
            InlineKeyboardButton(text="Close", callback_data="close"),
        ],
    ]
    return buttons


def auth_users_markup(_, status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(text="Auth Users", callback_data="AUTH_USERS_INFO"),
            InlineKeyboardButton(
                text="Admins" if status == True else "Everyone",
                callback_data="TOGGLE_AUTH_MODE",
            ),
        ],
        [
            InlineKeyboardButton(text="View List", callback_data="VIEW_AUTH_USERS"),
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="SETTINGS_BACK",
            ),
            InlineKeyboardButton(text="Close", callback_data="close"),
        ],
    ]
    return buttons


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(text="Search Mode", callback_data="SEARCH_MODE_INFO"),
            InlineKeyboardButton(
                text="Direct" if Direct == True else "Inline",
                callback_data="TOGGLE_SEARCH_MODE",
            ),
        ],
        [
            InlineKeyboardButton(text="Admin Commands", callback_data="CHANNEL_MODE_INFO"),
            InlineKeyboardButton(
                text="Admins" if Group == True else "Everyone",
                callback_data="TOGGLE_CHANNEL_MODE",
            ),
        ],
        [
            InlineKeyboardButton(text="Play Type", callback_data="PLAY_TYPE_INFO"),
            InlineKeyboardButton(
                text="Admins" if Playtype == True else "Everyone",
                callback_data="TOGGLE_PLAY_TYPE",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="SETTINGS_BACK",
            ),
            InlineKeyboardButton(text="Close", callback_data="close"),
        ],
    ]
    return buttons
