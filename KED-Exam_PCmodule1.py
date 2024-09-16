#MAIN MENU

def main():
    print("Welcome to Data Warehousing")
    print("The following are your data:")

    while True: 
        print('''[1] Read\n[2] Create\n[3] Update\n[4] Delete\n''')

        option = int(input("Please input one of the above: "))

        if option == 1 : 
            print ("You select Read.")
            read()
        elif option == 2 :
            print ("You select Create.")
            create()    
        elif option == 3 :
            print ("You select Update.") 
            update()
        elif option == 4 :
            print ("You select Delete.")
            delete() 
        else :
            print ("Not available menu. Please try again.")
    

#READ MENU
Inventories = [
    {"id": 1, "name" : "Ready to Wear", "stock": 72000, "loc": ["Europe", "Asia"], "store": ["Milan"]},
    {"id": 2, "name" : "accessories", "stock": 4000, "loc": ["Europe", "Australia"], "store": ["Zurich", "Milan"]},
    {"id": 3, "name" : "Customized", "stock": 150, "loc": ["Europe", "America"], "store": ["Milan","Zurich"]},
]

def welcomeText():
    print ("We are going to next page...")

def read ():
    welcomeText()
    while True: 
        print('''
            1. Show All Data 
            2. Search by id
            3. Return to Main Menu 
                ''')

        option = int(input("Please input one of the above: "))

        if option == 1 : 
            if len(Inventories) == 0:
                print ("Data doesn not exist")
            else:
                print (Inventories) 
        elif option == 2 :
            if len(Inventories) == 0:
                print ("Data doesn not exist")
            else:
                id_from_user = int(input("Please select id: "))
                found = False
                for Inventory in Inventories:
                    if id_from_user == Inventory["id"] :
                        found = True
                        print(Inventory)
                if found == False:
                    print("Data doesn't match!")
                    
        elif option == 2: 
            return
        
        else:
            print ("Not available menu. Please try again.")  

def create ():
    welcomeText()
    while True: 
        print('''
            1. Add new item 
            2. Return to Main Menu 
                ''')

        option = int(input("Please input one of the above: "))
        if option == 1 : 
            new_item= int(input(("Which item do you want to add?")))
            found = False
            for Inventory in Inventories: 
                if new_item == Inventory["id"]: 
                    found = True
                    print("Data already exists")
                    break
            if found == False : 
                new_inventory_name = (str(input("Please input new item: ") ))
                print("Do you want to save changes?")
                save_opt= int(input('''
                          1.yes ; or 
                          2. no
                          '''))
                if save_opt == 1 : 
                    new_inventory = {"id": new_item, "name": new_inventory_name}
                    Inventories.append(new_inventory)
                    print("Thank you. You just added {} to your new Inventory".format(new_inventory_name))
                    print("Here are your New Inventories: {}".format(Inventories))
        
        elif option == 2: 
            return
        
        else:
            print ("Not available menu. Please try again.")

def update(): 
    welcomeText()
    while True: 
        print('''
            1. Update existing item 
            2. Return to Main Menu 
                ''')

        option = int(input("Please select one of the above: "))
        if option == 1 : 
            id_from_user = int(input("Please select id: "))
            up_item = None
            for Inventory in Inventories:
                if id_from_user == Inventory["id"] :
                    up_item = Inventory
                    break

            if up_item == None:
                print("Data you are looking for does not exist")
            else : 
                print(up_item)
                print("Do you want to continue update item? ")
                up_opt= int(input('''
                          1.yes ; or 
                          2. no
                          '''))
                if up_opt == 1 : 
                    print('''
                    Which data you want to update?
                          1.Stock ; or 
                          2. Location
                          ''')
                    req_upt= int(input("Enter value: "))
                    order_update = str(input("Input value:  "))
                    update_opt = int(input(''' Are you sure you still want to update? 
                          1.yes ; or 
                          2. no
                          '''))
                    if update_opt == 1: 
                        if req_upt == 1: 
                            order_update = int(order_update)
                            up_item["stock"] = order_update
                        elif req_upt == 2: 
                            up_item["loc"].append(order_update)

                        for Inventory in Inventories:
                            if id_from_user == Inventory["id"] :
                                Inventory = up_item
                                break
                        print("Data has been successfully update!")
                        print(Inventories)
        elif option == 2: 
            return
        
        else:
            print ("Not available menu. Please try again.")



def delete(): 
    welcomeText()
    while True: 
        print('''
            1. Delete item 
            2. Return to Main Menu 
                ''')
        option = int(input("Please select one of the above: "))
        if option == 1 : 
            id_from_user = int(input("Please select id: "))
            del_item = None
            for Inventory in Inventories:
                if id_from_user == Inventory["id"] :
                    del_item = Inventory
                    break

            if del_item == None:
                print("Data you are looking for does not exist")
            else : 
                del_req = int(input(''' Are you sure you still want to delete? 
                          1.yes ; or 
                          2. no
                          '''))
                if del_req == 1: 
                    Inventories.remove(del_item)
                        

                print("Data has been successfully deleted!")
                print(Inventories)


        elif option == 2: 
            return
        
        else:
            print ("Not available menu. Please try again.")

main()
    