import requests
import xml
from bs4 import BeautifulSoup
import os
import json
import time
import pymysql

conn = pymysql.connect('47.98.50.245', 'zgf', 'ZGFroot1234@', 'web-boke')
cur = conn.cursor()


def insert_sql(title, url, datatime):
    try:
        sql = "INSERT INTO news1(title, url, datatime) VALUES('%s', '%s', '%s');" % (title, url, datatime)
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print('错误')


url = "https://www.ithome.com/"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}

res = requests.get(url, headers=headers)

# with open('news.html', 'wb')as f:
#     f.write(res.content)
# print('ok')
# print(res.encoding)
res.encoding = res.encoding
res.encoding = 'utf-8'
html = res.text
soup = BeautifulSoup(html, 'lxml')
ret = soup.find_all('li', class_='new')
for i in ret:
    title, url = i.a.text, i.a['href']
    try:
        localtime = time.strftime("%Y-%m-%d %H:%M:%S")
        print(localtime)
        insert_sql(title, url, localtime)
        print(title, url)
    except Exception as e:
        print('错误！', e)
