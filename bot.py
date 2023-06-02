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
