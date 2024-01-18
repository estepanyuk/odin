from bs4 import BeautifulSoup
import requests

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
models = soup.find_all('a', class_="title")
description = soup.find_all('p', class_="description")
price = soup.find_all('h4', class_="pull-right price")
with open('Laptops1.csv', 'w', encoding='utf8') as file:
    file.write(f'Модель; Конфигурация; Цена;\n')
    for m, d, p in zip(models, description, price):
        file.write(f"{m['title']};{d.get_text().strip()};{p.get_text()}\n")
