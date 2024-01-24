from aiogram.types import InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


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


def calc():
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


def profile(text: str | list):
    builder = ReplyKeyboardBuilder()
    if isinstance(text, str):
        text = [text]

    [builder.button(text=txt) for txt in text]

    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

    