from datetime import date
import random
from status import *
from vehicles import *
from user import *
class Order():
    def __init__(self, car=None, buyer=None, dateBought=None) -> None:
        self.id = random.randint(1, 1000)
        self.car = Car(car)
        #car.setStatus('ordered')
        self.buyer = buyer
        if not dateBought: dateBought = date.today()
        self.when = dateBought

    def to_dict(self):
        return {
            "id": self.id,
            "car": self.car,
            "buyer": self.buyer,
            "when": self.when
        }

    def serialize(order):
        if isinstance(order, Order):
            return order.to_dict()
        raise TypeError("Object of type 'Order' is not JSON serializable")

    def remOrder(self):
        self.car.setStatus(Status.AVAILABLE)
    
    def __str__(self):
        return f"Order #{self.id} by {self.buyer}"
