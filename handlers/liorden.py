from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.user_keyboards import cats_button
from states.user_satates import CarsState
from utils.db_api.user_comands import add_cars , show_cars

@dp.message_handler(commands="cars")
async def cars_handler(message:types.Message):
    text = "Assalomu aleykum aftomabil korasizmi Yoki qoshaszmi ?⬇️"
    await message.answer(text=text,reply_markup=cars_button)


@dp.message_handler(text="Qoshish➕")
async def add_carrs(message:types.Message , state:FSMContext):
    await CarsState.marka.set()
    text = "Aftomabilingizni Markasini krting"
    await message.answer(text=text)


@dp.message_handler(state=CarsState.marka)
async def add_carrs(message:types.Message , state:FSMContext):
    await state.update_data(marka=message.text)
    await CarsState.name.set()
    text = "Aftomabilni nomini kiriting"
    await message.answer(text=text)



@dp.message_handler(state=CarsState.name)
async def add_name(message:types.Message, state:FSMContext):
    await state.update_data(name=message.text)
    await CarsState.photo.set()
    text = "Aftomablini rasmini jonating krting"
    await message.answer(text=text)


@dp.message_handler(state=CarsState.photo, content_types=types.ContentType.PHOTO)
async def get_user_data_handler(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    text = "Rangini jonating"
    await CarsState.color.set()
    await message.answer(text=text)




@dp.message_handler(state=CarsState.color)
async def add_color(message:types.Message, state:FSMContext):
    await state.update_data(color=message.text)
    data = await state.get_data()
    new_car = await add_cars(data)
    if new_car:
        text = "Szning afttomabil qoshildi ✅"
    else:
        text = "Botda xatolik bor❌"
    await message.answer(text=text, reply_markup=cars_button)
    await state.finish()





@dp.message_handler(text="Korish👀")
async def show_all_cars_handler(message:types.Message):
    all_cars = await show_cars()
    text = "Aftomabil royxati  ro'yxati: \n\n"
    for cars in all_cars:
        text += f"{cars['marka']} -- {cars['name']} -- {cars['color']}\n"
        await message.answer_photo(photo=cars['photo'],caption=text)









