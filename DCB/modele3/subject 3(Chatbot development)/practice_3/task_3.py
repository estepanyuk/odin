import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет,{0.first_name}!".format(message.from_user, bot.get_me()))

@bot.message_handler(content_types=["text"])
def first(message):
    bot.send_message(message.chat.id, "Текст.")

@bot.message_handler(content_types=["audio"])
def second(message):
    bot.send_message(message.chat.id, "Аудио.")

@bot.message_handler(content_types=["video"])
def third(message):
    bot.send_message(message.chat.id, "Видео.")

@bot.message_handler(content_types=["document"])
def fourth(message):
    bot.send_message(message.chat.id, "Документ.")

bot.polling(none_stop=True)