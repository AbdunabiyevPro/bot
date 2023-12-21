from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from utils.chakers import chack
from states.user_satates import RegisterState
# from utils.db_api.user_comands  import get_user, add_user
from loader import dp
from keyboards.default.user_keyboards import *
from keyboards.inline.bals_keyboard import check_inline
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    chekcer = await chack(user_id=message.chat.id)
    if chekcer:
        text = "Assalomu alaykum"
    else:
        text = "Bu botdan foydalanish uchun kanalga a'zo bo'ling"
    await message.answer(text=text, reply_markup=check_inline)


@dp.callback_query_handler(text="check")
async def check_handler(call: types.CallbackQuery):
    chanel = await chack(user_id=call.message.chat.id)
    if chanel:
        text = "Assalomu alaykum"
        await call.message.answer(text=text)



#

#
#
# @dp.message_handler(commands="start")
# async def start_handler(message: types.Message):
#     find_user = get_user(chat_id=message.chat.id)
#     if find_user:
#         text = "Hello welkom to the bot"
#         await message.answer(text=text)
#     else:
#         text = "Hello please  wirte your full name"
#         await message.answer(text=text, reply_markup=register)
#         await RegisterState.full_name.set()
#
#
# @dp.message_handler(state=RegisterState.full_name)
# async def get_full_name(message: types.Message, state: FSMContext):
#     await state.update_data(full_name=message.text)
#     text = "Phone number"
#     await message.answer(text=text, reply_markup=user_phone_share)
#     await RegisterState.phone_number.set()
#
#
# @dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentType.CONTACT)
# async def get_phone_number_handler(message: types.Message, state: FSMContext):
#     await state.update_data(phone_number=message.contact.phone_number)
#     data = await state.get_data()
#     if await add_user(data):
#         text = "Welkom to the bot✅"
#         await message.answer(text=text, reply_markup=gym_menu)
#     else:
#         text = "Bot Has got problem❌"
#         await message.answer(text=text)
#         await state.finish()
#
#
