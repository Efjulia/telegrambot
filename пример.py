
import telebot
from telebot import types, TeleBot
from dotenv import load_dotenv
import os

load_dotenv()


bot = telebot.TeleBot(os.getenv("TOKEN"))

name = ''
age = -1
fl_ask = 0

@bot.callback_query_handler(func=lambda call: True)
def handler_call(call):
    global age
    match call.data:
        case "да": #call.data это callback_data, которую мы указали при объявлении кнопки
            bot.send_message(call.message.chat.id, 'Начнем, как тебя зовут?')
            age = -1
            bot.register_next_step_handler(call.message, get_name)        
        case "нет":
            bot.send_message(call.message.chat.id, 'Очень жаль! Если захочешь начать общение заново нажми на /start')
        case 'не определился':
            bot.send_message(call.message.chat.id, 'Поговорим о жизни тогда?')
            bot.register_next_step_handler(call.message, get_name)        




        
     
@bot.message_handler(commands=['start'])
def start(message): 
    keyboard = types.InlineKeyboardMarkup() #клавиатура да и нет
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='да') #кнопка «Да»
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='нет') #кнопка «Нет»
    keyboard.add(key_yes)#добавляем кнопку в клавиатуру
    keyboard.add(key_no)
    #keyboard.add(*[types.KeyboardButton(btn_name) for btn_name in ['да', 'нет']])
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}! познакомися?', reply_markup=keyboard)
            
def get_name(message):
    global name 
    name = message.text 
    bot.send_message(message.from_user.id, f'{name}, сколько тебе лет?')   
    bot.register_next_step_handler(message, get_age) 

def get_age(message):
    global age
    while age == -1:
        if message.text.isdigit():          
            age = int(message.text) 
            bot.send_message(message.from_user.id, f'тебя зовут {name}, родился в {2024 - age}')
            bot.register_next_step_handler(message, start)
        else:
            bot.send_message(message.from_user.id, 'введите число')             



bot.polling(none_stop=True, interval=0)