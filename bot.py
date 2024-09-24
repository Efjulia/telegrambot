from telebot import types, TeleBot
from dotenv import load_dotenv #сначала надо импортировать pip install python-dotenv
import os
import random


load_dotenv()
bot = TeleBot(os.getenv('TOKEN'))
name = ''
answer_user = ''
answer_bot = ""
answer_list = ['камень', 'ножницы', 'бумага']


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
            keyboard_variant = types.InlineKeyboardMarkup() #клавиатура да и нет
            key_stone= types.InlineKeyboardButton(text='Камень', callback_data='Камень') #кнопка «Да»
            key_scissors = types.InlineKeyboardButton(text='Ножницы', callback_data='Ножницы') #кнопка «Нет»
            key_paper = types.InlineKeyboardButton(text='Бумага', callback_data='Бумага') #кнопка «Нет»
            keyboard_variant.add(key_stone)#добавляем кнопку в клавиатуру
            keyboard_variant.add(key_scissors)
            keyboard_variant.add(key_paper)




@bot.callback_query_handler(func=lambda call: True)
def handler_call(call):
    global age, keyboard, keyboard_variant, answer_bot, answer_user
    match call.data:
        case "ДаПривет": #call.data это callback_data, которую мы указали при объявлении кнопки
            bot.send_message(call.message.chat.id, 'Начнем, как тебя зовут?')
            age = -1
            bot.register_next_step_handler(call.message, get_name)        
        case "НетПривет":
            bot.send_message(call.message.chat.id, 'Очень жаль! Если захочешь начать общение заново нажми на /start')
        case "ДаИгра": #call.data это callback_data, которую мы указали при объявлении кнопки
            bot.send_message(call.message.chat.id, 'Для продолжения нажми любую клавишу....')
            bot.register_next_step_handler(call.message, get_answer)
        case "НетИгра":
            bot.send_message(call.message.chat.id, 'Очень жаль! Если захочешь начать общение заново нажми на /start')
        case "Камень":
            answer_user = call.data.lower()
            text_otvet = otvet(answer_user, answer_bot)
            bot.send_message(call.message.chat.id, f'Ваш ответ {answer_user}, а ответ бота {answer_bot}. {text_otvet} Для продолжения нажми любую клавишу...')
            bot.register_next_step_handler(call.message, get_answer)  
        case "Ножницы":
            answer_user = call.data.lower()
            text_otvet = otvet(answer_user, answer_bot)
            bot.send_message(call.message.chat.id, f'Ваш ответ {answer_user}, а ответ бота {answer_bot}. {text_otvet} Для продолжения нажми любую клавишу...')
            bot.register_next_step_handler(call.message, get_answer)  
        case "Бумага":
            answer_user = call.data.lower()
            text_otvet = otvet(answer_user, answer_bot)
            bot.send_message(call.message.chat.id, f'Ваш ответ {answer_user}, а ответ бота {answer_bot}. {text_otvet} Для продолжения нажми любую клавишу....')
            bot.register_next_step_handler(call.message, get_answer)  

        
     
@bot.message_handler(commands=['start'])
def start(message):
    make_keyboard(1)
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}! познакомимся?', reply_markup=keyboard)

@bot.message_handler(commands=['stop'])
def end(message):
    bot.send_message(message.from_user.id, "/start - чтобы начать сначала ")
            
def get_name(message):
    global name
    name = message.text 
    make_keyboard(2)
    bot.send_message(message.from_user.id, f'{name}, сыграем в камень ножницы бумага?', reply_markup=keyboard_answer)
          

def get_answer(message):
    global answer_bot
    make_keyboard(3)
    answer_list_bot = ['камень', 'ножницы', 'бумага']
    random.shuffle(answer_list_bot)
    answer_bot = random.choice(answer_list_bot)
    bot.send_message(message.from_user.id, f'{name}, выбирай вариант? Для остановки выбери /stop', reply_markup=keyboard_variant)
    print(answer_bot)


def otvet(an, bn):
    a = answer_list.index(an)
    b = answer_list.index(bn)
    if a == b:
        return "Ничья"
    elif b == (a + 1) % 3:
        return 'Вы выиграли'
    else:
        return "Вы проиграли"
    

bot.polling(none_stop=True, interval=0)