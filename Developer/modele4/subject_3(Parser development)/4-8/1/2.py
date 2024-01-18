# задача 2
import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('span', class_='text')
print(quotes)