import requests
from bs4 import BeautifulSoup

HEADERS = {'Cookie': '_ym_uid=1603807505174420729; _ym_d=1645855624; _ga=GA1.2.1799029165.1645855628; __gads=ID=1ef682d215874c5f:T=1645855629:S=ALNI_Ma6jdSEeZkmOaXBEyKrewZYhzJiYQ; hl=ru; fl=ru; habr_web_home_feed=/all/; cto_bundle=58I4GF9YS3I4Q1JEYjQ3NUhkM281YUk1cFolMkZvR2k1QWtNV2VoUHJLSGtaUDlCZG5Pa2xBdGYySVJPUVpOYSUyRm9henNYdFA5OWhQRkc1VngwZSUyQiUyRmVJcWQ0YXhpVCUyQnFnVTA0U3lTQ0wlMkZFJTJCazlwNHFWMWd0aDRWJTJCS1RzTk5OcEdGQjVtQ1RISjklMkYxM2lMaU9MR2p3YTNHUyUyQlo5dyUzRCUzRA; _ym_isad=2; _gid=GA1.2.1017220013.1649494379; pmtimesig=[[1649498180961,0]]; _ym_visorc=w',
'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Cache-Control': 'max-age=0',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
'sec-ch-ua-mobile': '?0'
}

KEYWORDS = {'Дизайн', 'Фото', 'Web', 'Python'}

response = requests.get('https://habr.com/ru/all/',headers= HEADERS)
response.raise_for_status()
text = response.text

soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all('a', class_="tm-article-snippet__hubs-item-link")
    hubs = set([hub.find('span').text for hub in hubs])
    data = article.find('span', class_="tm-article-snippet__datetime-published")
    title = article.find ('a', class_="tm-article-snippet__title-link")
    span_title = title.find('span').text
    pre_url = article.find('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2')
    url = pre_url.find('a').get('href')
    if KEYWORDS & hubs:
        print(data.text)
        print(span_title)
        print (url)
        print ('\n')