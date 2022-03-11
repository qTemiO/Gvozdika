from loguru import logger
from telethon import TelegramClient
import datetime

api_id = 15316406
api_hash = 'ad62ac5526adf8d79b7d4b5d26f7e93e'
session_name = 'Igor'
client = TelegramClient(session_name, api_id, api_hash)
chat_list = ['https://t.me/voenacher']


from_date = datetime.date(2022,3, 1)
to_date = datetime.date(2022, 3, 7)
search_key = 'Украина'

with open('result.txt', 'w') as f:
    for chat in chat_list:
        async def get_messages_at_date(chat, from_date, to_date, search_key):
            result = []
            limit_day = to_date + datetime.timedelta(days=1)
            lower_day = from_date - datetime.timedelta(days=1)
            iterator = client.iter_messages(chat, offset_date=limit_day, search=search_key)
            async for message in iterator:
                if message.date.day == lower_day.day and message.date.month == lower_day.month and message.date.year == lower_day.year:
                    return result

                one_message_info = [message.sender.username, message.date, message.text]
                result.append(one_message_info)
                
                logger.debug(message.date)
                logger.debug(from_date)


        with client:
            date_filt = client.loop.run_until_complete(get_messages_at_date(chat, from_date, to_date, search_key))
            if date_filt != None:
                for item in date_filt:
                    f.write(f'{item[0]} {item[1]}\n')