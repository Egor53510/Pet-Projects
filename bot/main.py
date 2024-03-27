from aiogram import Bot, Dispatcher, _asyncio, types
from aiogram.filters import Command

import string, random

import config, buttons
#pytontelegram telethon pyrogram

HELP_COMMAND = """
<strong>help</strong> - <em>список команд</em>
<strong>start</strong> - <em>начать работу с ботом</em>
<strong>description</strong> - <em>описание бота</em>
<strong>give</strong> - <em>возвращает стикер</em>
<strong>картинка</strong> - <em>отправляет фотографию заставки доты</em>
GAIZENBERG_TOKIOGHOU _DEANHNOTEN=intelCOREi5#gg
"""


bot = Bot(config.TOKEN_API)
dp = Dispatcher()

async def on_startup():
    print("Бот был успешно запущен!")

@dp.message(Command("help"))
async def help_command(messege: types.Message):
    await bot.send_message(chat_id=messege.from_user.id, 
                           text=HELP_COMMAND, 
                           parse_mode="HTML",
                           reply_markup=buttons.keyboard_help())
    await messege.delete()

@dp.message(Command("start"))
async def start_command(messege: types.Message):
    await messege.answer(text='<em>Добро пожаловать в наш телеграмм бот!</em>', 
                         parse_mode="HTML",
                         reply_markup=buttons.keyboard_start())
    await messege.delete()

@dp.message(Command("description"))
async def desc_command(messege: types.Message):
    await messege.answer(text="Данный наверное что-то умеет, можешь проверить)")
    await messege.delete()

@dp.message(Command("give"))
async def give_sticker(messege:types.Message):
    await messege.answer(text="Смотри какой смешной клоун " + "❤️")
    await bot.send_sticker(messege.from_user.id, 
                           sticker=config.STICKER_shadow_fiend)
    await messege.delete()

@dp.message(Command("картинка"))
async def send_image(messege:types.Message):
    await bot.send_photo(chat_id=messege.chat.id,
                         photo=config.PHOTO_dota2)
    await messege.delete()


@dp.message()
async def bye(messege:types.Message):
    global count
    if messege.text in config.parting:
        await bot.send_sticker(messege.from_user.id, 
                               sticker=config.STICKER_Before_the_connection)
    if "❤️" in messege.text:
        await messege.answer(text="🖤" * messege.text.count("❤️"))
        count = messege.text.count("❤️")
        await messege.answer(text=f"Количество сердешек = {count}")

#@dp.message()
#async def send_sticker_id(messege:types.Message):
    #if messege.content_type == messege.sticker:
        #await messege.answer(messege.sticker.file_id)

#@dp.message()
#async def check_count(messege: types.Message):
    #await messege.reply('YES') if '0' in messege.text else await messege.reply('NO')

#@dp.message()
#async def send_random_letter(messege: types.Message):
   #await messege.reply(random.choice(messege.text))


async def main():
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == '__main__':
    _asyncio.run(main())