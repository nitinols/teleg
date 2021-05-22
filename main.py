import telebot
import sqlite3

bot = telebot.TeleBot('1251334241:AAEG_TGZUx_h2NXVN7OBFx5gTjnGVREgtzY')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте, Введите логин и пароль')
    bot.send_message(message.chat.id, 'Пимер: 12345 12345')


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Введи логин и пароль')
    bot.send_message(message.chat.id, 'Пимер: 12345 12345')


@bot.message_handler(content_types=['text'])
def collect_info(message):
    if len(message.text.split()) == 2:
        con = sqlite3.connect("pacient .db")
        cur = con.cursor()
        que = "SELECT * FROM pacient WHERE log = " + message.text.split()[0]
        result = cur.execute(que).fetchall()
        if result != []:
            print(result)
            if result[0][2] == message.text.split()[1]:
                bot.send_message(message.chat.id, result[0][3])
                photo = open( f'photo/{result[0][4]}', 'rb')
                bot.send_photo(message.chat.id, photo)
                #bot.register_next_step_handler(message, info)
            else:
                bot.send_message(message.chat.id, 'Неправильный логин или пароль')
        else:
            bot.send_message(message.chat.id, 'Неправильный логин или пароль')
    else:
        bot.send_message(message.chat.id, 'Проверьте правильность ввода')

def info(message):
        if message.text == 'Информация':
            bot.send_message(message.chat.id, 'Описание проекта')
        elif message.text == 'Статистика':
            bot.send_message(message.chat.id, 'Статистика проекта')
        else:
            bot.send_message(message.chat.id, 'Я не знаю спроси что-нибудь другое')




bot.polling()