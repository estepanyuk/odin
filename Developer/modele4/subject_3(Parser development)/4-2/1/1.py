# import requests
# from bs4 import BeautifulSoup
# url = 'https://quotes.toscrape.com/'
#
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)


# import requests
# from bs4 import BeautifulSoup
#
# def get_stop(empty_url):
#     sess = requests.Session()
#     sess.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
#     response = sess.get(empty_url)
#     global stop
#     soup = BeautifulSoup(response.text, "html.parser")
#     for link in soup.find_all("a", class_="stop-link"):
#         stop.append(link.text)
#     return print(stop)
#
# url = 'https://grodno.btrans.by/ostanovka'
# stop = []
# get_stop(url)

from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.livelib.ru/book/1002978643-ohotnik-za-tenyu-donato-karrizi'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
sp = soup.find('div', class_='bc-menu__image-wrapper')
img_url = re.findall(r'(?:https\:)?//.*\.(?:jpeg)', str(sp))[0]
response = requests.get(img_url, headers=headers)
if response.status_code == 200:
    file_name = url.split('-', 1)[1]
    with open(file_name + '.jpeg', 'wb') as file:
        file.write(response.content)