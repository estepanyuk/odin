from bs4 import BeautifulSoup
import requests
import re

url = "https://ru.wikipedia.org/wiki/100_%D0%B8%D0%B7%D0%B2%D0%B5%D1%81%D1%82%D0%BD%D1%8B%D1%85_%D1%86%D0%B8%D1%82%D0%B0%D1%82_%D0%B8%D0%B7_%D0%B0%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D1%85_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%BE%D0%B2_%D0%B7%D0%B0_100_%D0%BB%D0%B5%D1%82_%D0%BF%D0%BE_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8_AFI"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res, 'html.parser')
table = soup.find("table", class_="wikitable")
header = table.find_all('th')
quotes = table.find_all('tr')
quotes_1995 = []
for i in range(1, len(quotes)):
    q = quotes[i].get_text()
    if int(q[-5:]) > 1995:
        quotes_1995.append(" ".join(q.split('\n\n')[1:]).replace('\n', ""))
for quote in quotes_1995:
    print(quote)

