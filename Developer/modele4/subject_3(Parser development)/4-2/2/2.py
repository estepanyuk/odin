from bs4 import BeautifulSoup
import requests
import re

url = 'https://azku.ru/russkie-narodnie-skazki/kolobok.html'
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36'}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
res = soup.find_all('div', class_="entry-content")
text = res[0].get_text().split('Мне нравится')[0]
sp = re.sub(r'[-,.?!":—]', ' ', text).lower().split()
result_dict = {world: sp.count(world) for world in sp if len(world)>3}
max_value = sorted(result_dict.items(), key=lambda x:x[1],reverse=True)[:10]
for world, number in max_value:
    print(f'{world} - {number}')

