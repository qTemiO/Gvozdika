from telethon import TelegramClient

# Use your own values from my.telegram.org
api_id = 15316406
api_hash = 'ad62ac5526adf8d79b7d4b5d26f7e93e'
session_name = 'Igor'
client = TelegramClient(session_name, api_id, api_hash)
chat = '@alfiron'
async def main(chat):
    async for message in client.iter_messages(chat, search= 'март'):
        print(message.date, message.text)
with client:
    client.loop.run_until_complete(main(chat))