import requests
from bs4 import BeautifulSoup


url = 'https://ejje.weblio.jp/content/object to'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
a = soup.select('span.phoneticEjjeDesc')[-1].string
print(a)
