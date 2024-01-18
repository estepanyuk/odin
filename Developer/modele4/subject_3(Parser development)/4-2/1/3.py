import requests
from bs4 import BeautifulSoup

url = 'https://bbf.ru/quotes/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
authors = soup.find_all('small', class_='sentence__body')

for i in authors:
    print(i.text)