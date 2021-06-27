print("[INFO]: INITIALIZING")
from pyrogram import Client
import asyncio
from config import API_ID, API_HASH, BOT_TOKEN, MONGO_DB_URI, SUDO_USERS, LOG_ID
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import time
import uvloop
import logging
import os
import psutil
from datetime import datetime
from pyrogram import Client, idle, filters
from pyrogram.types import Message
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from timesexy import get_readable_time

print("[INFO]: INITIALIZING DATABASE")
MONGODB_CLI = MongoClient(MONGO_DB_URI)
db = MONGODB_CLI.wbb

YUKKI_START_TIME = time.time()

timesmode = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", 13" , "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",]

print("[INFO]: INITIALIZING BOT CLIENT")
app = Client(
    'YukkiBot',
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

print("[INFO]: STARTING BOT CLIENT")
app.start()
print("[INFO]: STARTED")


@app.on_message(filters.command(["ping", "start", "alive"]))
async def ping(_, message):
    start = datetime.now()
    bot_uptime = int(time.time() - YUKKI_START_TIME)
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await message.reply_text(f"**Alive!**\n**Responding in** {resp} ms\n\n<b><u>Uptime:</u></b>{get_readable_time((bot_uptime))}")   
    
    
@app.on_message(filters.command("Lock_on"))
async def on(_, message):             
    usage = f"This isn't a time.\n\nSelect from 0-23 where 0 is 00:00 AM and 23 is 11:00 PM\n\n"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    timer = message.text.split(None, 1)[1].strip()
    if theme not in themes:
        return await message.reply_text(usage)
    note = {
        "theme": timer,
    }
    await save_theme(message.chat.id, "timeon", note)  
    await message.reply_text(f"Changed Group Lock Time to {theme}")         
   








































idle()
