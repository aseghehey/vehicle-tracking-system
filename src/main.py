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

def PrintFormat(color_status, print_info):
    color_options = {"Invalid": bcolors.FAIL, "Success": bcolors.OKGREEN, "Action": bcolors.OKBLUE, "Important": bcolors.BOLD, "Warning": bcolors.WARNING}
    color_status = color_options[color_status]
    print(f"{color_status}{print_info}{bcolors.ENDC}")

''' Command line interface '''
def displayData(data):
    if not AvailableToShow(data): return
    for i, val in enumerate(data):
        print(f"{i}: {val}")

def ChangePassword():
    new_password = ValidateUserInput('new password')
    if new_password == user.password:
        PrintFormat("Invalid", "New password cannot be the same as old password")
        return
    user.UpdatePassword(new_password)
    PrintFormat("Success", "Password changed successfully")

def ChangeUsername():
    new_username = ValidateUserInput('new username')
    if new_username == user.username:
        PrintFormat("Invalid", "New username cannot be the same as old username")
        return
    
    for usr in interface.ViewUsers():
        if usr.username == new_username:
            PrintFormat("Invalid", "Username already taken")
            return
    user.UpdateUserName(new_username)
    PrintFormat("Success", "Username changed successfully")

def CarSearch() -> None:
    print('\nSearch car in inventory')
    search_decision = input("Enter model, make and year separated by commas\n")
    search_decision = list(map(lambda x: x.strip(), search_decision.split(',')))

    if len(search_decision) != 3: 
        PrintFormat('Invalid', '\nCar not found, make sure you entered the correct model, make and year')
        return

    model, make, year = search_decision[0], search_decision[1], search_decision[2]
    # validate input
    if not year.isnumeric(): 
        print('\nInvalid input')
        return

    car = interface.searchInventory(model, make, int(year))
    # check car exists
    if not car: 
        print('\nNo car match given criteria')
        return
    
    PrintFormat('Success', f"\nCar details:\n{car.Details()}")

def Stall():
    _ = input("\nPress enter to continue\n")

def ValidateUserInput(action="action"):
    usr_input = input(f"Enter {action}: ")
    while not usr_input:
        PrintFormat("Invalid", "Bad input")
        usr_input = input(f"Enter valid {action}: ")
    return usr_input

def AddCustomer():
    PrintFormat("Important", "\nEnter customer details\n")
    fn = ValidateUserInput("First Name")
    ln = ValidateUserInput("Last Name")
    email = ValidateUserInput("email")
    cc = input('Credit Card #: ')
    # validate credit card
    while len(cc) != 16:
        PrintFormat("Invalid", "Credit card # needs 16 digits and needs to be numbers only")
        cc = input('Credit Card #: ')
        if not cc.isnumeric():
            continue

    add = ValidateUserInput("Home address")
    customer = interface.AddCustomer(fn, ln, cc, email, add)
    PrintFormat('Success',f"\nAdded {customer} with success")
    return customer

def ConfirmSelection(response = {"y", "yes"}, msg="") -> bool:
    if not msg: msg = "\nAre you sure you want to proceed?\n"
    PrintFormat("Warning", msg)
    confirm = input("Enter [y/n] to confirm: ")
    if confirm.lower() not in response:
        PrintFormat("Success", "OK")
        return False
    return True

def RemoveCustomer():
    if not interface.customers:
        PrintFormat("Invalid", "No Available Customer to display")
        return
    cust_to_delete = SelectObject(interface.customers)
    if not ConfirmSelection(msg=f"\nAre you sure you want to delete {cust_to_delete}"): return
    interface.RemoveCustomer(cust_to_delete)
    PrintFormat("Success", "Removed customer successfully")

def PickIndex(arr):
    arr_len = len(arr) - 1
    while True:
        displayData(arr)
        PrintFormat('Action', '\nPick index from the dislayed list above\n')
        idx = input(f"\nEnter index [0-{arr_len}] OR enter 'q' to exit: ")
        if idx == 'q': return
        if not idx.isnumeric():
            PrintFormat('Invalid',f"Invalid index! Must be a number")
            continue
        idx = int(idx)
        if idx < 0 or idx > arr_len:
            PrintFormat('Invalid',f"Invalid index! Must be greater than 0 AND smaller than maximum length")
            continue
        return idx

def SelectObject(obj_arr):
    idx = PickIndex(obj_arr)
    if not idx: return
    obj = obj_arr[idx]
    PrintFormat('Success',f"\n{obj}")
    return obj

def AvailableToShow(arr):
    if not arr:
        PrintFormat("Invalid","None available to display")
        return False
    return True

''' Menus '''
def LoginPage():
    print('Welcome to PigeonBOX')
    user, attempt = None, 0
    while (user is None and attempt < 3):
        attempt+=1
        # usr_name = input("\nEnter username: ")
        # pwd = input("Enter password: ")
        # Admin: crapinett1 KcZy6yQfn
        usr_name = "crapinett1"
        pwd = "KcZy6yQfn"
        user = Auth().Authenticate(usr_name, pwd)

    if not user: 
        print('\nFailed all 3 attempts, sorry')
        return
    
    PrintFormat("Success",f'\nHi {user.first_name} you have successfully logged in')
    return user

def InventoryMenu():
    print('\nCars in the inventory')

    inventory = interface.ViewInventory()
    options = ["1. Search","2. Filter by", "3. Make a customer order"]
    if isinstance(interface, AdminInterface): 
        options.append("4. Add/Remove Cars")

    options.append("Type 'q' to exit inventory menu")
    opt_str = "\n" + "\n".join(options)

    while True:
        displayData(inventory)
        PrintFormat("Action", opt_str)
        decision = input("Enter action: ")
        if decision not in {"1", "2", "3", "4"}: return
        if decision == '1':
            CarSearch()
        elif decision == '2':
            filter_options = ["\nFilter by Status:","1. Available","2. Ordered","3. Backorder","4. Delivered"]
            PrintFormat("Action", "\n".join(filter_options))
            statuses = {"1": "available", "2": "ordered", "3": "backorder", "4": "delivered"}
            filter_decision = input("\nEnter here: ")
            # validate input
            if filter_decision not in statuses:
                PrintFormat("Invalid", "Invalid input") 
                continue
            {"1": displayData,
             "2": displayData,
             "3": displayData,
             "4": displayData}[filter_decision](interface.ViewByStatus(statuses[filter_decision]))
        elif decision == '3': OrderMenu()
        elif decision == '4':
            if not isinstance(interface, AdminInterface):
                break
            #TODO: add/remove cars
            PrintFormat("Important", "\n1. Add car\n2. Remove car")
            add_remove = input("\nEnter here: ")
            if add_remove == '1': AddCar()
            elif add_remove == '2': RemoveCar()
        Stall()

def InputToArr(inpt):
    inpt = inpt.split(',')
    inpt = list(map(lambda x: x.strip(), inpt))
    return inpt

def AddCar():
    vin = input("Enter new car's VIN: ")
    make_model_year = None
    while True:
        make_model_year = InputToArr(input("Enter make, model, year (Separated by commas): "))
        if len(make_model_year) != 3:
            PrintFormat("Invalid", "Make, Model, Year must be separated by a comma")
            continue
        if not make_model_year[2].isnumeric():
            PrintFormat("Invalid", "Year has to be a number")
            continue
        break
    mileage_color = None
    while True:
        mileage_color = InputToArr(input("Enter mileage, color (Separated by commas): "))
        if len(mileage_color) != 2:
            PrintFormat("Invalid", "Mileage and Color must be separated by a comma")
            continue
        if not mileage_color[0].isnumeric():
            PrintFormat("Invalid", "Mileage has to be a number")
            continue
        if not mileage_color[1].isalpha():
            PrintFormat("Invalid", "Color has to be a string")
            continue
        break
    price = input("Enter price: ")
    while not price.isnumeric():
        price = input("HAS TO BE NUMERIC! Enter price: ")
    price = int(price)
    engine_transmission = None
    while True:
        engine_transmission = InputToArr(input("Enter engine, transmission (Separated by commas): "))
        if len(engine_transmission) != 2:
            PrintFormat("Invalid", "Engine and Transmission must be separated by a comma")
            continue
        break
    interior_external_design =None
    while True:
        interior_external_design = InputToArr(input("Enter interior, external design (Separated by commas): "))
        if len(interior_external_design) != 2:
            PrintFormat("Invalid", "Interior and External Design must be separated by a comma")
            continue
        break

    handling = input("Enter handling: ")
    audio = input("Enter audio: ")
    comfort = input("Enter comfort features: ")
    package = input("Enter package: ")
    warranty_maintenance = None
    while True:
        warranty_maintenance = InputToArr(input("Enter warranty, maintenance (Separated by commas): "))
        if len(warranty_maintenance) != 2:
            PrintFormat("Invalid", "Warranty and Maintenance must be separated by a comma")
            continue
        break

    info = {"model": make_model_year[1],
            "make": make_model_year[0],
            "mileage": int(mileage_color[0]),
            "year": int(make_model_year[-1]),
            "color": mileage_color[-1],}
    
    performance = {"engine": engine_transmission[0],
                   "transmission": engine_transmission[-1]}
    
    design = {"interior": interior_external_design[0],
              "exterior": [{"extra": interior_external_design[-1]}]}
    
    protection = {"maintenance": warranty_maintenance[1], "warranty": warranty_maintenance[0]}
    add = interface.AddInventory(vin, info=info, performance=performance,comfort=comfort, design=design, protection=protection, price=price, handling=handling, package=package, entertainment=audio)    

    if add:
        PrintFormat("Success", "Car successfully added")
    else:
        PrintFormat("Invalid", "Car already exists")

def RemoveCar():
    if not interface.inventory:
        PrintFormat("Invalid", "No cars in inventory")
        return
    car_to_delete = SelectObject(interface.inventory)
    if not ConfirmSelection(msg=f"\nAre you sure you want to delete {car_to_delete}"): return
    rem = interface.RemoveInventory(car_to_delete)
    if rem:
        PrintFormat("Success", "Removed car successfully")
    else:
        PrintFormat("Invalid", "Car not found")
    

def OrderMenu():
    print('\nORDERS MENU')
    options = ["\nWhat would you like to do?","1. Add order","2. Remove order","3. View order details","Type 'q' to go back to main menu"]
    str_options = "\n".join(options)

    while True:
        print('Current Orders:\n')
        displayData(interface.orders)
        PrintFormat("Action", str_options)
        action = input("\nEnter action: ")

        if action not in {"1", "2", "3"}: 
            PrintFormat('Invalid', 'Invalid choice')
            break

        if action == "1":            
            car_to_order = SelectObject(interface.inventory)
            if not car_to_order: break
            PrintFormat('Important', "\nYou are about to order this car:")
            print(car_to_order)
            if not ConfirmSelection(): break
            # check new customer
            customer = None
            if ConfirmSelection(msg="Is this order for a new customer?"):
                customer = AddCustomer()
            else:
                customer = SelectObject(interface.customers)
                if not customer: break
            customer = interface.MakeOrder(customer, car_to_order)
            if not customer:
                PrintFormat("Invalid", "Failed to make order. This car has already been ordered by someone else.")
                break
            PrintFormat("Success", customer)
        else:
            # checker for empty orders
            if AvailableToShow(interface.orders): 
                if action == "2":
                    order_to_remove = SelectObject(interface.orders)
                    if not order_to_remove: break
                    interface.UndoOrder(order_to_remove)
                else:
                    order_to_view = SelectObject(interface.orders)
                    if not order_to_remove: break
                    PrintFormat("Success",f"\nCar details:\n{order_to_view.car.Details()}\n\nCustomer details:\n{order_to_view.buyer.Details()}\n")
        Stall()
                
def ManageCustomersMenu():
    options = ["1. View Customer details","2. Add Customer", "3. Remove Customer"]
    str_opt = "\n".join(options)
    while True:
        print("\nCustomer list\n")
        displayData(interface.customers)
        PrintFormat("Action",f"\nWhat would you like to do?\n{str_opt}")
        # validate input
        action = input("\nEnter action: ")
        if action not in {"1","2","3"}:
            PrintFormat("Invalid", "Invalid option!")
            break
        
        if action == "2":
            AddCustomer()
        else:
            if AvailableToShow(interface.customers): 
                if action == "1":
                    customer = SelectObject(interface.customers)
                    if not customer: break
                    print(customer.Details())
                else:
                    RemoveCustomer()
        Stall()

def ManageEmployees():
    # display employees
    # ask add/remove and handle it
    pass

def CarSalesMenu():
    # display orders
    # Set order statuses to delivered 
    pass

def AccountSettings():
    options = ["1. Change password","2. Change username", "3. View Account Details","Press any other key to go back"]
    str_opt = "\n".join(options)

    while True:
        print("\nAccount settings\n")
        PrintFormat("Action",f"\nWhat would you like to do?\n{str_opt}")
        # validate input
        action = input("Enter action: ")
        if action not in {"1","2", "3"}:
            PrintFormat("Invalid", "Invalid option!")
            break

        if action == "1":
            ChangePassword()
        elif action == "2":
            ChangeUsername()
        else:
            print(f"\nUser {user.username} details:\n{user}")
        Stall()

def menu():
    global user
    global interface

    user = LoginPage()
    if not user: return
    
    options = ["1. Customer Orders","2. Car Sales","3. Search Cars","4. Manage Customers"]
    
    if isinstance(user, Employee): 
        interface = Interface()
    else: 
        interface = AdminInterface()
        options.append("5. Manage Employees")

    options.append("\nA: Account settings")
    opt_str = "\n".join(options)

    while True:
        PrintFormat('Action','\nWhat do you wish to do?\n')
        print(opt_str)
        PrintFormat('Warning','\nType any key (besides the options) to log off')

        decision = input('Enter choice here: ')
        if not decision in {"1","2","3","4","5", "A"}: break

        {"1": OrderMenu,
         "2": CarSalesMenu,
         "3": InventoryMenu,
         "4": ManageCustomersMenu,
         "5": ManageEmployees,
         "A": AccountSettings}[decision]()
    
    # interface.LogOut()

if __name__ == "__main__":
    menu() 
    # Employee: gkubach0 2nBztx3qzXV
    # Admin: crapinett1 KcZy6yQfn