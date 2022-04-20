#!/usr/bin/env python3
# -*- coding: utf-8 -*-

server = 'your_server_name'

import pymysql.cursors
from bottle import route, run

@route("/")
def index():
    results = 'connection error'
    connection = pymysql.connect(host='mysql',
                             user='testuser',
                             password='testpasswd20220421',
                             database='testdb',
                             cursorclass=pymysql.cursors.DictCursor)
    with connection:
        connection.begin()
        cursor = connection.cursor()
        sql = "INSERT INTO `logs` (`server`, `dt`) VALUES (%s, cast(now() AS datetime))"
        cursor.execute(sql, (server,))
        sql = "SELECT `server`, `dt` FROM `logs` ORDER BY `dt` DESC LIMIT 10"
        cursor.execute(sql)
        connection.commit()
        logs = cursor.fetchall()
        results = '<H1>Recent Access</H1>'
        for log in logs:
            results += log['server']+' : '+log['dt'].strftime('%Y-%m-%d %H:%M:%S')+'<br/>'
        results += '<H1>Old Access</H1>'
    return str(results)

run(host='0.0.0.0', port=8412, reloader=True, debug=True)

