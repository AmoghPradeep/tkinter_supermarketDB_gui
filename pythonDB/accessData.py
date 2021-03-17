'''
Created by : Amogh Pradeep on 16/03/2020
'''

import mysql.connector

#get branch information

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Amogh2001#",
    database = "retail"
)

def getData(table, condition = ""):
    mycursor = db.cursor()
    if len(condition > 1):
        condition = " where " + condition
    sql = "select * from " + table + condition
    try:
        mycursor.execute(sql)
        data = mycursor.fetchall()
    except:
        print("retrieval failed!")
        return False

    return data

def insertData(table, vals):
    print(table)
    print(vals)
    mycursor = db.cursor()
    sql = "insert into " + table + " values ("
    for i in range(0, len(vals)):
        if i == len(vals) - 1:
            sql += "%s)"
            break;
        sql += "%s, "
    try:
        mycursor.execute(sql, vals)
        db.commit()
    except:
        return False
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

    
    

        

