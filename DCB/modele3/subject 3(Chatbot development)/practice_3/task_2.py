import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from config import *
import random

bot = telebot.TeleBot(TOKEN)

compliments = ['Выглядишь лучшее всех!', 'Сегодня будет замечательный день!', 'Ты обязательно всё сможешь!', 'Я не встречал людей добрее тебя!', 'С тобой приятно проводить время!']

@bot.message_handler(commands=["start"])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = KeyboardButton("🚀Старт")
    btn2 = KeyboardButton("🥰Комплимент")

    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name} \nВоспользуйся кнопочками:", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def btn(message):
    if message.text == "🥰Комплимент":
        compliment = random.choice(compliments)
        bot.send_message(message.chat.id, f"{compliment}")
    else:
        start(message)



bot.polling(none_stop=True)