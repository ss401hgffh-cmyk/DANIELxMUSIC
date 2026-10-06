# Saya Music
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class StatsCallbacks:
    SHOW_OVERVIEW = "stats:overview"
    SHOW_BOT_STATS = "stats:bot"
    BACK = "stats:back"
    CLOSE = "stats:close"


def build_stats_keyboard(_, is_sudo: bool) -> InlineKeyboardMarkup:
    non_sudo_row = [
        InlineKeyboardButton(
            text="Overview",
            callback_data=StatsCallbacks.SHOW_OVERVIEW,
        )
    ]
    sudo_row = [
        InlineKeyboardButton(
            text="System",
            callback_data=StatsCallbacks.SHOW_BOT_STATS,
        ),
        InlineKeyboardButton(
            text="Overview",
            callback_data=StatsCallbacks.SHOW_OVERVIEW,
        ),
    ]
    rows = [
        sudo_row if is_sudo else non_sudo_row,
        [
            InlineKeyboardButton(
                text="Close",
                callback_data=StatsCallbacks.CLOSE,
            )
        ],
    ]
    return InlineKeyboardMarkup(rows)


def build_back_keyboard(_) -> InlineKeyboardMarkup:
    rows = [
        [
            InlineKeyboardButton(
                text="Back",
                callback_data=StatsCallbacks.BACK,
            ),
            InlineKeyboardButton(
                text="Close",
                callback_data=StatsCallbacks.CLOSE,
            ),
        ]
    ]
    return InlineKeyboardMarkup(rows)
