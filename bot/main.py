from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from random import randrange

import config

bot = Bot(config.TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/help')).insert(KeyboardButton('/photo')).add(KeyboardButton('/random')).insert(KeyboardButton('/description'))

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/description</b> - <em>описание бота</em>
<b>/photo</b> - <em>отправка нашего фото</em>"""

async def on_startup(_):
    print('Я запустился!')

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='И снова сдрасте!',
                           reply_markup=kb)

@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')

@dp.message_handler(commands=['description'])
async def command_desc(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Наш бот что-то умеет проверь это)')

@dp.message_handler(commands=['photo'])
async def send_orange(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=config.PHOTO_dota2)

@dp.message_handler(commands=['random'])
async def send_random(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=randrange(1, 100),
                            longitude=randrange(1, 100))

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