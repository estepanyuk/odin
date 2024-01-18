from bs4 import BeautifulSoup
import requests

url = 'https://www.oreilly.com/radar/'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
xd = soup.find_all('h2', class_="post-title")
for post in xd:
    print(post.get_text())



