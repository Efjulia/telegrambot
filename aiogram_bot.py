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



if __name__=='__main__':
    executor.o