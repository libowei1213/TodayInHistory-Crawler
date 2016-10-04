# -*- coding: utf_8 -*-

import pymysql

def savedb(data):
    conn = pymysql.connect(host="127.0.0.1", user="root", password="libowei", db="today", charset="utf8")
    print(conn)
    cur = conn.cursor()
    cur.execute("insert into event values(null,%s,%s,%s,%s)" , data)
    cur.connection.commit()
    cur.close()
    conn.close()



