from datetime import date
import random
class Order():
    def __init__(self, car=None, buyer=None, dateBought=None) -> None:
        self.id = random.randint(1, 1000)
        if car: car.setStatus('ordered')
        self.car = car
        self.buyer = buyer
        if not dateBought: dateBought = date.today()
        self.when = dateBought
    
    def __str__(self):
        return f"Order {self.id} by {self.buyer.username}"
