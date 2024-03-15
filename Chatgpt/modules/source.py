# -----------CREDITS -----------
# telegram : @SAIF_DICTATOR
# github : SAIFDEAD
from pyrogram import filters
import asyncio
from .. import Mukesh
from ..modules.buttons import *


@Mukesh.on_message(
    filters.command(["source", "repo"], prefixes=["+", ".", "/", "-", "?", "$"])
)
async def source(_, m):
    await m.reply_photo(f"{sr}",
        caption=SOURCE_TEXT,
        reply_markup=SOURCE_BUTTONS
    )
