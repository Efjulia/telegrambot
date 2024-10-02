from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import pprint
load_dotenv()

Token = os.getenv("TOKEN")
bot = Bot(token=Token)
dp = Dispatcher(bot)

matrix = [[], [], []]

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    global bt
    inline_keyboard = types.InlineKeyboardMarkup(row_width=3)
    for i in range(9):
        bt = types.InlineKeyboardButton(i, callback_data=str(i))
        inline_keyboard.insert(bt)
    await message.answer('Ваш ход:', reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda callback_query: callback_query)
async def bt_callback(callback_query: types.CallbackQuery):
    print(bt.text)

    await callback_query.answer(callback_query.data)

if __name__ == '__main__':
    executor.start_polling(dp)
