from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.states import Form
from keyboards.reply import rmk
from keyboards.builders import profile

router = Router()


@router.message(Command('profile'))
async def fill_profile(msg: Message, state=FSMContext):
    await state.set_state(Form.name)
    await msg.answer("Boshlimiz, Ismingizmi kiriting!", reply_markup=profile(msg.from_user.first_name))


@router.message(Form.name)
async def Fname(msg: Message, state=FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(Form.lastname)
    await msg.answer("yaxshi endi familyangiz!", reply_markup=rmk)


@router.message(Form.lastname)
async def Flastname(msg: Message, state=FSMContext):
    await state.update_data(lastname=msg.text)
    await state.set_state(Form.age)
    await msg.answer("yaxshi endi yoshingiz!")


@router.message(Form.age)
async def Fage(msg: Message, state=FSMContext):
    inp_text = msg.text
    if inp_text.isdigit() and inp_text > 16 and inp_text < 70:
        await state.update_data(age=inp_text)
        await state.set_state(Form.sex)
        await msg.answer("yaxshi jinsingiz !", reply_markup=profile(["Erkak", "Ayol"]))
    else:
        await msg.answer("son kiriting!")


@router.message(Form.sex, F.text.casefold().in_(['Erkak', 'Ayol']))
async def Fsex(msg: Message, state=FSMContext):
    await state.update_data(sex=msg.text)
    await state.set_state(Form.about)
    await msg.answer("yaxshi endi siz haqizda malumot!", reply_markup=rmk)


@router.message(Form.sex)
async def incorrect_form(msg: Message, state=FSMContext):
    await msg.answer("buttoni bos")


@router.message(Form.about)
async def Fabout(msg: Message, state=FSMContext):
    if len(msg.text) < 5:
        await msg.answer("qiziqarliro narsa yoz")

    await state.update_data(about=msg.text)
    await state.set_state(Form.photo)
    await msg.answer("rasmingizni kirting")


@router.message(Form.photo, F.photo)
async def Fphoto(msg: Message, state=FSMContext):
    photo_file_id = msg.photo[-1].file_id
    data = await state.get_data()
    await state.clear()

    all_data = []

    [all_data.append(f"") for key, value in data.items]

    await msg.answer_photo(photo_file_id, '\n'.join(all_data))


@router(Form.photo, ~F.photo)
async def incorrect_photo(msg: Message, state=FSMContext):
    await msg.answer('photo yuboring')
