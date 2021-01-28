import sys
import os

product = []
courier = []
user = []
courier_user = []
orders = []
i, j, k, l = True, True, True, True

def asking_for_continu(c):
    print("Do you want to continue for changing or deleting in your list?")
    value8 = int(input("if yes please enter 1 and if no please enter 0\n"))
    if value8 == 1:
        os.system("cls")
        a, b = True, True
    else:
        print("Thanks for your ordering")
        with open("final_list.txt", "w") as f:
            f.write("List of products")
            for item in c:
                f.write("%s\n" % item)
        a, b = False, False  
    return a, b

def asking_for_going_to_couriers_list(c):
    os.system("cls")
    print("Do you want to choos from Couriers list?")
    value3 = int(input("If yes please enter 1 and if no please enter 2"))
    if value3 == 1:
        value = 3
        b, l = True, False
        os.system("cls")
    else:
        with open("final_list.txt", "w") as f:
            f.write("List of products")
            for item in c:
                f.write("%s\n" % item)
        print("Have a good time")
        b = False
        l = False
    return(b, l)

def deleting_number_of_string(a):
    c = []
    for i in range(len(a)):
        b = a[i]
        b = b[2:]
        c.append(b)
    return c

def file_to_list(entry_list, file):
    for line in file:
        stripped_line = line.strip()
        entry_list.append(stripped_line)
    return entry_list

def show_message(e):
    if len(e) > 1:
        print("It is your current list order")
        b = deleting_number_of_string(e)
        for i in range(len(e)):
            print("order " + str(i + 1) + ": "+ b[i])
        print(str(len(e)) + " items are in your order list, please enter the order number for the item that you want to change or remove.\n")
        previous_item = int(input())
        os.system("cls")
    else:
        print("It is your order")
        b = deleting_number_of_string(e)
        print(b[0])
        previous_item = 1
        print('    ')
        
    return previous_item

def update(a,c):
    previous_item = show_message(a)
    print(*c, sep = "\n")
    new_item = int(input("Enter the number of your new choice from above list.:\n"))
    a[previous_item - 1] = c[new_item - 1]
    b = deleting_number_of_string(a)
    os.system("cls")
    print(*b, sep = "\n")
    print("It is your new order list.")
    return a,b
    
def remove(a):
    remove_item = show_message(a)
    del a[remove_item - 1]
    b = deleting_number_of_string(a)
    os.system("cls")
    if len(b) > 0:
        print(*b, sep = "\n")
        print("It is your new order list")
    return a,b

with open("products.txt", "r") as a_file:
    products = file_to_list(product, a_file)

with open("couriers.txt") as b_file:
    couriers = file_to_list(courier, b_file)

print('Welcome to the app!')
while i == True:
    
    if l == True:
        print('                           ')
        print("Select an option from menu:")
        value = int(input('Option 1: close app\noption 2: show products list\noption 3: show couriers list\n'))
    else:
        value = 3
        j, k = True, True

    if value == 1:
        sys.exit(0)   #exit app
###################################### Product #############################################################       
    elif value == 2: 
        os.system("cls")
        print('Please choose one of below options: ')   #show app menu
        value2 = int(input('Option 1: go to main menu\noption 2: show products\noption 3: choose the product\n'))
        os.system("cls")
        while j == True:
            if value2 == 1:   #return to main menu
                j = False
            
            elif value2 == 2:   #print out products to screen
                print(*products, sep = "\n")
                print('                                         ')
                print("Do you want to choose one of the opthions:")
                value3 = int(input("if yes please enter 1 and if No please enter 2.\n"))
                if value3 == 1:   #allow user to pick product from products which are printed out to screen
                    value2 = 3
                    os.system("cls")
                
                elif value3 == 2:   #allow user to exit the app 
                    print("Thanks for coming")
                    i, j = False, False
                
            elif value2 == 3:  #allow user to pick product from products
                os.system("cls")
                print("Do you want to see the products menu?")
                value10 = int(input("if yes please enter 1 and if no please enter 2\n"))
                if value10 == 1:
                    os.system("cls")
                    print(*products, sep = "\n")
                print("Please Enter the product number: ")
                product_name = int(input())
                user.append(products[product_name - 1])
                os.system("cls")
                new_user = deleting_number_of_string(user)
                print(*new_user, sep = "\n")
                k = True
                while k == True:
                    print("                                            ")
                    print("Do you need another products, change the product or delete it?")
                    value4 = int(input("option 1: new product\noption2: change the product\noption3: delete product\noption 4: no need another product\n"))
                    os.system("cls")
                    if value4 == 1:   #allow user to pick new product and add it to previous list
                        value2 = 3
                        k = False
                    elif value4 == 2:   #allow user to pick new product and change it with previous item
                        os.system("cls")
                        print("Do you want to updat?")
                        value5 = int(input("if yes please enter 1 and if no please enter 0\n"))
                        if value5 == 0:
                            continue
                        elif value5 == 1:
                            os.system("cls")
                            user, new_user = update(user,products)
                            j, k = asking_for_continu(new_user)
                            if j == False and k == False:
                                i, l = asking_for_going_to_couriers_list(new_product)
                    elif value4 == 3:   #allow user to remove products from list of items
                        if len(user) >= 1:
                            print("Do you want to delete?")
                            value6 = int(input("if yes please enter 1 and if no please enter 0\n"))
                            if value6 == 0:
                                os.system("cls")
                                continue
                            else:
                                os.system("cls")
                                user, new_user = remove(user)
                                j, k = asking_for_continu(new_user)
                                if j == False and k == False:
                                    i, l = asking_for_going_to_couriers_list(new_user)
                                
                        else:
                            print("         ")
                            print("There is not any order for deleting")
                    
                    elif value4 == 4:   #allow user to close the app
                        print("                           ")
                        print("Thanks for your ordering")
                        with open("final_list.txt", "w") as f:
                            f.write("List of products\n")
                            for item in new_user:
                                f.write("%s\n" % item)
                        i, j, k = False, False, False
                        
############################################# Couriers Part ###################################################

    elif value == 3:
        os.system("cls")
        print('Please choose one of below options: ')   #show app menu
        value2 = int(input('Option 1: go to main menu\noption 2: show couriers\noption 3: choose the couriers\n'))
        os.system("cls")
        while j == True:
            if value2 == 1:   #return to main menu
                j = False
            elif value2 == 2:   #print out couriers to screen
                print('                           ')
                print(*couriers, sep = "\n")
                print('                                         ')
                print("Do you want to choose one of the opthion:")
                value3 = int(input("if yes please enter 1 and if No please enter 2.\n"))
                if value3 == 1:   #allow user to pick product from couriers which are printed out to screen
                    value2 = 3
                    os.system("cls")
                    
                elif value3 == 2:   #allow user to exit the app 
                    print("Thanks for coming")
                    i, j = False, False
                    
            elif value2 == 3:  #allow user to pick courier from couriers
                os.system("cls")
                print("Do you want to see the courier menu?")
                value10 = int(input("if yes please enter 1 and if no please enter 2\n"))
                if value10 == 1:
                    os.system("cls")
                    print(*couriers, sep = "\n")
                print("Please Enter the courier number: ")
                couriers_num = int(input())
                courier_user.append(couriers[couriers_num - 1])
                os.system("cls")
                new_courier = deleting_number_of_string(courier_user)
                print(*new_courier, sep = "\n")
                k = True
                while k == True:
                    print(" ")
                    print("Do you need to change the courier or delete?")
                    value4 = int(input("option1: change the couier\n option2: delete couriers\n option 3:no need another couier\n"))
                    os.system("cls")
                    if value4 == 1:   #allow user to pick new product and change it with previous item
                        os.system("cls")
                        print("Do you want to update?")
                        value5 = int(input("If yes please enter 1 and in no please enter 0\n"))
                        if value5 == 0:
                            continue
                        elif value5 == 1:
                            os.system("cls")
                            courier_user, new_courier = update(courier_user, couriers)
                            j, k = asking_for_continu(new_courier )
                            i = False
                            #l = False
                    elif value4 == 2:   #allow user to remove couriers from list of items
                        print("Do you want to remove?")
                        value6 = int(input("if yes please enter 1 and if no please enter 0"))
                        if value6 == 0:
                            continue
                        else:
                            os.system("cls")
                            courier_user, new_courier = remove(courier_user)
                            print("Do you want to choose new courier?")
                            value8 = int(input("if yes please enter 1 and if no please enter2:\n"))
                            if value8 == 1:
                                k = False
                                value2 = 3
                            else:
                                os.system("cls")
                                print("Thanks for your ordering")
                                with open("final_list.txt", "w") as f:
                                    f.write("List of couriers\n")
                                    for item in new_courier:
                                        f.write("%s\n" % item)
                                i, j, k = False, False, False
                        
                    elif value4 == 3:   #allow user to close the app
                        print("                           ")
                        print("Thanks for your ordering")
                        with open("final_list.txt", "w") as f:
                            f.write("List of couriers\n")
                            for item in new_courier:
                                f.write("%s\n" % item)
                        i, j, k = False, False, False

################################Orders###############################################################
    elif value == 4:
        os.system("cls")
        print('Please choose one of below options: ')   #show app menu
        value2 = int(input('Option 1: go to main menu\noption 2: show orders\noption 3: creat new order\noption 4: update the order'))
        os.system("cls")
        while j == True:
            if value2 == 1:   #return to main menu
                j = False
            elif value2 == 2:   #print out couriers to screen
                print('                           ')
                x = input("please choose one of bellow order updat")
                for order in orders:
                    for keys, values in orders[order].items():
                        print(keys + ": " + str(values))
                    print("-------------------------------------------") 
                value3 = input("if you want to creat new order please enter 1")
                if value3 == 1:
                    valu2 = 3                 
            elif value2 == 3:  #allow user to pick courier from couriers
                os.system("cls")
                dictionary = {}
                name = input("Please enter your name:")
                address = input("Please enter your address:")
                phone = input("Please enter your phone:")
                courier = int(input("Please enter your courier:"))
                dictionary["customer_name"] = name
                dictionary["customer_address"] = address
                dictionary["customer_phone"] = phone
                dictionary["courier"] = courier
                dictionary["status"]= "preparing"
                orders.append(dictionary.copy())
                
            elif value2 == 4:
                print(" ")
                os.system("cls")
                print("Do you want to update?")
                value5 = int(input("If yes please enter order number for updating and if no please enter 0\n"))
                if value5 == 0:
                    continue
                elif value5 == 1:
                    os.system("cls")
                    print("It is your previous order")
                    for keys, values in orders[value5].items():
                        print(keys + ": " + str(values)) 
                    for i, j in orders[value5].items():
                        x = str(input("if you want to update the value of {} please enter the new value and if no, please skip it"))
                        if len(x) > 0:
                            orders[value5][i] = x
                        else:
                            orders[value5][i] = j
                            
                        os.system("cls")
                        print("It is your new order")
                        for keys, values in orders[y].items():
                            print(keys + ": " + str(values))
                        print("-------------------------------------------") 
            elif value4 == 5:   #allow user to remove order from list of orders
                print("Do you want to remove?")
                value6 = int(input("if yes please enter the order number for deleting and if no please enter 0"))
                if value6 == 0:
                    continue
                else:
                    os.system("cls")
                    del(orders[value6]) 
                    for keys, values in orders[y].items():
                        print(keys + ": " + str(values))
                    print("-------------------------------------------")                   
                
            elif value4 == 6:   #allow user to close the app
                print("                           ")
                print("Thanks for your ordering")
                i, j, k = False, False, False
