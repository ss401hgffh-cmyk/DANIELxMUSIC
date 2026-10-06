# Saya Music
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SayaMusic import app


TOTAL_SECTIONS = 29

HELP_LABELS = {
    1: "Action",
    2: "Admin",
    3: "Auth",
    4: "Blacklist Chat",
    5: "Blacklist User",
    6: "Channel Play",
    7: "Extra",
    8: "Global Ban",
    9: "Broadcast",
    10: "Games",
    11: "ChatGPT",
    12: "Info",
    13: "Image",
    14: "Logs",
    15: "Loop",
    16: "Group",
    17: "Masti",
    18: "Mass Actions",
    19: "Ping",
    20: "Play",
    21: "Repo Info",
    22: "Search",
    23: "Seek",
    24: "Shuffle",
    25: "Song",
    26: "Speed",
    27: "Sticker",
    28: "Tag All",
    29: "Text",
}


def generate_help_buttons(_, start: int, end: int, current_page: int):
    """Create a grid of three buttons per row for the given range."""
    buttons, per_row = [], 3
    for idx, i in enumerate(range(start, end + 1)):
        if idx % per_row == 0:
            buttons.append([])
        buttons[-1].append(
            InlineKeyboardButton(
                text=HELP_LABELS.get(i, f"Help {i}"),
                callback_data=f"help_callback hb{i}_p{current_page}"
            )
        )
    return buttons


def first_page(_):
    buttons = generate_help_buttons(_, 1, 15, current_page=1)
    buttons.append(
        [
            InlineKeyboardButton(text="Menu", callback_data="back_to_main"),
            InlineKeyboardButton(text="Next", callback_data="help_next_2")
        ]
    )
    return InlineKeyboardMarkup(buttons)


def second_page(_):
    buttons = generate_help_buttons(_, 16, TOTAL_SECTIONS, current_page=2)
    buttons.append(
        [
            InlineKeyboardButton(text="Back", callback_data="help_prev_1"),
            InlineKeyboardButton(text="Menu", callback_data="back_to_main")
        ]
    )
    return InlineKeyboardMarkup(buttons)


def action_sub_menu(_, current_page: int):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Promotion",
                    callback_data="action_prom_1"
                ),
                InlineKeyboardButton(
                    text="Punishment",
                    callback_data="action_pun_1"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Back",
                    callback_data=f"help_back_{current_page}"
                )
            ]
        ]
    )


def help_back_markup(_, current_page: int):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Back",
                    callback_data=f"help_back_{current_page}"
                ),
                InlineKeyboardButton(
                    text="Close",
                    callback_data="close"
                ),
            ]
        ]
    )


def private_help_panel(_):
    return [
        [
            InlineKeyboardButton(
                text="Open Help",
                url=f"https://t.me/{app.username}?start=help"
            ),
        ],
    ]
