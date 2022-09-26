import requests
from bs4 import BeautifulSoup

url = 'https://habr.com'
headers = {
'authority': 'www.google.com',
'method' : 'GET',
'path' : '/',
'scheme' : 'https',
'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding' : 'gzip, deflate, br',
'accept-language' : 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
'cache-control' : 'max-age=0',
'sec-fetch-dest' : 'document',
'sec-fetch-mode' : 'navigate',
'sec-fetch-site' : 'same-origin',
'sec-fetch-user' : '?1',
'upgrade-insecure-requests' : '1',
'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}

KEYWORDS = ['фото', 'дизайн', 'web', 'python']

response = requests.get(url, headers=headers)
response.raise_for_status()
text = response.text
soup = BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')


for article in articles:
    title = article.h2.string
    paragraphs = article.find_all('p')
    hubs = article.find_all(class_='tm-article-snippet__title tm-article-snippet__title_h2')
    date = article.find(class_='tm-article-snippet__datetime-published')
    paragraphs = set(paragraph.text.strip() for paragraph in paragraphs)
    hubs = set(hub.text.strip() for hub in hubs)
    href = url + article.h2.a['href']


    if None in (title, paragraphs, hubs, date, href):
        continue
    keywords_ = set(KEYWORDS)


    preview_info = str(title.text.lower() + str(paragraphs).lower() + str(hubs).lower()).split()

    for keyword in keywords_:
        if keyword in preview_info:

            print(f' Когда создана {date.text} наименование статьи "{title.text}" ссылка на статью: {href}')