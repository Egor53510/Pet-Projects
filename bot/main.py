from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton,  InlineKeyboardButton, InlineKeyboardMarkup
from random import randrange
import wikipedia, easyocr
from PIL import Image
import os

from aiogram.contrib.middlewares.logging import LoggingMiddleware
import logging

import config, keyboards

logging.basicConfig(level=logging.INFO)

bot = Bot(config.TOKEN_API)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описание бота</em>
<b>/photo</b> - <em>отправка нашего фото</em>
<b>/vote</b> - <em>голосование нравится ли тебе эта игра</em>
<b>/wiki</b> - <em>поиск статей по википедии</em>"""

async def on_startup(_):
    print('Я запустился!')

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='И снова сдрасте!',
                           reply_markup=keyboards.kb)
    
#      помощь с командами
@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')

#       описание бота
@dp.message_handler(commands=['description'])
async def command_desc(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Наш бот что-то умеет проверь это)')
    
#       отправляет фотографию
@dp.message_handler(commands=['photo'])
async def send_orange(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=config.PHOTO_dota2)

#     случайное место
@dp.message_handler(commands=['random'])
async def send_random(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=randrange(1, 100),
                            longitude=randrange(1, 100))
    
#     википедия поиск информации    
dialogs = {}
@dp.message_handler(commands=["wiki"])
async def command_wiki(message: types.Message):
    await message.reply("Введите ваш запрос")

    dialogs[message.chat.id] = "waiting_for_query"
@dp.message_handler(lambda message: message.chat.id in dialogs and dialogs[message.chat.id] == "waiting_for_query")
async def proccess_wiki_query(message:types.Message):
    query = message.text

    wikipedia.set_lang("ru")
    search_results = wikipedia.search(query)
    if search_results:
        page = wikipedia.page(search_results[0])
        await message.reply(page.summary)
    else:
        await message.reply("По вашему запросу ничего не найдено.")

    del dialogs[message.chat.id]

#     текст с картинки
reader = easyocr.Reader(['ru']) 
@dp.message_handler(commands=['text'])
async def handle_text_command(message: types.Message):
    photo = message.photo[-1]
    file_id = photo.file_id

    file = await bot.get_file(file_id)
    file_path = file.file_path

    downloaded_file = await bot.download_file(file_path)

    with open('image.jpg', 'wb') as new_file:
        new_file.write(downloaded_file.read())

    result = reader.readtext('image.jpg')

    text = '\n'.join([bbox[1] for bbox in result])

    os.remove('image.jpg')

    await message.answer(text)

#     голосование картинки    
@dp.message_handler(commands=['vote'])
async def command_vote(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                           photo=config.PHOTO_dota2,
                           caption="Нравится ли тебе эта игра?",
                           reply_markup=keyboards.ikb)
    
@dp.callback_query_handler(lambda query: query.data in ["like", "dislike"])
async def callback_vote(callback: types.CallbackQuery):
    if callback.data == 'like':
        await bot.answer_callback_query(callback.id, text='Нравится')
    await bot.answer_callback_query(callback.id, text='Не нравится')

#     отправляет сердечки
@dp.message_handler()
async def send_cat(message: types.Message):
    if message.text == '❤️':
        await bot.send_sticker(chat_id=message.from_user.id,
                               sticker=config.STICKER_HEART)
    if message.text in config.parting:
        await bot.send_sticker(chat_id=message.from_user.id,
                               sticker=config.STICKER_Before_the_connection)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)