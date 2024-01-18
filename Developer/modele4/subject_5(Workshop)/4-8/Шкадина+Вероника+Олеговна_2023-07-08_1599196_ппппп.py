import requests
from bs4 import BeautifulSoup

url = "https://moscow.e2e4online.ru/catalog/noutbuki-42/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

models = soup.find_all('a', class_='block-offer-item__name')
description = soup.find_all('div', class_='block-offer-item__description lg-and-up')
prices = soup.find_all('div', class_='price-block__price _WAIT')

with open("e2e4.csv", "w", encoding='utf8') as file:
    for m, d, p in zip(models, description, prices):
        file.write(f'{m.get_text()}|{d.get_text()}|{p.get_text()}\n')