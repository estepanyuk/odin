import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
selection = soup.find_all('span', class_='text')
for i in selection:
    print(i.text)

print(selection)
