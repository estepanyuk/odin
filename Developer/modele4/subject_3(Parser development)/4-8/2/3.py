from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(cache_valid_range=10).install()))
url = 'https://webscraper.io/test-sites/e-commerce/scroll/computers/tablets'
driver.get(url)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
models = soup.find_all('a', class_="title")
prices = soup.find_all('h4', class_="pull-right price")
for model, price in zip(models, prices):
    m = model.get_text()
    p = price.get_text()
    print(f'Планшет {m}, цена - {p}')