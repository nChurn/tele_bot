from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Создать анкету')
        ],
        [
            KeyboardButton(text='Начать поиск'),
            KeyboardButton(text='Help')
        ]
    ],
    resize_keyboard = True
)