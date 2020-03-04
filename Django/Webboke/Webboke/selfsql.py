import pymysql
import redis


class SelfSql:
    def __init__(self):
        self.conn = pymysql.connect(host='47.98.50.245',
                                    user='zgf',
                                    password='ZGFroot1234@',
                                    database='web-boke')
        self.cursor = self.conn.cursor()
        self.result = ''

    def sel_sql_login(self, uname):
        sql = "SELECT `password` FROM UserLogin WHERE `username` = '%s'" % (uname)
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        print("this is selfsql-result:", self.result)
        return self.result

    def sel_sql_news(self):
        sql = "SELECT * FROM news1;"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        return self.result

    def sel_sql_text(self):
        sql = "SELECT * FROM text;"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        return self.result
