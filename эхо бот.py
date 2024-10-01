from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()

Token = os.getenv("TOKEN")
bot = Bot(token=Token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('привет!')

@dp.message_handler()
async def send_message(message: types.Message):
    await message.answer(text='ты что-то написал')

    

if __name__ == '__main__':
    executor.start_polling(dp)




