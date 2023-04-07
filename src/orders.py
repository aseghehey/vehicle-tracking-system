from datetime import *
import random
from status import *
from bcolors import bcolors
from vehicles import *
import json

class Order():

    """ Class represents orders made, works like a database one-to-one relationship with a buyer and a car"""
    def __init__(self, id, car=None, buyer=None, dateBought=None, employee=None) -> None:
        self.id = id # works like the primary key in a database
        self.car = car
        if car: Car.SetStatus(car, 'ordered')  #  set car status to ordered
        # Car and Customer objects
        self.buyer = buyer #the user id
        self.salesBy = employee
        # if a date is not specified, it will be set to today's date
        if not dateBought: dateBought = date.today()
        self.when = dateBought
     

    def to_dict(self):
        return {
            "id": self.id,
            "buyer": self.buyer,
            "salesBy": self.salesBy,
            "when": self.when
        }
    
    def serialize(order):
        if isinstance(order, Order):
            return order.to_dict()
        raise TypeError("Object of type 'Order' is not JSON serializable")

    def RemoveOrder(self):
        """ Removes the order from the buyer's orders list and sets the car status to available"""
        self.buyer.orders.remove(self)
        self.car.SetStatus("available")
    
    def orderDetails(self):
        toret = f"\nCar:\n{self.car.Details()}\n\nSales by: {self.salesBy}\n\nCustomer {self.buyer.Details()}\n"
        return toret

    def __str__(self):
        salesBy = self.salesBy.__str__()
        salesBy = " ".join(salesBy.split(" ")[:3])
        return f"Order #{self.id} {bcolors.BOLD}Made by {salesBy}{bcolors.ENDC}: {self.car.info['make']} {self.car.info['model']} for {bcolors.BOLD}{self.buyer.ln}, {self.buyer.fn}{bcolors.ENDC}"
    
    # def __repr__(self) -> str:
    #     return f" {self.buyer.fn}'s: {self.car.info['make']} {self.car.info['model']} {self.car.status}"
    
    """ Overriding the equality operator to compare two Order objects"""
    def __eq__(self, value) -> bool:
        if isinstance(value, Order):
            return value.id == self.id
        return False
