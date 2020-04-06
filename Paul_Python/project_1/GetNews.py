import requests
from bs4 import BeautifulSoup

def get_hotline_udnews(url):
  resp = requests.get(url)

  if resp.status_code == 200:
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    scope1 = soup.select(".udn-tab")
    # 選到全部class為tab-link
    # scope2 = scope1[0].select(".tab-link")

    # 選到data-id為real，且class為tab-link
    scope2 = scope1[0].find("div", {"data-id" : "real"}).select(".tab-link")

    hot_lines = []
    for line in scope2:
      hot_lines.append(line.get_text())

    return hot_lines


if __name__ == '__main__':
  udnews_lines = get_hotline_udnews("https://udn.com/news/index")
  # 簡易做法
  i = 0
  while i < len(udnews_lines):
    print(udnews_lines[i])
    i += 1

  # 使用字典的作法
  j = 0
  udnews_dicts = {}
  while j < len(udnews_lines):
    udnews_dicts['time'] = udnews_lines[j][1:6]
    udnews_dicts['title'] = udnews_lines[j][7:]
    print("Time[{}]: {}\n".format(udnews_dicts['time'], udnews_dicts['title']))
    j += 1




