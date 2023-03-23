from interface import *
from session import Auth
from users import *

''' Input colors '''
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def PrintWithColor(color_status, print_info):
    color_options = {"Invalid": bcolors.FAIL, "Success": bcolors.OKGREEN, "Action": bcolors.OKBLUE, "Important": bcolors.BOLD, "Warning": bcolors.WARNING}
    color_status = color_options[color_status]
    print(f"{color_status}{print_info}{bcolors.ENDC}")

''' Command line interface '''
def LoginPage():
    print('Welcome to PigeonBOX')
    user, attempt = None, 0
    while (user is None and attempt < 3):
        attempt+=1
        # usr_name = input("\nEnter username: ")
        # pwd = input("Enter password: ")
        usr_name = "gkubach0"
        pwd = "2nBztx3qzXV"
        user = Auth().Authenticate(usr_name, pwd)

    if not user: 
        print('\nFailed all 3 attempts, sorry')
        return
    
    PrintWithColor("Success",f'\nHi {user.first_name} you have successfully logged in')
    return user

def displayData(data):
    if not data:
        PrintWithColor("Warning",'No matches for given criteria')
        return

    for i, val in enumerate(data):
        print(f"{i + 1}: {val}")

def CarSearch() -> None:
    print('\nSearch car in inventory')
    search_decision = input("Enter model, make and year separated by commas\n")
    search_decision = list(map(lambda x: x.strip(), search_decision.split(',')))
    if len(search_decision) != 3: return
    model, make, year = search_decision[0], search_decision[1], search_decision[2]
    if not year.isnumeric(): 
        print('\nInvalid input')
        return
    car = interface.searchInventory(model, make, int(year))
    if not car: 
        print('\nNo car match given criteria')
        return
    PrintWithColor('Success', f"\nCar details:\n{car.Details()}")
    #TODO
    # finish orders
    # make_order()

def InventoryMenu():
    print('\nCars in the inventory')

    inventory = interface.ViewInventory()
    displayData(inventory)

    options = ["1. Search","2. Filter by", "3. Make a customer order"]
    if isinstance(interface, AdminInterface): 
        options.append("4. Add/Remove Cars")

    options.append("Type 'q' to exit inventory menu")
    opt_str = "\n" + "\n".join(options)

    while True:
        PrintWithColor("Action", opt_str)
        decision = input("Enter action: ")
        if decision == '1':
            CarSearch()
        elif decision == '2':
            filter_options = ["\nFilter by Status:","1. Available","2. Ordered","3. Backorder","4. Delivered"]
            PrintWithColor("Action", "\n".join(filter_options))
            statuses = {"1": "available", "2": "ordered", "3": "backorder", "4": "delivered"}
            filter_decision = input("\nEnter here: ")
            if filter_decision not in statuses:
                PrintWithColor("Invalid", "Invalid input") 
                continue
            {"1": displayData,
             "2": displayData,
             "3": displayData,
             "4": displayData}[filter_decision](interface.ViewByStatus(statuses[filter_decision]))
        elif decision == '3': OrderMenu()
        elif decision == '4':
            if not isinstance(interface, AdminInterface):
                break
        else: return

def AddCustomer():
    PrintWithColor("Important", "\nEnter customer details\n")
    fn = input('First Name: ')
    ln = input('Last Name: ')
    email = input('Email address: ')
    cc = input('Credit Card #: ')
    add = input('Home address: ')
    # validate input
    customer = interface.AddCustomer(fn, ln, cc, email, add)
    PrintWithColor('Success',f"\nAdded {customer} with success")
    return customer

def RemoveCustomer():
    cust_to_delete = SelectObject(interface.customers)
    # PrintWithColor("Warning", f"\nAre you sure you want to delete {cust_to_delete}")
    # confirm = input("\nEnter [y/n]: ")
    # if confirm.lower() not in {"y", "yes"}: return
    interface.RemoveCustomer(cust_to_delete)
    PrintWithColor("Success", "Removed customer successfully")

def PickIndex(arr):
    arr_len = len(arr) - 1
    while True:
        print(arr)
        PrintWithColor('Action', '\nPick index from the dislayed list above\n')
        idx = input(f"\nEnter index [0-{arr_len}]: ")
        if not idx.isnumeric():
            PrintWithColor('Invalid',f"Invalid index! Must be a number")
            continue
        idx = int(idx)
        if idx < 0 or idx > arr_len:
            PrintWithColor('Invalid',f"Invalid index! Must be greater than 0 AND smaller than maximum length")
            continue
        return idx

def SelectObject(obj_arr):
    idx = PickIndex(obj_arr)
    obj = obj_arr[idx]
    PrintWithColor('Success',f"\n{obj}")
    return obj

def OrderMenu():
    print('\nORDER MENU')
    options = ["\nWhat would you like to do?","1. Add order","2. Remove order","3. View order details","Type 'q' to go back to main menu"]
    str_options = "\n".join(options)
    while True:
        print('Current Orders:\n')
        displayData(interface.orders)
        PrintWithColor("Action", str_options)
        action = input("\nEnter action: ")

        if action not in {"1", "2", "3"}: 
            PrintWithColor('Invalid', 'Invalid choice')
            break

        if action == "1":            
            car_to_order = SelectObject(interface.inventory)
            PrintWithColor('Important', "\nYou are about to order this car:")
            print(car_to_order)
            confirm = input("Enter y/n: ")
            if confirm not in {"yes", "y", "Y"}: break
            new_customer = input("\nEnter 'yes' if this order is for a new Customer: ")

            customer = None
            if new_customer == 'yes':
                customer = AddCustomer()
            else:
                customer = SelectObject(interface.customers)
            PrintWithColor("Success",interface.MakeOrder(customer, car_to_order))
        elif action == "2":
            order_to_remove = SelectObject(interface.orders)
            interface.UndoOrder(order_to_remove)
        elif action == "3":
            if not interface.orders:
                print("None to show")
                continue
            order_to_view = SelectObject(interface.orders)
            PrintWithColor("Success",f"\nCar details:\n{order_to_view.car.Details()}\n\nCustomer details:\n{order_to_view.buyer.Details()}\n")
            
def ManageCustomersMenu():
    options = ["1. View Customer details","2. Add Customer", "3. Remove Customer"]
    str_opt = "\n".join(options)
    while True:
        print("\nCustomer list\n")
        displayData(interface.customers)
        print(f"\nWhat would you like to do?\n{str_opt}")
        action = input("\nEnter Action here: ")
        if action not in {"1","2","3"}:
            PrintWithColor("Invalid", "Invalid option!")
            break
        if action == "1":
            customer = SelectObject(interface.customers)
            print(customer.Details())
        elif action == "2":
            AddCustomer()
        elif action == "3":
            RemoveCustomer()

def ManageEmployees():
    # display employees
    # ask add/remove and handle it
    pass

def CarSalesMenu():
    pass

def menu():
    global user
    global interface

    user = LoginPage()
    if not user: return
    
    options = ["1. Customer Orders","2. Car Sales","3. Search Cars","4. Manage Customers"]
    
    if isinstance(user, Employee): interface = Interface()
    else: 
        interface = AdminInterface()
        options.append("5. Add/Remove Employees")

    opt_str = "\n".join(options)
    while True:
        PrintWithColor('Action','\nWhat do you wish to do?\n')
        print(opt_str)
        PrintWithColor('Warning','\nType any key (besides the options) to log off')
        decision = input('Enter choice here: ')
        if not decision in {"1","2","3","4","5"}: break

        {"1": OrderMenu,
         "2": CarSalesMenu,
         "3": InventoryMenu,
         "4": ManageCustomersMenu,
         "5": ManageEmployees}[decision]()
    
    # interface.LogOut()

if __name__ == "__main__":
    menu() # gkubach0 2nBztx3qzXV
    
