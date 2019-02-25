#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
from DBUtils.PooledDB import PooledDB
# db = MySQLdb.connect("localhost", "j", "123QWEasd", "wallsteet", charset='utf8',port=3306 )

def getPool():
    pool = PooledDB(MySQLdb, 5, host='localhost', user='j', passwd='123QWEasd', db='wallsteet',port=3306)  # 5为连接池里的最少连接数
    return pool
def getConnection ():
    conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
    return conn
def closeConnection (conn):
    conn.close()

def insert (table, insertObj):
    db = MySQLdb.connect(host ="localhost", user ="j", passwd ="123QWEasd", db="wallsteet", charset='utf8',port=3306 )
    cursor = db.cursor()
    fields = []
    values = []
    queryStr = 'INSERT INTO `' + table + '` '
    if type(insertObj)==list and len(insertObj)>0:
        valuesArray = []
        for field in insertObj[0]:
            fields.append(field)

        for index in insertObj:
            for fieldName in dataObj[index]:
                if fieldName == 'NOW()':
                    values.append(dataObj[index][fieldName])
                else:
                    values.append(MySQLdb.escape_string(dataObj[index][fieldName]))
            valuesArray.push('(' + (''.join(values)) + ')')
        valuesArray = ''.join(valuesArray);
        queryStr += ' ( ' + (''.join(fields)) + ' ) VALUES ' + valuesArray
    else:
        for i in insertObj:
            fields.append(i)
            if fieldName == 'NOW()':
                values.append(insertObj[i])
            else:
                values.append(MySQLdb.escape_string(insertObj[i]))

        fields = ''.join(fields)
        values = ''.join(values)
        queryStr = queryStr + ' ( ' + fields + ' ) '
        queryStr = queryStr + ' VALUES ( ' + values + ' ) ' + ';'

    try:
        cursor.execute(queryStr)
        db.commit()
    except:
        db.rollback()
    db.close()