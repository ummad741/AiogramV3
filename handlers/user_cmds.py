from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from keyboards import reply

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Asalomu alekum botimizga hush kelibsiz!", reply_markup=reply.main)
