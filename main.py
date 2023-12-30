import asyncio
import logging
import sys
from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest
# pythoni standartni kutubxonasi
from contextlib import suppress
import keyboards as kb

TOKEN = '6640659910:AAG1IRM-Vt8-HP3QkhP5RsHln3u0TfBJ1wU'
bot = Bot(TOKEN, parse_mode='HTML')
dp = Dispatcher()


# projectni strukturasi va run qiladigan functionlari
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Asalomu alekum botimizga hush kelibsiz!", reply_markup=kb.main_kb)


smiles = [
    ["🥑", 'Avacadoni yaxshi korasizmi?'],
    ["🍓", 'Qulpinoyni yaxshi korasizmi ?'],
    ["☁️", 'Ideyalariz bormi?'],
    ["😄", 'Sizda hammasi oxshidi!'],

]

# bitta handlerni ichida 2ta keyboardsni eventlarini yaratish "in_" functiasi yordamida


@dp.callback_query(kb.Pagination.filter(F.action.in_(['next', 'prew'])))
# callback_data izalirovanie
async def pagination_handler(call: CallbackQuery, callback_data: kb.Pagination):
    page_num = int(callback_data.page)
    # page num 0 dan kotta bosa ayiradi -cheksilika qarab yurib ketmidi
    page = page_num - 1 if page_num > 0 else 0  # prew

    if callback_data.action == 'next':
        # page_num smileseni lenidan kotalashib ketomidi
        page = page_num + 1 if page_num < (len(smiles)-1) else page_num

    # try exceptioni ornini bosadi va hato qataligni ushab beradi telegram botga nma hodisa bovotganini yetqazadi
    with suppress(TelegramBadRequest):
        # pageni almashtiradi smilesni lenidan oshib ketmagan holda
        await call.message.edit_text(f"{smiles[page][0]} <b>{smiles[page][1]}</b>", reply_markup=kb.paginator(page))
        await call.answer()


@dp.message(F.text.lower().in_(["qalesan", 'qaleman']))
async def groups_msg(message: Message):
    text = message.text.lower()
    await message.reply(f"{"zorman"}")

# bu function keybordalni eventlariga javob beradi 'main'


@dp.message()
async def main_echo(message: Message):
    input_text = message.text.lower()
    if input_text == 'link':
        await message.answer("<b>Linklar Royxati</b>", reply_markup=kb.links_kb)
    elif input_text == 'special button':
        await message.answer('<b>Spetc Knopkalar</b>', reply_markup=kb.spec_kb)
    elif input_text == 'calculiator':
        await message.answer('<b>Calculator</b>', reply_markup=kb.calc_kb())
    elif input_text == 'emoji':
        await message.answer(f'{smiles[0][0]} <b>{smiles[0][1]}</b>', reply_markup=kb.paginator())


# projectni strukturasi va run qiladigan functionlari
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
