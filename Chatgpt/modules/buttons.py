# CREDITS
# telegram : @SAIF_DICTATOR
# github : SAIFDEAD

from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from config import *
from random import choice
from .. import Mukesh

import requests

def send():
    headers = {"accept": "application/json"}
    response = requests.get("https://mukesh-api.vercel.app/base/decode?query=aHR0cHM6Ly9naXRodWIuY29tL05vb2ItbXVrZXNoL0NoYXRncHQtYm90", headers=headers)
    return response.json()["results"]
xy=send()  

START = f""" <b>
๏ ʜᴇʏ, ɪ ᴀᴍ <a href="https://t.me/{Mukesh.username}"> {Mukesh.name} </a>

➻ ᴀɴ ᴏᴘᴇɴ-ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛɢᴘᴛ.
──────────────────
ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇ ʙᴏᴛ ᴀɴᴅ ᴄᴀɴ 

ᴀɴsᴡᴇʀ ʏᴏᴜʀ ᴏ̨ᴜᴇʀɪᴇs ᴇᴀsʟɪʏ
──────────────────
Rᴇᴀᴅ Tʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ

Pᴏᴡᴇʀᴇᴅ Bʏ [𝐃ɪᴄᴛᴀᴛᴏʀ](https://t.me/SAIF_DICTATOR) </b>"""
SOURCE_TEXT = f"""<b>
๏ ʜᴇʏ, ɪ ᴀᴍ <a href="https://t.me/{Mukesh.username}"> {Mukesh.name} </a>
──────────────────
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ</b>
"""
HELP = f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {Mukesh.mention}
/chatgpt <prompt> ᴇxᴀᴍᴘʟᴇ: `/ᴄʜᴀᴛɢᴘᴛ ᴡʀɪᴛᴇ sʜᴏʀᴛs ɴᴏᴛᴇs ᴏғ ᴇʟᴇᴄᴛʀɪᴄɪᴛʏ`
/bard <prompt> ᴇxᴀᴍᴘʟᴇ: `/ʙᴀʀᴅ ᴡʀɪᴛᴇ ᴀ sɪᴍᴘʟᴇ ғʟᴀsᴋ ᴀᴘᴘ ɪɴ ᴘʏᴛʜᴏɴ.`
/blackbox <prompt> ᴇxᴀᴍᴘʟᴇ: `/ʙʟᴀᴄᴋʙᴏx ᴡʀɪᴛᴇ ᴀ sɪᴍᴘʟᴇ ᴡᴇʙsɪᴛᴇ ᴜsɪɴɢ ᴘʏᴛʜᴏɴ.`
/ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ ᴏғ ᴛʜᴇ ʙᴏᴛ.
/source Tᴏ ɢᴇᴛ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ,
/help Tᴏ ɢᴇᴛ ʜᴇʟᴘ   
/start Tᴏ sᴛᴀʀᴛ ʙᴏᴛ
/stats Tᴏ ɢᴇᴛ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ


"""

SAIFA = [
    "https://te.legra.ph/file/77e80dd7b51a410cc9e9f.jpg",
]
g =choice(SA)

SAIFH = [
    "https://te.legra.ph/file/35f8b42234608be1f97f1.jpg",
]
g =choice(SH)

SAIFR = [
    "https://te.legra.ph/file/464ccd43dd3cd1e96f452.jpg",
]
g = choice(SR)

SAIFS = [
    "https://te.legra.ph/file/685ba5e8be9ddf6eb5e18.jpg",
]
g = choice(SS)

x = ["❤️", "🎉", "✨", "🪸", " 🎉 ", " 🎈 ", "🎯"]
g = choice(x)


MAIN = [
    [
        IKB(
            text="•─╼⃝𖠁 𝐀ᴅᴅ 𝐌ᴇ 𝐁ᴀʙʏ 𖠁⃝╾─•",
            url=f"https://t.me/{Mukesh.username}?startgroup=true",
        ),
    ],
    [
        IKB(text="𝐇ᴇʟᴘs", callback_data="HELP"),
    ],
    [
        IKB(text="𝐒ᴏᴜʀᴄᴇ ", callback_data="HELP_source"),
        
        IKB(text="𝐃ᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER_ID),
]
]

PNG_BTN = [
    [
        IKB(
            text="•─╼⃝𖠁 𝐀ᴅᴅ 𝐌ᴇ 𝐁ᴀʙʏ 𖠁⃝╾─•",
            url=f"https://t.me/{Mukesh.username}?startgroup=true",
        ),
    ],
    [
        IKB("𝐒ᴜᴘᴘᴏʀᴛ",
            url=f"https://t.me/{SUPPORT_GRP}",
        ),
    ],
]

gpt_button = [
    [
        IKB(
            text="•─╼⃝𖠁 𝐀ᴅᴅ 𝐌ᴇ 𝐁ᴀʙʏ 𖠁⃝╾─•",
            url=f"https://t.me/{Mukesh.username}?startgroup=true",
        ),

        IKB("𝐃ɪᴄᴛᴀᴛᴏʀ", user_id=OWNER_ID)
    ],
]



HELP_BACK = [

    [
        IKB("𝐁ᴀᴄᴋ", callback_data="HELP_BACK"),
    ],
]

SOURCE_BUTTONS = IKM(
    [
        [IKB("𝐒ᴏᴜʀᴄᴇ", callback_data="HELP_hurr")],
        [
            IKB(" 𝐒ᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GRP}"),
            IKB(text="𝐁ᴀᴄᴋ ", callback_data="HELP_BACK")
        ]
    ]
)
SOURCE_BUTTON = IKM(
    [
        [IKB("𝐒ᴏᴜʀᴄᴇ" ,url=xy)
        ]
    ]
)
