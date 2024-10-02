from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv #сначала надо импортировать pip install python-dotenv
import os
import random
import sqlite3


load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token =TOKEN)
dp =Dispatcher(bot)
# fl = 0 - общее меню, fl = 1  - играем
fl = 0
name = ''
answer_list = ['камень', 'ножницы', 'бумага']
spisok_otvetov = {('камень', 'ножницы'): 'Камень бьет ножницы!',
                  ('камень', 'бумага'): 'Бумага кроет камень!',
                  ('ножницы', 'бумага'): 'Ножницы режут бумагу!'
}
            

def make_keyboard(n):
    global keyboard, keyboard_variant     
    global keyboard_answer
    match n:
        case 1:
            keyboard = types.InlineKeyboardMarkup() #клавиатура да и нет
            key_yes = types.InlineKeyboardButton(text='Да', callback_data='ДаПривет') #кнопка «Да»
            key_no= types.InlineKeyboardButton(text='Нет', callback_data='НетПривет') #кнопка «Нет»
            keyboard.add(key_yes)#добавляем кнопку в клавиатуру
            keyboard.add(key_no)
        case 2:
            keyboard_answer = types.InlineKeyboardMarkup() #клавиатура да и нет
            key_yes = types.InlineKeyboardButton(text='Да', callback_data='ДаИгра')#кнопка «Да»
            key_no= types.InlineKeyboardButton(text='Нет', callback_data='НетИгра') #кнопка «Нет»
            keyboard_answer.add(key_yes)#добавляем кнопку в клавиатуру
            keyboard_answer.add(key_no)
        case 3:
            keyboard_variant = types.InlineKeyboardMarkup() #клавиатура камень ножницы бумага
            key_stone= types.InlineKeyboardButton(text='Камень', callback_data='Камень') #кнопка камень
            key_scissors = types.InlineKeyboardButton(text='Ножницы', callback_data='Ножницы') #кнопка ножницы
            key_paper = types.InlineKeyboardButton(text='Бумага', callback_data='Бумага') #кнопка бумага
            keyboard_variant.add(key_stone)#добавляем кнопку в клавиатуру
            keyboard_variant.add(key_scissors)
            keyboard_variant.add(key_paper)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    make_keyboard(1)
    await message.answer("Привет! Познакомимся?", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'ДаПривет')
async def process_callback_button(callback_query: types.CallbackQuery): #название функции любое!
    global fl
    make_keyboard(2)
    #await callback_query.answer('Вы нажали кнопку да')
    await callback_query.message.answer('Приятно познакомиться, ' + callback_query.from_user.first_name)

    await callback_query.message.answer('Играем?', reply_markup=keyboard_answer)


@dp.callback_query_handler(lambda c: c.data == 'НетПривет')
async def process_callback_button(callback_query: types.CallbackQuery):
    await callback_query.answer("Вы нажали кнопку Нет")
    await callback_query.message.answer('Чтобы начать заново нажмите /start')


@dp.callback_query_handler(lambda c: c.data == 'ДаИгра')
async def process_callback_button(callback_query: types.CallbackQuery): #название функции любое!
    make_keyboard(3)
    await callback_query.message.answer('Твой выбор?', reply_markup=keyboard_variant)


@dp.callback_query_handler(lambda c: c.data == 'Бумага' or c.data == 'Ножницы' or c.data == 'Камень')
async def process_callback_button(callback_query: types.CallbackQuery): #название функции любое!
    global fl, answer_bot
    answer_user = callback_query.data.lower()
    answer_bot = get_answer()
    text_otvet = otvet(answer_user, answer_bot)
    text_long_otvet = get_long_otvet(answer_user, answer_bot)
    make_keyboard(3)
    await callback_query.message.answer(f'Ваш ответ "{answer_user}", а ответ бота "{answer_bot}". {text_long_otvet} {text_otvet}')
    await callback_query.message.answer('Твой выбор?', reply_markup=keyboard_variant)



def get_answer():
    answer_list_bot = ['камень', 'ножницы', 'бумага']
    random.shuffle(answer_list_bot)
    answer_bot = random.choice(answer_list_bot)
    return answer_bot

def get_long_otvet(a, b):
    for key, value in spisok_otvetov.items():
        if (a == key[0] and b == key[1]) or (a == key[1] and b == key[0] ):
            return value
    return ''

def otvet(an, bn):
    a = answer_list.index(an)
    b = answer_list.index(bn)
    if a == b:
        return "Ничья"
    elif b == (a + 1) % 3:
        return 'Вы выиграли'
    else:
        return "Вы проиграли"


if __name__=='__main__':
    executor.start_polling(dp)