from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import pprint
load_dotenv()

Token = os.getenv("TOKEN")
bot = Bot(token=Token)
dp = Dispatcher(bot)


@dp.callback_query_handler(lambda c: c.data == 'yes')
async def pres_yes_button(callback_query: types.CallbackQuery):
    #print(callback_query)
    await callback_query.message.answer(callback_query.from_user.first_name + ', ты - молодец!')


@dp.callback_query_handler(lambda c: c.data == 'no')
async def pres_yes_button(callback_query: types.CallbackQuery):
    #print(callback_query)
    await callback_query.message.answer(callback_query.from_user.first_name + ', ты - молодец!')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton('Да', callback_data='yes')
    key_no = types.InlineKeyboardButton('Нет', callback_data='no')
    inline_keyboard.add( key_yes, key_no)
    await message.answer('Познакомимся?', reply_markup=inline_keyboard)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text="""Данный телеграмм-бот работает для вас!
         Автор я! История моя!""")


@dp.message_handler()
async def send_message(message: types.Message):
    pprint.pprint(message)
    await message.reply(text=(message.chat.first_name + " " + message.chat.last_name))
    await message.reply(text=(message.from_user.full_name))
    await message.reply(text=message.text)

if __name__ == '__main__':
    executor.start_polling(dp)




