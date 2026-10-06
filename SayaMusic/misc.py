# Saya Music
import time

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus

from config import OWNER_ID
from SayaMusic.core.mongo import mongodb
from .logging import LOGGER

SUDOERS = filters.user()
COMMANDERS = [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
_boot_ = time.time()

def dbb():
    global db
    db = {}
    LOGGER(__name__).info("ᴅᴀᴛᴀʙᴀsᴇ ʟᴏᴀᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ")

async def sudo():
    SUDOERS.add(OWNER_ID)
    sudoersdb = mongodb.sudoers
    data = await sudoersdb.find_one({"sudo": "sudo"}) or {}
    sudoers = data.get("sudoers", [])

    if OWNER_ID not in sudoers:
        sudoers.append(OWNER_ID)
        await sudoersdb.update_one(
            {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
        )

    for user_id in sudoers:
        SUDOERS.add(user_id)

    LOGGER(__name__).info("sᴜᴅᴏ ᴜsᴇʀs ᴅᴏɴᴇ..")
