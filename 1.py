import telebot;

bot = telebot.TeleBot(token='7976932364:AAFEqk0224G30XpGg8176rTSZd-Md5M7xD8')


global flag 

flag = True

@bot.message_handler(content_types=['text']) #слушаем бота

def get_text(message):
    global flag
    if message.text == "/start": #проверям сообщение от пользователя
        bot.send_message(message.from_user.id, "Здравствуй, мой дорогой друг! Представься...") #отвечаем пользователю
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "напиши: Привет")
    else:
        if flag:
            name = message.text
            flag = False
            bot.send_message(message.from_user.id, "Привет," + name + '\n Сколько тебе лет') #отвечаем пользователю
            
        else:
            age = message.text
            bot.send_message(message.from_user.id, "Твой возраст!" + age) #отвечаем пользователю
        
bot.polling(none_stop=True, interval=0)# бот постоянно будет опрашивает сервер

