from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.markdown import hbold

def keyboard_start():
    builder = ReplyKeyboardBuilder()

    builder.button(text="/help")

    return builder.as_markup()

def keyboard_help():
    builder = ReplyKeyboardBuilder()

    builder.button(text="/help")
    builder.button(text="/start")
    builder.button(text="/description")
    builder.button(text="/give")
    builder.button(text="/картинка")
    builder.adjust(1)

    return builder.as_markup()