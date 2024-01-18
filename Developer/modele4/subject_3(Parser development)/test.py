# Импортируем модуль Requests, чтобы собрать данные с веб-страницы:
# import requests
# # # Импортируйте Beautiful Soup
# from bs4 import BeautifulSoup
#
# # Присваиваем URL-адрес тестовой страницы (в данном случае это mockturtle.html) переменной url.
# url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'
#
# # Затем можно присвоить результат запроса этой страницы переменной page с помощью метода request.get().
# # Передаем URL-адрес страницы, который был присвоен переменной url, этому методу.
# page = requests.get(url)
#
# soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())
# print(soup.find_all(id='third'))


# import requests
# from bs4 import BeautifulSoup
# import csv
# import time
# # import urllib
# # import fake_useragent
#
# HEADERS = {
#     'Host': 'mail.ru',
#     'Pragma': 'no-cache',
#     'Referer': 'https://mail.ru/',
#     'Sec-Ch-Ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114',
#     'Sec-Ch-Ua-Mobile': '?0',
#     'Sec-Ch-Ua-Platform': 'macOS',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
# }
#
# data ={
#     'news': 'sport',
#     'json': '1',
# }
#
# URL = 'https://mail.ru/?news=sport&json=1&build=bd7cb39&cloudWidgetUpdateEnabled=1'
#
# def get_html(URL, params=data):
#     r = requests.get(URL, headers=HEADERS, params=params)
#     return r
#
# page = requests.get(URL)
# html = get_html(URL, params={'PAGEN_1': page})
# soup = BeautifulSoup(html, 'html.parser')
# print(soup)


#
# def get_pages_count(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     paginationTo = soup.find('div', class_='nums')
#     if paginationTo:
#         paginationTo = soup.find('div', class_='nums')
#         pagination = paginationTo.find_all('a')
#         return int(pagination[-1].get_text())
#     else:
#         return 1
#
#
# def get_content(html):
#     soup = BeautifulSoup(html, 'html.parser')
#
#     items = soup.find_all('a')
#
#     catalog = []
#     for item in items:
#         item = str(item)
#         a = item.find("svelte-1kcqj27")
#         if a != -1:
#             continue
#         print(item)
#
#         catalog.append({
#
#         })
#     return catalog
#
#
# def save_file(items, path):
#     with open(path, 'w', encoding='utf8', newline='') as file:
#         writer = csv.writer(file, delimiter=',')
#         writer.writerow([])
#         for item in items:
#             writer.writerow([])
#
#
# def parse():
#     for URL in ['https://mail.ru/?news=sport&json=1&build=bd7cb39&cloudWidgetUpdateEnabled=1',
#     ]:
#
#         html = get_html(URL)
#         if html.status_code == 200:
#             catalog = []
#             pages_count = get_pages_count(html.text)
#             for page in range(1, pages_count + 1):
#                 print(f'Парсинг страницы {page} {pages_count} {URL}...')
#                 html = get_html(URL, params={'PAGEN_1': page})
#                 catalog.extend(get_content(html.text))
#                 time.sleep(1)
#             FILE = 'parseResult' + '.csv'
#             save_file(catalog, FILE)
#
#             print(f'Получено {len(catalog)} товаров')
#         else:
#             print('Error')
#
#
# parse()

#задача 1
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup)

# задача 2
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')

print(quotes)

# задача 3
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
authors = soup.find_all('small', class_='author')

for quote in authors:
    print(quote.text)


# задача 4
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print('--' + authors[i].text)
    tagsforquote = tags[i].find_all('a', class_='tag')
    for tagforquote in tagsforquote:
        print(tagforquote.text)
    print('\n')