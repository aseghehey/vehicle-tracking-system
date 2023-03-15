from interface import *
from session import Auth

def login_page():
    print('Welcome to PigeonBOX')
    user, attempt = None, 0
    while (user is None and attempt < 3):
        attempt+=1
        usr_name = input("\nEnter username: ")
        pwd = input("Enter password: ")
        user = Auth().authenticate(usr_name, pwd)

    if not user: 
        print('\nFailed all 3 attempts, sorry')
        return
    
    print(f'\nHi {user.first_name} you have successfully logged in')
    return user

def inventory_menu(interface):
    print('in inv')
    pass

def order_menu(interface):
    print('in order')
    pass

def employee_menu(interface):
    print('in emp')
    pass

def menu():
    user = login_page()
    if not user: return
    
    interface = None
    options = "1. View Inventory\n2. View Orders"
    if isinstance(user, Employee): interface = Interface()
    else: 
        interface = AdminInterface()
        options += '\n3. Add/Remove Employees'
    
    while True:
        print('\nWhat do you wish to do?')
        print(options)
        print('\nType "q" if you want to exit')
        decision = input('Enter choice here: ')
        if decision == 'q': break
        # employee cannot view employee list - change later
        {"1": inventory_menu,
         "2": order_menu,
         "3": employee_menu}[decision](interface)
    
if __name__ == "__main__":
    menu() # gkubach0 2nBztx3qzXV
    
