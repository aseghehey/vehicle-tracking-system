"""
####################################################################################################################
[replace text and delete in bracket]
PROGRAM [name]:  [purpose of code and function. brief]

PROGRAMMER: [firstName] [lastName] [email]

VERSION 1: written [day] [month] 2023 by [firstInitial]. [lastName]
REVISION [revision# ex: 1.1]: [day] [month] 2023 by [firstInitial]. [lastName] to [purpose of revision]


PURPOSE:
[general purpose of code and each functionality. thorough description]

DATA STRUCTURES:
[major data structures and variables]
[ex: variable LENGTH - integer]

ALGORITHM:
[brief description of logic flow]

ERROR HANDLING:
[brief description error handling]

####################################################################################################################
"""
from datetime import date
from orders import *
from status import *
class User():
    def __init__(self, username='', password='', first_name='',last_name='', date_joined=None, session=None) -> None:
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        if not date_joined: date_joined = date.today()
        self.date_joined = date_joined
        self.system = session

    def changePassword(self, newpassword):
        # MAYBE add verifiers? 
        self.password = newpassword
        print('password changed successfully')
    
    def changeUserName(self, newusername):
        # MAYBE check if username already exists
        self.username = newusername
        print('username changed successfully')
        # write username to json

    def username_to_User():
        # map to User object
        pass

    def __eq__(self, __o):
        if isinstance(__o, User) or isinstance(__o, Admin) or isinstance(__o, Customer):
            return __o.username == self.username
        
    def __str__(self):
        return f"User {self.first_name} {self.last_name} Joined in {self.date_joined}"

class Admin(User):
    # def addInventory(self) -> None:
    
    def removeInventory(self, vehicle) -> None:
        if not self.system.inInventory(vehicle) or not self.system.available(vehicle): return
        self.system.pop(vehicle)
        
    def UpdateInventory(self, vehicle):
        if not self.system.inInventory(vehicle) or not self.system.available(vehicle): return

        price_or_status = input('Would you like to update the price (input "1") or status ("2")?')
        while price_or_status not in {1,2}: 
            price_or_status = input('Would you like to update the price (input "1") or status ("2")?')
        
        if price_or_status == 1:
            newprice = input(f'Enter new price for {vehicle}')
            if newprice < 0: return
            vehicle.updatePrice(newprice)
            return
        
        new_status = input('Enter updated status (Available, Ordered, Backorder, Delivered)')
        while new_status.lower() not in {'available', 'ordered', 'backorder', 'delivered'}:
            new_status = input('Enter updated status (available, ordered, backorder, delivered)')
        vehicle.setStatus(new_status)

    def __str__(self):
        return f"Admin {self.first_name} {self.last_name} Joined in {self.date_joined}"

class Customer(User):
    def __init__(self, order=[], username='', password='', first_name='',last_name='', date_joined=None):
        self.orders = order
        super().__init__(username, password, first_name, last_name, date_joined)

    def order(self, vehicle) -> None:
        if not self.system.inInventory(vehicle) or not self.system.available(vehicle): return
        self.orders[self.system.makeOrder(self, vehicle)] # revisit...

    def __str__(self):
        return f"Customer {self.first_name} {self.last_name} Joined in {self.date_joined}"
