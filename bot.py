from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime, date
import zoneinfo
from strings import *
from settings import *

zone = zoneinfo.ZoneInfo("Europe/Moscow")
app = Client("bot", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.chat(posts_from_1))
async def on_new_message_1(client, message:Message):
    if date.today().weekday() > 3:
        return
    if datetime.now(zone).hour < 9 or datetime.now(zone).hour > 12:
        return
    text = ''
    file_id = None
    if message.text:
        text = message.text
    elif message.photo:
        if message.caption:
            text = message.caption
            file_id = message.photo.file_id
        else:
            await app.send_photo(send_to_1, message.photo.file_id)
            return

    if '#старт' in text.lower():
        await app.send_message(send_to_1, START_MESSAGE)
    elif '#бо' in text.lower():
        await app.send_message(send_to_1, BO_MESSAGE)
    else:
        if file_id:
            await app.send_photo(send_to_1, file_id, text)
        else:
            await app.send_message(send_to_1, text)

@app.on_message(filters.chat(posts_from_2))
async def on_new_message_2(client, message:Message):
    print(2)
    if date.today().weekday() > 4:
        return
    if datetime.now(zone).hour < 13 or datetime.now(zone).hour > 22:
        return
    text = ''
    file_id = None
    if message.text:
        text = message.text
    elif message.photo:
        if message.caption:
            text = message.caption
            file_id = message.photo.file_id
        else:
            await app.send_photo(send_to_2, message.photo.file_id)
            return
    print('Текст:', text)
    if '#об' in text.lower():
        await app.send_message(send_to_2, OB_MESSAGE)
    elif '#трейд' in text.lower():
        await app.send_message(send_to_2, TRADE_MESSAGE)
    elif '#стоп' in text.lower():
        await app.send_message(send_to_2, STOP_MESSAGE)
    else:
        if file_id:
            await app.send_photo(send_to_2, file_id, text)
        else:
            await app.send_message(send_to_2, text)

app.run()