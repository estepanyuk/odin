# задача 1
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.kinopoisk.ru/lists/movies/top250/?page=1'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())


import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

url = 'https://www.kinopoisk.ru/lists/movies/top250/?page=1'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())


