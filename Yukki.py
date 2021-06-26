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


async def bot_sys_stats():
    bot_uptime = int(time.time() - YUKKI_START_TIME)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    stats = f'''
Uptime: {get_readable_time((bot_uptime))}'''
    return stats


@Client.on_message(filters.command(["ping", "start", "alive"]) & filters.user(SUDO_USERS))
async def ping(_, message):
    start = datetime.now()
    uptime = await bot_sys_stats()
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await message.reply_text(f"**Alive!**\n**Responding in**`⚡{resp} ms`\n\n<b><u>Uptime:</u></b>{uptime}")   









































idle()
