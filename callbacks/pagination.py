from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards import inline, builders
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from data.subloader import get_json

router = Router()


@router.callback_query(builders.Pagination.filter(F.action.in_(['next', 'prew'])))
# callback_data izalirovanie
async def pagination_handler(call: CallbackQuery, callback_data: builders.Pagination):
    smiles = await get_json('smiles.json')
    page_num = int(callback_data.page)
    # page num 0 dan kotta bosa ayiradi -cheksilika qarab yurib ketmidi
    page = page_num - 1 if page_num > 0 else 0  # prew

    if callback_data.action == 'next':
        # page_num smileseni lenidan kotalashib ketomidi
        page = page_num + 1 if page_num < (len(smiles)-1) else page_num

    # try exceptioni ornini bosadi va hato qataligni ushab beradi telegram botga nma hodisa bovotganini yetqazadi
    with suppress(TelegramBadRequest):
        # pageni almashtiradi smilesni lenidan oshib ketmagan holda
        await call.message.edit_text(f"{smiles[page][0]} <b>{smiles[page][1]}</b>", reply_markup=builders.paginator(page))
        await call.answer()
