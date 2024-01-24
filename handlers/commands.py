from aiogram import Router, F
from aiogram.types import Message
from keyboards import inline, reply, builders
from data.subloader import get_json

router = Router()


# bitta handlerni ichida 2ta keyboardsni eventlarini yaratish "in_" functiasi yordamida
@router.message(F.text.lower().in_(["qalesan", 'qaleman']))
async def groups_msg(message: Message):
    text = message.text.lower()
    await message.reply(f"{"zorman"}")


# bu function keybordalni eventlariga javob beradi 'main'
@router.message()
async def main_echo(message: Message):
    input_text = message.text.lower()
    smiles = await get_json('smiles.json')

    if input_text == 'link':
        await message.answer("<b>Linklar Royxati</b>", reply_markup=inline.links)
    elif input_text == 'special button':
        await message.answer('<b>Spetc Knopkalar</b>', reply_markup=reply.spec)
    elif input_text == 'calculiator':
        await message.answer('<b>Calculator</b>', reply_markup=builders.calc())
    elif input_text == 'emoji':
        await message.answer(f'{smiles[0][0]} <b>{smiles[0][1]}</b>', reply_markup=builders.paginator())
