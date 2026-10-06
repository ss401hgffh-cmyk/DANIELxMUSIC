# Saya Music
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SayaMusic import app
import config
from config import BOT_USERNAME

repo_caption = """**
 ᴄʟᴏɴᴇ ᴀɴᴅ ᴅᴇᴘʟᴏʏ – Saya Music 

 ᴅᴇᴘʟᴏʏ ᴇᴀsɪʟʏ ᴏɴ Railway ᴡɪᴛʜ Docker
 ᴄʟᴇᴀɴ Saya Music ʙʀᴀɴᴅɪɴɢ
 ᴅᴏᴄᴋᴇʀ, ᴘʀᴏᴄꜰɪʟᴇ, ᴀɴᴅ Railway ᴄᴏɴꜰɪɢ ʀᴇᴀᴅʏ
 ʀᴜɴ 24/7 ʟᴀɢ ꜰʀᴇᴇ

ɪꜰ ʏᴏᴜ ꜰᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ, ᴏᴘᴇɴ ᴀɴ ɪꜱꜱᴜᴇ ᴏʀ ᴄʜᴇᴄᴋ ꜱᴜᴘᴘᴏʀᴛ
**"""

@app.on_message(filters.command("repo"))
async def show_repo(_, msg):
    buttons = [
        [InlineKeyboardButton(" ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton(" ᴏᴡɴᴇʀ", url=f"https://github.com/{config.OWNER_USERNAME}"),
            InlineKeyboardButton(" ꜱᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_CHAT)
        ],
        [
            InlineKeyboardButton(" Railway", url="https://railway.com/new"),
            InlineKeyboardButton(" ɢɪᴛʜᴜʙ", url=config.UPSTREAM_REPO)
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    try:  
        await msg.reply_photo(
            photo="https://telegra.ph/file/58afe55fee5ae99d6901b.jpg",
            caption=repo_caption,
            reply_markup=reply_markup
        )
    except:
        pass
