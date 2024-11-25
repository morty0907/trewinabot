import telebot

bot = telebot.TeleBot('7720181112:AAG7oJ-oviEPM68wnT07Jpc8qlsrPy8_QDk')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    print(message)
    bot.send_message(user_id,f'Привет, @{message.from_user.first_name}!')


@bot.message_handler(content_types=['text'])
def text(message):
    user_id = message.from_user.id
    if message.text.title() == 'Википедия':
        bot.send_message()
    bot.send_message(user_id, 'Давай поговорим')


bot.polling(non_stop=True)