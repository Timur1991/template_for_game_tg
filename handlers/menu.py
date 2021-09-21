# импорты для работы aiogram
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink


from loader import dp

# импорт приложений
from applications.weather import get_weather, get_weather_week



# испорт клавиатур
from keyboards import menu, translate_menu, weather_back, news_back, film_search, reddit_main, \
    subscriber_menu


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    """Команда menu открывает основное меню"""
    await message.answer("Выберите действие из меню ниже 🤖", reply_markup=menu)


@dp.message_handler(text="Закрыть клавиатуру 🔒")
async def exit_from_menu(message: types.Message):
    """Выбор из основного меню для закрытия менюшки"""
    await message.answer("Вы отключили клавиатуру ❎", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Поесть 👅")
async def translate_text(message: types.Message):
    """Выбор из основного меню для открытия клавиатуры выбора переводов"""
    await message.answer("Выберите варианты переводов 🤖", reply_markup=translate_menu)


# class Weather(StatesGroup):
#     command1 = State()
#     command2 = State()
#
#
# @dp.message_handler(text="Узнать погоду 🌏")
# async def show_translate_menu(message: types.Message):
#     """По команде get_translation открывает клавиатуру для выбора переводов"""
#     await message.answer("Нажмите на нужную вам кнопку 🔀", reply_markup=weather_back)
#
#
# #  активация первого состояния Weather
# @dp.message_handler(text="Погода ⛅", state=None)
# async def state_activate_weather_command1(message: types.Message):
#     await message.answer('Просто вводи город или населенный пункт 🏙:', reply_markup=weather_back)
#     await Weather.command1.set()
#
#
# # выполняем команду первого состояния, выводим температуру и описание погоды
# @dp.message_handler(state=Weather.command1)
# async def get_answer_one_day(message: types.Message, state: FSMContext):
#     weather = get_weather(message)
#     await message.answer(weather)
#     await state.finish()
#
#
# # активация второго состояния Weather
# @dp.message_handler(text="Погода на 6 дней 📆")
# async def state_activate_weather_command2(message: types.Message):
#     await message.answer('Просто вводи город или населенный пункт 🏙:', reply_markup=weather_back)
#     await Weather.command2.set()
#
#
# # выполняем команду второго состояния, выводим прогноз погоды на следующие 6 дней
# @dp.message_handler(state=Weather.command2)
# async def get_answer_six_days(message: types.Message, state: FSMContext):
#     days = get_weather_week(message)
#     if len(days) > 2:
#         text_test = "{day}"
#         text = '\n\n'.join(
#             [
#                 text_test.format(day=day)
#                 for day in days
#             ]
#         )
#         await message.answer(text)
#     else:
#         await message.answer(' '.join(days))
#     await state.finish()


class Films(StatesGroup):
    command1 = State()


# активация первого состояния Films
@dp.message_handler(text="Повторы 🎦", state=None)
async def state_activate_films_command1(message: types.Message):
    await message.answer(
        '📺 Тут ваши повторы',
        reply_markup=film_search)
    # await Films.command1.set()


# выполняем команду1 первого состояния, выводим названия фильмов и их рейтинг
@dp.message_handler(state=Films.command1)
async def get_rate_films_by_keyword(message: types.Message, state: FSMContext):
    """Выводит рейтинг фильмов по ключевому слову"""
    # try:
    #     films = get_film(message.text)
    #     for film, year, rate, link in films:
    #         await message.answer(f'Фильм: "{film}"\nГод: {year}\nРейтинг: "{rate}\nСсылка: {link}')
    # except:
    #     await message.answer(
    #         'В написании допущена ошибка! 🤖 \nСледуйте правилам написания "название"-"количество выдачи"')
    # await state.finish()
    pass


@dp.message_handler(text="Рейтинг 🔺")
async def get_top20_films_by_rate_kinopoisk(message: types.Message):
    """Выводит топ20 фильмов по версии кинопоиска"""
    # films = get_film_top20()
    # text_films = 'Фильм: "{film}"\nРейтинг: "{rate}"'
    # text = '\n\n'.join(
    #     [
    #         text_films.format(film=film, rate=rate)
    #         for film, rate in films.items()
    #     ]
    # )
    # await message.answer(text, reply_markup=top20_films)
    pass


@dp.message_handler(text="Новости⚡")
async def show_news_menu(message: types.Message):
    """По команде show_news_menu открывает клавиатуру для выбора новостей"""
    await message.answer("Нажмите на нужную вам кнопку 🔀", reply_markup=news_back)


@dp.message_handler(text="Новости hi-tech 👤")
async def get_news(message: types.Message):
    """Выводит 5 последний записей новостей из базы"""
    # get_news_and_save_bd()
    # del_table()
    # create_table()
    # data = get_data_from_db()
    # for d in data:
    #     await message.answer(f'Новость 🗞:\n{d[0]}\nСсылка:\n{d[1]}', reply_markup=news_back)
    pass

@dp.message_handler(text="Свежие новости hi-tech 🗣")
async def get_fresh_news(message: types.Message):
    # await message.answer("Идет обработка... ⏰")
    # fresh_news = get_news_and_save_bd()
    # if len(fresh_news) == 0:
    #     await message.reply("Нету свежих новостей ⏰")
    # else:
    #     for f in fresh_news:
    #         await message.answer(f'Новость 🗞:\n{f["title"]}\n{f["link"]}')
    pass

# открытие клавиатуры переводов
@dp.message_handler(Command("get_translation"))
async def show_translate_menu(message: types.Message):
    """По команде get_translation открывает клавиатуру для выбора переводов"""
    await message.answer("Выберите варианты переводов 👅", reply_markup=translate_menu)


class Translation(StatesGroup):
    command1 = State()
    command2 = State()


# активация первого состояния Translation
@dp.message_handler(text="Перевод на русский (⌒_⌒;)", state=None)
async def state_activate_translation_command1(message: types.Message):
    await message.answer('🇬🇧 Введите текст для перевода на русский язык ⬇')
    # активируем состояние 1
    # await Translation.command1.set()


# выполняем команду первого состояния, переводим текст на русский язык
@dp.message_handler(state=Translation.command1)
async def get_russian_text_from_english(message: types.Message, state: FSMContext):
    # try:
    #     await message.answer(translator_ru(message.text))
    #     await state.finish()
    # except:
    #     await message.answer('Текст вводите на английском языке 🇬🇧')
    pass


# активация второго состояния Translation
@dp.message_handler(text="Перевод на английский (づ￣ ³￣)づ")
async def state_activate_translation_command2(message: types.Message):
    await message.answer('🇷🇺 Введите текст для перевода на ангийский язык ⬇')
    # await Translation.command2.set()


# выполняем команду второго состояния, переводим текст на английский язык
@dp.message_handler(state=Translation.command2)
async def get_english_text_from_russian(message: types.Message, state: FSMContext):
    # try:
    #     await message.answer(translator_en(message.text))
    #     await state.finish()
    # except:
    #     await message.answer('Текст вводите на русском языке 🇷🇺')
    pass

@dp.message_handler(text='Подурачиться 🤡')
async def show_reddit_menu(message: types.Message):
    """По команде get_memes открывает клавиатуру для выбора переводов"""
    await message.answer("Нажмите на кнопку", reply_markup=reddit_main)


@dp.message_handler(text="Вернуться в основное меню 🔙")
async def show_menu(message: types.Message):
    """Выбор из меню переводов для возврата в основное меню"""
    await message.answer("Вы вернулись в основное меню 🔙", reply_markup=menu)


@dp.message_handler(text="Подписка 🤖")
async def subscribers(message: types.Message):
    """Открывает меню подписки/отписки"""
    await message.answer(
        "Бот находится на бесплатном сервере heroku, могут быть перебои в работе, подпишитесь и вы при активации бота будете уведомлены 🔀",
        reply_markup=subscriber_menu)


@dp.message_handler(text="Подписаться 🔗")
async def subscribe(message: types.Message):
    # print(message.from_user.id)
    # name = message.from_user.full_name
    # user_id = message.from_user.id
    # text = add_subscriber(name=name, user_id=user_id)
    # await message.answer(text)
    pass


@dp.message_handler(text="Отписаться 🖇")
async def get_unsubscribe(message: types.Message):
    # text = unsubscribers(message.from_user.id)
    # await message.answer(text)
    pass