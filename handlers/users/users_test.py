from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram import types
from aiogram.types import InputFile
from keyboards.default.user_keyboards import *
from keyboards.inline.bals_keyboard import *
from aiogram.types import ReplyKeyboardRemove




@dp.message_handler(text="Contact📞")
async def cpntact_handler(message:types.Message):
    text = "Botda Xatolik Topsangiz \n@NASAnx Ga murojat Qilin!"
    await message.answer(text=text)



@dp.callback_query_handler(text="back_main_menu")
async def back_handler(call:types.CallbackQuery):
    text="choose⬇️"
    await call.message.answer(text=text,reply_markup=main_menu)


@dp.message_handler(text="Products🛍")
async def menu_handler(message:types.Message):
    text = "Products⬇️"
    await message.answer(text=text,reply_markup=gym_menu)


@dp.message_handler(text="Back")
async def beck_handler(message:types.Message):
    text="Products⬇️"
    await message.answer(text=text,reply_markup=main_menu)

@dp.callback_query_handler(text="back_top")
async def back_handler(call:types.CallbackQuery):
    text = "All Bals"
    photo = InputFile(path_or_bytesio="./photoo/balls.jpg")
    await call.message.answer_photo(caption=text, photo=photo, reply_markup=balls)


@dp.message_handler(text="Balls⚽️")
async def handlaer(message:types.Message):
    text="All Bals"
    photo = InputFile(path_or_bytesio="./photoo/balls.jpg")
    await message.answer_photo(caption=text,photo=photo,reply_markup=balls)
    


@dp.callback_query_handler(text="amerika")
async def amerika_handler(call:types.CallbackQuery):
    text = "Ball\nPrice 15$"
    photo = InputFile(path_or_bytesio="./photoo/usa_ball.jpg")
    await call.message.answer_photo(photo=photo,caption=text,reply_markup=shop_keyboard)


@dp.message_handler(text="GYM🏋️‍♀️")
async def gym_handler(message:types.Message):
    text= "All_gym"
    photo = InputFile(path_or_bytesio="./photoo/gym.jpg")
    await message.answer_photo(caption=text,photo=photo,reply_markup=gym_shop)

@dp.message_handler(text="")
async def boks_handler(message:types.Message):
    text = "All_gym"
    photo = InputFile(path_or_bytesio="./photoo/boks_photo.jpg")
    await message.answer_photo(caption=text,photo=photo)