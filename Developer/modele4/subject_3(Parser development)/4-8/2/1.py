from bs4 import BeautifulSoup
import requests
import re

url = 'https://azku.ru/russkie-narodnie-skazki/kolobok.html'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
res1 = soup.find_all('div', class_="entry-content")
text = res1[0].get_text().split('Мне нравится')[0]
xd = re.sub(r'[-,.?!"—:]', ' ', text).lower().split()
result_dict = {word: xd.count(word) for word in xd if len(word) > 3}
max_values = sorted(result_dict.items(), key=lambda x:x[1], reverse=True)[:10]
for word, values in max_values:
    print(f'{word} - {values}')







