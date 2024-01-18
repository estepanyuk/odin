import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
selection = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

for i in range(0, len(selection)):
    print(selection[i].text)
    print('--' + authors[i].text)
    a = tags[i].find_all('a', class_='tag')
    for c in a:
        print(c.text)
    print('\n')


from bs4 import BeautifulSoup
import requests
import lxml

url = "https://quotes.toscrape.com/"
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
need_class = soup.find_all("div", class_="quote")


for i in need_class:

    author_three = i.find("small", class_= "author")
    CITATI = i.find("span", class_= "text") # эту строчку я добавил
    CCILKA = "https://quotes.toscrape.com/" + i.find("a").get("href") # ну и эту
    tags = i.find("div", class_="tags").find_all("a", class_="tag")
    print(f"The greatest ||{author_three.text}|| said \n {CITATI.text} \n Переведено и озвучено {CCILKA}")

    for j in tags:
        url_tag = "https://quotes.toscrape.com/" + j.get("href")
        tag_name = j.text
        print("TAG:", url_tag, "---", tag_name)
    print()
