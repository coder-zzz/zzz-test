from bs4 import BeautifulSoup
from lxml import html
import xml
import requests

url = "https://movie.douban.com/chart"
f = requests.get(url) #get该网页获取html内容
soup = BeautifulSoup(f.content, "lxml")
#lxml解析器解析网页内容
for k in soup.find_all('div', class_ = "p12"):
	a = k.find_all('span')
	print(a[0].string)
