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
        self.orders = [] # LoadOrders() # have to pass customers and car functionality to correctly add to buyers list and such
        # for inventory, 
        self.updates = [False] * 4
        
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
        order = Order(vehicle, user)
        self.orders.append(order)
        self.customers[self.customers.index(user)].orders.append(order)
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
        pass

    def RemoveInventory(self) -> None:
        pass

    def AddCustomer(self, first, last, card, email, address):
        new_customer = Customer(first, last, card, email, address)
        self.customers.append(new_customer)
        return new_customer

    def RemoveCustomer(self, customer):
        # delete from orders if they exist
        # set car to available if customer has been deleted
        order_to_rem = None
        for order in self.orders:
            if order.buyer == customer:
                car = order.car
                if car.status == Status.ORDERED:
                    car.SetStatus('available')
                else:
                    car.SetStatus('backorder')
                order_to_rem = order
                break
        if order_to_rem: 
            self.orders.remove(order_to_rem)
            del order_to_rem
        self.customers.remove(customer)
        del customer

    def LogOut(self):
        close = EndSession(self.updates, inventory=self.inventory, orders=self.orders)
        close.Terminate()

class AdminInterface(Interface):
    def __init__(self, users):
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


