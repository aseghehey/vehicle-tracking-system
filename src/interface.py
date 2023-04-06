# keep list of admins, customers, cars and where they are etc...
from read_write_json import *
from status import *
from users import *
from orders import *
from session import Session, EndSession

class Interface():
    def __init__(self):
        self.inventory = LoadInventory()
        self.customers = LoadCustomers()
        self.employees = Session().ReturnEmployees()
        self.admins = Session().ReturnAdmins()
        self.__users__ = self.employees + self.admins
        self.orders = loadOrders() # LoadOrders() # have to pass customers and car functionality to correctly add to buyers list and such
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
    
    def MakeOrder(self, customer, vehicle, emp):
        # check that a vehicle is available before making an order
        if not vehicle.isAvailable(): return
        # grab new id which is the length of the orders list + 1
        id = len(self.orders) + 1
        order = Order(id, vehicle, customer, employee=emp) # create order object
        # add order to order list and deal with the customer dependency
        self.orders.append(order)
        customer.orders.append(order)
        self.updates[1] = True # to write to json -- orders have been updated
        return order
    
    def UndoOrder(self, order):
        # will remove an order from the orders list and update the car status
        # also removes order from the users.orders list
        self.orders.remove(order)
        order.RemoveOrder()
        del order # delete order object and free up memory
    
    def ViewInventory(self):
        return self.inventory
    
    def searchInventory(self, model, make, year):
        """ Given relevant info, finds and returns a car object"""
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
        
    def AddCustomer(self, first, last, card, email, address):
        id = len(self.customers) + 1
        new_customer = Customer(first, last, card, email, address, id)
        self.customers.append(new_customer)
        return new_customer

    def RemoveCustomer(self, customer):
        """delete from orders if they exist AND set car to available if customer has been deleted """
        # grab customer orders
        customer_orders = []
        for order in self.orders:
            if order.buyer == customer:
                customer_orders.append(order)
                if order.car.status != Status.ORDERED: # if car has already been delivered
                    order.car.setStatus('backorder')
        # delete orders for customers:
        while customer_orders:
            order = customer_orders.pop()
            self.UndoOrder(order)
        # delete customer
        self.customers.remove(customer)
        del customer

    def LogOut(self):
        close = EndSession(self.updates, inventory=self.inventory, orders=self.orders)
        close.Terminate()

class AdminInterface(Interface):
    """ Admin can do everything an employee can do and MORE, hence why it has its own class, which inherits all the methods from Interface
        but an admin can add and remove employees, and add and remove cars from inventory """
    def UserExists(self, employee):
        """ Useful for when we want to add or remove an employee"""
        for usr in self.__users__:
            if usr == employee:
                return True
        return False

    def addAdmin(self, usrname, passwd, fname, lname, djoined=None):
        self.updates[2] = True
        new_admin = Admin(usrname, passwd, fname, lname)
        if self.UserExists(new_admin):
            return False
        self.admins.append(new_admin)
        return True

    """ Modifying the employee list functions"""
    def AddEmployee(self, usrname, passwd, fname, lname, djoined=None) -> None:
        self.updates[2] = True # to write to json -- employees have been updated
        new_employee = Employee(usrname, passwd, fname, lname)
        if self.UserExists(new_employee):
            return False
        self.employees.append(new_employee)
        return True

    def RemoveUser(self, usr_to_remove) -> bool:
        self.updates[2] = True # to write to json -- employees have been updated
        if not self.UserExists(usr_to_remove):
            return False
        
        if (isinstance(usr_to_remove, Admin)):
            self.admins.remove(usr_to_remove)
        else:
            self.employees.remove(usr_to_remove)
        self.__users__.remove(usr_to_remove)
        return True

    def AddInventory(self, v, info, performance, design, handling, comfort, entertainment, protection, package, price) -> bool:
        new_car = Car(vin=v, info=info, performance=performance, design=design, handling=handling, comfort=comfort, entertainment=entertainment, protection=protection, package=package, price=price)
        # check if the car already exists, if so, return False meaning do not add to inventory
        if self.inInventory(new_car): return False 
        self.inventory.append(new_car) # add to inventory
        self.updates[0] = True # to write to json -- inventory has been updated
        return True # meaning that the car was sucessfully added

    def RemoveInventory(self, car) -> bool:
        if not self.inInventory(car):
            return False
        # check if car is ordered and remove it from orders 
        if car.status == Status.ORDERED:
            current_order = None
            for order in self.orders:
                if order.car == car: # grab current order because the UndoOrder function takes in an order object
                    current_order = order
                    break
            if current_order: self.UndoOrder(current_order)
        # remove car from inventory
        self.inventory.remove(car)
        self.updates[0] = True # to write to json
        return True

    def LogOut(self):
        close = EndSession(self.updates, inventory=self.inventory, orders=self.orders, users=self.__users__)
        close.Terminate()


