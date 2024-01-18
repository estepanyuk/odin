from bs4 import BeautifulSoup
import requests

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
models = soup.find_all('a', class_="title")
description = soup.find_all('p', class_="description")
price = soup.find_all('h4', class_="pull-right price")
with open('laptops.csv', 'w', encoding='utf8') as file:
    for m, d, p in zip(models, description, price):
        file.write(f"{m.get_text()}| {d.get_text()}| {p.get_text()}\n")