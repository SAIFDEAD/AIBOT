# -----------CREDITS -----------
# telegram : @SAIF_DICTATOR
# github : SAIFDEAD
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup

from .. import Mukesh
from ..modules.buttons import *

@Mukesh.on_message(
    filters.command(
        ["help", f"help@{Mukesh.username}"], prefixes=["+", ".", "/", "-", "?", "$"]
    )
)
async def help(_, m):
    await m.reply_photo(f"{sh}",
        caption=f"{HELP}",
        reply_markup=InlineKeyboardMarkup(HELP_BACK),quote=True
    )
