from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


main_kb = ReplyKeyboardMarkup(
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


# Pagination class Clalback datadan voris ovoti va unga parametra bervoti
class Pagination(CallbackData, prefix='Pag'):
    action: str
    page: int


def paginator(page: int = 0):
    inline_builder = InlineKeyboardBuilder()
    # bu codeam "buttonga" oxshab malumot qoshib button yaratib beradi
    inline_builder.row(
        InlineKeyboardButton(
            text='⏮️',
            # Pagination yordamimda Callback Yaratadi
            callback_data=Pagination(action='prew', page=page).pack()
        ),
        InlineKeyboardButton(
            text='⏭️',
            # Pagination yordamimda Callback Yaratadi
            callback_data=Pagination(action='next', page=page).pack()
        ),
        width=2
    )
    return inline_builder.as_markup()


links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Telegram', url='tg://resolve?domain=MBOSSL'),
            InlineKeyboardButton(
                text='GitHub', url='https://github.com/ummad741')
        ]
    ]
)


def calc_kb():
    calc_items = [
        '1', '2', '3', '/',
        '4', '5', '6', '*',
        '7', '8', '9', '-',
        '0', '.', '=', '*',
    ]

    builder = ReplyKeyboardBuilder()
    # bitta qatordagoi for tikli calc itemsdan malumotlarni olib button yaratadi
    [builder.button(text=item) for item in calc_items]
    builder.button(text="ORQAGA")
    builder.adjust(*[4]*4, 1)

    #
    return builder.as_markup(resize_keyboard=True)


spec_kb = ReplyKeyboardMarkup(
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
