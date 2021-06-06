import telebot


bot = telebot.TeleBot('1893650795:AAGzBJGW2gszlLUvcUEbIUD0UxHw8DgjELY')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Hey, nice to meet you, {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def repeat_message(message):
    repeat = message.text
    bot.send_message(message.from_user.id, repeat)


bot.polling(none_stop=True, interval=0)