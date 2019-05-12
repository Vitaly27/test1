import telebot

bot = telebot.TeleBot("835209382:AAFeY1RmWlpq0l35z2W0ywgYnre1-GSX9AA")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling( none_stop = True)
