from  bs4  import BeautifulSoup
import requests

url = "https://www.livelib.ru/genre/%D0%A2%D1%80%D0%B8%D0%BB%D0%BB%D0%B5%D1%80%D1%8B/top"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
res  = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')
title = soup.find_all('a', class_="brow-book-name with-cycle")
author = soup.find_all('a', class_="brow-book-author")
rating = soup.find_all('span', class_="rating-value stars-color-orange")
# i = 1
# for t, a, r in zip(title, author, rating):
#     print(f'"{t.get_text()}" {a.get_text()} - {r.get_text()}')
#     i += 1

with open('list.txt', 'w', encoding='utf8') as file:
    file.write(f'Название; Автор; Рейтинг;\n')
    i = 1
    for t, a, r in zip(title, author, rating):
        file.write(f"{t['title']} {a.get_text()}-{r.get_text()}\n")
        i += 1