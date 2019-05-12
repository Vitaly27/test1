import telebot

bot = telebot.TeleBot("835209382:AAFeY1RmWlpq0l35z2W0ywgYnre1-GSX9AA")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, "Здравствуйте, на данном этапе я пока не понимаю Вас! Но всё изменится!")

bot.polling( none_stop = True)
