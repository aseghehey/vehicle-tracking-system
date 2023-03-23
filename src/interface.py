# keep list of admins, customers, cars and where they are etc...
from read_write_json import *
from status import *
from user import *
from orders import *
from session import Session, EndSession
from typing import Type
class Interface:
    def __init__(self):
        self.inventory = loadInventory()
        self.orders = loadOrders()
        self.updates = [False, False, False]
        
    def inInventory(self, vehicle):
        for v in self.inventory:
            if v == vehicle:
                return True
        return False 
    
    def viewByStatus(self, status):
        if (status.lower() == 'available'):
            return self.viewAvailableInventory()

        stat = {'ordered': Status.ORDERED, 'backorder': Status.BACKORDER, 'delivered': Status.DELIVERED}[status.lower()]
        by_status = []
        for car in self.inventory:
            if car.status == stat:
                by_status.append(car)
        return by_status
    
    def makeOrder(self, user, vehicle):
        if not vehicle.isAvailable(): return
        order = Order(vehicle, user)
        self.orders.append(order)
        self.updates[1] = True
        return order
    
    def viewInventory(self):
        return self.inventory
    
    def searchInventory(self, model, make, year):
        for car in self.inventory:
            info = car.info
            if model == info['model'] and make == info['make'] and year == info['year']:
                return car
        return
    
    def printCarInfo(self, vehicle):
        info = vehicle.info
        print()
        print(vehicle)
        print(f"VIN: {vehicle.vin}\nYear: {info['year']}\nMileage: {info['mileage']} mi")
        print(f"\nEngine: {vehicle.performance['engine']} and {vehicle.performance['transmission']} transmission")

    
    def viewAvailableInventory(self):
        avail = []
        for v in self.inventory:
            if v.status == Status.AVAILABLE:
                avail.append(v)
        return avail
    
    def logOut(self):
        close = EndSession(self.updates, inventory=self.inventory, orders=self.orders)
        close.terminate()

class AdminInterface(Interface):
    def __init__(self, users):
        super().__init__()
        self.__usrs__ = Session.returnEmployees()
    
    def addInventory(self) -> None:
        pass
    
    def removeInventory(self) -> None:
        pass

    def addEmployee(self) -> None:
        self.updates[2] = True
        pass

    def removeEmployee(self, usr_to_remove) -> None:
        self.updates[2] = True
        pass

    def logOut(self):
        close = EndSession(self.updates, inventory=self.inventory, orders=self.orders, users=self.__usrs__)
        close.terminate()


