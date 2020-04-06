import requests
from bs4 import BeautifulSoup as bs
resp = requests.get("https://goodinfo.tw/StockInfo/index.asp")
resp.text
soup = bs(resp.text)
soup.select("#solid_1_padding_3_2_tbl")