from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def spamkb(chatId, messageId, userId):
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton(text='Удаляем💀', callback_data=f'1_{chatId}_{messageId}_{userId}'), 
        InlineKeyboardButton(text='Оставляем😇', callback_data=f'0_{chatId}_{messageId}_{userId}')
    )
    return keyboard