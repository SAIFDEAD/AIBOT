# -----------CREDITS -----------
# telegram : @SAIF_DICTATOR
# github : SAIFDEAD
from pyrogram import filters
import asyncio
from .. import Mukesh
from ..database import *


@Mukesh.on_message(filters.command(["stats", f"tgt@{Mukesh.username}"]))
async def stats(_, m):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await m.reply(f"""  𝐓ᴏᴛᴀʟ 𝐒ᴛᴀᴛꜱ 🥀 {Mukesh.mention}:\n𝐔ꜱᴇʀꜱ: {users}\n𝐂ʜᴀᴛ: {chats}""")
