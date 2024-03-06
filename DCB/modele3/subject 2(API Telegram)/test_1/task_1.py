import telebot
import config

#bot = telebot.TeleBot(config.token)

API_TOKEN = '<api_token>'#нужно получить свой токен и ввести его

#пример
#API_TOKEN = '6806370604:AAEZxzLW20JDQ8fPmNFGAS-bNb1bnFVpIZw'


bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=["text"])
def all_message(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == "__main__":
    #bot.infinity_polling()
    bot.polling(non_stop=True)


