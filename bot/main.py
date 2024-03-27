from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton,  InlineKeyboardButton, InlineKeyboardMarkup
from random import randrange

import config, keyboards

bot = Bot(config.TOKEN_API)
dp = Dispatcher(bot)

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
                           reply_markup=keyboards.kb)

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
    
@dp.message_handler(commands=['vote'])
async def command_vote(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='❤️',
                           callback_data="like")
    ib2 = InlineKeyboardButton(text='🖤',
                           callback_data="dislike")
    ikb.add(ib1, ib2)

    await bot.send_photo(chat_id=message.from_user.id,
                           photo=config.PHOTO_dota2,
                           caption="Нравится ли тебе эта игра?",
                           reply_markup=ikb)
@dp.callback_query_handler()
async def callback_vote(callback: types.CallbackQuery):
    if callback.data == 'like':
        print('Нажата кнопка')
        await callback.answer(text='Нравится', show_alert=True)
    await callback.answer(text='Не нравится', show_alert=True)


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