import requests

url2 = "https://kemerovo.e2e4online.ru/catalog/noutbuki-42/"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
# собираем куки
url1 = "https://kemerovo.e2e4online.ru/"
res1 = requests.get(url1, headers=headers, timeout=3)
cooc = res1.cookies
# получаем информацию с нашей страницы
res2 = requests.get(url2, headers=headers, cookies=cooc, timeout=3)
print(res2.text)


