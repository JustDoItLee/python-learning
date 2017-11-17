#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1', user='root', password='lizhi', database='springbootdb')
cursor = conn.cursor()
print(cursor.rowcount)
try:
    cursor.execute('select * from city')
    value = cursor.fetchall()
    print(value)
except Exception as e:
    print(e)
finally:
    if cursor:
        cursor.close()
    conn.close()
