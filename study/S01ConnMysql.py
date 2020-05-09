#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:EnzoLuo
import pymysql
conn = pymysql.connect('localhost','root','root','test')
cursor = conn.cursor()
query_alarm = 'select * from t_alarm'
cursor.execute(query_alarm)
dataList = cursor.fetchall()
for i in dataList:
    print(i)

