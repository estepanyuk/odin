#задача 1
import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.token)

#1. Простая клавиатура:
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton(text='Кнопка 1')
    itembtn2 = types.KeyboardButton(text='Кнопка 2')
    itembtn3 = types.KeyboardButton(text='Кнопка 3')
    itembtn4 = types.KeyboardButton(text='Кнопка 4')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    #markup.add( itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Выберите одну из кнопок:", reply_markup=markup)

#2. Клавиатура с вложенными кнопками:
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    itembtn1 = types.InlineKeyboardButton('Раздел 1', callback_data='section1')
    itembtn2 = types.InlineKeyboardButton('Раздел 2', callback_data='section2')
    itembtn3 = types.InlineKeyboardButton('Раздел 3', callback_data='section3')
    markup.add(itembtn1, itembtn2, itembtn3)
    sub_markup = types.InlineKeyboardMarkup(row_width=2)
    sub_itembtn1 = types.InlineKeyboardButton('Подраздел 1', callback_data='subsection1')
    sub_itembtn2 = types.InlineKeyboardButton('Подраздел 2', callback_data='subsection2')
    sub_itembtn3 = types.InlineKeyboardButton('Подраздел 3', callback_data='subsection3')
    sub_markup.add(sub_itembtn1, sub_itembtn2, sub_itembtn3)
    bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)
    bot.send_message(message.chat.id, "Выберите подраздел:", reply_markup=sub_markup)

#3. Варианты ответов с 2-мя кнопками:
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    itembtn1 = types.InlineKeyboardButton('Да', callback_data='yes')
    itembtn2 = types.InlineKeyboardButton('Нет', callback_data='no')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Вы уверены?", reply_markup=markup)



bot.polling(none_stop=True)












