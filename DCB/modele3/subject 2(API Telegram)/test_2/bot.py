# задача
import config
import telebot
import requests

bot = telebot.TeleBot(config.token)
API_key = config.API_key

#storage = {}
#def init_storage(user_id):
#  storage[user_id] = dict(first_number=None, second_number=None)
# init_storage(message.from_user.id)

@bot.message_handler(commands=["start"])
def start(message):  # Название функции не играет никакой роли
    bot.send_message(message.chat.id, "Привет, рад тебя видеть! Напиши название города")


@bot.message_handler(content_types=['text'])
def get_weather(message):
    bot.register_next_step_handler(message, get_weather)
    city_name = message.text.strip().lower()
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric')

    data = response.json()
    # получаем значение погоды
    cur_temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    weather_description = data["weather"][0]["main"]
    weather_icon = data["weather"][0]["icon"]
    """
    code_to_smile = {
        "Clear": "Ясно",
        "Clouds": "Облачно",
        "Rain": "Дождь",
        "Drizzle": "Дождь",
        "Thunderstorm": "Гроза",
        "Snow": "Снег ", 
        "Mist": "Туман"
    }
    """


    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    if weather_description in code_to_smile:
        global wd
        wd = code_to_smile[weather_description]
    else:
        # если эмодзи для погоды нет, выводим другое сообщение
        wd = "Посмотри в окно, я не понимаю, что там за погода..."


    if "Новосибирск" in message.text:
        bot.send_message(message.chat.id, 'Напиши другое название города')
    else:
        bot.reply_to(message, f'Сейчас погода: {round(cur_temp)} °C,\nОщущается как {round(feels_like)}°C, {wd}')


    #bot.reply_to(message, f'Сейчас погода: {round(cur_temp)} °C,\nОщущается как {round(feels_like)}°C, {wd}')
    #bot.send_photo(message.chat.id, f'https://openweathermap.org/img/wn/{weather_icon}@2x.png')

if __name__ == '__main__':
    bot.polling(none_stop=True)

