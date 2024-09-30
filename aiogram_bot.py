from aiogram import Bot, Dispatcher, types, executor

from dotenv import load_dotenv #сначала надо импортировать pip install python-dotenv
import os
import random


load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token =TOKEN)
dp =Dispatcher(bot)
fl = 0
name = ''

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton('Да', callback_data='key_yes')
    key_no = types.InlineKeyboardButton('Нет', callback_data='key_no')
    inline_keyboard.add(key_yes)
    inline_keyboard.add(key_no)
    await message.answer("Привет! Познакомимся?", reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda c: c.data == 'key_yes')
async def process_callback_button(callback_query: types.CallbackQuery):
    global fl
    await callback_query.answer('Вы нажали кнопку да')
    fl = 1
    await text_message(callback_query.message)


@dp.callback_query_handler(lambda c: c.data == 'key_no')
async def process_callback_button(callback_query: types.CallbackQuery):
    await callback_query.answer("Вы нажали кнопку Нет")
    await callback_query.message.answer('Чтобы начать заново нажмите /start')


@dp.message_handler()
async def text_message(message: types.Message):
    global fl
    global name
    match fl:
        case 1:
            await message.answer('Как тебя зовут?')
            fl = 2
        case 2:
            name = message.text
            await message.answer(f'{name}, сколько тебе лет?')
            fl = 3
        case 3:
            try:
                age = int(message.text)
                await message.answer(f'{name}, ты родился в {2024 - age} году')
                fl = 1
            except Exception:
                await message.answer(f'{name}, введи число')
                


if __name__=='__main__':
    executor.start_polling(dp)