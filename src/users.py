import datetime
class Users():
    def __init__(self, username='', password='', first_name='',last_name='', date_joined=None) -> None:
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        # if not date_joined:  
        self.date_joined = date_joined

class Admin(Users):
    def addInventory(vehicle) -> None:
        pass
    def removeInventory(vehicle) -> None:
        pass

class Customer(Users):
    # keeps a list of ordered vehicles
    def order(vehicle) -> None:
        pass
