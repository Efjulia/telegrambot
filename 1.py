import telebot;
import password
import datetime

bot = telebot.TeleBot(token=password.token)


flag = 0

@bot.message_handler(content_types=['text']) #слушаем бота

def get_text(message):
    global flag

    current_year = int(datetime.datetime.now().year)
    #print(current_year)
    if message.text == "/start": #проверям сообщение от пользователя
        flag = 0
        bot.send_message(message.from_user.id, "Здравствуй, мой дорогой друг! Представься...") #отвечаем пользователю
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Я умею ловко здороваться и вычислять год рождения, но все по-порядку...Набери /start")
    else:
        if flag == 0:
            name = message.text
            flag += 1
            bot.send_message(message.from_user.id, "Привет, " + name + '!\nСколько тебе лет? Напиши, пожалуйста цифрами') #отвечаем пользователю
        elif flag == 1:
            age = message.text
            if age.isdigit():
                bot.send_message(message.from_user.id, 
                                 "Замечательный возраст, ты родился в " 
                                 + str(current_year - int(age)) + ' году') #отвечаем пользователю
                bot.send_message(message.from_user.id, 
                                 "Мои функции исчерпаны...набери /start для того,чтобы начать сначала") #отвечаем пользователю
                flag += 1
            else:
                bot.send_message(message.from_user.id, "Кто-то у нас маленький бунтарь? Напиши возраст ЦИФРАМИ...") #отвечаем пользователю
        elif flag == 2:
            bot.send_message(message.from_user.id, 
                                 "/start - чтобы начать сначала \n /help - чтобы получить справку.")

bot.polling(none_stop=True, interval=0)# бот постоянно будет опрашивает сервер

