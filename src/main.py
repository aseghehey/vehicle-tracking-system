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

def print_with_colors(color_status, print_info):
    color_options = {"Invalid": bcolors.FAIL, "Success": bcolors.OKGREEN, "Action": bcolors.OKBLUE, "Important": bcolors.BOLD, "Warning": bcolors.WARNING}
    color_status = color_options[color_status]
    print(f"{color_status}{print_info}{bcolors.ENDC}")

''' Command line interface '''
def login_page():
    print('Welcome to PigeonBOX')
    user, attempt = None, 0
    while (user is None and attempt < 3):
        attempt+=1
        # usr_name = input("\nEnter username: ")
        # pwd = input("Enter password: ")
        usr_name = "gkubach0"
        pwd = "2nBztx3qzXV"
        user = Auth().authenticate(usr_name, pwd)

    if not user: 
        print('\nFailed all 3 attempts, sorry')
        return
    
    print(f'\nHi {user.first_name} you have successfully logged in')
    return user

def displayData(data):
    if not data:
        print_with_colors("Warning",'No matches for given criteria')
        return

    for i, val in enumerate(data):
        print(f"{i + 1}: {val}")

def car_search(interface) -> None:
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
    interface.printCarInfo(car)
    #TODO
    # finish orders
    # make_order()

def inventory_menu():
    print('\nCars in the inventory')

    inventory = interface.viewInventory()
    displayData(inventory)

    options = ["1. Search","2. Filter by", "3. Make a customer order"]
    if isinstance(interface, AdminInterface): 
        options.append("4. Add/Remove Cars")

    options.append("Type 'q' to exit inventory menu")
    opt_str = "\n" + "\n".join(options)

    while True:
        print_with_colors("Action", opt_str)
        decision = input("Enter action: ")
        if decision == '1':
            car_search(interface)
        elif decision == '2':
            filter_options = ["\nFilter by Status:","1. Available","2. Ordered","3. Backorder","4. Delivered"]
            print_with_colors("Action", "\n".join(filter_options))
            statuses = {"1": "available", "2": "ordered", "3": "backorder", "4": "delivered"}
            filter_decision = input("\nEnter here: ")
            if filter_decision not in statuses:
                print_with_colors("Invalid", "Invalid input") 
                continue
            {"1": displayData,
             "2": displayData,
             "3": displayData,
             "4": displayData}[filter_decision](interface.viewByStatus(statuses[filter_decision]))
        elif decision == '3': order_menu()
        elif decision == '4':
            if not isinstance(interface, AdminInterface):
                break
        else: return

def AddCustomer():
    print_with_colors("Important", "\nEnter customer details\n")
    fn = input('First Name: ')
    ln = input('Last Name: ')
    email = input('Email address: ')
    cc = input('Credit Card #: ')
    add = input('Home address: ')
    # validate input
    customer = interface.AddCustomer(fn, ln, cc, email, add)
    print_with_colors('Success',f"\nAdded {customer} with success")
    return customer

def order_menu():
    print('\nORDER MENU')
    print('Current Orders:\n')
    displayData(interface.orders)
    options = ["\nWhat would you like to do?","1. Add order","2. Remove order","3. View order details","Type 'q' to go back to main menu"]
    str_options = "\n".join(options)
    while True:
        print_with_colors("Action", str_options)
        action = input("\nEnter action: ")

        if action not in {"1", "2", "3"}: 
            print_with_colors('Invalid', 'Invalid choice')
            break

        if action == "1":
            print_with_colors('Action', '\nPick an index for the car you want to order')
            print(interface.inventory)
            inv_len = len(interface.inventory) - 1
            idx = input(f"\nEnter index [0-{inv_len}]: ")
            if not idx.isnumeric():
                print_with_colors('Invalid', 'Input must be a number')
                break
            idx = int(idx)
            if idx > inv_len or idx < 0:
                print_with_colors('Invalid', 'Invalid index')
                break
            
            car_to_order = interface.inventory[idx]
            print_with_colors('Important', "\nYou are about to order this car:")
            print(car_to_order)
            confirm = input("Enter y/n: ")
            if confirm not in {"yes", "y", "Y"}: break
            new_customer = input("\nEnter 'yes' if this order is for a new Customer: ")
            customer = None

            if new_customer == 'yes':
                customer = AddCustomer()
            else:
                print_with_colors('Action', '\nPick the index from the customers in the system\n')
                print(interface.customers)
                cust_len = len(interface.customers) - 1
                idx = input(f"\nEnter index [0-{cust_len}]: ")
                # validate idx
                idx = int(idx)
                customer = interface.customers[idx]
                print_with_colors('Success',f"\n{customer}")
            print('Next steps')
            
            # Make order
            
            #new customer case
            
        elif action == "2":
            # delete
            to_rem = input("\nPick index of order to remove")
            if not to_rem.isnumeric(): 
                print('Invalid option')
                break
            to_rem = int(to_rem) - 1
            #TODO
            if to_rem >= len(interface.orders):
                print_with_colors("Invalid", "Invalid index")
                break
            # interface.orders[to_rem].remOrder()
            
def employee_menu():
    print('in emp')
    pass

def add_remove_customer():
    pass

def manage_customers():
    pass

def car_sales_menu():
    pass

def menu():
    global user
    global interface

    user = login_page()
    if not user: return
    
    options = ["1. Customer Orders","2. Car Sales","3. Search Cars","4. Manage Customers"]
    if isinstance(user, Employee): interface = Interface()
    else: 
        interface = AdminInterface()
        options.append("5. Add/Remove Employees")
    
    while True:
        print('\nWhat do you wish to do?\n')
        print("\n".join(options))
        print('\nType any key (besides the options) to log off')
        decision = input('Enter choice here: ')
        if not decision in {"1","2","3","4","5"}: break
        {"1": order_menu,
         "2": car_sales_menu,
         "3": inventory_menu,
         "4": add_remove_customer,
         "5": manage_customers}[decision]()
    
    # interface.logOut()

if __name__ == "__main__":
    menu() # gkubach0 2nBztx3qzXV
    
