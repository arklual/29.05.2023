from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime, date
import zoneinfo
from strings import *
from settings import *

zone = zoneinfo.ZoneInfo("Europe/Moscow")
app = Client("bot1", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.chat(posts_from_3))
async def on_new_message_3(client, message:Message):
    if date.today().weekday() > 5:
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
            await app.send_photo(send_to_3, message.photo.file_id)
            return

    if '#start' in text.lower():
        await app.send_message(send_to_3, START_ENG_MESSAGE)
    elif '#soon' in text.lower():
        await app.send_message(send_to_3, SOON_MESSAGE)
    elif '#start2' in text.lower():
        await app.send_message(send_to_3, START_2_MESSAGE)
    elif '#stop' in text.lower():
        await app.send_poll(send_to_3, STOP_ENG_MESSAGE, [STOP_ENG_MESSAGE_1, STOP_ENG_MESSAGE_2])
    elif 'вверх' in text.lower():
        await app.send_message(send_to_3, UP_MESSAGE)
    elif 'вниз' in text.lower():
        await app.send_message(send_to_3, DOWN_MESSAGE)
    elif 'возврат' in text.lower():
        await app.send_message(send_to_3, RETURN_MESSAGE)
    elif '+' in text.lower():
        await app.send_message(send_to_3, PLUS_MESSAGE)
    elif '-' in text.lower():
        await app.send_message(send_to_3, MINUS_MESSAGE)
    elif 'догон' in text.lower():
        await app.send_message(send_to_3, DOUBNEDEAL_MESSAGE)
    else:
        if file_id:
            await app.send_photo(send_to_3, file_id, text)
        else:
            await app.send_message(send_to_3, text)

@app.on_message(filters.chat(posts_from_4))
async def on_new_message_4(client, message:Message):
    if date.today().weekday() > 3:
        return
    if datetime.now(zone).hour < 9 or datetime.now(zone).hour > 11:
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
            await app.send_photo(send_to_4, message.photo.file_id)
            return

    if '#testing' in text.lower():
        await app.send_message(send_to_4, TESTING_MESSAGE)
    elif '#stoping' in text.lower():
        await app.send_message(send_to_4, STOPING_MESSAGE)
    else:
        if file_id:
            await app.send_photo(send_to_4, file_id, text)
        else:
            await app.send_message(send_to_4, text)

app.run()