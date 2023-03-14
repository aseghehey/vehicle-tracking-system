# keep list of admins, customers, cars and where they are etc...
from read_write_json import *

class System(object):
    def __init__(self):
        self.inventory = loadInventory()
        self.customers, self.admins = loadUsers(self)
        self.orders = loadOrders()
        
        # not sure if necessary
        self.all_users = self.customers
        self.all_users.extend(self.admins)
        
    def inInventory(self, vehicle):
        for v in self.inventory:
            if v == vehicle:
                return True
        return False 

    def available(self, vehicle):
        return vehicle.status == Status.AVAILABLE
    
    def makeOrder(self, user, vehicle):
        order = Order(vehicle, user)
        self.orders.append(order)
        return order
    
    def logOut(self):
        """ Write changes to inventory, orders and users """
        pass

    # at end of session, update inventory -> write json

#  Testing 
'''
s = System()
c, a = loadUsers()
print(c[0])
print(s.isUser(a[-1]))
'''