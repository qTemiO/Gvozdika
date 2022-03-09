import asyncio
import datetime
from re import search 

from loguru import logger
from telethon import TelegramClient

# Use your own values from my.telegram.org
api_id = 15316406
api_hash = 'ad62ac5526adf8d79b7d4b5d26f7e93e'
session_name = 'Igor'
chats = ['@rf200_now']
client = TelegramClient(session_name, api_id, api_hash)

async def main(chats):
    messages = []
    for chat in chats:
        message = await client.get_messages(chat, limit=15, offset_date=datetime.date(2022, 3, 7), search='Андреев Александр Геннадьевич')
        messages.append(message)

    logger.debug(messages[0][0].stringify())
    logger.debug(len(messages))

with client.start():
    client.loop.run_until_complete(main(chats))