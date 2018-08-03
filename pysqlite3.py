#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Filename:pysqlite3.py
"I am : doestr.__doc__"

# 读写    sqlite3
import sqlite3

#创建SQLite3数据库链接，创建students工作表并插入一条记录
def creatDB():
    # 连接到SQLite数据库
    # 数据库文件是mytest1.db
    # 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect('./mytest1.db')
    # 创建一个Cursor:
    cursor = conn.cursor()
    print("Hello SQL {0}".format("sqlite3"))
    # 执行一条SQL语句，创建students表:
    #执行语句
    sqlStr1 = "create table students(name text, username text,id int)"
    cursor.execute(sqlStr1)
    # 继续执行一条SQL语句，插入一条记录:
    sqlStr2 = "insert into students(id, username, name) values (\'1\', \'Michael\',\'Mick\')"
    cursor.execute(sqlStr2)
    # 通过rowcount获得插入的行数:
    print("cursor.rowcount ==> {0}".format(cursor.rowcount))
    # 关闭Cursor:
    cursor.close()
    # 提交事务:
    conn.commit()
    # 关闭Connection:
    conn.close()

def selectDB():
    conn = sqlite3.connect('./mytest1.db')
    cursor = conn.cursor()
    # 执行查询语句:
    cursor.execute('select * from students')
    # 获得查询结果集:
    values = cursor.fetchall()
    print(values)
    # 关闭Cursor:
    cursor.close()
    # 关闭Connection:
    conn.close()
    
def demo():
    selectDB()

if __name__ == '__main__':
    demo()
