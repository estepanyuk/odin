from bs4 import BeautifulSoup
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'}
url = 'https://moscow.e2e4online.ru/catalog/noutbuki-42/?sort=PRICE_DESC'
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
models = soup.find_all('a', class_='block-offer-item__name')
description = soup.find_all('div', class_='block-offer-item__description lg-and-up')
prices = soup.find_all('div', class_='price-block__price _WAIT')
data = zip(models, description, prices)
data = list(data)[:22]



with open('laptops.csv', 'w', encoding='utf-8') as file:
    file.write(f'Модель;Описание;Цена\n')
    for laptop in data:
        model = laptop[0].get_text()
        description = laptop[1].get_text()
        price = laptop[2].get_text().replace('\xa0', ' ')

        file.write(f"{model};{description};{price}\n")