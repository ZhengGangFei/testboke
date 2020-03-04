import requests
import xml
from bs4 import BeautifulSoup
import os
import json
import time
import pymysql

conn = pymysql.connect('47.98.50.245', 'zgf', 'ZGFroot1234@', 'web-boke')
cur = conn.cursor()


def insert_sql(title, link):
    try:
        sql = "INSERT INTO text(title, link) VALUES('%s', '%s');" % (title, link)
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print('错误')




url = "https://www.csdn.net/"

headers = {

    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.122 Safari/537.36 "
}

res = requests.get(url, headers=headers)
print(res.status_code)
# with open("text.html", 'wb')as f:
#     f.write(res.content)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'lxml')
div = soup.find_all('div', class_='title')
for d in div:
    text = d.a.text
    link = d.a['href']
    if text and link:
        text = text.replace('荐', '')
        text = text.replace('\n', '')
        text = text.replace('                                                        ', '')
        print(text, link)
        insert_sql(text, link)