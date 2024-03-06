import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def PodpishisNaTg(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_geo = types.KeyboardButton(text='Отправить местоположение', request_location=True)
    button_phone = types.KeyboardButton(text='Отправить контакт', request_contact=True)
    markup.add(button_geo, button_phone)
    start_handler = f'<code>Привет {message.from_user.first_name}, что тебя интересует</code>'
    bot.send_message(message.chat.id, start_handler, reply_markup=markup, parse_mode='html')


if __name__ == '__main__':
    bot.polling(none_stop=True)