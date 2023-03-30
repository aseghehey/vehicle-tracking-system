from datetime import date
import random
from status import *
class Order():
    """ Class represents orders made, works like a database one-to-one relationship with a buyer and a car"""
    def __init__(self, id, car=None, buyer=None, dateBought=None) -> None:
        self.id = id # works like the primary key in a database
        if car: car.SetStatus('ordered')  #  set car status to ordered
        # Car and Customer objects
        self.car = car
        self.buyer = buyer
        # if a date is not specified, it will be set to today's date
        if not dateBought: dateBought = date.today()
        self.when = dateBought

    def RemoveOrder(self):
        """ Removes the order from the buyer's orders list and sets the car status to available"""
        self.buyer.orders.remove(self)
        self.car.SetStatus("available")
    
    def __str__(self):
        return f"Order #{self.id}: {self.car.info['make']} {self.car.info['model']} for {self.buyer.ln}, {self.buyer.fn}"
    
    def __repr__(self) -> str:
        return f" {self.buyer.fn}'s: {self.car.info['make']} {self.car.info['model']} {self.car.status}"
    
    """ Overriding the equality operator to compare two Order objects"""
    def __eq__(self, value) -> bool:
        if isinstance(value, Order):
            return value.id == self.id
        return False
