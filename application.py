import sys
import os
import csv
import pymysql
import function
import order_func
from tabulate import tabulate
from dotenv import load_dotenv

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
i, j, k = True, True,True 

print('Welcome to the app!')
while i == True:
    print('                           ')
    print("Select an option from menu:")
    value = int(input('option 1: close app\noption 2: show products list\noption 3: show couriers list\noption 4: show orders list\n'))

    if value == 1:
        print("have a nice day")
        sys.exit(0)   #exit app
        
# # ####################################### Product ############################################################
    elif value == 2:
        j = True
        while j == True:
            os.system("cls")
            b = "(product, price, product_quantity)"
            c = "(%s, %s, %s)"
            row_titles = ["products_id","product", "price", "product_quantity"]
            print('Please choose one of below options: ')
            value2 = int(input('Option 1: go to main menu\noption 2: show products\noption 3: add to product list\noption 4: update product\noption 5: delete product\noption 6: add/reduce inventory\noption 7: dont want to continue\n'))
            os.system("cls")
            k = True
            while k == True:
                if value2 == 1:
                    j, k = False, False
                elif value2 == 2:   
                    function.showing_rows("products", row_titles)
                    print("Do you want to continue for adding, updating or deleting?")
                    value5 = int(input("if yes please enter 1 and no else enter another number.\n"))
                    if value5 == 1:
                        k = False
                    else:
                        print("Have a nice day")
                        i, j, k = False, False, False 
                elif value2 == 3:  #allow user to add product to products list
                    os.system("cls")
                    name = input("Please enter name of product:\n")
                    price = float(input("Please enter price of product:\n"))
                    quantity = int(input("Please enter quantity of product:\n"))
                    row = (name, price, quantity)
                    function.inserting("products", b, c, row)
                    os.system("cls")
                    print("Do you want to see table after changing?")
                    value3 = int(input("if you want please enter 1 and if no please enter another number\n"))
                    if value3 == 1:
                        function.showing_rows("products", row_titles)
                    print("Do you want to continue for adding, updating or deleting?")
                    value5 = int(input("if yes please enter 1 and no else enter another number.\n"))
                    if value5 == 1:
                        k = False
                    else:
                        print("Have a nice day")
                        i, j, k = False, False, False                   
                elif value2 == 4:
                    print("Do you want to update?")
                    value5 = int(input("If yes please enter product number for updating and if no please enter 0\n"))
                    if value5 == 0:
                        continue
                    else:
                        column = []
                        column = input("please enter name of columns that you want to change (put comma between them)\n").split(",")
                        column_name = function.preparing_data_for_updating(column)
                        # new_val = [column_name]
                        new_val = []
                        new_val = input("please enter the new values (put comma between them)\n").split(",")
                        new_val.append(value5)
                        new = tuple(new_val)
                        function.updating("products",column_name, new)
                        print("Do you want to see table after changing?")
                        value3 = int(input("if you want please enter 1 and if no please enter another number\n"))
                        if value3 == 1:
                            function.showing_rows("products", row_titles)
                        print('Do you want to continue for adding, updating or deleting?')
                        val = int(input('if yes please enter 1 and if no please enter another number.'))
                        if val == 1:
                            k = False
                        else:
                            print('Have a nice day.')
                            i, j, k = False, False, False
                elif value2 == 5:   #allow user to remove order from list of orders
                    print("Do you want to remove?")
                    value6 = int(input("if yes please enter the product number for deleting and if no please enter 0\n"))
                    if value6 == 0:
                        k = False
                    else:
                        os.system("cls")
                        function.deleting(value6, "products")
                        print("Do you want to see table after changing?")
                        value3 = int(input("if you want please enter 1 and if no please enter another number\n"))
                        if value3 == 1:
                            function.showing_rows("products", row_titles)
                        print('Do you want to continue for adding, updating or deleting?')
                        val = int(input('if yes please enter 1 and if no please enter another number.'))
                        if val == 1:
                            k = False
                        else:
                            print('Have a nice day.')
                            i, j, k = False, False, False                  
                elif value2 == 6:
                    id = int(input("pleae enter the product id that you want to add or reduce:\n"))
                    sign = input("please enter '+' for adding or '-' for reducing:\n")
                    quantity = int(input("please enter product quantity that you want add or reduce:\n"))
                    order_func.operating_on_inventory(sign, quantity, id)
                    print("Do you want to see table after changing?")
                    value3 = int(input("if you want please enter 1 and if no please enter another number\n"))
                    if value3 == 1:
                        function.showing_rows("products", row_titles)
                    print('Do you want to continue for adding, updating or deleting?')
                    val = int(input('if yes please enter 1 and if no please enter another number.'))
                    if val == 1:
                        k = False
                    else:
                        print('Have a nice day.')
                        i, j, k = False, False, False 
                elif value2 == 7:   #allow user to close the app
                    print("                           ")
                    print("Have a nice day.")
                    i, j, k = False, False, False             

######################################### Couriers ###########################################################
    elif value == 3:
        j = True
        while j == True:
            os.system("cls")
            b = "(courier, courier_phone_number)"
            c = "(%s, %s)"
            row_titles = ["courier_id","courier", "phone_number"]
            print('Please choose one of below options: ')   #show app menu
            value2 = int(input('Option 1: go to main menu\noption 2: show couriers\noption 3: add to courier list\noption 4: update courier\noption 5: delete courier\noption 6: dont want to continue\n'))
            os.system("cls")
            k = True
            while k == True:
                if value2 == 1:
                    j, k = False, False
                elif value2 == 2: 
                    function.showing_rows("couriers", row_titles)
                    print("Do you want to continue for adding, updating or deleting?")
                    value5 = int(input("if yes please enter 1 and no else enter another number.\n"))
                    if value5 == 1:
                        k = False
                    else:
                        print("Have a nice day")
                        i, j, k = False, False, False
                elif value2 == 3:  #allow user to add courier to products list
                    os.system("cls")
                    name = input("Please enter your courier name:")
                    number= input("Please enter courier number:")
                    row_titles = (name, number)
                    function.inserting("couriers", b, c, row_titles)
                    print("Do you want to see table after changing?")
                    value3 = int(input("if you want please enter 1 and if no please enter another number\n"))
                    if value3 == 1:
                        function.showing_rows("couriers", row_titles)
                    os.system("cls")
                    print("Do you want to continue for adding, updating or deleting?")
                    value5 = int(input("if yes please enter 1 and no else enter another number.\n"))
                    os.system("cls")
                    if value5 == 1:
                        k = False
                    else:
                        print("Have a nice day")
                        i, j, k = False, False, False 
                elif value2 == 4:
                    os.system("cls")
                    print("Do you want to update?")
                    value5 = int(input("If yes please enter courier number for updating and if no please enter 0\n"))
                    if value5 == 0:
                        continue
                    else:
                        column = []
                        column = input("please enter name of columns that you want to change (put comma between them)\n").split(",")
                        column_name = function.preparing_data_for_updating(column)
                        new_val = []
                        new_val = input("please enter the new values (put comma between them)\n").split(",")
                        new_val.append(value5)
                        new = tuple(new_val)
                        function.updating("couriers", column_name, new)
                        print("Do you want to see table after changing?")
                        value3 = int(input("if you want please enter 1 and if no please enter another number\n"))
                        if value3 == 1:
                            function.showing_rows("couriers", row_titles)
                        print("Do you want to continue for adding, updating or deleting?")
                        val = int(input('if yes please enter 1 and if no please enter another number.'))
                        if val == 1:
                            k = False
                        else:
                            print('Have a nice day.')
                            i, j, k = False, False, False
                elif value2 == 5:   #allow user to remove order from list of orders
                    print("Do you want to remove?")
                    value6 = int(input("if yes please enter the order number for deleting and if no please enter 0\n"))
                    if value6 == 0:
                        continue
                    else:
                        os.system("cls")
                        function.deleting(value6, "couriers")
                        print("Do you want to see table after changing?")
                        value3 = int(input("if you want please enter 1 and if no please enter another number\n"))
                        if value3 == 1:
                            function.showing_rows("couriers", row_titles)
                        print('Do you want to continue for adding, updating or deleting?')
                        val = int(input('if yes please enter 1 and if no please enter another number.'))
                        if val == 1:
                            k = False
                        else:
                            print('Have a nice day.')
                            i, j, k = False, False, False                  
                
                elif value2 == 6:   #allow user to close the app
                    print("                           ")
                    print("Have a nice day.")
                    i, j, k = False, False, False     

# ######################################## Orders ############################################################
    elif value == 4:
        j = True
        while j == True:
            os.system("cls")
            print('Please choose one of below options: ')   #show app menu
            value2 = int(input('Option 1: go to main menu\noption 2: show orders\noption 3: add to order list\noption 4: update order\noption 5: delete order\noption 6: dont want to continue\n'))
            os.system("cls")
            k = True
            while k == True:
                if value2 == 1:
                    j, k = False, False
                elif value2 == 2:   
                    order_func.showing_orders()
                    print("Do you want to continue for adding, updating or deleting?")
                    value5 = int(input("if yes please enter 1 and no else enter another number.\n"))
                    if value5 == 1:
                        k = False
                    else:
                        print("Have a nice day")
                        i, j, k = False, False, False 
                elif value2 == 3:  #allow user to add order to products list
                    os.system("cls")
                    customer_name = input("Please enter name of customer:\n")
                    customer_address = input("Please enter address of customer:\n")
                    customer_phone = input("Please enter phone of customer:\n")
                    customer_row = (customer_name, customer_address, customer_phone)
                    customer_row = tuple(customer_row)
                    couriers_id = int(input("Please enter number of courier:\n"))
                    status = input("Please enter status:\n")
                    print("please enter the product ids that you want to insert(please put space between them):\n")
                    item = [int(x) for x in input().split()]
                    items = order_func.checking_inventory(item)
                    customer_column = "(customers_name, customers_address, customers_phone)"
                    condition_value = order_func.finding_customer(customer_row)
                    if condition_value == 0:
                        connection = order_func.create_connection()  
                        function.inserting("customers", customer_column, "(%s, %s, %s)", customer_row)
                        connection = order_func.create_connection()
                        customer_id = order_func.finding_max("customers", "customers_id")
                    else:
                        customer_id = condition_value
                    order_row = (customer_id, couriers_id, status)
                    connection = order_func.create_connection()
                    function.inserting("orders", "(customers_id, couriers_id, status)", "(%s, %s, %s)", order_row)
                    b = order_func.finding_max("orders", "orders_id")  
                    for i in range(len(items)):
                        item_row = (b, items[i], i)
                        connection = order_func.create_connection()
                        function.inserting("orders_products", "(order_id, product_id, counters)", "(%s, %s, %s)", item_row)
                        order_func.operating_on_inventory("-", 1, items[i])
                    os.system("cls")
                    print("Do you want to continue for adding, updating or deleting?")
                    value5 = int(input("if yes please enter 1 and no else enter another number.\n"))
                    if value5 == 1:
                        k = False
                    else:
                        print("Have a nice day")
                        i, j, k = False, False, False
                    
                elif value2 == 4:
                    os.system("cls")
                    print("Do you want to update?")
                    value5 = int(input("If yes please enter order number for updating and if no please enter 0\n"))
                    if value5 == 0:
                        continue
                    else:
                        list_name = input("please enter all the column names that you want to change(please put two space between them\n").split("  ")
                        new_values = input("please enter all the new values(please put two space between them\n").split("  ")
                        order_func.updating_orders_and_customers(list_name, new_values, "customers", "orders", value5)
                        print("Please enter products ids that want to update(please put space between them):\n")
                        items = [int(x) for x in input().split()]
                        order_func.operations_befor_and_after_updating(value5, "+")
                        function.deleting_order(value5, "orders_products")
                        for i in range(len(items)):
                            item_row = (value5, items[i], i)
                            connection = order_func.create_connection()
                            function.inserting("orders_products", "(order_id, product_id, counters)", "(%s, %s, %s)", item_row)
                        order_func.operations_befor_and_after_updating(value5, "-")
                        val = int(input('if yes please enter 1 and if no please enter another number.'))
                        if val == 1:
                            k = False
                        else:
                            print('Have a nice day.')
                            i, j, k = False, False, False
                elif value2 == 5:   #allow user to remove order from list of orders
                    print("Do you want to remove?")
                    value6 = int(input("if yes please enter the order number for deleting and if no please enter 0\n"))
                    if value6 == 0:
                        continue
                    else:
                        os.system("cls")
                        function.deleting_order(value6, "orders_products")
                        function.deleting(value6, "orders")
                        print('Do you want to continue for adding, updating or deleting?')
                        val = int(input('if yes please enter 1 and if no please enter another number.'))
                        if val == 1:
                            k = False
                        else:
                            print('Have a nice day.')
                            i, j, k = False, False, False                  
                
                elif value2 == 6:   #allow user to close the app
                    print("                           ")
                    print("Have a nice day.")
                    i, j, k = False, False, False     
