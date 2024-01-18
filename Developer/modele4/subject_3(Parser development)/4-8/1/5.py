import requests
from bs4 import BeautifulSoup

url = 'https://www.oreilly.com/radar/'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('h2', class_="post-title")
for post in quotes:
    print(post.get_text())
