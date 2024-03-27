from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton,  InlineKeyboardButton, InlineKeyboardMarkup

import config

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb.add(KeyboardButton('/help')).insert(KeyboardButton('/photo')).add(KeyboardButton('/random')).insert(KeyboardButton('/description'))

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Button 1',
                           url=config.URL_youtube)
ib2 = InlineKeyboardButton(text='Button 2',
                           url=config.URL_youtube)


ikb.add(ib1, ib2)