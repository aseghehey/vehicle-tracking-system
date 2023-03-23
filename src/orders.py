from datetime import date
import random
from status import *
class Order():
    def __init__(self, car=None, buyer=None, dateBought=None) -> None:
        self.id = random.randint(1, 1000)
        if car: car.SetStatus('ordered')
        self.car = car
        self.buyer = buyer
        if not dateBought: dateBought = date.today()
        self.when = dateBought

    def RemoveOrder(self):
        self.buyer.orders.remove(self)
        self.car.SetStatus(Status.AVAILABLE)
    
    def __str__(self):
        return f"Order #{self.id}: {self.car.info['make']} {self.car.info['model']} for {self.buyer.ln}, {self.buyer.fn}"
    
    def __repr__(self) -> str:
        return f" {self.buyer.fn}'s: {self.car.info['make']} {self.car.info['model']}"
    
    def __eq__(self, value) -> bool:
        if isinstance(value, Order):
            return value.id == Order.id
        return False
