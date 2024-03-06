import requests
import time
"""
API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
BOT_TOKEN = '6508292789:AAEcmsG1EexOBrJ-HBfTk4sKvCkBTWJ6-4w'
ERROR_TEXT = 'Здесь должна была быть картинка с котиком'
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int
cat_link: str

while counter < MAX_COUNTER:
    print('Я жив = ', counter)

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()


    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1

"""

API_URL: str = 'https://api.telegram.org/bot'
API_CATS_URL: str = 'https://api.thecatapi.com/v1/images/search'
API_DOGS_URL: str = 'https://random.dog/woof.json'
API_FOXS_URL: str = 'https://randomfox.ca/floof/'
BOT_TOKEN: str = '6508292789:AAEcmsG1EexOBrJ-HBfTk4sKvCkBTWJ6-4w'
ERROR_TEXT: str = 'Здесь должна была быть картинка с грязным бесчувственным животным :('

offset: int = -2
counter: int = 0
response: requests.Response
link: str


while counter < 100:  # Инициализация цикла while для выполнения действий пока счетчик counter меньше 100
    print('attempt =', counter)  # Вывод значения счетчика попыток в консоль
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()  # Получение обновлений от Telegram API

    # Проверка наличия обновлений
    if updates['result']:
        # Обработка каждого результата обновлений
        for result in updates['result']:
            offset = result['update_id']  # Обновление значения переменной offset
            chat_id = result['message']['from']['id']  # Получение идентификатора чата пользователя

            # Проверка значения счетчика попыток
            if counter % 3 == 0:  # Если счетчик делится на 3 без остатка
                response = requests.get(API_DOGS_URL)  # Получение ответа от API для изображений с собаками
                link = response.json()['url']  # Получение URL изображения с собакой из ответа
            elif counter % 2 == 0:  # Если счетчик делится на 2 без остатка
                response = requests.get(API_FOXS_URL)  # Получение ответа от API для изображений с лисами
                link = response.json()['image']  # Получение URL изображения с лисой из ответа
            else:  # Во всех остальных случаях
                response = requests.get(API_CATS_URL)  # Получение ответа от API для изображений с котиками
                link = response.json()[0]['url']  # Получение URL изображения с котиком из ответа

            # Проверка успешного получения ответа
            if response.status_code == 200:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={link}')  # Отправка изображения пользователю
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')  # Отправка сообщения об ошибке

    time.sleep(1)  # Пауза на 1 секунду
    counter += 1  # Увеличение значения счетчика на 1


