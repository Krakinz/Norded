import os
import io
from re import I
import sys
import math
import time
import asyncio
import logging
import threading
import importlib
import pytgcalls
from os import execl
from time import time
from os import getenv
from datetime import *
from time import sleep
try:
    from pytgcalls import pytgcalls
except ImportError:
    os.system("pip install pytgcalls")
try:
    import requests
except ImportError:
    os.system("pip install requests")
try:
    import youtube_search
except ImportError:
    os.system("pip install youtube_search")
try:
    import youtube_dl
except ImportError:
    os.system("pip install youtube_dl")
try:
    import wheel
except ImportError:
    os.system("pip install wheel")
try:
    import TgCrypto
except ImportError:
    os.system("pip install TgCrypto")
try:
    import pyrogram
except ImportError:
    os.system("pip install pyrogram")
try:
    import heroku3
except ImportError:
    os.system("pip install heroku3")
try:
    import ffmpeg
except ImportError:
    os.system("pip install ffmpeg-python")
try:
    import urllib3
except ImportError:
    os.system("pip install urllib3")
try:
    from termcolor import *
except ImportError:
    os.system("pip install termcolor")
try:
    from loguru import logger
except ImportError:
    os.system("pip install loguru")
try:
    from dotenv import load_dotenv
except ImportError:
    os.system("pip install python-dotenv")
try: 
    import signal
except ImportError:
    os.system("pip install signal")
try: 
    import requests
except ImportError:
    os.system("pip install requests")
try: 
    import pyromod
except ImportError:
    os.system("pip install pyromod")

import pyrogram
import wheel
import heroku3
import ffmpeg
import urllib3
import termcolor
import dotenv
import requests
import youtube_search
import youtube_dl
import signal
import pyromod
importlib.reload(pyrogram)
importlib.reload(wheel)
importlib.reload(heroku3)
importlib.reload(ffmpeg)
importlib.reload(urllib3)
importlib.reload(termcolor)
importlib.reload(dotenv)
importlib.reload(requests)
importlib.reload(youtube_search)
importlib.reload(signal)
importlib.reload(youtube_dl)
importlib.reload(pyromod)

load_dotenv("./.env")
file = open("db.py", "w") 
file.write("def init():\n    global db\n    db = {}") 
file.close()
import db
db.init()
import asyncio
from db import db
from pyromod import listen
from youtube_search import YoutubeSearch
from pyrogram.types import ChatPermissions
from pyrogram.utils import MAX_CHANNEL_ID
from pyrogram import Client, filters,idle
from asyncio.exceptions import TimeoutError
from pyrogram.raw.base import InputGroupCall
## from pytgcalls import GroupCall as NORDCALLER
utcnow = datetime.utcnow().replace(microsecond=0)
from pyrogram.types import Message as ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pytgcalls import GroupCallFactory, GroupCallFileAction
from pyrogram.raw.functions.phone import EditGroupCallTitle
from pyrogram.errors.exceptions import internal_server_error_500
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR as HYPEDLDIR
from pyrogram.types import InlineKeyboardMarkup as HypeKeyboardMarkup,InlineKeyboardButton as HypeKeyboardButton
from pyrogram.errors import SessionPasswordNeeded, FloodWait,PhoneNumberInvalid, ApiIdInvalid,PhoneCodeInvalid, PhoneCodeExpired

MIB = HypeKeyboardMarkup([[
HypeKeyboardButton(
text="🏷Group",
url="https://t.me/hypevoidsoul"),
HypeKeyboardButton(
text="💰Channel",
url="https://t.me/KrakinzLab"),
HypeKeyboardButton(
text="⚜️Dev+Git",
url="https://t.me/krakinz")],
[HypeKeyboardButton(
text="🧸Master Bot",
url="https://t.me/XERONOIDBOT")]])

HELP_BUTTONS = HypeKeyboardMarkup([[
HypeKeyboardButton(
"𝙈𝙚𝙢𝙗𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 💛",
callback_data="𝙈𝙚𝙢𝙗𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 💛"),],[
HypeKeyboardButton(
"𝘼𝙙𝙢𝙞𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 ⚜️",
callback_data="𝘼𝙙𝙢𝙞𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 ⚜️"),],[  
HypeKeyboardButton(
"𝙃𝙚𝙧𝙤𝙠𝙪 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 🟣",
callback_data="𝙃𝙚𝙧𝙤𝙠𝙪 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 🟣"),],[
HypeKeyboardButton(
"𝙀𝙭𝙞𝙩 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪🔺",
callback_data="𝙀𝙭𝙞𝙩 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪🔺")]])

CLOSE_BUTTON = HypeKeyboardMarkup(
[[HypeKeyboardButton(
"𝙀𝙭𝙞𝙩 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪🔺",
callback_data="𝙀𝙭𝙞𝙩 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪🔺")]])

MEM_BUTT = HypeKeyboardMarkup([[
HypeKeyboardButton(
"𝘼𝙙𝙢𝙞𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 ⚜️",
callback_data="𝘼𝙙𝙢𝙞𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 ⚜️"),],[
HypeKeyboardButton(
"𝙃𝙚𝙧𝙤𝙠𝙪 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 🟣",
callback_data="𝙃𝙚𝙧𝙤𝙠𝙪 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 🟣"),],[
HypeKeyboardButton(
"𝙀𝙭𝙞𝙩 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪🔺",
callback_data="𝙀𝙭𝙞𝙩 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪🔺")]])


ADM_BUTT = HypeKeyboardMarkup([[
HypeKeyboardButton(
"𝙈𝙚𝙢𝙗𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 💛",
callback_data="𝙈𝙚𝙢𝙗𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 💛"),],[
HypeKeyboardButton(
"𝙃𝙚𝙧𝙤𝙠𝙪 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 🟣",
callback_data="𝙃𝙚𝙧𝙤𝙠𝙪 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 🟣"),],[
HypeKeyboardButton(
"𝙀𝙭𝙞𝙩 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪🔺",
callback_data="𝙀𝙭𝙞𝙩 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪🔺")]])


HERO_BUTT = HypeKeyboardMarkup([[
HypeKeyboardButton(
"𝙈𝙚𝙢𝙗𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 💛",
callback_data="𝙈𝙚𝙢𝙗𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 💛"),],[
HypeKeyboardButton(
"𝘼𝙙𝙢𝙞𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 ⚜️",
callback_data="𝘼𝙙𝙢𝙞𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 ⚜️"),],[
HypeKeyboardButton(
"𝙀𝙭𝙞𝙩 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪🔺",
callback_data="𝙀𝙭𝙞𝙩 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪🔺")]])


HEROKU = getenv("HEROKU",None)
if HEROKU == "HEROKU":
    "--------------------------------------------------------------------------------" 
    NORD_ADMINS                 =   list(map(int, getenv("NORD_ADMINS",None).split()))
    CHAT_ID                     =   list(map(int, getenv("CHAT_ID",None).split()))
    ALIVE_CHECK_CHAT            =   int(getenv("ALIVE_CHECK_CHAT",None))
    HEROKU_APP_NAME             =   str(getenv("HEROKU_APP_NAME",None))  
    HEROKU_API_KEY              =   str(getenv("HEROKU_API_KEY",None))  
    NORDED_SESSION              =   str(getenv("NORDED_SESSION",None))  
    "--------------------------------------------------------------------------------"
    OWNER_USERNAME              =   str(getenv("OWNER_USERNAME",None)) 
    if OWNER_USERNAME.startswith("@"):
        OWNER_USERNAME           =  OWNER_USERNAME
    else:
        OWNER_USERNAME           =  "@"+OWNER_USERNAME
    "--------------------------------------------------------------------------------"
    BOT_USERNAME                 =   str(getenv("BOT_USERNAME",None))  
    if BOT_USERNAME.startswith("@"):
        BOT_USERNAME             =  BOT_USERNAME
    else:
        BOT_USERNAME             =  "@"+BOT_USERNAME
    "--------------------------------------------------------------------------------"
    BOT_TOKEN                   =   str(getenv("BOT_TOKEN",None))  
    API_HASH                    =   str(getenv("API_HASH",None))  
    CLEANER                     =   int(getenv("CLEANER",None))  
    API_ID                      =   int(getenv("API_ID",None))  
    DYNO                        =   str(getenv("DYNO",None))  
    "--------------------------------------------------------------------------------"

elif HEROKU != "HEROKU": # make a .env file and append your stuffs in it if not heroku.
    "--------------------------------------------------------------------------------" 
    NORD_ADMINS                 =   list(map(int, getenv("NORD_ADMINS",None).split()))
    CHAT_ID                     =   list(map(int, getenv("CHAT_ID",None).split()))
    ALIVE_CHECK_CHAT            =   int(getenv("ALIVE_CHECK_CHAT",None))
    HEROKU_APP_NAME             =   str(getenv("HEROKU_APP_NAME",None))  
    HEROKU_API_KEY              =   str(getenv("HEROKU_API_KEY",None))  
    NORDED_SESSION              =   str(getenv("NORDED_SESSION",None))  
    "--------------------------------------------------------------------------------"
    OWNER_USERNAME              =   str(getenv("OWNER_USERNAME",None)) 
    if OWNER_USERNAME.startswith("@"):
        OWNER_USERNAME          =  OWNER_USERNAME
    else:
        OWNER_USERNAME          =   "@"+OWNER_USERNAME
    "--------------------------------------------------------------------------------"
    BOT_USERNAME                =   str(getenv("BOT_USERNAME",None))  
    if BOT_USERNAME.startswith("@"):
        BOT_USERNAME            =   BOT_USERNAME
    else:
        BOT_USERNAME            =   "@"+BOT_USERNAME
    "--------------------------------------------------------------------------------"
    BOT_TOKEN                   =   str(getenv("BOT_TOKEN",None))  
    API_HASH                    =   str(getenv("API_HASH",None))  
    CLEANER                     =   int(getenv("CLEANER",None))  
    API_ID                      =   int(getenv("API_ID",None))  
    DYNO                        =   str(getenv("DYNO",None))  
    "--------------------------------------------------------------------------------"
else:
    cprint("Unknown Vars ..", "red")

def print():
    cprint(ALIVE_CHECK_CHAT,
    "magenta")
    cprint(API_HASH,
    "magenta")
    cprint(API_ID,
    "magenta")
    cprint(BOT_TOKEN,
    "magenta")
    cprint(BOT_USERNAME,
    "magenta")
    cprint(CHAT_ID,
    "magenta")
    cprint(CLEANER,
    "magenta")
    cprint(DYNO,
    "magenta")
    cprint(HEROKU,
    "red")
    cprint(HEROKU_API_KEY,
    "magenta")
    cprint(HEROKU_APP_NAME,
    "magenta")
    cprint(NORD_ADMINS,
    "magenta")
    cprint(NORDED_SESSION,
    "magenta")
    cprint(OWNER_USERNAME,
    "magenta")

GROUP_CALLS = {}
FFMPEG_PROCESSES = {}

𝙽𝙾𝚁𝙳𝙴𝙳 = Client(
session_name=NORDED_SESSION,
api_id=API_ID,
api_hash=API_HASH
)


𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃 = Client(
bot_token=BOT_TOKEN,
api_id=API_ID,
api_hash=API_HASH,
session_name="𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃"
)
heroku_api = "https://api.heroku.com"
group_calls = pytgcalls.GroupCallFactory(Client).get_group_call()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
𝙽𝙾𝚁𝙴𝙳_HUD="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg"
𝙽𝙾𝚁𝙴𝙳_ERROR = "https://telegra.ph/file/3b0adb8bdcf025bd61ccd.mp4"
nordanimer="https://telegra.ph/file/745b406e98758fe8c9089.gif"
ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ = "🕊**𝙽𝙾𝚁𝙳𝙴𝙳-𝚂𝚖𝚊𝚛𝚝 𝙼𝚞𝚜𝚒𝚌 𝙿𝚕𝚊𝚢𝚎𝚛**🕊\n[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/hypevoidsoul)\n"
LINK = "(https://en.wikipedia.org/wiki/GNU_General_Public_License#:~:text=The%20GNU%20General%20Public%20License,share%2C%20and%20modify%20the%20software.&text=Prominent%20free%20software%20programs%20licensed,GNU%20Compiler%20Collection%20(GCC)"
DURATION_PLAY_HOUR = 3
HRKU = heroku3.from_key(HEROKU_API_KEY)
𝙽𝙾𝚁𝙴𝙳_FIXER = prefixes=DYNO


MEMBER_CATEG=f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}[𝗠𝗲𝗺𝗯𝗲𝗿_𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀]{LINK}\n
**{DYNO}stream**
•♪ `𝘙𝘦𝘱𝘭𝘺 𝘵𝘰 𝘢𝘶𝘥𝘪𝘰 𝘧𝘪𝘭𝘦 𝘵𝘰 𝘱𝘭𝘢𝘺/𝘲𝘶𝘦𝘶𝘦 𝘵𝘰` 🕊Norded Smart Music Player🕊.
**{DYNO}stream**
•♪ `𝘜𝘴𝘦 𝘵𝘰 𝘤𝘩𝘦𝘤𝘬𝘰𝘶𝘵 𝘵𝘩𝘦 𝘱𝘭𝘢𝘺𝘭𝘪𝘴𝘵 𝘰𝘧` 🕊Norded Smart Music Player🕊.
**{DYNO}ping**   
•♪ `𝘊𝘩𝘦𝘤𝘬 𝘵𝘩𝘦 𝘱𝘪𝘯𝘨 𝘴𝘵𝘢𝘵𝘶𝘴 𝘰𝘧` 🕊Norded Smart Music Player🕊.
**{DYNO}license**
•♪ `𝘊𝘩𝘦𝘤𝘬 𝘭𝘪𝘤𝘦𝘯𝘴𝘦 𝘰𝘧` 🕊Norded Smart Music Player🕊.
**{DYNO}yt**
•♪ __Direct youtube music download and play with 🕊Norded Smart Music Player🕊.__
"""


ADMIN_CATEG=f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}[𝗔𝗱𝗺𝗶𝗻 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀]{LINK}\n
**{DYNO}norded** 
•♪ `𝘊𝘩𝘦𝘤𝘬 𝘸𝘩𝘦𝘳𝘦 𝘪𝘴 𝘵𝘩𝘦` —••÷[🕊NORDED🕊]÷••— `𝘶𝘴𝘦𝘳𝘣𝘰𝘵 𝘱𝘭𝘶𝘨𝘨𝘦𝘥.`
**{DYNO}plug**   
•♪ —••÷[🕊NORDED🕊]÷••— `𝘑𝘰𝘪𝘯 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵.`
**{DYNO}unplug** 
•♪ `𝘓𝘦𝘢𝘷𝘦 𝘵𝘩𝘦 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵 𝘸𝘩𝘦𝘳𝘦` —••÷[🕊NORDED🕊]÷••— `𝘸𝘢𝘴 𝘱𝘭𝘢𝘺𝘪𝘯𝘨.`
**{DYNO}end**    
•♪ `𝘊𝘭𝘦𝘢𝘯 𝘵𝘩𝘦 𝘱𝘭𝘢𝘺𝘭𝘪𝘴𝘵 𝘢𝘯𝘥 𝘴𝘵𝘰𝘱 𝘢𝘭𝘭 𝘮𝘶𝘴𝘪𝘤.`
**{DYNO}pause**  
•♪ `𝘗𝘢𝘶𝘴𝘦 𝘮𝘶𝘴𝘪𝘤 𝘪𝘯 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵.`
**{DYNO}resume** 
•♪ `𝘜𝘯-𝘱𝘢𝘶𝘴𝘦 𝘵𝘩𝘦 𝘮𝘶𝘴𝘪𝘤 𝘪𝘯 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵.`
**{DYNO}replay** 
•♪ `𝘗𝘭𝘢𝘺 𝘧𝘳𝘰𝘮 𝘵𝘩𝘦 𝘣𝘦𝘨𝘪𝘯𝘯𝘪𝘯𝘨 𝘰𝘨 𝘤𝘶𝘳𝘳𝘦𝘯𝘵 𝘮𝘶𝘴𝘪𝘤 𝘣𝘦𝘪𝘯𝘨 𝘱𝘭𝘢𝘺𝘦𝘥.`
**{DYNO}next**   
•♪ `𝘔𝘰𝘷𝘦 𝘵𝘰 𝘵𝘩𝘦 𝘯𝘦𝘹𝘵 𝘵𝘳𝘢𝘤𝘬 𝘰𝘳 𝘚𝘬𝘪𝘱 𝘵𝘳𝘢𝘤𝘬 𝘪𝘯 𝘲𝘶𝘦𝘶𝘦 𝘭𝘪𝘬𝘦`: "𝘯𝘦𝘹𝘵 2".
**{DYNO}temp**   
•♪ `𝘊𝘭𝘦𝘢𝘯 𝘵𝘦𝘮𝘱 𝘢𝘶𝘥𝘪𝘰 𝘧𝘪𝘭𝘦𝘴 𝘪𝘯 𝘴𝘦𝘳𝘷𝘦𝘳 𝘰𝘧` 🕊Norded Smart Music Player🕊.
"""

'''
.................................................................
Some Bot and Userbot 
Variables and not to be changed
.................................................................
'''



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



'''
.................................................................
Some Bot and Userbot 
Variables and not to be changed
.................................................................
'''

HEROKU_CATEG=f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}[𝗛𝗲𝗿𝗼𝗸𝘂 𝗔𝗱𝗺𝗶𝗻 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀]{LINK}\n
**{DYNO}restart**
•♪ `𝘙𝘦𝘴𝘵𝘢𝘳𝘵` —••÷[🕊NORDED🕊]÷••— `𝘮𝘢𝘯𝘶𝘢𝘭𝘭𝘺 𝘪𝘯 𝘏𝘌𝘙𝘖𝘒𝘜.`
**{DYNO}usage**  
•♪ `𝘍𝘪𝘯𝘥` —••÷[🕊NORDED🕊]÷••— `𝘏𝘌𝘙𝘖𝘒𝘜 𝘥𝘺𝘯𝘰 𝘶𝘴𝘢𝘨𝘦`
"""
INFO_CATEG = f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}**__Please press below buttons to check the available commands.__**

⛵️Ðêv Mêñ†ïðñ§:
    @HypeVoisoul
    @qtell @five34
"""
NORN = f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}**__Audio is here.__**\n**Please reply to the audio file with** /stream"""

'''
.................................................................
Some Bot and Userbot 
Variables and not to be changed
.................................................................
'''



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



'''
.................................................................
Some Bot and Userbot 
Variables and not to be changed
.................................................................
'''

XERO_HELP = f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}[𝗠𝗲𝗺𝗯𝗲𝗿_𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀]{LINK}
**{DYNO}stream**   
•♪ `𝘙𝘦𝘱𝘭𝘺 𝘵𝘰 𝘢𝘶𝘥𝘪𝘰 𝘧𝘪𝘭𝘦 𝘵𝘰 𝘱𝘭𝘢𝘺/𝘲𝘶𝘦𝘶𝘦 𝘵𝘰` 🕊Norded Smart Music Player🕊.
`{DYNO}stream`   
•♪ `𝘜𝘴𝘦 𝘵𝘰 𝘤𝘩𝘦𝘤𝘬𝘰𝘶𝘵 𝘵𝘩𝘦 𝘱𝘭𝘢𝘺𝘭𝘪𝘴𝘵 𝘰𝘧` 🕊Norded Smart Music Player🕊.
`{DYNO}ping`   
•♪ `𝘊𝘩𝘦𝘤𝘬 𝘵𝘩𝘦 𝘱𝘪𝘯𝘨 𝘴𝘵𝘢𝘵𝘶𝘴 𝘰𝘧` 🕊Norded Smart Music Player🕊.
`{DYNO}license`
•♪ `𝘊𝘩𝘦𝘤𝘬 𝘭𝘪𝘤𝘦𝘯𝘴𝘦 𝘰𝘧` 🕊Norded Smart Music Player🕊.\n\n[𝗔𝗱𝗺𝗶𝗻 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀]{LINK}
`{DYNO}norded` 
•♪ `𝘊𝘩𝘦𝘤𝘬 𝘸𝘩𝘦𝘳𝘦 𝘪𝘴 𝘵𝘩𝘦` —••÷[🕊NORDED🕊]÷••— `𝘶𝘴𝘦𝘳𝘣𝘰𝘵 𝘱𝘭𝘶𝘨𝘨𝘦𝘥.`
`{DYNO}plug`   
•♪ —••÷[🕊NORDED🕊]÷••— `𝘑𝘰𝘪𝘯 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵.`
`{DYNO}unplug` 
•♪ `𝘓𝘦𝘢𝘷𝘦 𝘵𝘩𝘦 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵 𝘸𝘩𝘦𝘳𝘦` —••÷[🕊NORDED🕊]÷••— `𝘸𝘢𝘴 𝘱𝘭𝘢𝘺𝘪𝘯𝘨.`
`{DYNO}end`    
•♪ `𝘊𝘭𝘦𝘢𝘯 𝘵𝘩𝘦 𝘱𝘭𝘢𝘺𝘭𝘪𝘴𝘵 𝘢𝘯𝘥 𝘴𝘵𝘰𝘱 𝘢𝘭𝘭 𝘮𝘶𝘴𝘪𝘤.`
`{DYNO}pause`  
•♪ `𝘗𝘢𝘶𝘴𝘦 𝘮𝘶𝘴𝘪𝘤 𝘪𝘯 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵.`
`{DYNO}resume` 
•♪ `𝘜𝘯-𝘱𝘢𝘶𝘴𝘦 𝘵𝘩𝘦 𝘮𝘶𝘴𝘪𝘤 𝘪𝘯 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵.`
`{DYNO}replay` 
•♪ `𝘗𝘭𝘢𝘺 𝘧𝘳𝘰𝘮 𝘵𝘩𝘦 𝘣𝘦𝘨𝘪𝘯𝘯𝘪𝘯𝘨 𝘰𝘨 𝘤𝘶𝘳𝘳𝘦𝘯𝘵 𝘮𝘶𝘴𝘪𝘤 𝘣𝘦𝘪𝘯𝘨 𝘱𝘭𝘢𝘺𝘦𝘥.`
`{DYNO}next`   
•♪ `𝘔𝘰𝘷𝘦 𝘵𝘰 𝘵𝘩𝘦 𝘯𝘦𝘹𝘵 𝘵𝘳𝘢𝘤𝘬 𝘰𝘳 𝘚𝘬𝘪𝘱 𝘵𝘳𝘢𝘤𝘬 𝘪𝘯 𝘲𝘶𝘦𝘶𝘦 𝘭𝘪𝘬𝘦`: "𝘯𝘦𝘹𝘵 2".
`{DYNO}temp`   
•♪ `𝘊𝘭𝘦𝘢𝘯 𝘵𝘦𝘮𝘱 𝘢𝘶𝘥𝘪𝘰 𝘧𝘪𝘭𝘦𝘴 𝘪𝘯 𝘴𝘦𝘳𝘷𝘦𝘳 𝘰𝘧` 🕊Norded Smart Music Player🕊.\n\n[𝗛𝗲𝗿𝗼𝗸𝘂 𝗔𝗱𝗺𝗶𝗻 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀]{LINK}
`{DYNO}restart`
•♪ `𝘙𝘦𝘴𝘵𝘢𝘳𝘵` —••÷[🕊NORDED🕊]÷••— `𝘮𝘢𝘯𝘶𝘢𝘭𝘭𝘺 𝘪𝘯 𝘏𝘌𝘙𝘖𝘒𝘜.`
`{DYNO}usage`  
•♪ `𝘍𝘪𝘯𝘥` —••÷[🕊NORDED🕊]÷••— `𝘏𝘌𝘙𝘖𝘒𝘜 𝘥𝘺𝘯𝘰 𝘶𝘴𝘢𝘨𝘦`
"""
#`{DYNO}shutdown`
#•♪ `𝘛𝘶𝘳𝘯 𝘰𝘧𝘧 𝘏𝘌𝘙𝘖𝘒𝘜 𝘋𝘺𝘯𝘰 𝘧𝘰𝘳` 🕊Norded Smart Music Player🕊.

'''
.................................................................
Some Bot and Userbot 
Variables and not to be changed
.................................................................
'''



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



PHONE_NUMBER_TEXT = """
`Please Send your Telegram Phone number with valid country code.`
 
`Example:`
**+254000000000**

ᴘʀᴇꜱꜱ /exit ᴛᴏ ᴄᴀɴᴄᴇʟ ᴘʀᴏɢʀᴇꜱꜱ.
"""



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



OTP =  """
÷•• ᴀɴ ᴏᴛᴘ ɪꜱ ꜱᴇɴᴛ ᴛᴏ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ

÷•• ᴘʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ᴏᴛᴘ ɪɴ `1 2 3 4 5` [**DO NOT FORGET SPACES IN BETWEEN**]

÷•• ɪꜰ 𝕡𝕪𝕣𝕠𝕘𝕣𝕒𝕞 ɴᴏᴛ ꜱᴇɴᴅɪɴɢ ᴏᴛᴘ ᴛʜᴇɴ ᴛʀʏ ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴛᴀꜱᴋ ᴀɢᴀɪɴ ᴡɪᴛʜ /start ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʙᴏᴛ.



ᴘʀᴇꜱꜱ /exit ᴛᴏ ᴄᴀɴᴄᴇʟ ᴘʀᴏɢʀᴇꜱꜱ.
"""



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"""
𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐚𝐮𝐝𝐢𝐨 𝐟𝐢𝐥𝐞 𝐭𝐨 𝐩𝐥𝐚𝐲/𝐪𝐮𝐞𝐮𝐞 𝐭𝐨 🕊Norded Smart Music Player🕊.
𝐔𝐬𝐞 𝐭𝐨 𝐜𝐡𝐞𝐜𝐤𝐨𝐮𝐭 𝐭𝐡𝐞 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐨𝐟 🕊Norded Smart Music Player🕊.
𝐂𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐩𝐢𝐧𝐠 𝐬𝐭𝐚𝐭𝐮𝐬 𝐨𝐟 🕊Norded Smart Music Player🕊. 
𝐂𝐡𝐞𝐜𝐤 𝐥𝐢𝐜𝐞𝐧𝐬𝐞 𝐨𝐟 🕊Norded Smart Music Player🕊.
𝐂𝐡𝐞𝐜𝐤 𝐰𝐡𝐞𝐫𝐞 𝐢𝐬 𝐭𝐡𝐞 —••÷[🕊NORDED🕊]÷••—𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐩𝐥𝐮𝐠𝐠𝐞𝐝
𝐉𝐨𝐢𝐧 𝐠𝐫𝐨𝐮𝐩 𝐯𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭.
𝐋𝐞𝐚𝐯𝐞 𝐭𝐡𝐞 𝐠𝐫𝐨𝐮𝐩 𝐯𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭 𝐰𝐡𝐞𝐫𝐞 🕊Norded Smart Music Player🕊. 𝐰𝐚𝐬 𝐩𝐥𝐚𝐲𝐢𝐧𝐠.
𝐂𝐥𝐞𝐚𝐧 𝐭𝐡𝐞 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐚𝐧𝐝 𝐬𝐭𝐨𝐩 𝐚𝐥𝐥 𝐦𝐮𝐬𝐢𝐜..
𝐏𝐚𝐮𝐬𝐞 𝐦𝐮𝐬𝐢𝐜 𝐢𝐧 𝐠𝐫𝐨𝐮𝐩 𝐯𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭.
𝐔𝐧-𝐩𝐚𝐮𝐬𝐞 𝐭𝐡𝐞 𝐦𝐮𝐬𝐢𝐜 𝐢𝐧 𝐠𝐫𝐨𝐮𝐩 𝐯𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭.
𝐏𝐥𝐚𝐲 𝐟𝐫𝐨𝐦 𝐭𝐡𝐞 𝐛𝐞𝐠𝐢𝐧𝐧𝐢𝐧𝐠 𝐨𝐠 𝐜𝐮𝐫𝐫𝐞𝐧𝐭 𝐦𝐮𝐬𝐢𝐜 𝐛𝐞𝐢𝐧𝐠 𝐩𝐥𝐚𝐲𝐞𝐝.
𝐌𝐨𝐯𝐞 𝐭𝐨 𝐭𝐡𝐞 𝐧𝐞𝐱𝐭 𝐭𝐫𝐚𝐜𝐤 𝐨𝐫 𝐒𝐤𝐢𝐩 𝐭𝐫𝐚𝐜𝐤 𝐢𝐧 𝐪𝐮𝐞𝐮𝐞 𝐥𝐢𝐤𝐞 : "𝐧𝐞𝐱𝐭 𝟐".
𝐂𝐥𝐞𝐚𝐧 𝐭𝐞𝐦𝐩 𝐚𝐮𝐝𝐢𝐨 𝐟𝐢𝐥𝐞𝐬 𝐢𝐧 𝐬𝐞𝐫𝐯𝐞𝐫 𝐨𝐟 🕊Norded Smart Music Player🕊.
𝐓𝐮𝐫𝐧 𝐨𝐟𝐟 𝐇𝐄𝐑𝐎𝐊𝐔 𝐃𝐲𝐧𝐨 𝐟𝐨𝐫 🕊Norded Smart Music Player🕊.
𝐑𝐞𝐛𝐨𝐨𝐭 —••÷[🕊NORDED🕊]÷••—𝐦𝐚𝐧𝐮𝐚𝐥𝐥𝐲 𝐢𝐧 𝐇𝐄𝐑𝐎𝐊𝐔.
𝐅𝐢𝐧𝐝 —••÷[🕊NORDED🕊]÷••—𝐇𝐄𝐑𝐎𝐊𝐔 𝐝𝐲𝐧𝐨 𝐮𝐬𝐚𝐠𝐞

𝗥𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮𝘂𝗱𝗶𝗼 𝗳𝗶𝗹𝗲 𝘁𝗼 𝗽𝗹𝗮𝘆/𝗾𝘂𝗲𝘂𝗲 𝘁𝗼 🕊Norded Smart Music Player🕊.
𝗨𝘀𝗲 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝘁𝗵𝗲 𝗽𝗹𝗮𝘆𝗹𝗶𝘀𝘁 𝗼𝗳 🕊Norded Smart Music Player🕊.
𝗖𝗵𝗲𝗰𝗸 𝘁𝗵𝗲 𝗽𝗶𝗻𝗴 𝘀𝘁𝗮𝘁𝘂𝘀 𝗼𝗳 🕊Norded Smart Music Player🕊.
𝗖𝗵𝗲𝗰𝗸 𝗹𝗶𝗰𝗲𝗻𝘀𝗲 𝗼𝗳 🕊Norded Smart Music Player🕊.
𝗖𝗵𝗲𝗰𝗸 𝘄𝗵𝗲𝗿𝗲 𝗶𝘀 𝘁𝗵𝗲 —••÷[🕊NORDED🕊]÷••—𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𝗽𝗹𝘂𝗴𝗴𝗲𝗱
𝗝𝗼𝗶𝗻 𝗴𝗿𝗼𝘂𝗽 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁.
𝗟𝗲𝗮𝘃𝗲 𝘁𝗵𝗲 𝗴𝗿𝗼𝘂𝗽 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁 𝘄𝗵𝗲𝗿𝗲 —••÷[🕊NORDED🕊]÷••—𝘄𝗮𝘀 𝗽𝗹𝗮𝘆𝗶𝗻𝗴.
𝗖𝗹𝗲𝗮𝗻 𝘁𝗵𝗲 𝗽𝗹𝗮𝘆𝗹𝗶𝘀𝘁 𝗮𝗻𝗱 𝘀𝘁𝗼𝗽 𝗮𝗹𝗹 𝗺𝘂𝘀𝗶𝗰..
𝗣𝗮𝘂𝘀𝗲 𝗺𝘂𝘀𝗶𝗰 𝗶𝗻 𝗴𝗿𝗼𝘂𝗽 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁.
𝗨𝗻-𝗽𝗮𝘂𝘀𝗲 𝘁𝗵𝗲 𝗺𝘂𝘀𝗶𝗰 𝗶𝗻 𝗴𝗿𝗼𝘂𝗽 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁.
𝗣𝗹𝗮𝘆 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗯𝗲𝗴𝗶𝗻𝗻𝗶𝗻𝗴 𝗼𝗴 𝗰𝘂𝗿𝗿𝗲𝗻𝘁 𝗺𝘂𝘀𝗶𝗰 𝗯𝗲𝗶𝗻𝗴 𝗽𝗹𝗮𝘆𝗲𝗱.
𝗠𝗼𝘃𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗻𝗲𝘅𝘁 𝘁𝗿𝗮𝗰𝗸 𝗼𝗿 𝗦𝗸𝗶𝗽 𝘁𝗿𝗮𝗰𝗸 𝗶𝗻 𝗾𝘂𝗲𝘂𝗲 𝗹𝗶𝗸𝗲 : "𝗻𝗲𝘅𝘁 𝟮".
𝗖𝗹𝗲𝗮𝗻 𝘁𝗲𝗺𝗽 𝗮𝘂𝗱𝗶𝗼 𝗳𝗶𝗹𝗲𝘀 𝗶𝗻 𝘀𝗲𝗿𝘃𝗲𝗿 𝗼𝗳 🕊Norded Smart Music Player🕊.
𝗧𝘂𝗿𝗻 𝗼𝗳𝗳 𝗛𝗘𝗥𝗢𝗞𝗨 𝗗𝘆𝗻𝗼 𝗳𝗼𝗿 🕊Norded Smart Music Player🕊.
𝗥𝗲𝗯𝗼𝗼𝘁 —••÷[🕊NORDED🕊]÷••—𝗺𝗮𝗻𝘂𝗮𝗹𝗹𝘆 𝗶𝗻 𝗛𝗘𝗥𝗢𝗞𝗨.
𝗙𝗶𝗻𝗱 —••÷[🕊NORDED🕊]÷••—𝗛𝗘𝗥𝗢𝗞𝗨 𝗱𝘆𝗻𝗼 𝘂𝘀𝗮𝗴𝗲
"""
NORDEDBΣ=f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}`ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ᴏɴʟʏ ꜰᴏʀ ɴᴏʀᴅ ᴀᴅᴍɪɴꜱ ᴏꜰ ᴛʜᴇ ɢʀᴏᴜᴘꜱ ᴡʜᴇʀᴇ —••÷[🕊NORDED🕊]÷••—ɪꜱ ᴘʟᴜɢɢᴇᴅ ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.`
**__If needed to know the commands then use /nord__**

[𝗣𝗹𝗲𝗮𝘀𝗲 𝘂𝘀𝗲 𝗶𝗻 𝗴𝗿𝗼𝘂𝗽𝘀.](https://t.me/hypevoidsoul)"""


async def 𝙽𝙾𝚁𝙴𝙳_VERITY(_, __, ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    if ΣOЯ.from_user.id in NORD_ADMINS:
        return True
    return False
𝙽𝙾𝚁𝙴𝙳_ADMINS = filters.create(𝙽𝙾𝚁𝙴𝙳_VERITY)


async def 𝙽𝙾𝚁𝙴𝙳_CONNECTED(_, __, ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
    if not (ռօʀɖʀɨռɢ and ռօʀɖʀɨռɢ.is_connected):
        return False
    return True
𝙽𝙾𝚁𝙴𝙳_RINGER = filters.create(𝙽𝙾𝚁𝙴𝙳_CONNECTED)


async def 𝙽𝙾𝚁𝙴𝙳_GHOST(_, __, ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    return bool(
    ΣOЯ.from_user is None 
    and ΣOЯ.sender_chat
    )
Nord_Ghost = filters.create(𝙽𝙾𝚁𝙴𝙳_GHOST)

"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"
"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"plug",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def plug(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            NORDEDBΣ,
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoidsoul",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"stream",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def stream(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            NORDEDBΣ,
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"next",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def next(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            NORDEDBΣ,
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.command(
"nord"))
async def nord(bot, update):
    try:
        try:
            text = INFO_CATEG.format(update.from_user.mention)
            reply_markup = HELP_BUTTONS
            pic=𝙽𝙾𝚁𝙴𝙳_HUD
            await update.reply_photo(
            photo=pic,
            caption=text,
            reply_markup=reply_markup)
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            ΣOЯ = ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ
            await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)            
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"

"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_callback_query()
async def cb_data(bot, update):
    try:
        try:
            if update.data == "help":
                await update.message.edit(
                text=INFO_CATEG,
                reply_markup=HELP_BUTTONS
                )
            elif update.data == "𝙈𝙚𝙢𝙗𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 💛":
                await update.message.edit(
                text=MEMBER_CATEG,
                reply_markup=MEM_BUTT
                )
            elif update.data == "𝘼𝙙𝙢𝙞𝙣 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 ⚜️":
                await update.message.edit(
                text=ADMIN_CATEG,
                reply_markup=ADM_BUTT
                )
            elif update.data == "𝙃𝙚𝙧𝙤𝙠𝙪 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 🟣":
                await update.message.edit(
                text=HEROKU_CATEG,
                reply_markup=HERO_BUTT
                )
            elif update.data == "𝙀𝙭𝙞𝙩 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪🔺":
                await update.message.delete()
            else:
                return False
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            ΣOЯ = ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ
            await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"


"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"norded",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def norded(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            NORDEDBΣ,
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/KrakinzC",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/Hypevoisoul")
            ]]))
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"end",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def end(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            NORDEDBΣ,
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"replay",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def replay(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            NORDEDBΣ,
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"pause",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def pause(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            NORDEDBΣ,
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"resume",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def resume(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            NORDEDBΣ,
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"temp",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def temp(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            NORDEDBΣ,
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.command(
"ping",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def ping_pong(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            await ΣOЯ.delete()
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            start = datetime.now()
            end = datetime.now()
            delta_energy1 = (end - start).seconds
            delta_energy2= (end - start).microseconds
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
|   𝚂𝚎𝚛𝚟𝚎𝚛 𝚛𝚎𝚜𝚙𝚘𝚗𝚜𝚎 𝚝𝚒𝚖𝚎 𝚒𝚜   |
    📡 **{delta_energy1}** `𝙨𝙚𝙘𝙤𝙣𝙙𝙨` 
    📡 **{delta_energy2}** `𝙢𝙞𝙘𝙧𝙤𝙨𝙚𝙘𝙤𝙣𝙙𝙨`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
            await asyncio.sleep(
            CLEANER
            )
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.command(
"license"))
async def on_license(
_,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=LICENSE,
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& filters.command("start"))
async def on_start(
_,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            try:
                PERM = await ΣOЯ.reply_text("**CHECKING BOT PERMISSIONS.........**")
                await asyncio.sleep(2)
                await PERM.delete()
                await ΣOЯ.delete()
            except Exception:
                await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
@Admins 𝘗𝘭𝘦𝘢𝘴𝘦 𝘮𝘢𝘬𝘦 [𝙽𝚘𝚛𝚍𝚎𝚍 𝚂𝚖𝚊𝚛𝚝 𝙼𝚞𝚜𝚒𝚌 𝙿𝚕𝚊𝚢𝚎𝚛](https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg) 𝘢𝘥𝘮𝘪𝘯.

    **Bot is missing required permissions to work properly.**
    `❌ CHAT_ADMIN`
    `❌ RIGHT TO DELETE`
    `❌ RIGHT TO PIN MESSAGE`

𝘖𝘯𝘤𝘦 𝘨𝘪𝘷𝘦𝘯 𝘱𝘳𝘰𝘱𝘦𝘳 𝘳𝘪𝘨𝘩𝘵, 𝘣𝘰𝘵 𝘸𝘪𝘭𝘭 𝘴𝘵𝘰𝘱 𝘴𝘦𝘯𝘥𝘪𝘯𝘨 𝘢𝘯𝘺 𝘴𝘶𝘤𝘩 𝘦𝘳𝘳𝘰𝘳 𝘯𝘰𝘵𝘪𝘧𝘪𝘤𝘢𝘵𝘪𝘰𝘯𝘴.

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
            disable_notification=False)
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.command(
"start"))
async def on_start(
_,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
**I ΛM** [𝙽𝚘𝚛𝚍𝚎𝚍 𝚂𝚖𝚊𝚛𝚝 𝙼𝚞𝚜𝚒𝚌 𝙿𝚕𝚊𝚢𝚎𝚛](https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg) 
**𝘧𝘰𝘳 𝘱𝘭𝘢𝘺𝘪𝘯𝘨 𝘮𝘶𝘴𝘪𝘤 𝘪𝘯 𝘵𝘩𝘦 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵𝘴 𝘰𝘧 𝘛𝘦𝘭𝘦𝘨𝘳𝘢𝘮 𝘎𝘳𝘰𝘶𝘱𝘴 & 𝘊𝘩𝘢𝘯𝘯𝘦𝘭𝘴**.

𝚂𝚎𝚗𝚍 𝚖𝚎 `/nord` 𝚏𝚘𝚛 𝚖𝚘𝚛𝚎 𝚒𝚗𝚏𝚘.

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
async def roku():
    try:
        HEROKU = heroku3.from_key(HEROKU_API_KEY)
        app = HEROKU.apps()[HEROKU_APP_NAME]
        app.restart()
        # ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ
        # await ΣOЯ.reply_photo(
        # photo=𝙽𝙾𝚁𝙴𝙳_HUD,
        # caption=f"{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ} **𝙽𝙾𝚁𝙳𝙴𝙳 𝙝𝙖𝙨 𝙘𝙡𝙚𝙖𝙣𝙚𝙙 𝙪𝙥 𝙖𝙣𝙙 𝙧𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙 𝙞𝙩𝙨𝙚𝙡𝙛!**",
        # reply_markup=HypeKeyboardMarkup([[
        # HypeKeyboardButton(
        # text="🕊DΣV GЯӨЦP",
        # url=f"https://t.me/Krakns",),],[
        # HypeKeyboardButton(
        # text="✨••Hype Void Lab••✨",
        # url=f"https://t.me/KrakinzBot")
        # ]]))
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~filters.edited
& 𝙽𝙾𝚁𝙴𝙳_ADMINS
& filters.command(
"restart",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def restart(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            if HEROKU_API_KEY is not None and HEROKU_APP_NAME is not None:
                await ΣOЯ.delete()
                ΣOЯPS = await ΣOЯ.reply_photo(
                photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                caption=
                f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
⚠️𝘔𝘢𝘯𝘶𝘢𝘭𝘭𝘺 𝘳𝘦𝘴𝘵𝘢𝘳𝘵𝘪𝘯𝘨 𝘏𝘦𝘳𝘰𝘬𝘶-𝘋𝘺𝘯𝘰.
𝙋𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩 𝙛𝙤𝙧 30𝙨𝙚𝙘-1𝙢𝙞𝙣

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
                reply_markup=
            HypeKeyboardMarkup([[
                HypeKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/Krakns",),],[
                HypeKeyboardButton(
                text="✨••Hype Void Lab••✨",
                url=f"https://t.me/KrakinzBot")
                ]]))
                await roku()
                # await asyncio.sleep(15)
                # await ΣOЯPS.delete()
                # await ΣOЯ.reply_photo(
                # photo=𝙽𝙾𝚁𝙴𝙳_HUD,
                # caption=f"{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ} Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  **{𝙽𝙾𝚁𝙴𝙳_MENTION}**\n  **𝙽𝙾𝚁𝙳𝙴𝙳 𝙝𝙖𝙨 𝙘𝙡𝙚𝙖𝙣𝙚𝙙 𝙪𝙥 𝙖𝙣𝙙 𝙧𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙 𝙞𝙩𝙨𝙚𝙡𝙛!**",
                # reply_markup=HypeKeyboardMarkup([[
                # HypeKeyboardButton(
                # text="🕊DΣV GЯӨЦP",
                # url=f"https://t.me/Krakns",),],[
                # HypeKeyboardButton(
                # text="✨••Hype Void Lab••✨",
                # url=f"https://t.me/KrakinzBot")
                # ]]))
                # lic = await ΣOЯ.reply_photo(
                # photo=𝙽𝙾𝚁𝙴𝙳_HUD,
                # caption=f"{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ} Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  **{𝙽𝙾𝚁𝙴𝙳_MENTION}**\n{LICENSE}")
                # await asyncio.sleep(12)
                # await lic.delete()
            else:
                if HEROKU_API_KEY is None:
                    await ΣOЯ.delete()
                    await ΣOЯ.reply_photo(
                    photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                    caption=
                    f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  {OWNER_USERNAME}

⚠️𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 𝘺𝘰𝘶𝘳 𝗛𝗘𝗥𝗢𝗞𝗨_𝗔𝗣𝗜_𝗞𝗘𝗬 𝘪𝘴 𝘦𝘪𝘵𝘩𝘦𝘳 𝘦𝘮𝘱𝘵𝘺 𝘰𝘳 𝘸𝘳𝘰𝘯𝘨.

𝗣𝗹𝗲𝗮𝘀𝗲 𝗳𝗶𝘅 𝗶𝘁 𝗮𝗻𝗱 𝗯𝗼𝘁 𝘄𝗶𝗹𝗹 𝘄𝗼𝗿𝗸 𝗽𝗲𝗿𝗳𝗲𝗰𝘁𝗹𝘆!

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
                    reply_markup=
            HypeKeyboardMarkup([[
                    HypeKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/Krakns",),],[
                    HypeKeyboardButton(
                    text="✨••Hype Void Lab••✨",
                    url=f"https://t.me/KrakinzBot")
                    ]]))
                elif HEROKU_APP_NAME is None:
                    await ΣOЯ.delete()
                    await ΣOЯ.reply_photo(
                    photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                    caption=
                    f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  {OWNER_USERNAME}

⚠️𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 𝘺𝘰𝘶𝘳 𝗛𝗘𝗥𝗢𝗞𝗨_𝗔𝗣𝗣_𝗡𝗔𝗠𝗘 𝘪𝘴 𝘦𝘪𝘵𝘩𝘦𝘳 𝘦𝘮𝘱𝘵𝘺 𝘰𝘳 𝘸𝘳𝘰𝘯𝘨.

𝗣𝗹𝗲𝗮𝘀𝗲 𝗳𝗶𝘅 𝗶𝘁 𝗮𝗻𝗱 𝗯𝗼𝘁 𝘄𝗶𝗹𝗹 𝘄𝗼𝗿𝗸 𝗽𝗲𝗿𝗳𝗲𝗰𝘁𝗹𝘆!

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
                    reply_markup=
            HypeKeyboardMarkup([[
                    HypeKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/Krakns",),],[
                    HypeKeyboardButton(
                    text="✨••Hype Void Lab••✨",
                    url=f"https://t.me/KrakinzBot")
                    ]]))
                elif HEROKU_API_KEY is None and HEROKU_APP_NAME is None:
                    await ΣOЯ.delete()
                    await ΣOЯ.reply_photo(
                    photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                    caption=
                    f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  {OWNER_USERNAME}

⚠️𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 𝘺𝘰𝘶𝘳 𝗛𝗘𝗥𝗢𝗞𝗨_𝗔𝗣𝗜_𝗞𝗘𝗬 𝗮𝗻𝗱 𝗛𝗘𝗥𝗢𝗞𝗨_𝗔𝗣𝗣_𝗡𝗔𝗠𝗘 𝘪𝘴 𝘦𝘪𝘵𝘩𝘦𝘳 𝘦𝘮𝘱𝘵𝘺 𝘰𝘳 𝘸𝘳𝘰𝘯𝘨.

𝗣𝗹𝗲𝗮𝘀𝗲 𝗳𝗶𝘅 𝗶𝘁 𝗮𝗻𝗱 𝗯𝗼𝘁 𝘄𝗶𝗹𝗹 𝘄𝗼𝗿𝗸 𝗽𝗲𝗿𝗳𝗲𝗰𝘁𝗹𝘆!

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
                    reply_markup=
            HypeKeyboardMarkup([[
                    HypeKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/Krakns",),],[
                    HypeKeyboardButton(
                    text="✨••Hype Void Lab••✨",
                    url=f"https://t.me/KrakinzBot")
                    ]]))
                else:
                    await ΣOЯ.delete()
                    await ΣOЯ.reply_photo(
                    photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                    caption=
                    f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ} 
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
𝐏𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐇𝐞𝐫𝐨𝐤𝐮 𝐥𝐨𝐠𝐬 𝐭𝐨 @Krakns 𝐢𝐟 𝐚𝐧𝐲𝐭𝐡𝐢𝐧𝐠 𝐰𝐫𝐨𝐧𝐠 𝐡𝐚𝐩𝐩𝐞𝐧𝐬

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
                    reply_markup=
            HypeKeyboardMarkup([[
                    HypeKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/Krakns",),],[
                    HypeKeyboardButton(
                    text="✨••Hype Void Lab••✨",
                    url=f"https://t.me/KrakinzBot")
                    ]]))
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
# @𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
# filters.chat(
# CHAT_ID
# )
# & ~filters.edited
# & 𝙽𝙾𝚁𝙴𝙳_ADMINS
# & filters.command(
# "shutdown",
# 𝙽𝙾𝚁𝙴𝙳_FIXER
#))
# async def shutdown(
# client,
# ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
#     try:
#         try:
#             𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
#             await ΣOЯ.delete()
#             shuts = await ΣOЯ.reply_photo(
#             photo=
#            𝙽𝙾𝚁𝙴𝙳_HUD,
#             caption=
#            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
# Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  **{𝙽𝙾𝚁𝙴𝙳_MENTION}**# ⚠️`𝗧𝘂𝗿𝗶𝗻𝗴 𝗢𝗳𝗳 𝗛𝗲𝗿𝗼𝗸𝘂 𝗗𝘆𝗻𝗼𝘀 𝗳𝗼𝗿 NORDED🕊 𝗺𝘂𝘀𝗶𝗰 𝗽𝗹𝗮𝘆𝗲𝗿.\n𝗠𝗮𝗻𝘂𝗮𝗹𝗹𝘆 𝘁𝘂𝗿𝗻 𝗶𝘁 𝗼𝗻 𝘁𝗼 𝘀𝘁𝗮𝗿𝘁 𝗮𝗴𝗮𝗶𝗻.`
# """
# )
#             await asyncio.sleep(6)
#             await shuts.delete()
#             if HEROKU_APP_NAME is not None:
#                 #HEROKU_APP_NAME.process_formation()["worker"].scale(0)
#                 HEROKU = heroku3.from_key(HEROKU_API_KEY)
#                 app = HEROKU.apps()[HEROKU_APP_NAME]
#                 app.kill_dyno(HEROKU_APP_NAME)
#                 app.dynos['run.1'].kill()
#             else:
#                 HEROKU = heroku3.from_key(HEROKU_API_KEY)
#                 app = HEROKU.apps()[HEROKU_APP_NAME]
#                 app.kill()
#                 sys.exit()
#         except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
#             𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
#             animation=
#            𝙽𝙾𝚁𝙴𝙳_ERROR,
#             caption=
#         f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
# Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
#🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
# ⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
# **𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

# `{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`
# """
# )
#             await asyncio.sleep(CLEANER)
#             await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
#     except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
#         print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
#         sys.exit()
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.command("usage",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def usage(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            event = await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
⚠️**𝗔𝘀𝗸𝗶𝗻𝗴 𝗛𝗲𝗿𝗼𝗸𝘂 𝗮𝗻𝗱 𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝗥𝗲𝗾𝘂𝗲𝘀𝘁**

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            useragent = (
                "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/80.0.3987.149 Mobile Safari/537.36"
            )
            user_id = HRKU.account().id
            headers = {
                "User-Agent": useragent,
                "Authorization": f"Bearer {HEROKU_API_KEY}",
                "Accept": "application/vnd.heroku+json; version=3.account-quotas",
            }
            path = "/accounts/" + user_id + "/actions/get-quota"
            r = requests.get(heroku_api + path, headers=headers)
            if r.status_code != 200:
                return await event.edit(
                    "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
                )
            result = r.json()
            quota = result["account_quota"]
            quota_used = result["quota_used"]

            """ - Used - """
            remaining_quota = quota - quota_used
            percentage = math.floor(remaining_quota / quota * 100)
            minutes_remaining = remaining_quota / 60
            hours = math.floor(minutes_remaining / 60)
            minutes = math.floor(minutes_remaining % 60)

            """ - Current - """
            App = result["apps"]
            try:
                App[0]["quota_used"]
            except IndexError:
                AppQuotaUsed = 0
                AppPercentage = 0
            else:
                AppQuotaUsed = App[0]["quota_used"] / 60
                AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
            AppHours = math.floor(AppQuotaUsed / 60)
            AppMinutes = math.floor(AppQuotaUsed % 60)
            await asyncio.sleep(1.5)
            return await event.edit(
            f""""
👾 **Dyno Usage** 👾:
➠ __Dyno usage for__ • **{HEROKU_APP_NAME}** • :
★  `{AppHours}**h**  `{AppMinutes}**min**  
**|**  `{AppPercentage}**%**"
➠ __Dyno hours remaining this month__ :
★  `{hours}**h**  `{minutes}**YΣ**  
**|**  `{percentage}**%**

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"LET ME TRY TO MAKE THE CODE FOR DIRECT YOUTUBE PLAY USING /yt COMMAND"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& 𝙽𝙾𝚁𝙴𝙳_RINGER
& ~filters.edited
& filters.command(
"yt",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def yt(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            query = ''
            for i in ΣOЯ.command[1:]:
                query += ' ' + str(i)
            ydl_opts = {
            "format":
            "bestaudio[ext=m4a]"}
            try:
                results = []
                count = 0
                while len(results) == 0 and count < 6:
                    if count>0:
                        results = YoutubeSearch(
                        query,
                        max_results=1).to_dict()
                    count += 1
                try:
                    𝙽𝙾𝚁𝙴𝙳_PSYCODE =  await ΣOЯ.reply_animation(
                    animation="worklord/norded_dling.gif",
                    duration=4,
                    caption=
                    f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
𝘗𝘭𝘦𝘢𝘴𝘦 𝘞𝘢𝘪𝘵 𝘵𝘪𝘭𝘭 **𝙽𝚘𝚛𝚍𝚎𝚍 𝚂𝚖𝚊𝚛𝚝 𝙼𝚞𝚜𝚒𝚌 𝙿𝚕𝚊𝚢𝚎𝚛** 𝘥𝘰𝘸𝘯𝘭𝘰𝘢𝘥𝘴 𝘢𝘯𝘥 𝘤𝘰𝘯𝘷𝘦𝘳𝘵𝘴 𝘈𝘶𝘥𝘪𝘰 𝘧𝘰𝘳 𝘴𝘵𝘳𝘦𝘢𝘮𝘪𝘯𝘨 𝘪𝘯 𝘵𝘩𝘦 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵!

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
                    link = f"https://youtube.com{results[0]['url_suffix']}"
                    title = results[
                    0][
                    "title"]
                    thumbnail = results[
                    0][
                    "thumbnails"][
                    0]
                    duration = results[0][
                    "duration"]
                    views = results[
                    0][
                    "views"]
                    NORDED_THUMBNAIL = f'🎧•NORDED•🎧 by 🔥ΉYPΣ VӨID LΛB🔥-𝙽𝙾𝚁𝙳𝙴𝙳{ΣOЯ.message_id}.jpg'
                    thumb = requests.get(
                    thumbnail,
                    allow_redirects=False
                    )
                    open(
                    NORDED_THUMBNAIL,
                    'wb').write(
                    thumb.content
                    )

                except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
                    𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC =  await ΣOЯ.reply_photo(
                    photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                    caption=
                    f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
✖️**𝗙𝗼𝘂𝗻𝗱 𝗻𝗼𝘁𝗵𝗶𝗻𝗴. 𝗧𝗿𝘆 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝘁𝗵𝗲 𝘀𝗽𝗲𝗹𝗹𝗶𝗻𝗴 𝗮 𝗹𝗶𝘁𝘁𝗹𝗲.**

𝘗𝘭𝘦𝘢𝘴𝘦 𝘐𝘯𝘧𝘰𝘳𝘮 @Krakinz or @Krakns:
`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
                    reply_markup=
            HypeKeyboardMarkup([[
                    HypeKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/Krakns",),],[
                    HypeKeyboardButton(
                    text="✨••Hype Void Lab••✨",
                    url=f"https://t.me/KrakinzBot")
                    ]]))
                    await asyncio.sleep(CLEANER)
                    await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
                    return
                    
            except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
                𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
                photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                caption=
                f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
✖️**𝗙𝗼𝘂𝗻𝗱 𝗻𝗼𝘁𝗵𝗶𝗻𝗴. 𝗧𝗿𝘆 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝘁𝗵𝗲 𝘀𝗽𝗲𝗹𝗹𝗶𝗻𝗴 𝗮 𝗹𝗶𝘁𝘁𝗹𝗲.**

𝘗𝘭𝘦𝘢𝘴𝘦 𝘐𝘯𝘧𝘰𝘳𝘮 @Krakinz or @Krakns:
`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",          
                reply_markup=
            HypeKeyboardMarkup([[
                HypeKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/Krakns",),],[
                HypeKeyboardButton(
                text="✨••Hype Void Lab••✨",
                url=f"https://t.me/KrakinzBot")
                ]]))
                await asyncio.sleep(CLEANER)
                await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
                return
            try:
                with youtube_dl.YoutubeDL(ydl_opts) as nordl:
                    info_dict = nordl.extract_info(
                    link,
                    download=False
                    )
                    𝙽𝙾𝚁𝙴𝙳_AUDIO_SOURCE = nordl.prepare_filename(
                    info_dict
                    )
                    nordl.process_info(
                    info_dict
                    )

                𝙽𝙾𝚁𝙴𝙳_CAP = f"""
📜`ᴀᴜᴅɪᴏ ᴛɪᴛʟᴇ`: **[{title[:35]}]({link})**
⏳`ᴀᴜᴅɪᴏ ᴅᴜʀᴀᴛɪᴏɴ`: **[{duration}]({link})**

☢️𝘛𝘩𝘪𝘴 𝘈𝘶𝘥𝘪𝘰 𝘪𝘴 𝘴𝘦𝘯𝘵 𝘣𝘺 **𝙽𝚘𝚛𝚍𝚎𝚍 𝚂𝚖𝚊𝚛𝚝 𝙼𝚞𝚜𝚒𝚌 𝙿𝚕𝚊𝚢𝚎𝚛** 𝘧𝘰𝘳 𝘰𝘯𝘭𝘺 𝘴𝘵𝘳𝘦𝘢𝘮𝘪𝘯𝘨 𝘪𝘯 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵𝘴❗️
🤖𝘗𝘭𝘦𝘢𝘴𝘦 𝘶𝘴𝘦 𝘉𝘦𝘭𝘰𝘸 𝘉𝘰𝘵𝘴 𝘵𝘰 𝘥𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘢𝘯𝘺 𝘰𝘵𝘩𝘦𝘳 𝘠𝘰𝘶𝘛𝘶𝘣𝘦 𝘝𝘪𝘥𝘦𝘰/𝘈𝘶𝘥𝘪𝘰 𝘪𝘯 𝘜𝘏𝘋
"""
                secmul, dur, dur_arr = 1, 0, duration.split(':')
                for i in range(len(dur_arr)-1, -1, -1):
                    dur += (int(
                    dur_arr[i]) * secmul)
                    secmul *= 60

                await 𝙽𝙾𝚁𝙴𝙳_PSYCODE.delete()
                psychoded = await ΣOЯ.reply_animation(
                animation="https://telegra.ph/file/c8f986b67bb8b3ab566b3.mp4",
                caption=
                f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
🔥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ꜰɪɴɪꜱʜᴇᴅ

𝗔𝘂𝗱𝗶𝗼 𝗯𝗲𝗶𝗻𝗴 𝗽𝗿𝗲𝗽𝗱 𝗳𝗼𝗿 𝗦𝘁𝗿𝗲𝗮𝗺𝗶𝗻𝗴 𝘂𝘀𝗶𝗻𝗴 
**𝙽𝚘𝚛𝚍𝚎𝚍 𝚂𝚖𝚊𝚛𝚝 𝙼𝚞𝚜𝚒𝚌 𝙿𝚕𝚊𝚢𝚎𝚛**

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/hypevoidsoul)
"""
)

                ADU = await ΣOЯ.reply_audio(
                audio=𝙽𝙾𝚁𝙴𝙳_AUDIO_SOURCE,
                caption=𝙽𝙾𝚁𝙴𝙳_CAP,
                title=title,
                duration=dur,
                thumb=NORDED_THUMBNAIL,
                reply_markup=
            HypeKeyboardMarkup([[
                HypeKeyboardButton(
                text="📷 YouTube Downloader",
                url=f"https://t.me/HVYouTubeBot",),],[
                HypeKeyboardButton(
                text="⭕️ YouTube Music Downloader",
                url=f"https://t.me/HVYouTubeMusicBot",),],[
                HypeKeyboardButton(
                text="✨••Hype Void Lab••✨",
                url=f"https://t.me/KrakinzBot")
                ]]))

                await psychoded.delete()
                await ADU.reply_photo(
                photo=NORDED_THUMBNAIL,
                caption=NORN
                )
                await asyncio.sleep(CLEANER)


            except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
                𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_text(
                f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
❌ Error

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
                await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
            try:
                os.remove(𝙽𝙾𝚁𝙴𝙳_AUDIO_SOURCE)
                os.remove(NORDED_THUMBNAIL)
                os.system("clear")
                cprint("Success and Cleared Screen", "cyan")
            except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
                𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_text(
                f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
❌ Error 𝘤𝘭𝘦𝘢𝘯𝘪𝘯𝘨 𝘺𝘵 𝘵𝘦𝘮𝘱 𝘧𝘪𝘭𝘦𝘴.

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
 Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
# @𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
# filters.chat(
# CHAT_ID
#)
# & 𝙽𝙾𝚁𝙴𝙳_RINGER
# & ~filters.edited
# & filters.command(
# "ytlicoius",
# 𝙽𝙾𝚁𝙴𝙳_FIXER
#))
# async def yt(
# client,
# ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
#     try:
#         𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
#         await ΣOЯ.delete()
#         query = ''
#         for i in ΣOЯ.command[1:]:
#             query += ' ' + str(i)
#         ydl_opts = {
#         "format":
#         "bestaudio[ext=m4a]"}
#         try:
#             results = []
#             count = 0
#             while len(results) == 0 and count < 6:
#                 if count>0:
#                     results = YoutubeSearch(
#                     query,
#                     max_results=1).to_dict()
#                 count += 1
#             try:
#                 link = f"https://youtube.com{results[0]['url_suffix']}"
#                 title = results[
#                 0][
#                 "title"]
#                 thumbnail = results[
#                 0][
#                 "thumbnails"][
#                 0]
#                 duration = results[0][
#                 "duration"]
#                 views = results[
#                 0][
#                 "views"]
#                 NORDED_THUMBNAIL = f'𝙽𝙾𝚁𝙳𝙴𝙳{ΣOЯ.message_id}.jpg'
#                 thumb = requests.get(
#                 thumbnail,
#                 allow_redirects=True)
#                 open(
#                 NORDED_THUMBNAIL,
#                 'wb').write(
#                 thumb.content)
#             except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
#                 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC =  await ΣOЯ.reply_photo(
#                 photo=
#                𝙽𝙾𝚁𝙴𝙳_HUD,
#                 caption=
#                f"""
#                 {ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ} Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  **{𝙽𝙾𝚁𝙴𝙳_MENTION}**\n✖️**𝗙𝗼𝘂𝗻𝗱 𝗻𝗼𝘁𝗵𝗶𝗻𝗴. 𝗧𝗿𝘆 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝘁𝗵𝗲 𝘀𝗽𝗲𝗹𝗹𝗶𝗻𝗴 𝗮 𝗹𝗶𝘁𝘁𝗹𝗲.**\n\n\n**Please Inform @Krakinz or @Krakns:>>**\n`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`""",
#                 reply_markup=
#            HypeKeyboardMarkup([[
#                 HypeKeyboardButton(
#                 text="🕊DΣV GЯӨЦP",
#                 url=f"https://t.me/Krakns",),],[
#                 HypeKeyboardButton(
#                 text="🔖ɢɪᴛʜᴜʙ",
#                 url=f"https://t.me/KrakinzBot",),],[
#                 HypeKeyboardButton(
#                 text="✨••Hype Void Lab••✨",
#                 url=f"https://t.me/KrakinzBot")
#                 ]]))
#                 await asyncio.sleep(
#            CLEANER
#           )
#                 await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
#                 return
#         except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
#             𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
#             photo=
#            𝙽𝙾𝚁𝙴𝙳_HUD,
#             caption=
#            f"""
#             {ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ} Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  **{𝙽𝙾𝚁𝙴𝙳_MENTION}**\n✖️ **𝙁𝙤𝙪𝙣𝙙 𝙉𝙤𝙩𝙝𝙞𝙣𝙜. 𝙎𝙤𝙧𝙧𝙮.**\n\n**𝗧𝗿𝘆 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗸𝗲𝘆𝘄𝗼𝗿𝗱 𝗼𝗿 𝗺𝗮𝘆𝗯𝗲 𝘀𝗽𝗲𝗹𝗹 𝗶𝘁 𝗽𝗿𝗼𝗽𝗲𝗿𝗹𝘆.**\n\n\n**Please Inform @Krakinz or @Krakns:>>**\n`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`""",
#             reply_markup=
#            HypeKeyboardMarkup([[
#             HypeKeyboardButton(
#             text="🕊DΣV GЯӨЦP",
#             url=f"https://t.me/Krakns",),],[
#             HypeKeyboardButton(
#             text="🔖ɢɪᴛʜᴜʙ",
#             url=f"https://t.me/KrakinzBot",),],[
#             HypeKeyboardButton(
#             text="✨••Hype Void Lab••✨",
#             url=f"https://t.me/KrakinzBot")
#             ]]))
#             await asyncio.sleep(
#           CLEANER
#           )
#             await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
#             return
#         try:
#             with youtube_dl.YoutubeDL(ydl_opts) as nordl:
#                 info_dict = nordl.extract_info(link, download=False)
#                 𝙽𝙾𝚁𝙴𝙳_AUDIO_SOURCE = nordl.prepare_filename(info_dict)
#                 nordl.process_info(info_dict)
#             𝙽𝙾𝚁𝙴𝙳_CAP = f'🎧 **Title**: [{title[:35]}]({link})\n⏳ **Duration**: `{duration}`\n👁‍🗨 **Views**: `{views}`'
#             secmul, dur, dur_arr = 1, 0, duration.split(':')
#             for i in range(len(dur_arr)-1, -1, -1):
#                 dur += (int(dur_arr[i]) * secmul)
#                 secmul *= 60
#             chat_id = int(str(ΣOЯ.chat.id))
#             ADU = await ΣOЯ.reply_audio(
#             audio=𝙽𝙾𝚁𝙴𝙳_AUDIO_SOURCE,
#             caption=𝙽𝙾𝚁𝙴𝙳_CAP,
#             title=title,
#             duration=dur,
#             thumb=NORDED_THUMBNAIL
#             )
#             await ADU.reply_photo(
#             photo=NORDED_THUMBNAIL,
#             caption=NORN,
#             reply_markup=
#            HypeKeyboardMarkup([[
#             HypeKeyboardButton(
#             text="🕊DΣV GЯӨЦP",
#             url=f"https://t.me/Krakns",),],[
#             HypeKeyboardButton(
#             text="🔖ɢɪᴛʜᴜʙ",
#             url=f"https://t.me/KrakinzBot",),],[
#             HypeKeyboardButton(
#             text="✨••Hype Void Lab••✨",
#             url=f"https://t.me/KrakinzBot")
#             ]]))
#         except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
#             𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_text(f"{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ} Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  **{𝙽𝙾𝚁𝙴𝙳_MENTION}**\n❌ Error\n\n`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`")
#             await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
#         try:
#             os.remove(𝙽𝙾𝚁𝙴𝙳_AUDIO_SOURCE)
#             os.remove(NORDED_THUMBNAIL)
#         except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
#             𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_text(f"{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ} Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  **{𝙽𝙾𝚁𝙴𝙳_MENTION}**\n❌ Error cleaning yt temp files.\n\n`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`")
#     except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
#         await ΣOЯ.reply_photo(
#         photo=
#        𝙽𝙾𝚁𝙴𝙳_HUD,
#         caption=
#        f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
# Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
#🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
# ⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**\n**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**\n\n `{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`
# """)
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~𝙽𝙾𝚁𝙴𝙳_RINGER
& ~filters.edited
& filters.command(
"stream",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def stream(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
🕊 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🕊

⚠️𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 —••÷[🕊NORDED🕊]÷••— 𝘩𝘢𝘴 𝘯𝘰𝘵 𝘣𝘦𝘦𝘯 𝘪𝘯𝘪𝘵𝘪𝘢𝘭𝘪𝘻𝘦𝘥 𝘺𝘦𝘵 𝘢𝘯𝘥 **__{chat.title}__** 𝘩𝘢𝘴 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵/𝘤𝘢𝘭𝘭 𝘯𝘰𝘵 𝘤𝘰𝘯𝘯𝘦𝘤𝘵𝘦𝘥 𝘺𝘦𝘵.
𝘗𝘭𝘦𝘢𝘴𝘦 𝘢𝘴𝘬 𝘕𝘖𝘙𝘋-𝘈𝘋𝘔𝘐𝘕𝘚 𝘰𝘧 **__{chat.title}__** 𝘵𝘰 𝘵𝘶𝘳𝘯 𝘪𝘵 𝘰𝘯 𝘧𝘪𝘳𝘴𝘵 𝘢𝘯𝘥 𝘳𝘦𝘵𝘳𝘺 /stream

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(
            CLEANER
            )
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~𝙽𝙾𝚁𝙴𝙳_RINGER
& ~filters.edited
& filters.command(
"pause",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def yt(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
    🕊 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🕊
⚠️𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 —••÷[🕊NORDED🕊]÷••— 𝘩𝘢𝘴 𝘯𝘰𝘵 𝘣𝘦𝘦𝘯 𝘪𝘯𝘪𝘵𝘪𝘢𝘭𝘪𝘻𝘦𝘥 𝘺𝘦𝘵 𝘢𝘯𝘥 **__{chat.title}__** 𝘩𝘢𝘴 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵/𝘤𝘢𝘭𝘭 𝘯𝘰𝘵 𝘤𝘰𝘯𝘯𝘦𝘤𝘵𝘦𝘥 𝘺𝘦𝘵.
𝘗𝘭𝘦𝘢𝘴𝘦 𝘢𝘴𝘬 𝘕𝘖𝘙𝘋-𝘈𝘋𝘔𝘐𝘕𝘚 𝘰𝘧 **__{chat.title}__** 𝘵𝘰 𝘵𝘶𝘳𝘯 𝘪𝘵 𝘰𝘯 𝘧𝘪𝘳𝘴𝘵 𝘢𝘯𝘥 𝘳𝘦𝘵𝘳𝘺 /pause

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(
            CLEANER
            )
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~𝙽𝙾𝚁𝙴𝙳_ADMINS
& 𝙽𝙾𝚁𝙴𝙳_RINGER
& ~filters.edited
& filters.command(
"pause",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def yt(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
🕊 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🕊
😲🐣𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 𝘺𝘰𝘶 𝘢𝘳𝘦 𝘯𝘰𝘵 𝘢 𝘷𝘢𝘭𝘪𝘥 𝘕𝘖𝘙𝘋-𝘈𝘥𝘮𝘪𝘯.
𝘗𝘭𝘦𝘢𝘴𝘦 𝘶𝘴𝘦 `/nord` 𝘵𝘰 𝘤𝘩𝘦𝘤𝘬 𝘔𝘦𝘮𝘣𝘦𝘳 𝘰𝘯𝘭𝘺 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴
"""
)
            await asyncio.sleep(
            CLEANER
            )
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~𝙽𝙾𝚁𝙴𝙳_RINGER
& ~filters.edited
& filters.command(
"resume",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def yt(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
    🕊 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🕊
⚠️𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 —••÷[🕊NORDED🕊]÷••— 𝘩𝘢𝘴 𝘯𝘰𝘵 𝘣𝘦𝘦𝘯 𝘪𝘯𝘪𝘵𝘪𝘢𝘭𝘪𝘻𝘦𝘥 𝘺𝘦𝘵 𝘢𝘯𝘥 **__{chat.title}__** 𝘩𝘢𝘴 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵/𝘤𝘢𝘭𝘭 𝘯𝘰𝘵 𝘤𝘰𝘯𝘯𝘦𝘤𝘵𝘦𝘥 𝘺𝘦𝘵.
𝘗𝘭𝘦𝘢𝘴𝘦 𝘢𝘴𝘬 𝘕𝘖𝘙𝘋-𝘈𝘋𝘔𝘐𝘕𝘚 𝘰𝘧 **__{chat.title}__** 𝘵𝘰 𝘵𝘶𝘳𝘯 𝘪𝘵 𝘰𝘯 𝘧𝘪𝘳𝘴𝘵 𝘢𝘯𝘥 𝘳𝘦𝘵𝘳𝘺 /resume

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(
            CLEANER
            )
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~𝙽𝙾𝚁𝙴𝙳_ADMINS
& 𝙽𝙾𝚁𝙴𝙳_RINGER
& ~filters.edited
& filters.command(
"resume",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def yt(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
🕊 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🕊

😲🐣𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 𝘺𝘰𝘶 𝘢𝘳𝘦 𝘯𝘰𝘵 𝘢 𝘷𝘢𝘭𝘪𝘥 𝘕𝘖𝘙𝘋-𝘈𝘥𝘮𝘪𝘯.
𝘗𝘭𝘦𝘢𝘴𝘦 𝘶𝘴𝘦 `/nord` 𝘵𝘰 𝘤𝘩𝘦𝘤𝘬 𝘔𝘦𝘮𝘣𝘦𝘳 𝘰𝘯𝘭𝘺 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴
"""
)
            await asyncio.sleep(
            CLEANER
            )
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~𝙽𝙾𝚁𝙴𝙳_RINGER
& ~filters.edited
& filters.command(
"unplug",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def yt(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
    🕊 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🕊
⚠️𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 —••÷[🕊NORDED🕊]÷••— 𝘩𝘢𝘴 𝘯𝘰𝘵 𝘣𝘦𝘦𝘯 𝘪𝘯𝘪𝘵𝘪𝘢𝘭𝘪𝘻𝘦𝘥 𝘺𝘦𝘵 𝘢𝘯𝘥 **__{chat.title}__** 𝘩𝘢𝘴 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵/𝘤𝘢𝘭𝘭 𝘯𝘰𝘵 𝘤𝘰𝘯𝘯𝘦𝘤𝘵𝘦𝘥 𝘺𝘦𝘵.
𝘗𝘭𝘦𝘢𝘴𝘦 𝘢𝘴𝘬 𝘕𝘖𝘙𝘋-𝘈𝘋𝘔𝘐𝘕𝘚 𝘰𝘧 **__{chat.title}__** 𝘵𝘰 𝘵𝘶𝘳𝘯 𝘪𝘵 𝘰𝘯 𝘧𝘪𝘳𝘴𝘵 𝘢𝘯𝘥 𝘳𝘦𝘵𝘳𝘺 /unplug

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(
            CLEANER
            )
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()


        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~𝙽𝙾𝚁𝙴𝙳_ADMINS
& 𝙽𝙾𝚁𝙴𝙳_RINGER
& ~filters.edited
& filters.command(
"unplug",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def yt(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
🕊 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🕊
😲🐣𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 𝘺𝘰𝘶 𝘢𝘳𝘦 𝘯𝘰𝘵 𝘢 𝘷𝘢𝘭𝘪𝘥 𝘕𝘖𝘙𝘋-𝘈𝘥𝘮𝘪𝘯.
𝘗𝘭𝘦𝘢𝘴𝘦 𝘶𝘴𝘦 `/nord` 𝘵𝘰 𝘤𝘩𝘦𝘤𝘬 𝘔𝘦𝘮𝘣𝘦𝘳 𝘰𝘯𝘭𝘺 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(
            CLEANER
            )
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()


        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~𝙽𝙾𝚁𝙴𝙳_RINGER
& ~filters.edited
& filters.command(
"vol",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def volume(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        usage = "**Usage:**\n/volume [1-200]"
        if len(ΣOЯ.command) != 2:
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=usage
            )
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
            return

        if "plug" not in db:
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption="VC isn't started"
            )
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
            return

        vc = db["plug"]
        volume = int(
        ΣOЯ.text.split(
        None, 1)[1])
        if (volume < 1) or (volume > 200):
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=usage
            )
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
            return
            
        try:
            await vc.set_my_volume(
            volume=volume
            )       
            return
        except ValueError:
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=usage
            )
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()


        𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
            animation=𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=f"**Volume Set To {volume}**"
            )
        await asyncio.sleep(CLEANER)
        await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~𝙽𝙾𝚁𝙴𝙳_RINGER
& ~filters.edited
& filters.command(
"temp",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def yt(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
🕊 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🕊
⚠️𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 —••÷[🕊NORDED🕊]÷••— 𝘩𝘢𝘴 𝘯𝘰𝘵 𝘣𝘦𝘦𝘯 𝘪𝘯𝘪𝘵𝘪𝘢𝘭𝘪𝘻𝘦𝘥 𝘺𝘦𝘵 𝘢𝘯𝘥 **__{chat.title}__** 𝘩𝘢𝘴 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵/𝘤𝘢𝘭𝘭 𝘯𝘰𝘵 𝘤𝘰𝘯𝘯𝘦𝘤𝘵𝘦𝘥 𝘺𝘦𝘵.
𝘗𝘭𝘦𝘢𝘴𝘦 𝘢𝘴𝘬 𝘕𝘖𝘙𝘋-𝘈𝘋𝘔𝘐𝘕𝘚 𝘰𝘧 **__{chat.title}__** 𝘵𝘰 𝘵𝘶𝘳𝘯 𝘪𝘵 𝘰𝘯 𝘧𝘪𝘳𝘴𝘵 𝘢𝘯𝘥 𝘳𝘦𝘵𝘳𝘺 [/temp]

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(
            CLEANER
            )
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~𝙽𝙾𝚁𝙴𝙳_ADMINS
& 𝙽𝙾𝚁𝙴𝙳_RINGER
& ~filters.edited
& filters.command(
"temp",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def yt(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
🕊 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🕊
😲🐣𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 𝘺𝘰𝘶 𝘢𝘳𝘦 𝘯𝘰𝘵 𝘢 𝘷𝘢𝘭𝘪𝘥 𝘕𝘖𝘙𝘋-𝘈𝘥𝘮𝘪𝘯.
𝘗𝘭𝘦𝘢𝘴𝘦 𝘶𝘴𝘦 `/nord` 𝘵𝘰 𝘤𝘩𝘦𝘤𝘬 𝘔𝘦𝘮𝘣𝘦𝘳 𝘰𝘯𝘭𝘺 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(
            CLEANER
            )
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"unplug",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def unplug(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ): 
    try:
        𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
        await ΣOЯ.delete()
        try:
            await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            NORDEDBΣ,
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 

⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

 `{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"|"
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~𝙽𝙾𝚁𝙴𝙳_RINGER
& ~filters.edited
& filters.command(
"yt",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def yt(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ): 
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
🕊 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🕊
⚠️𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 —••÷[🕊NORDED🕊]÷••— 𝘩𝘢𝘴 𝘯𝘰𝘵 𝘣𝘦𝘦𝘯 𝘪𝘯𝘪𝘵𝘪𝘢𝘭𝘪𝘻𝘦𝘥 𝘺𝘦𝘵 𝘢𝘯𝘥 **__{chat.title}__** 𝘩𝘢𝘴 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵/𝘤𝘢𝘭𝘭 𝘯𝘰𝘵 𝘤𝘰𝘯𝘯𝘦𝘤𝘵𝘦𝘥 𝘺𝘦𝘵.
𝘗𝘭𝘦𝘢𝘴𝘦 𝘢𝘴𝘬 𝘕𝘖𝘙𝘋-𝘈𝘋𝘔𝘐𝘕𝘚 𝘰𝘧 **__{chat.title}__** 𝘵𝘰 𝘵𝘶𝘳𝘯 𝘪𝘵 𝘰𝘯 𝘧𝘪𝘳𝘴𝘵 𝘢𝘯𝘥 𝘳𝘦𝘵𝘳𝘺 [/yt SONG.NAME]

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
"---------------------------------------------------------------------------------|____🤖𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃🤖____"
"|"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"""—••÷[🕊NORDED🕊]÷••—
* FROM HERE THE CODE FOR —••÷[🕊NORDED🕊]÷••— SESSION_MAKER STARTS
—••÷[🕊NORDED🕊]÷••—"""'''
EXIT module when users do it wrong
'''

async def exit_work(hn, text: str):
    if text.startswith("/exit"):
        await hn.reply("Process Cancelled.")
        return True
    return False

'''
EXIT module when users do it wrong
'''

@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command("session"))
async def norded(client, hn: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            await hn.delete()
            chat = hn.chat
            HYPE_ASK_API = await hn.reply_photo(
            photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
            caption=
            f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


ɴᴏᴡ ꜱᴇɴᴅ ʏᴏᴜʀ `API_ID` ᴛᴏ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ —••÷[🕊NӨЯDΣD🕊]÷••— ᴘʏʀᴏɢʀᴀᴍ ꜱᴇꜱꜱɪᴏɴ ɴᴀᴍᴇ.


**ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴇɪᴛʜᴇʀ ᴏꜰ ᴛʜᴏꜱᴇ ᴛʜᴇɴ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ʙᴏᴛ**

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))

            """
            =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    —••÷[🕊NORDED🕊]÷••— 
                                                                Telegram Music player userbot 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
            ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
            """

            HYPE_API = await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.ask(
            chat.id,
            f"**÷••>**")


            await HYPE_ASK_API.delete()


            if await exit_work(hn, HYPE_API.text):
                return
            """
            =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    —••÷[🕊NORDED🕊]÷••— 
                                                                Telegram Music player userbot 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
            ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
            """
            try:
                HYPE_API_CHECK = int(HYPE_API.text)
            except Exception:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=
                f"""
*—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


`API_ID` ɪꜱ ɪɴᴠᴀʟɪᴅ.
ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
                return
            """
            =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    —••÷[🕊NORDED🕊]÷••— 
                                                                Telegram Music player userbot 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
            ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
            """
            api_id = HYPE_API.text
            HYPE_ASK_HASK =  await hn.reply_photo(
            photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
            caption=
            f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


ɴᴏᴡ ꜱᴇɴᴅ ʏᴏᴜʀ `API_HASH`.

ᴘʀᴇꜱꜱ /exit ᴛᴏ ᴄᴀɴᴄᴇʟ ᴘʀᴏɢʀᴇꜱꜱ.

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))

            HYPE_HASH = await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.ask(
            chat.id,
            f"**÷••>**")
            await HYPE_ASK_HASK.delete()
            await HYPE_API.delete()
            """
            =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    —••÷[🕊NORDED🕊]÷••— 
                                                                Telegram Music player userbot 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
            ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
            """
            if await exit_work(hn, HYPE_HASH.text):
                return           
            if not len(HYPE_HASH.text) >= 30:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=
                f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


🔴 ＣＯＤＥ－ＲＥＤ 🔴
`API_HASH` ɪꜱ ɪɴᴠᴀʟɪᴅ.
ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
                return
            """
            =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    —••÷[🕊NORDED🕊]÷••— 
                                                                Telegram Music player userbot 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
            ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
            """
            api_hash = HYPE_HASH.text
            while True:
                number = await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.ask(chat.id,PHONE_NUMBER_TEXT)
                if not number.text:
                    continue
                if await exit_work(hn, number.text):
                    return
                phone = number.text
                HYPE_ASK_Y = await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=
                f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


ɪꜱ ```{phone}``` ᴄᴏʀʀᴇᴄᴛ? (y/n)

Ｓｅｎｄ： `y` 
or
Ｓｅｎｄ： `n` 

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))

                confirm = await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.ask(
                chat.id,
                f"**÷••>**")
                await HYPE_HASH.delete()

                if await exit_work(hn, confirm.text):
                    return
                if "y" in confirm.text:
                    await  HYPE_ASK_Y.delete()
                    await confirm.delete()
                    break
            """
            =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    —••÷[🕊NORDED🕊]÷••— 
                                                                Telegram Music player userbot 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
            ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
            """
            try:
                morphed = Client(
                "my_account",
                api_id=api_id,
                api_hash=api_hash
                )
            except Exception as e:
                await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.send_photo(
                chat.id,
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                text=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
**ᴇʀʀᴏʀ:** `{str(e)}`
ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
                return
            """
            =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    —••÷[🕊NORDED🕊]÷••— 
                                                                Telegram Music player userbot 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
            ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
            """
            try:
                await morphed.connect()
            except ConnectionError:
                await morphed.disconnect()
                await morphed.connect()
            """
            =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    —••÷[🕊NORDED🕊]÷••— 
                                                                Telegram Music player userbot 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
            ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
            """
            try:
                code = await morphed.send_code(phone)
            except FloodWait as e:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=
                f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


ʏᴏᴜ ʜᴀᴠᴇ ꜰʟᴏᴏᴅᴡᴀɪᴛ ᴏꜰ {e.x} ꜱᴇᴄᴏɴᴅꜱ

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
                return
                """
                =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                        Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                        —••÷[🕊NORDED🕊]÷••— 
                                                                    Telegram Music player userbot 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
                ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
                """
            except ApiIdInvalid:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=
                f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


**ᴀᴘɪ ɪᴅ** ᴀɴᴅ **ᴀᴘɪ ʜᴀꜱʜ** ᴀʀᴇ ɪɴᴠᴀʟɪᴅ.

ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
                return


            except PhoneNumberInvalid:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=
                f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪꜱ ɪɴᴠᴀʟɪᴅ.

ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
                return
            """
            =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    —••÷[🕊NORDED🕊]÷••— 
                                                                Telegram Music player userbot 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
            ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
            """
            try:
                HYPE_OTP = await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.ask(
                chat.id,
                OTP,
                timeout=300)
            except TimeoutError:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=
                f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏꜰ 5 ᴍɪɴ.

ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
                return
            """
            =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    —••÷[🕊NORDED🕊]÷••— 
                                                                Telegram Music player userbot 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
            ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
            """
            if await exit_work(hn, HYPE_OTP.text):
                return           
            HYPE_otp_CODE = HYPE_OTP.text
            try:
                await morphed.sign_in(
                phone,
                code.phone_code_hash,
                phone_code=' '.join(str(HYPE_otp_CODE)))

            except PhoneCodeInvalid:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=
                f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
ɪɴᴠᴀʟɪᴅ ᴄᴏᴅᴇ.


ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
                return
                """
                =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                        Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                        —••÷[🕊NORDED🕊]÷••— 
                                                                    Telegram Music player userbot 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
                ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
                """
            except PhoneCodeExpired:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=
                f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
ᴄᴏᴅᴇ ɪꜱ **𝐄𝐗𝐏𝐈𝐑𝐄𝐃** ᴏʀ ʏᴏᴜ ꜰᴏʀɢᴏᴛ ᴛᴏ **𝐏𝐔𝐓 𝐏𝐑𝐎𝐏𝐄𝐑 𝐒𝐏𝐀𝐂𝐄𝐒**

ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
                return
                """
                =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                        Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                        —••÷[🕊NORDED🕊]÷••— 
                                                                    Telegram Music player userbot 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
                ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
                """
            except SessionPasswordNeeded:
                try:
                    await hn.reply_photo(
                    photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                    caption=
                    f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʜᴀᴠᴇ **𝐓𝐰𝐨-𝐒𝐭𝐞𝐩 𝐕𝐞𝐫𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧.**
ᴘʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴘᴀꜱꜱᴡᴏʀᴅ.

ᴘʀᴇꜱꜱ /exit ᴛᴏ ᴄᴀɴᴄᴇʟ ᴘʀᴏɢʀᴇꜱꜱ.

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
                    HYPE_PASSCODE = await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.ask(chat.id,f"**÷••>**",timeout=300)
                    """
                    =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                        GNU GENERAL PUBLIC LICENSE 
                                                                            Version 3, 29 June 2007
                                                                    Copyright (C) 2007 Free Software Foundation
                                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            —••÷[🕊NORDED🕊]÷••— 
                                                                        Telegram Music player userbot 
                                                                has been licensed under GNU General Public License
                                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
                    ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
                    """
                except TimeoutError:
                    await hn.reply_photo(
                    photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                    caption=
                    f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


`ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏꜰ 5 ᴍɪɴ`

ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.`

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
                    return
                """
                =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                        Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                        —••÷[🕊NORDED🕊]÷••— 
                                                                    Telegram Music player userbot 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
                ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
                """
                if await exit_work(hn,HYPE_PASSCODE.text):
                    return
                HYPE_GOT_CODE = HYPE_PASSCODE.text
                try:
                    await morphed.check_password(HYPE_GOT_CODE)
                except Exception as e:
                    await hn.reply_photo(
                    photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                    caption=
                    f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
**ᴇʀʀᴏʀ:** `{str(e)}`

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
                    return

            
            except Exception as e:
                await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.send_photo(
                chat.id,
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                text=f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
**ᴇʀʀᴏʀ:** `{str(e)}`

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
                return
            """
            =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    —••÷[🕊NORDED🕊]÷••— 
                                                                Telegram Music player userbot 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
            ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
            """
            try:
                SESSION_HYPED = await morphed.export_session_string()
                await morphed.send_photo(
                "me",
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=
                f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨
ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ 𝘽𝙖𝙨𝙞𝙘 𝙋𝙮𝙧𝙤𝙜𝙧𝙖𝙢 𝙎𝙚𝙨𝙨𝙞𝙤𝙣 𝙉𝙖𝙢𝙚:


```{SESSION_HYPED}```

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))           
                await morphed.disconnect()
                await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.send_photo(
                chat.id,
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=
                f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


`𝘚𝘵𝘳𝘪𝘯𝘨 𝘨𝘦𝘯𝘦𝘳𝘢𝘵𝘪𝘰𝘯 𝘸𝘢𝘴 𝘚𝘶𝘤𝘤𝘦𝘴𝘴𝘧𝘶𝘭𝘭𝘺 𝘤𝘰𝘮𝘱𝘭𝘦𝘵𝘦𝘥`
ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴀᴠᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
                """
                =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                        Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                        —••÷[🕊NORDED🕊]÷••— 
                                                                    Telegram Music player userbot 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
                ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
                """
            except Exception as e:
                await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.send_photo(
                chat.id,
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=
                f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
**ᴇʀʀᴏʀ:** `{str(e)}`

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
                return
            """
            =================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    —••÷[🕊NORDED🕊]÷••— 
                                                                Telegram Music player userbot 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
            ====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
            """
        except Exception as e:
            await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.send_photo(
            chat.id,
            photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
            caption=
            f"""
**—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` ✨••Hype Void Lab••✨


🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
**ᴇʀʀᴏʀ:** `{str(e)}`

—••÷[🕊NӨЯDΣD🕊]÷••—

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
        reply_markup = HypeKeyboardMarkup([[
        HypeKeyboardButton(
        text="🏷Group",
        url="https://t.me/Krakns"),],[
        HypeKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        HypeKeyboardButton(
        text="💰Channel",
        url="https://t.me/KrakinzLab"),],[
        HypeKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/KrakinzBot")
        ]]))
            return
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass





"""=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—======================================================================="""
"""—••÷[🕊NORDED🕊]÷••—
* FROM HERE THE CODE FOR —••÷[🕊NORDED🕊]÷••— USERBOT STARTS....
GONNA BE LONG LOL
"""
@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID
)
& ~filters.edited
& 𝙽𝙾𝚁𝙴𝙳_ADMINS
& filters.command(
"plug",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def plug(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    os.system("clear")
    𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
    ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
    if not ռօʀɖʀɨռɢ:
        ռօʀɖɦօք.ռօʀɖʀɨռɢ = GroupCallFactory(client).get_file_group_call()
        ռօʀɖɦօք.ռօʀɖʀɨռɢ.add_handler(
        network_status_changed_handler,
        GroupCallFileAction.NETWORK_STATUS_CHANGED)
        ռօʀɖɦօք.ռօʀɖʀɨռɢ.add_handler(
        playout_ended_handler,
        GroupCallFileAction.PLAYOUT_ENDED)
        await ռօʀɖɦօք.ռօʀɖʀɨռɢ.start(ΣOЯ.chat.id)
        await ΣOЯ.delete()
    if ռօʀɖʀɨռɢ and ռօʀɖʀɨռɢ.is_connected:
        await ΣOЯ.delete()
        xy = await ΣOЯ.reply_photo(
        photo=
        𝙽𝙾𝚁𝙴𝙳_HUD,
        caption=f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
`𝗡𝗼𝗿𝗱𝗲𝗱 𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𝗵𝗮𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗽𝗹𝘂𝗴𝗴𝗲𝗱 𝗺𝘂𝘀𝗶𝗰 𝗽𝗹𝗮𝘆𝗲𝗿 𝗶𝗻 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁!`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
        await asyncio.sleep(CLEANER)
        await xy.delete()



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



async def network_status_changed_handler(context, is_connected: bool):
    if is_connected:
        ռօʀɖɦօք.chat_id = MAX_CHANNEL_ID - context.full_chat.id
        kai = await 𝙽𝙾𝚁𝙴𝙳_ANIMATE(
        f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
𝗡𝗼𝗿𝗱𝗲𝗱 𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𝗵𝗮𝘀 𝗽𝗹𝘂𝗴𝗴𝗲𝗱 𝗺𝘂𝘀𝗶𝗰 𝗽𝗹𝗮𝘆𝗲𝗿 𝗶𝗻 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁!

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
        await asyncio.sleep(
        CLEANER
        )
        await kai.delete()
    else:
        kai = await 𝙽𝙾𝚁𝙴𝙳_ANIMATE(
        f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
𝐍𝐨𝐫𝐝𝐞𝐝 𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐡𝐚𝐬 𝐥𝐞𝐟𝐭 𝐚𝐧𝐝 𝐮𝐧𝐩𝐥𝐮𝐠𝐠𝐞𝐝 𝐦𝐮𝐬𝐢𝐜 𝐩𝐥𝐚𝐲𝐞𝐫 𝐢𝐧 𝐯𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭!
`Please wait till —••÷[🕊NORDED🕊]÷••— restarts.`
𝙏𝙖𝙠𝙚𝙨 𝙖𝙧𝙤𝙪𝙣𝙙 30𝙨𝙚𝙘-1𝙢𝙞𝙣.

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
        ռօʀɖɦօք.chat_id = None
        await asyncio.sleep(
        CLEANER
        )
        await kai.delete()
async def playout_ended_handler(_, __):
    await NorDIgnoreNow()



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



async def restart(text):
    HEROKU = heroku3.from_key(HEROKU_API_KEY)
    app = HEROKU.apps()[HEROKU_APP_NAME]
    app.restart()
    ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
    client = ռօʀɖʀɨռɢ.client
    chat_id = ռօʀɖɦօք.chat_id
    message = await client.send_message(chat_id,text)
    return message



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID
)
& ~filters.edited
& 𝙽𝙾𝚁𝙴𝙳_RINGER
& 𝙽𝙾𝚁𝙴𝙳_ADMINS
& filters.command(
"unplug",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def unplug(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        await ΣOЯ.delete()
        try:
            HEROKU = heroku3.from_key(HEROKU_API_KEY)
            app = HEROKU.apps()[HEROKU_APP_NAME]
            app.restart()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            await ΣOЯ.reply_text(
            f"{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}\nPlease use /restart before replugging as auto restart failed")
            return

        𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
        ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
        ռօʀɖɦօք.ռօʀɖքʟǟʏɛʀʟɨֆȶ.clear()
        ռօʀɖʀɨռɢ.input_filename = ""
        await ռօʀɖʀɨռɢ.stop()
        await ΣOЯ.delete()


        try:
            if HEROKU_API_KEY is not None and HEROKU_APP_NAME is not None and HEROKU == "HEROKU":
                wait = await ΣOЯ.reply_photo(
                photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                caption=
                f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️𝘗𝘭𝘦𝘢𝘴𝘦 𝘸𝘢𝘪𝘵 𝘵𝘪𝘭𝘭 𝘤𝘰𝘥𝘦 𝘤𝘭𝘦𝘢𝘯𝘴 𝘢𝘯𝘥 𝘳𝘦𝘴𝘵𝘢𝘳𝘵𝘴 𝘪𝘵𝘴𝘦𝘭𝘧.
𝙏𝙖𝙠𝙚𝙨 𝙖𝙧𝙤𝙪𝙣𝙙 30𝙨𝙚𝙘-1𝙢𝙞𝙣.

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
                reply_markup=
            HypeKeyboardMarkup([[
                HypeKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/Krakns",),],[
                HypeKeyboardButton(
                text="✨••Hype Void Lab••✨",
                url=f"https://t.me/KrakinzBot")
                ]]))
                await wait.delete()


            else:
                await ΣOЯ.reply_photo(
                photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                caption=
                f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️𝘗𝘭𝘦𝘢𝘴𝘦 𝘔𝘢𝘯𝘶𝘢𝘭𝘭𝘺 `/restart` 𝘵𝘩𝘦 𝘣𝘰𝘵 𝘢𝘴 𝘪𝘵 𝘪𝘴 𝘪𝘯 𝗡𝗢𝗡-𝗛𝗘𝗥𝗢𝗞𝗨  𝘮𝘰𝘥𝘦.

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
                reply_markup=
            HypeKeyboardMarkup([[
                HypeKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/Krakns",),],[
                HypeKeyboardButton(
                text="✨••Hype Void Lab••✨",
                url=f"https://t.me/KrakinzBot")
                ]]))
                
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID
)
& ~filters.edited
& 𝙽𝙾𝚁𝙴𝙳_RINGER
& filters.command("stream",𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def stream(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
        ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
        ռօʀɖքʟǟʏɛʀʟɨֆȶ = ռօʀɖɦօք.ռօʀɖքʟǟʏɛʀʟɨֆȶ
        try:
            if ΣOЯ.audio:
                if ΣOЯ.audio.duration > (
                    DURATION_AUTOPLAY_MIN * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60):
                    𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
                    photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                    caption=f"{str(DURATION_AUTOPLAY_MIN)}",
                    reply_markup=
            HypeKeyboardMarkup([[
                    HypeKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/Krakns",),],[
                    HypeKeyboardButton(
                    text="✨••Hype Void Lab••✨",
                    url=f"https://t.me/KrakinzBot")
                    ]]))
                    await asyncio.sleep(
                CLEANER
                )
                    await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
                    return
                m_audio = ΣOЯ

                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
        
            elif ΣOЯ.reply_to_message and ΣOЯ.reply_to_message.audio:
                m_audio = ΣOЯ.reply_to_message
                if m_audio.audio.duration > (
                    DURATION_PLAY_HOUR * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60):
                    𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
                    photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                    caption=f"{str(DURATION_PLAY_HOUR)}",
                    reply_markup=
            HypeKeyboardMarkup([[
                    HypeKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/Krakns",),],[
                    HypeKeyboardButton(
                    text="✨••Hype Void Lab••✨",
                    url=f"https://t.me/KrakinzBot")
                    ]]))
                    await asyncio.sleep(
                CLEANER
                )
                    await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
                    return

                    """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
                    """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""

            else:
                await ռօʀɖɦօք.send_playlist()
                await ΣOЯ.delete()
                return

                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""

            if ռօʀɖքʟǟʏɛʀʟɨֆȶ and ռօʀɖքʟǟʏɛʀʟɨֆȶ[-1].audio.file_unique_id \
                    == m_audio.audio.file_unique_id:
                𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
                photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                caption=
                f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
That Audio file was successfully already added

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
                reply_markup=
            HypeKeyboardMarkup([[
                HypeKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/Krakns",),],[
                HypeKeyboardButton(
                text="✨••Hype Void Lab••✨",
                url=f"https://t.me/KrakinzBot")
                ]]))
                await asyncio.sleep(
                CLEANER
                )
                await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
                return

                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""

            ռօʀɖքʟǟʏɛʀʟɨֆȶ.append(m_audio)
            if len(ռօʀɖքʟǟʏɛʀʟɨֆȶ) == 1:
                m_status = await ΣOЯ.reply_photo(
                photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                caption=f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
𝘗𝘭𝘦𝘢𝘴𝘦 𝘸𝘢𝘪𝘵 𝘧𝘰𝘳 —••÷[🕊NORDED🕊]÷••— 𝘵𝘰 𝘭𝘪𝘯𝘬 𝘸𝘪𝘵𝘩 𝘶𝘴𝘦𝘣𝘰𝘵 𝘴𝘦𝘳𝘷𝘦𝘳..

`𝙂𝙧𝙚𝙖𝙩𝙚𝙧 𝙖𝙪𝙙𝙞𝙤 𝙨𝙞𝙯𝙚, 𝙢𝙤𝙧𝙚 𝙩𝙞𝙢𝙚 𝙩𝙤 𝙖𝙙𝙙 𝙩𝙤 𝙨𝙚𝙧𝙫𝙚𝙧`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
                reply_markup=
            HypeKeyboardMarkup([[
                HypeKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/Krakns",),],[
                HypeKeyboardButton(
                text="✨••Hype Void Lab••✨",
                url=f"https://t.me/KrakinzBot")
                ]]))
                await ռօʀɖɖօառʟօǟɖɛʀ(ռօʀɖքʟǟʏɛʀʟɨֆȶ[0])
                ռօʀɖʀɨռɢ.input_filename = os.path.join(
                client.workdir,
                HYPEDLDIR,
                f"{ռօʀɖքʟǟʏɛʀʟɨֆȶ[0].audio.file_unique_id}.raw")
                await ռօʀɖɦօք.𝙽𝙾𝚁𝙴𝙳_CLOCK()
                await m_status.delete()
            await ռօʀɖɦօք.send_playlist()

            """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
            """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
            try:
                async for YΣ in client.search_messages(
                    ΣOЯ.chat.id,
                    filter="pinned",
                    limit=1):
                    if YΣ.audio:
                        await YΣ.unpin()
                await ΣOЯ.reply_to_message.pin(True)
                NORD_TITLE = "🎶🌟NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ"
                try:
                    chatID = ΣOЯ.chat.id
                    EditGroupCallTitle(call=chatID, title=NORD_TITLE)
                except Exception:
                    await ΣOЯ.reply_photo(
                    photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                    caption=f"{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}\n[ERROR]: FAILED TO EDIT VC TITLE, MAKE ME ADMIN."
                    )
                    pass
            except ChatAdminRequired:
                pass
            except FloodWait:
                pass
            for track in ռօʀɖքʟǟʏɛʀʟɨֆȶ[:2]:
                await ռօʀɖɖօառʟօǟɖɛʀ(track)
            if not ΣOЯ.audio:
                await ΣOЯ.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID
)
& ~filters.edited
& 𝙽𝙾𝚁𝙴𝙳_RINGER
& 𝙽𝙾𝚁𝙴𝙳_ADMINS
& filters.command(
"next",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def next(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
        try:
            await ΣOЯ.delete()
            ռօʀɖքʟǟʏɛʀʟɨֆȶ = ռօʀɖɦօք.ռօʀɖքʟǟʏɛʀʟɨֆȶ
            if len(ΣOЯ.command) == 1:
                await NorDIgnoreNow()
            else:
                try:
                    items = list(dict.fromkeys(ΣOЯ.command[1:]))
                    items = [int(x) for x in items if x.isdigit()]
                    items.sort(reverse=True)
                    text = []
                    for i in items:
                        if 2 <= i <= (len(ռօʀɖքʟǟʏɛʀʟɨֆȶ) - 1):
                            audio = f"[{ռօʀɖքʟǟʏɛʀʟɨֆȶ[i].audio.title}]({ռօʀɖքʟǟʏɛʀʟɨֆȶ[i].link})"
                            ռօʀɖքʟǟʏɛʀʟɨֆȶ.pop(i)
                            text.append(f" {i}. **{audio}**")
                        else:
                            text.append(f" {i}")
                    𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
                    photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                    caption="\n".join(text),disable_web_page_preview=True,
                    reply_markup=
            HypeKeyboardMarkup([[
                    HypeKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/Krakns",),],[
                    HypeKeyboardButton(
                    text="✨••Hype Void Lab••✨",
                    url=f"https://t.me/KrakinzBot")
                    ]]))
                    await ռօʀɖɦօք.send_playlist()

                    """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
                    """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""

                except (ValueError, TypeError):
                    𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
                    photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                    caption=
                    f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
⚠️𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙞𝙣𝙥𝙪𝙩

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
                    reply_markup=
            HypeKeyboardMarkup([[
                    HypeKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/Krakns",),],[
                    HypeKeyboardButton(
                    text="✨••Hype Void Lab••✨",
                    url=f"https://t.me/KrakinzBot")
                    ]]))
                    await asyncio.sleep(
                CLEANER
                )
                    await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID
)
& filters.command(
"nord",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def help(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            if cb_data is False:
                await ΣOЯ.reply_text(f"Add @{BOT_USERNAME} to group")
            else:
                await ΣOЯ.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID
)
& ~filters.edited
& 𝙽𝙾𝚁𝙴𝙳_ADMINS
& filters.command(
"norded",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def norded(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
            if ռօʀɖʀɨռɢ and ռօʀɖʀɨռɢ.is_connected:
                chat_id = int("-100" + str(ռօʀɖʀɨռɢ.full_chat.id))
                chat = await client.get_chat(chat_id)
                𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
                photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                caption=
                f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
÷🕊𝙽𝙾𝚁𝙳𝙴𝙳 - 𝚂𝚖𝚊𝚛𝚝𝙼𝚞𝚜𝚒𝚌𝙿𝚕𝚊𝚢𝚎𝚛🕊÷ 𝘪𝘴 𝘤𝘶𝘳𝘳𝘦𝘯𝘵𝘭𝘺 𝘪𝘯 𝘵𝘩𝘦 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵 𝘰𝘧:
- **__{chat.title}__**

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
                reply_markup=
            HypeKeyboardMarkup([[
                HypeKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/Krakns",),],[
                HypeKeyboardButton(
                text="✨••Hype Void Lab••✨",
                url=f"https://t.me/KrakinzBot")
                ]]))
                await asyncio.sleep(
                CLEANER
                )
                await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()

                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""

            else:
                join = await ΣOЯ.reply_photo(
                photo=
                𝙽𝙾𝚁𝙴𝙳_HUD,
                caption=
                f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
⚠️••÷🕊𝙽𝙾𝚁𝙳𝙴𝙳 - 𝚂𝚖𝚊𝚛𝚝𝙼𝚞𝚜𝚒𝚌𝙿𝚕𝚊𝚢𝚎𝚛🕊÷•• 𝘥𝘪𝘥𝘯'𝘵 𝘫𝘰𝘪𝘯 𝘢𝘯𝘺 𝘷𝘰𝘪𝘤𝘦 𝘤𝘢𝘭𝘭 𝘺𝘦𝘵.

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
                reply_markup=
            HypeKeyboardMarkup([[
                HypeKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/Krakns",),],[
                HypeKeyboardButton(
                text="✨••Hype Void Lab••✨",
                url=f"https://t.me/KrakinzBot")
                ]]))
                await ΣOЯ.delete()
                await asyncio.sleep(
                CLEANER
                )
                await join.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID
)
& ~filters.edited
& 𝙽𝙾𝚁𝙴𝙳_RINGER
& 𝙽𝙾𝚁𝙴𝙳_ADMINS
& filters.command(
"end",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def end(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
            ռօʀɖʀɨռɢ.stop_playout()
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
⏹❗️ **÷🕊𝙽𝙾𝚁𝙳𝙴𝙳 - 𝚂𝚖𝚊𝚛𝚝𝙼𝚞𝚜𝚒𝚌𝙿𝚕𝚊𝚢𝚎𝚛🕊÷ 𝘀𝘁𝗼𝗽𝗽𝗲𝗱 𝗽𝗹𝗮𝘆𝗶𝗻𝗴**

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
            await ռօʀɖɦօք.𝙽𝙾𝚁𝙴𝙳_CLOCK(reset=True)

            """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
            """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""

            try:
                async for YΣ in client.search_messages(ΣOЯ.chat.id,filter="pinned",limit=1):
                    if YΣ.audio:
                        await YΣ.unpin()
            except ChatAdminRequired:
                pass
            except FloodWait:
                pass
            ռօʀɖɦօք.ռօʀɖքʟǟʏɛʀʟɨֆȶ.clear()
            await asyncio.sleep(
            CLEANER
            )
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID
)
& ~filters.edited
& 𝙽𝙾𝚁𝙴𝙳_RINGER
& 𝙽𝙾𝚁𝙴𝙳_ADMINS
& filters.command(
"replay",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def restart(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
            if not ռօʀɖɦօք.ռօʀɖքʟǟʏɛʀʟɨֆȶ:
                return
            ռօʀɖʀɨռɢ.restart_playout()
            await ռօʀɖɦօք.𝙽𝙾𝚁𝙴𝙳_CLOCK()
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
⏹❗️ **÷🕊𝙽𝙾𝚁𝙳𝙴𝙳 - 𝚂𝚖𝚊𝚛𝚝𝙼𝚞𝚜𝚒𝚌𝙿𝚕𝚊𝚢𝚎𝚛🕊÷ 𝗶𝘀 𝗻𝗼𝘄 𝗽𝗹𝗮𝘆𝗶𝗻𝗴 𝗰𝘂𝗿𝗿𝗲𝗻𝘁 𝘀𝗼𝗻𝗴 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗯𝗲𝗴𝗶𝗻𝗻𝗶𝗻𝗴...**

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
            await asyncio.sleep(
            CLEANER
            )
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID
)
& ~filters.edited
& 𝙽𝙾𝚁𝙴𝙳_RINGER
& 𝙽𝙾𝚁𝙴𝙳_ADMINS
& filters.command(
"pause",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def pause(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            ռօʀɖɦօք.ռօʀɖʀɨռɢ.pause_playout()
            await ռօʀɖɦօք.𝙽𝙾𝚁𝙴𝙳_CLOCK(reset=True)
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
**÷🕊𝙽𝙾𝚁𝙳𝙴𝙳 - 𝚂𝚖𝚊𝚛𝚝𝙼𝚞𝚜𝚒𝚌𝙿𝚕𝚊𝚢𝚎𝚛🕊÷ 𝗽𝗮𝘂𝘀𝗲𝗱 𝗰𝘂𝗿𝗿𝗲𝗻𝘁 𝗺𝘂𝘀𝗶𝗰 𝗶𝗻 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁**

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
            ռօʀɖɦօք.ռօʀɖʍֆɢʀ["pause"] = 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC
            try:
                await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.pin()
            except ChatAdminRequired:
                pass
            except FloodWait:
                pass
            await asyncio.sleep(8)
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID
)
& ~filters.edited
& 𝙽𝙾𝚁𝙴𝙳_RINGER
& 𝙽𝙾𝚁𝙴𝙳_ADMINS
& filters.command(
"resume",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def resume(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            ռօʀɖɦօք.ռօʀɖʀɨռɢ.resume_playout()
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
**÷🕊𝙽𝙾𝚁𝙳𝙴𝙳 - 𝚂𝚖𝚊𝚛𝚝𝙼𝚞𝚜𝚒𝚌𝙿𝚕𝚊𝚢𝚎𝚛🕊÷ 𝗿𝗲𝘀𝘂𝗺𝗲𝗱 𝗺𝘂𝘀𝗶𝗰 𝗶𝗻 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁**

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
            if ռօʀɖɦօք.ռօʀɖʍֆɢʀ.get("pause") is not None:
                await ռօʀɖɦօք.ռօʀɖʍֆɢʀ["pause"].delete()
            await asyncio.sleep(
            CLEANER
            )
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID
)
& ~filters.edited
& 𝙽𝙾𝚁𝙴𝙳_RINGER
& 𝙽𝙾𝚁𝙴𝙳_ADMINS
& filters.command(
"temp",
𝙽𝙾𝚁𝙴𝙳_FIXER
))
async def clean(
client,
ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    try:
        try:
            𝙽𝙾𝚁𝙴𝙳_MENTION = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            download_dir = os.path.join(
            client.workdir,
            HYPEDLDIR)
            temp_nord: list[str] = os.listdir(
            download_dir)
            for track in ռօʀɖɦօք.ռօʀɖքʟǟʏɛʀʟɨֆȶ[:2]:
                track_fn = f"{track.audio.file_unique_id}.raw"
                if track_fn in temp_nord:
                    temp_nord.remove(track_fn)
            count = 0
            if temp_nord:
                for ʀǟաƈ in temp_nord:
                    if ʀǟաƈ.endswith(".raw"):
                        count += 1
                        os.remove(
                        os.path.join(
                        download_dir,
                        ʀǟաƈ))
            𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC = await ΣOЯ.reply_photo(
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧
**÷🕊𝙽𝙾𝚁𝙳𝙴𝙳 - 𝚂𝚖𝚊𝚛𝚝𝙼𝚞𝚜𝚒𝚌𝙿𝚕𝚊𝚢𝚎𝚛🕊÷ 𝗰𝗹𝗲𝗮𝗻𝗲𝗱 {count} 𝘁𝗲𝗺𝗽/𝗿𝗮𝘄 𝗳𝗶𝗹𝗲𝘀

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
""",
            reply_markup=
            HypeKeyboardMarkup([[
            HypeKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/Krakns",),],[
            HypeKeyboardButton(
            text="✨••Hype Void Lab••✨",
            url=f"https://t.me/KrakinzBot")
            ]]))
            await asyncio.sleep(
            CLEANER
            )
            await 𝙽𝙾𝚁𝙴𝙳_PSYCHODELIC.delete()
        except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
            𝙽𝙾𝚁𝙴𝙳_ZYGOTE = await ΣOЯ.reply_animation(
            animation=
            𝙽𝙾𝚁𝙴𝙳_ERROR,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
Hey 𝙽𝙾𝚁𝙳𝙴𝙳 User 🍾:  
🐧 **{𝙽𝙾𝚁𝙴𝙳_MENTION}** 🐧 
⚠️**𝘛𝘩𝘦𝘳𝘦 𝘸𝘢𝘴 𝘢𝘯 𝘌𝘳𝘳𝘰𝘳 𝘱𝘳𝘰𝘤𝘦𝘴𝘴𝘪𝘯𝘨 𝘵𝘩𝘦 𝘱𝘳𝘦𝘷𝘪𝘰𝘶𝘴 𝘳𝘦𝘲𝘶𝘦𝘴𝘵.**
**𝘗𝘭𝘦𝘢𝘴𝘦 𝘤𝘩𝘦𝘤𝘬 𝘣𝘦𝘭𝘰𝘸 𝘦𝘳𝘳𝘰𝘳 𝘵𝘰 𝘭𝘦𝘢𝘳𝘯 𝘮𝘰𝘳𝘦.**

`{Σ_𝙽𝙾𝚁𝙴𝙳_Σ}`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
            await asyncio.sleep(CLEANER)
            await 𝙽𝙾𝚁𝙴𝙳_ZYGOTE.delete()
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"""—••÷[🕊NORDED🕊]÷••—
* FROM HERE THE CODE FOR —••÷[🕊NORDED🕊]÷••— NORD_PLAYER STARTS
—••÷[🕊NORDED🕊]÷••—
"""
class NORDPLAYER(object):
    def __init__(self):
        self.client = None
        self.chat_id = None
        self.ռօʀɖʀɨռɢ = None
        self.ռօʀɖƈʟօƈӄ = None
        self.ռօʀɖʍֆɢʀ = {}
        self.ռօʀɖքʟǟʏɛʀʟɨֆȶ = []
        
    async def send_playlist(self):
        ռօʀɖքʟǟʏɛʀʟɨֆȶ = self.ռօʀɖքʟǟʏɛʀʟɨֆȶ
        if not ռօʀɖքʟǟʏɛʀʟɨֆȶ:
            𝙽𝙾𝚁𝙴𝙳 = f"{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}[🕊NORDED🕊 𝗠𝘂𝘀𝗶𝗰 𝗹𝗶𝘀𝘁 𝙞𝙨 𝙘𝙪𝙧𝙧𝙚𝙣𝙩𝙡𝙮 𝙚𝙢𝙥𝙩𝙮 𝙖𝙣𝙙 𝙬𝙖𝙞𝙩𝙞𝙣𝙜 𝙛𝙤𝙧 𝙞𝙣𝙥𝙪𝙩](https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg)"
        else:
            if len(ռօʀɖքʟǟʏɛʀʟɨֆȶ) == 1:
                𝙽𝙾𝚁𝙴𝙳 = "[🕊𝙽𝙾𝚁𝙳𝙴𝙳-𝚂𝚖𝚊𝚛𝚝 𝙼𝚞𝚜𝚒𝚌 𝙿𝚕𝚊𝚢𝚎𝚛🕊](https://t.me/KrakinzBot)\n"
            else:
                𝙽𝙾𝚁𝙴𝙳 = "[🕊𝙽𝙾𝚁𝙳𝙴𝙳-𝚂𝚖𝚊𝚛𝚝 𝙼𝚞𝚜𝚒𝚌 𝙿𝚕𝚊𝚢𝚎𝚛🕊](https://t.me/KrakinzBot)\n"
            
            𝙽𝙾𝚁𝙴𝙳 += "\n🦋".join([
                f"**{i}:**𝗦𝗼𝗻𝗴🍪:[{x.audio.title}]({x.link})"

                for i, x in enumerate(ռօʀɖքʟǟʏɛʀʟɨֆȶ)
                ])
        if ռօʀɖɦօք.ռօʀɖʍֆɢʀ.get("ռօʀɖքʟǟʏɛʀʟɨֆȶ") is not None:
            await ռօʀɖɦօք.ռօʀɖʍֆɢʀ["ռօʀɖքʟǟʏɛʀʟɨֆȶ"].delete()
        ռօʀɖɦօք.ռօʀɖʍֆɢʀ["ռօʀɖքʟǟʏɛʀʟɨֆȶ"] = await 𝙽𝙾𝚁𝙴𝙳_ANIMATE(𝙽𝙾𝚁𝙴𝙳)
    async def 𝙽𝙾𝚁𝙴𝙳_CLOCK(self, reset=False):
        self.ռօʀɖƈʟօƈӄ = (None if reset else datetime.utcnow().replace(microsecond=0))       
ռօʀɖɦօք = NORDPLAYER()



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



async def 𝙽𝙾𝚁𝙴𝙳_ANIMATE(text):
    ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
    client = ռօʀɖʀɨռɢ.client
    chat_id = ռօʀɖɦօք.chat_id   
    animation="https://telegra.ph/file/976f71e4175c2f626fe04.mp4"
    message = await client.send_animation(
    chat_id,
    animation,
    text
    )
    return message



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



async def NorDIgnoreNow():
    ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
    ռօʀɖքʟǟʏɛʀʟɨֆȶ = ռօʀɖɦօք.ռօʀɖքʟǟʏɛʀʟɨֆȶ
    if not ռօʀɖքʟǟʏɛʀʟɨֆȶ:
        return
    if len(ռօʀɖքʟǟʏɛʀʟɨֆȶ) == 1:
        await ռօʀɖɦօք.𝙽𝙾𝚁𝙴𝙳_CLOCK()
        return
    client = ռօʀɖʀɨռɢ.client
    download_dir = os.path.join(
    client.workdir,
    HYPEDLDIR)
    ռօʀɖʀɨռɢ.input_filename = os.path.join(
    download_dir,
    f"{ռօʀɖքʟǟʏɛʀʟɨֆȶ[1].audio.file_unique_id}.raw")
    await ռօʀɖɦօք.𝙽𝙾𝚁𝙴𝙳_CLOCK()
    old_track = ռօʀɖքʟǟʏɛʀʟɨֆȶ.pop(0)
    await ռօʀɖɦօք.send_playlist()
    os.remove(os.path.join(
    download_dir,
    f"{old_track.audio.file_unique_id}.raw"))
    if len(ռօʀɖքʟǟʏɛʀʟɨֆȶ) == 1:
        return
    await ռօʀɖɖօառʟօǟɖɛʀ(ռօʀɖքʟǟʏɛʀʟɨֆȶ[1])



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



async def ռօʀɖɖօառʟօǟɖɛʀ(ΣOЯ: ΣOЯ_𝙽𝙾𝚁𝙴𝙳_ΣOЯ):
    ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
    client = ռօʀɖʀɨռɢ.client
    raw_file = os.path.join(
    client.workdir,
    HYPEDLDIR,
    f"{ΣOЯ.audio.file_unique_id}.raw")
    if not os.path.isfile(raw_file):
        original_file = await ΣOЯ.download()
        ffmpeg.input(original_file).output(
            raw_file,
            format="s16le",
            acodec="pcm_s16le",
            ac=2,
            ar="48k",
            loglevel="error"
        ).overwrite_output().run()
        os.remove(original_file)



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



"""—••÷[🕊NORDED🕊]÷••—
* FROM HERE THE CODE FOR —••÷[🕊NORDED🕊]÷••— LOOGER USING LOGURU STARTS
—••÷[🕊NORDED🕊]÷••—
"""
class InterceptHandler(logging.Handler):
    LEVELS_MAP = {
        logging.CRITICAL:
         "CRITICAL",
        logging.ERROR:
         "ERROR",
        logging.WARNING:
         "WARNING",
        logging.INFO:
         "INFO",
        logging.DEBUG:
         "DEBUG"        }
    def _get_level(
        self,
        record):
        return self.LEVELS_MAP.get(
        record.levelno,
        record.levelno)
    def emit(self, record):
        logger_opt = logger.opt(
        depth=6,
        exception=record.exc_info,
        ansi=True,
        lazy=True)
        logger_opt.log(self._get_level(record),
        record.getMessage())
logging.basicConfig(handlers=[InterceptHandler()],
level=logging.INFO)
ɴᴏʀᴅᴘᴜᴛ = logging.getLogger(__name__)
LICE="""
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧➕🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
GNU GENERAL PUBLIC LICENSE 
Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
—••÷[🕊NORDED🕊]÷••—  
Telegram Music player userbot 
has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧➕🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
"""
"+"
"+"
"+"
"+"
# file = open("bootlock.py", "w") 
# file.write("from 𝙽𝙾𝚁𝙳𝙴𝙳 import *\n\n\nNORDED𝗕𝗢𝗧.start()\nidle()\nNORDED𝗕𝗢𝗧.stop()") 
"+"
"+"
"+"
"+"
# file = open("bootlocker.py", "w") 
# file.write("from 𝙽𝙾𝚁𝙳𝙴𝙳 import *\n\n\nNORDED.start()\nidle()\nNORDED.stop()") 
"+"
"+"
"+"
"+"
# import subprocess
# subprocess.run("python3 bootlock.py & python3 bootlocker.py", shell=True)
"+"
"+"
"+"
"+"



"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""



import os
import sys
from os import getenv
from termcolor import *
from dotenv import load_dotenv
NORD_FFWS = 64 * 1024
NORD_DCPG = getenv(
"HEROKU")
if HEROKU == "HEROKU":
    pass
else:
    if HEROKU == "HEROKU":
        pass
    else:
        os.system("clear")
    "+"
    "+"
    "+"
    "+"
    ɴᴏʀᴅᴘᴜᴛ.info("••••••••••••••••••••••••••••••••")
    ɴᴏʀᴅᴘᴜᴛ.info(":              🤖+🟢")
    ɴᴏʀᴅᴘᴜᴛ.info(":              ONLINE")
    ɴᴏʀᴅᴘᴜᴛ.info(":              𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃")
    ɴᴏʀᴅᴘᴜᴛ.info(":              🟢+🤖")
    ɴᴏʀᴅᴘᴜᴛ.info("••••••••••••••••••••••••••••••••")
    𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.start()
    ɴᴏʀᴅᴘᴜᴛ.info("••••••••••••••••••••••••••••••••")
    ɴᴏʀᴅᴘᴜᴛ.info(":              😈+🟢")
    ɴᴏʀᴅᴘᴜᴛ.info(":              ONLINE")
    ɴᴏʀᴅᴘᴜᴛ.info(":              𝙽𝙾𝚁𝙳𝙴𝙳")
    ɴᴏʀᴅᴘᴜᴛ.info(":              🟢+😈")
    ɴᴏʀᴅᴘᴜᴛ.info("••••••••••••••••••••••••••••••••")
    𝙽𝙾𝚁𝙳𝙴𝙳.start()
    ɴᴏʀᴅᴘᴜᴛ.info("••••••••••••••••••••••••••••••••")
    "+"
    "+"
    "+"
    "+"
    try:
        𝙽𝙾𝚁𝙳𝙴𝙳.join_chat("@KrakinzLab")
        𝙽𝙾𝚁𝙳𝙴𝙳.join_chat("@Krakns")
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
        pass
        "+"
        "+"
        "+"
        "+"
    try:
        "+"
        "+"
        "+"
        "+"
        if HEROKU == "HEROKU":
            𝙽𝙾𝚁𝙳𝙴𝙳.send_photo(
            chat_id=ALIVE_CHECK_CHAT,
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
`Congrats on Successfull Bootup of` 
**—••÷[🕊NORDED🕊]÷••—**

-:**Stats**:-
𝙽𝙾𝚁𝙳𝙴𝙳_Bot=✅`check done`
𝙽𝙾𝚁𝙳𝙴𝙳_User=✅`check done`
𝙷𝙴𝚁𝙾𝙺𝚄=✅`check done`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)

        else:
            𝙽𝙾𝚁𝙳𝙴𝙳.send_photo(
            chat_id=ALIVE_CHECK_CHAT,
            photo=
            𝙽𝙾𝚁𝙴𝙳_HUD,
            caption=
            f"""{ӼɛӼօ_𝙽𝙾𝚁𝙴𝙳_ӼɛӼօ}
`Congrats on Successfull Bootup of` 
**—••÷[🕊NORDED🕊]÷••—**

-:**Stats**:-
𝙽𝙾𝚁𝙳𝙴𝙳_Bot=✅`check done`
𝙽𝙾𝚁𝙳𝙴𝙳_User=✅`check done`
𝙷𝙴𝚁𝙾𝙺𝚄=❌`non-heroku_mode`

[🦋•=•=•=•=•=•=•=•=•=•=•=•=•=•🦋](https://t.me/KrakinzBot)
"""
)
        "+"
        "+"
        "+"
        "+"   
    except Exception as Σ_𝙽𝙾𝚁𝙴𝙳_Σ:
        print(Σ_𝙽𝙾𝚁𝙴𝙳_Σ)
    ɴᴏʀᴅᴘᴜᴛ.info("••••••••••••••••••••••••••••••••")
    "+"
    "+"     
    if HEROKU == "HEROKU":
        ɴᴏʀᴅᴘᴜᴛ.info(
        f"\n\n\n\n{LICE}")
    else:
        cprint(
        LICE,
        "green")
    "+"
    "+"   
    "+"
    "+"
    idle()
    "+"
    "+"
    "+"
    "+"  
    ɴᴏʀᴅᴘᴜᴛ.info("••••••••••••••••••••••••••••••••")
    if HEROKU == "HEROKU":
        pass
    else:
        os.system("clear")
    "+"
    "+"
    "+"
    "+"
    ɴᴏʀᴅᴘᴜᴛ.info("••••••••••••••••••••••••••••••••")
    ɴᴏʀᴅᴘᴜᴛ.info(":              🤖+🔴")
    ɴᴏʀᴅᴘᴜᴛ.info(":              OFFLINE")
    ɴᴏʀᴅᴘᴜᴛ.info(":              𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃")
    ɴᴏʀᴅᴘᴜᴛ.info(":              🔴+🤖")
    ɴᴏʀᴅᴘᴜᴛ.info("••••••••••••••••••••••••••••••••")
    𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.stop()
    ɴᴏʀᴅᴘᴜᴛ.info("••••••••••••••••••••••••••••••••")
    ɴᴏʀᴅᴘᴜᴛ.info(":              😈+🔴")
    ɴᴏʀᴅᴘᴜᴛ.info(":              OFFLINE")
    ɴᴏʀᴅᴘᴜᴛ.info(":              𝙽𝙾𝚁𝙳𝙴𝙳")
    ɴᴏʀᴅᴘᴜᴛ.info(":              🔴+😈")
    ɴᴏʀᴅᴘᴜᴛ.info("••••••••••••••••••••••••••••••••")
    𝙽𝙾𝚁𝙳𝙴𝙳.stop()
    ɴᴏʀᴅᴘᴜᴛ.info("••••••••••••••••••••••••••••••••")
    "+"
    "+"
    "+"
    "+"
    sys.exit()
    ɴᴏʀᴅᴘᴜᴛ.info("Overriding code to exit system")
    sys.exit()




"""
=================================================================—••÷[🕊NORDED🕊]÷••—==========================================================================
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
====================================================================—••÷[🕊NORDED🕊]÷••—=======================================================================
"""
