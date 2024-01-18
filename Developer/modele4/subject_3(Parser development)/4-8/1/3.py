# задача 3
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
authors = soup.find_all('small', class_='author')

for i in authors:
    print(i.text)