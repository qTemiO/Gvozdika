from telethon import TelegramClient
import datetime
from datetime import timedelta

api_id = 15316406
api_hash = 'ad62ac5526adf8d79b7d4b5d26f7e93e'
session_name = 'Igor'
client = TelegramClient(session_name, api_id, api_hash)
chat_list = ['https://t.me/voenacher', '@alfiron']


from_date = datetime.date(2022,3, 5)
to_date = datetime.date(2022, 3, 11)
date_list = []
delta = to_date - from_date
if delta.days <= 0:
    print("Error")
for i in range(delta.days + 1):
    date = from_date + timedelta(i)
    date_list.append(date)
print(date_list)

for date in date_list:
    for chat in chat_list:
        async def get_messages_at_date(chat, date):
            result = []
            tomorrow = date + datetime.timedelta(days=1)
            async for msg in client.iter_messages(chat, offset_date=tomorrow, search= 'Украина'):
                edited_date = (msg.date).date()
                if edited_date == date:
                    one_message_info = [msg.sender.username, str(msg.date), msg.text]
                    result.append(one_message_info)
                else:
                    return result

        with client:
            date_filt = client.loop.run_until_complete(get_messages_at_date(chat, date))
            print(date_filt)
