from bs4 import BeautifulSoup
import requests

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
title = soup.find_all('a', class_="title")
description = soup.find_all('p', class_="description")
price = soup.find_all('h4', class_="pull-right price")
with open('laptops.csv', 'w', encoding='utf8') as file:
    i = 1
    for t, d, p in zip(title, description, price):
        file.write(f'{i}.{t["title"]}|{d.get_text()}|{p.get_text()}\n')
        i += 1



