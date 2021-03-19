'''
Created by : Amogh Pradeep on 16/03/2020
amoghpradeep241@gmai.com
'''

import mysql.connector

#get branch information

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Amogh2001#",
    database = "retail"
)

def getData(table, condition = "", column = "*"):
    if column == "All":
        column = '*' 
    mycursor = db.cursor()
    if len(condition) > 1:
        condition = " where " + condition
    sql = "select " + column + " from " + table + condition
    print(sql)
    try:
        mycursor.execute(sql)
        data = mycursor.fetchall()
    except:
        return False

    return data

def insertData(table, vals):
    mycursor = db.cursor()
    sql = "insert into " + table + " values ("
    for i in range(0, len(vals)):
        if i == len(vals) - 1:
            sql += "%s)"
            break;
        sql += "%s, "
    mycursor.execute(sql, vals)
    db.commit()
    return True

def delData(table, id, val):
    mycursor = db.cursor()

    sql = "delete from " + table + " where " + id + " = " + val
    try:
        mycursor.execute(sql)
        db.commit()
    except:
        return False
    
    return True

def getTableInfo():
    mycursor = db.cursor()

    sql = "select table_name, table_rows from information_schema.tables where table_schema = 'retail'"
    try:
        mycursor.execute(sql)
        tables = mycursor.fetchall()
    except:
        return False
     
    return tables
