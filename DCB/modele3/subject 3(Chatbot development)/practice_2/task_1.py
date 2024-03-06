import telebot
import config

bot = telebot.TeleBot(config.token)

users = {}

#1.Пусть при отправке команды /start, наш бот будет приветствовать пользователя.
@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_save = telebot.types.InlineKeyboardButton(text="Написать в поддержку")
    keyboard.add(button_save)
    bot.send_message(chat_id,'Добро пожаловать в бота сбора обратной связи',reply_markup=keyboard)

#имя
@bot.message_handler(func=lambda message: message.text == 'Написать в поддержку')
def write_to_support(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Введите своё имя')
    users[chat_id] = {}
    bot.register_next_step_handler(message, save_username)


def save_username(message):
    chat_id = message.chat.id
    name = message.text
    users[chat_id]['name'] = name
    bot.send_message(chat_id, f'Отлично, {name}. Теперь напиши свою фамилию')
    bot.register_next_step_handler(message, save_surname)

def save_surname(message):
    chat_id = message.chat.id
    surname = message.text
    users[chat_id]['surname'] = surname
    bot.send_message(chat_id, f'Ваши данные успешно сохранены')
    #bot.register_next_step_handler(message, save_username)


#@bot.callback_query_handler(func=lambda, call: call.data == 'who_i')
@bot.message_handler(commands=['who_i'])
def who_i(message):
    chat_id = message.chat.id
    name = users[chat_id]['name']
    surname = users[chat_id]['surname']
    bot.send_message(chat_id, f'Вы: {name} {surname}')


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()