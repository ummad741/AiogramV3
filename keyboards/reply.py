from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Emoji'),
            KeyboardButton(text='Link')
        ],
        [
            KeyboardButton(text='Calculiator'),
            KeyboardButton(text='Special button')
        ]
    ],
    # olchamini yaxshilab beradi
    resize_keyboard=True,
    # bir marta ishlatgandan keyin yoqolib ketadai
    one_time_keyboard=True,
    # bu inputga place holder
    input_field_placeholder="Menudan birini tanlang"
)
spec = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='GEO jonatish', request_location=True),
            KeyboardButton(text='Kontakt jonatish', request_contact=True)
        ],
        [
            KeyboardButton(text='Orqaga')
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
rmk = ReplyKeyboardRemove()
