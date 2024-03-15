# -----------CREDITS -----------
# telegram : @SAIF_DICTATOR
# github : SAIFDEAD
from pyrogram import filters
from pyrogram.enums import ChatAction
from pyrogram.types import InlineKeyboardMarkup
import asyncio, time,requests
from .. import Mukesh
from config import *
from ..modules.buttons import *
#  bard 
x=None
@Mukesh.on_message(filters.command(["bard"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def bard_chat(bot, message):
    global x
    if len(message.command) < 2:
            await message.reply_text(
            "ᴇxᴀᴍᴘʟᴇ:**\n\n`/ʙᴀʀᴅ ᴡʀɪᴛᴇ sʜᴏʀᴛs ɴᴏᴛᴇs ᴏɴ ʜᴜᴍᴀɴ ᴇʏᴇs`")
    else:
        a = message.text.split(' ', 1)[1]
    
    try:
        response = requests.get(f'https://mukesh-api.vercel.app/bard?query={a}') 
        if response.status_code==200:
            await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
            x=response.json()["results"]
            
            await message.reply_text(f"{x}\n🥀 𝐏ᴏᴡᴇʀᴇᴅ 𝐁ʏ @{Mukesh.username} ",reply_markup=InlineKeyboardMarkup(gpt_button),quote=True)  
        else:
            pass

            
    except requests.exceptions.RequestException as e:
        pass
        
