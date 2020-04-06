#--------------------- 28 將網頁內容扒回來並整理 ---------------------
import requests
resp = requests.get("https://udn.com/news/index")
resp.text
# 看是否為UTF-5或BIG-5
resp.encoding

# pip install bs4
from bs4 import BeautifulSoup

soup = BeautifulSoup(resp.text, 'html.parser')
# 不一定每個網頁都會支援lxml
soup = BeautifulSoup(resp.text, 'lxml')

table = soup.select(".udn-tab")
print(table)
len(table)
table[0]
table[0].text

#--------------------- 29 將扒回來的資料作分項及歸類處理 ---------------------
scope = soup.select(".udn-tab")
scope
# class的抓法 ".class-name", id的抓法 "#id-name"
scop2 = scope[0].select(".tab-link")
scop2
len(scop2)
scop2[0]
scop2[0].text
for line in scop2:
  print(line.text)
# 標籤的抓法 "span"
scop2[0].select("span")
sp = scop2[0].select("span")
sp[0].text
sp[1].text
#切字串
news = sp[1].text
news[0:6]
news[7:]
