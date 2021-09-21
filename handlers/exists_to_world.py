from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from applications.weather import get_weather, get_weather_week
from keyboards import weather_back, menu
from keyboards.menu import menu_navigation
from loader import dp



@dp.message_handler(text="Выйти в мир ⚡")
async def get_news(message: types.Message):
    # открываем клавиатуру движения
    await message.answer("Нажмите на нужную вам кнопку 🔀", reply_markup=menu_navigation)


@dp.message_handler(text="Вперед 👆🏻", state=None)
async def state_activate_weather_command1(message: types.Message):
    await message.answer('Вы пошли в вперед в город и вас схватили бандиты 🔫:')


@dp.message_handler(text="Влево 👈", state=None)
async def state_activate_weather_command1(message: types.Message):
    await message.answer('Вы свернули налево, прошли вдоль ручья и встретили медведя 💩')


@dp.message_handler(text="Вправо 👉", state=None)
async def state_activate_weather_command1(message: types.Message):
    await message.answer('Вы свернули на право и под деревом нашли клад 🤑:')