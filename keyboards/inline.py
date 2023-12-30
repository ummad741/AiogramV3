from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Telegram', url='tg://resolve?domain=MBOSSL'),
            InlineKeyboardButton(
                text='GitHub', url='https://github.com/ummad741')
        ]
    ]
)
