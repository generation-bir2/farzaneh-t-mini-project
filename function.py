import sys
import os
import csv
import pymysql
from tabulate import tabulate
from dotenv import load_dotenv
import order_func

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="app",
)

def showing_rows(table_name, row_title):
    try:
        connection = order_func.create_connection()
        cursor = connection.cursor()
        sql = """SELECT * from {}""".format(table_name)
        cursor.execute(sql)
        records = cursor.fetchall() 
        l = []
        for row in records:
            l.append(row)
        print(tabulate(l, headers=row_title))     
        connection.commit()    
        cursor.close()
        connection.close()
    except Exception as e:
        print("Failed to read data from table", e)
        
def inserting(table_name, column_name, c, val):
    # try:
    connection = order_func.create_connection()
    cursor = connection.cursor()
    sql = """INSERT INTO {} {} VALUES {}""".format(table_name, column_name, c)
    cursor.execute(sql, val)
    connection.commit()    
    cursor.close()
    connection.close()       
    print("Python Variables inserted successfully into product table")
        # cursor.close()
    # except Exception as e:
    #     print("Failed to insert Python variable into sqlite table", e)
        
def deleting(a, table_name):
    try:
        connection = order_func.create_connection()
        cursor = connection.cursor()
        sql = """DELETE FROM {} WHERE {}_id = %s""".format(table_name, table_name)
        cursor.execute(sql, (a,))
        connection.commit()    
        cursor.close()
        connection.close()
    except Exception as e:
        print("Failed to delete record from table", e)

def deleting_order(a, table_name):
    try:
        connection = order_func.create_connection()
        cursor = connection.cursor()
        sql = """DELETE FROM {} WHERE order_id = %s""".format(table_name)
        cursor.execute(sql, (a,))
        connection.commit()    
        cursor.close()
        connection.close()
    except Exception as e:
        print("Failed to delete record from table", e)
        
def updating(table,coul_names, value):
    try:
        connection = order_func.create_connection()
        cursor = connection.cursor()
        sql = """UPDATE {} SET {} WHERE {}_id = %s""".format(table, coul_names, table)
        cursor.execute(sql, value) 
        connection.commit()    
        cursor.close()
        connection.close()
    except Exception as e:
        print("Failed to update multiple columns of sqlite table", e)

def preparing_data_for_updating(column_name): 
    try:
        s = ""
        for i in range(len(column_name)):
            if i != len(column_name) - 1:
                s1 = column_name[i] + " = %s, "
                s += s1
            else:
                s1 = column_name[i] + " = %s"
                s += s1
        return s
    except Exception as e:
        print("Failed to update multiple columns of sqlite table", e)