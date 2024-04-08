from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton,  InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, executor, types

import config

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb.add(KeyboardButton('/help')).insert(KeyboardButton('/photo')).add(KeyboardButton('/random')).insert(KeyboardButton('/description'))
kb.add(KeyboardButton('/wiki'))

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='❤️',
                                callback_data="like")
ib2 = InlineKeyboardButton(text='🖤',
                                callback_data="dislike")
ikb.add(ib1, ib2)
    
