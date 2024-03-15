# -----------CREDITS -----------
# telegram : @SAIF_DICTATOR
# github : SAIFDEAD
from pyrogram import filters
import asyncio, time,requests
from pyrogram.types import InlineKeyboardMarkup
from .. import Mukesh
from pyrogram.enums import ChatAction,ParseMode
from config import *
from ..modules.buttons import *



x=None
#blackbox
@Mukesh.on_message(filters.command(["blackbox"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def blackbox_chat(bot, message):
    if len(message.command) < 2:
            await message.reply_text(
            "ᴇxᴀᴍᴘʟᴇ:**\n\n`/ʙʟᴀᴄᴋʙᴏx ᴡʀɪᴛᴇ sɪᴍᴘʟᴇ ғʟᴀsᴋ ᴀᴘᴘ ᴄᴏᴅᴇ`")
    else:
        a = message.text.split(' ', 1)[1]
    # CREDITS
    # telegram : @SAIF_DICTATOR
    # github : SAIFDEAD
    try:
        response = requests.get(f'https://mukesh-api.vercel.app/blackbox?query={a}') 
        if response.status_code==200:
            await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
            x=response.json()["results"]
            
            await message.reply_text(f"{x}\n🌹 𝐏ᴏᴡᴇʀᴇᴅ 𝐁ʏ @{Mukesh.username} ",reply_markup=InlineKeyboardMarkup(gpt_button),quote=True,disable_web_page_preview =True)  
        else:
            pass

            
    except requests.exceptions.RequestException as e:
        pass
        
