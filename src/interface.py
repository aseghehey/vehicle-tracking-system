"""
####################################################################################################################
[replace text and delete in bracket]
PROGRAM interface:  load users, inheritance, info as dict param in Car

PROGRAMMER: Emanuel Aseghehey [email]

VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION 1.1: 14 March 2023 by E. Aseghehey to add system, orderes and more functionality


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
# keep list of admins, customers, cars and where they are etc...
from read_write_json import *
from status import *
from orders import *

class Session(object):
    def __init__(self):
        self.inventory = loadInventory()
        self.orders = loadOrders()
        
    def inInventory(self, vehicle):
        for v in self.inventory:
            if v == vehicle:
                return True
        return False 
    
    def viewOrders(self):
        for order in self.orders:
            print(order)
    
    def viewStatus(self, status):
        if (status.lower() == 'available'):
            self.viewAvailableInventory()
            return
        stat = {'backorder': Status.BACKORDER, 'delivered': Status.DELIVERED}[status.lower()]
        i = 0
        for car in self.inventory:
            if car.status == stat:
                i += 1
                print(car)
        if i == 0: print('None to show')

    def available(self, vehicle):
        return vehicle.status == Status.AVAILABLE
    
    def makeOrder(self, user, vehicle):
        order = Order(vehicle, user)
        self.orders.append(order)
        return order
    
    def viewInventory(self):
        print('Current cars on the inventory\n')
        for v in self.inventory:
            print(v)
    
    def viewAvailableInventory(self):
        print('Available inventory\n')
        for v in self.inventory:
            if v.status == Status.AVAILABLE:
                print(v)
    
    def logOut(self):
        """ Write changes to inventory, orders and users """
        pass

    # at end of session, update inventory -> write json


#  Testing 
<<<<<<< HEAD
'''
s = System()
c, a = loadUsers()
print(c[0])
print(s.isUser(a[-1]))
'''
=======
if __name__ == "__main__":
    pass
    # sesh = Session()
    # sesh.viewInventory()
>>>>>>> fbd9dbd (deleted customer and worked on interface)
