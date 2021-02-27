import sys
import os
import csv
import pymysql
from dotenv import load_dotenv
from tabulate import tabulate

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="app",
)

def create_connection():
    return pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="app",
)

def showing_orders():
    create_connection()
    # try:
    row_title = ["orders_id", "couriers_id", "status", "customers_name", "customers_address", "customers_phone", "items"]
    cursor = connection.cursor()
    sql = """SELECT orders_id, couriers_id, status, customers_name, customers_address, customers_phone,
    (SELECT GROUP_CONCAT(p.product_id) FROM orders_products p WHERE p.order_id = o.orders_id) AS items
    FROM orders o
    inner join customers c
    on o.customers_id = c.customers_id
    order by couriers_id"""
    cursor.execute(sql)
    records = cursor.fetchall()
    l = []
    # l.append(row_title)
    for row in records:
        s = []
        for i in row:
            s.append(str(i))
        l.append(s)
    # for i in l:
    #     print(i)
    print(tabulate(l, headers=row_title))
    connection.commit()    
    cursor.close()
    connection.close()
    # except Exception as e:
    #     print("Failed to update multiple columns of sqlite table", e)

def updating_orders_and_customers(list_name, new_value, table_name1, table_name2, id):
    try:
        l = ['customers_id', 'customers_name', 'customers_address', 'customers_phone']
        for i in range(len(list_name)):
            if list_name[i] in l:
                connection = create_connection()
                cursor = connection.cursor()
                sql = """SELECT customers_id FROM orders WHERE orders_id = %s"""
                cursor.execute(sql, (id,))
                for record in cursor.fetchall():
                    k = int(record[0])
                sql2 = """UPDATE {} SET {} = %s WHERE {}_id = %s""".format(table_name1, list_name[i], table_name1)
                val = (new_value[i], k)
                cursor.execute(sql2, val)
                connection.commit()    
                cursor.close()
                connection.close()
            else:
                connection = create_connection()
                cursor = connection.cursor()
                sql = """UPDATE {} SET {} = %s WHERE {}_id = %s""".format(table_name2, list_name[i], table_name2)
                val = (new_value[i], id)
                cursor.execute(sql, val)
                connection.commit()    
                cursor.close()
                connection.close()
    except Exception as e:
        print("Failed to read data from table", e)

        
def finding_max(table_name, column_name):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("""SELECT MAX({}) FROM {}""".format(column_name, table_name))
        records = cursor.fetchall() 
        for i in records: 
            maximum= int(i[0]) 
        connection.commit()    
        cursor.close()
        connection.close()
        return maximum
    except Exception as e:
        print("Failed to read data from table", e)

def finding_customer(val):
    try:
        global k
        k = 0
        cursor = connection.cursor()
        sql = """SELECT customers_id FROM customers WHERE customers_name = %s 
                AND customers_address = %s AND customers_phone = %s"""
        cursor.execute(sql, val)
        for record in cursor.fetchall():
            k = int(record[0])
        connection.commit()    
        cursor.close()
        connection.close()
        return k
    except Exception as e:
        print("Failed to read data from table", e)

def operating_on_inventory(operation, number, id):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        sql = """SELECT product_quantity FROM products WHERE products_id = %s"""
        cursor.execute(sql, (id,))
        for record in cursor.fetchall():
            k = int(record[0])
            connection.commit()
        if operation == "+":
            summation = (number + k)
        else:
            summation = (k - number)
        sql = """UPDATE products SET product_quantity = %s WHERE products_id = %s"""
        val = (summation, id)
        cursor.execute(sql, val)
        connection.commit()    
        cursor.close()
        connection.close()
    except Exception as e:
        print("Failed to read data from table", e)

    
def operations_befor_and_after_updating(id, sign):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        sql = """SELECT * FROM orders_products WHERE order_id = %s"""
        cursor.execute(sql, (id,))
        for record in cursor.fetchall():
            k = int(record[1])
            if sign == "+":
                operating_on_inventory("+", 1, k)
            else:
                operating_on_inventory("-", 1, k)
        connection.commit()    
        cursor.close()
        connection.close()
    except Exception as e:
        print("Failed to read data from table", e)
        
def checking_zero_for_item(prod_id):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        sql = """SELECT product_quantity FROM products WHERE products_id = %s"""
        cursor.execute(sql, (prod_id,))
        for record in cursor.fetchall():
            k = int(record[0])
        connection.commit()    
        cursor.close()
        connection.close()
        return k
    except Exception as e:
        print("Failed to read data from table", e)
        
def checking_inventory(items):
    try:
        global add
        add = []
        for i in range(len(items)):
            x = checking_zero_for_item(items[i])
            if x <= 0:
                os.system("cls")
                print("sorry, product with product_id = " + str(items[i]) + " is finished. Do you want to continue for ordering?")
                items[i] = 0
                s = int(input("if yes please enter 1 and if no please enter another number:\n"))
                if s != 1:
                    print("Have a nice day!")
                    # i, j, k = False, False, False
                    break
                os.system("cls")
                print("Do you want to add new product to your items list?")
                m = int(input("if yes please enter 1 and if no please enter another number\n"))
                if m ==1 :
                    os.system("cls")
                    print("please enter new items (put space between them)")
                    add = [int(x) for x in input().split()]
        items = list(filter(lambda a: a != 0, items))
        for row in add:
            items.append(row)
        return items
    except Exception as e:
        print("Failed to read data from table", e)