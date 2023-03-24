# keep list of admins, customers, cars and where they are etc...
from read_write_json import *
from status import *
from users import *
from orders import *
from session import Session, EndSession

class Interface:
    def __init__(self):
        self.inventory = LoadInventory()
        self.customers = LoadCustomers()
        self.__users__ = Session().ReturnEmployees() + Session().ReturnAdmins()
        #TODO
        self.orders = [] # LoadOrders() # have to pass customers and car functionality to correctly add to buyers list and such
        # for inventory, 
        self.updates = [False] * 4 # TODO
    
    def ViewUsers(self):
        return self.__users__
        
    def inInventory(self, vehicle):
        for v in self.inventory:
            if v == vehicle:
                return True
        return False 
    
    def ViewByStatus(self, status):
        if (status.lower() == 'available'):
            return self.ViewAvailableInventory()

        stat = {'ordered': Status.ORDERED, 'backorder': Status.BACKORDER, 'delivered': Status.DELIVERED}[status.lower()]
        by_status = []
        for car in self.inventory:
            if car.status == stat:
                by_status.append(car)
        return by_status
    
    def MakeOrder(self, user, vehicle):
        if not vehicle.isAvailable(): return
        id = len(self.orders) + 1
        order = Order(id, vehicle, user)
        self.orders.append(order)
        user.orders.append(order)
        self.updates[1] = True
        return order
    
    def UndoOrder(self, order):
        self.orders.remove(order)
        order.RemoveOrder()
    
    def ViewInventory(self):
        return self.inventory
    
    def searchInventory(self, model, make, year):
        for car in self.inventory:
            info = car.info
            if model == info['model'] and make == info['make'] and year == info['year']:
                return car
        return
    
    def ViewAvailableInventory(self):
        avail = []
        for v in self.inventory:
            if v.status == Status.AVAILABLE:
                avail.append(v)
        return avail

    def AddInventory(self) -> None:
        #TODO
        pass

    def RemoveInventory(self) -> None:
        #TODO
        pass

    def AddCustomer(self, first, last, card, email, address):
        id = len(self.customers) + 1
        new_customer = Customer(first, last, card, email, address, id)
        self.customers.append(new_customer)
        return new_customer

    def RemoveCustomer(self, customer):
        """delete from orders if they exist AND set car to available if customer has been deleted """
        order_to_rem = None
        flag = False # will tell us if order has been processed
        # check if customer has any orders
        for order in self.orders:
            if order.buyer == customer:
                if order.car.status != Status.ORDERED: 
                    flag = True
                order_to_rem = order
                break
        # delete order and update car statuses
        if order_to_rem:
            car = order_to_rem.car
            self.UndoOrder(order_to_rem)
            if flag: # if order was already processed 
                car.setStatus('backorder')
        # delete customer
        self.customers.remove(customer)
        del customer

    def LogOut(self):
        close = EndSession(self.updates, inventory=self.inventory, orders=self.orders)
        close.Terminate()

class AdminInterface(Interface):
    def __init__(self):
        super().__init__()
        self.__usrs__ = Session.ReturnEmployees()

    def AddEmployee(self) -> None:
        self.updates[2] = True
        pass

    def RemoveEmployee(self, usr_to_remove) -> None:
        self.updates[2] = True
        pass

    def LogOut(self):
        close = EndSession(self.updates, inventory=self.inventory, orders=self.orders, users=self.__usrs__)
        close.Terminate()


