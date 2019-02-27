#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql.cursors

'''
insert function 

example of invoking:
insert('table_name',{'a':1,'b':2,'c':3})
insert('c_table',[{'a':1,'b':2,'c':3},{'a':4,'b':5,'c':6}])
'''
def insert (table, insertObj):
    connection = pymysql.connect(host ="localhost", user ="j", passwd ="123QWEasd", db="wallstreet", charset='utf8',port=3306 )
    cursor = connection.cursor()
    fields = []
    values = []
    queryStr = 'INSERT INTO `' + table + '` '
    if type(insertObj)==list and len(insertObj)>0:
        valuesArray = []
        for field in insertObj[0]:
            fields.append(field)

        for index in range(len(insertObj)):
            values = []
            for fieldName in insertObj[index]:
                if fieldName == 'NOW()':
                    values.append(insertObj[index][fieldName])
                else:
                    values.append(connection.escape(insertObj[index][fieldName]))
            valuesArray.append('(' + (','.join(values)) + ')')
        valuesArray = ','.join(valuesArray);
        queryStr += ' ( ' + (','.join(fields)) + ' ) VALUES ' + valuesArray+';'
    else:
        for i in insertObj:
            fields.append(i)
            if i == 'NOW()':
                values.append(insertObj[i])
            else:
                values.append(connection.escape(insertObj[i]))

        fields = ','.join(fields)
        values = ','.join(values)
        queryStr = queryStr + ' ( ' + fields + ' ) '
        queryStr = queryStr + ' VALUES ( ' + values + ' ) ' + ';'
    # print(queryStr)
    try:
        cursor.execute(queryStr)
        connection.commit()
    except MySQLError as e:
        print ('there is a fucking error!:'+e)
        connection.rollback()
    connection.close()

'''
update function 

example of invoking:
insert('table_name',{'b':'1','c':'2','d':3},{'a':1})
insert('table_name',{'c':1,'d':2,'e':3},{'a':1,'b':1})
'''
def update (table, dataObj, condiObj):
    if len(dataObj)>0 and len(condiObj)>0:
        connection = pymysql.connect(host="localhost", user="j", passwd="123QWEasd", db="wallstreet", charset='utf8',port=3306)
        cursor = connection.cursor()
        queryStr = "UPDATE `" + table + "` SET  "
        whereCondi = ' WHERE '
        values = []
        for i in dataObj:
            if i == 'NOW()':
                values.append(i+'=NOW()')
            else:
                values.append(i+'='+connection.escape(dataObj[i]))
        values = ','.join(values)
        queryStr = queryStr+values
        arr = []
        for key in condiObj:
            arr.append(key+'='+connection.escape(condiObj[key]))
        whereCondi = whereCondi + ' AND '.join(arr);
        queryStr = queryStr+whereCondi
        print (queryStr)

        try:
            cursor.execute(queryStr)
            connection.commit()
        except:
            print ('there is a fucking error!')
            connection.rollback()
        connection.close()

'''
select function 

example of invoking:
select('table1',
       ['table1.Findex', 'table2.Fname', 'table3.Fextra'],
       [['table1.a','=','1']],
       [['table2','table1.a','=','table2.a'],['table3','table1.a','=','table3.a']])

select('table1',
       ['*'],
       [['table1.a', '>', '1']])

select('stock_basic_info',
       ['*'],[])
       
'''
def select (mainTable, selectFields, conditions, *fromCondition):
    connection = pymysql.connect(host="localhost", user="j", passwd="123QWEasd", db="wallstreet", charset='utf8',port=3306)
    cursor = connection.cursor()
    query = 'SELECT ' + ','.join(selectFields) +' FROM '+mainTable +' '
    if isinstance(fromCondition, str):
        query = query+fromCondition
    elif type(fromCondition)==list:
        from_list = []
        for f in range(len(fromCondition)):
            query=query+' LEFT JOIN '+fromCondition[f][0]+' ON '+fromCondition[f][1]+fromCondition[f][2]+fromCondition[f][3]
            # from_list.append(connection.escape(fromCondition[f][0])+connection.escape(fromCondition[f][1])+connection.escape(fromCondition[f][2]))

    if len(conditions)>0:
        query = query +' WHERE '
        condition_list = []
        for c in range(len(conditions)):
            condition_list.append(conditions[c][0]+conditions[c][1]+conditions[c][2])
        query = query + ' AND '.join(condition_list)
    query+=';'
    print (query)
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except MySQLError as e:
        print ('there is a fucking error!:'+e)
        return ''
    connection.close()

