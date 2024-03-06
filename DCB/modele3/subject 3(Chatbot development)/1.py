import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    keyboard.add(button_geo, button_phone)
    start_handler = f"<b>Привет {message.from_user.first_name}, что именно тебя интересует?</b>"
    bot.send_message(message.chat.id, start_handler, parse_mode='html', reply_markup=keyboard)
    keyboard = types.ReplyKeyboardRemove(selective=False)


bot.polling(none_stop=True)
