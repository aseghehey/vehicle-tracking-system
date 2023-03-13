from datetime import date
class User():
    def __init__(self, username='', password='', first_name='',last_name='', date_joined=None) -> None:
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        if not date_joined: date_joined = date.today()
        self.date_joined = date_joined

    def changePassword(self, newpassword):
        # MAYBE add verifiers? 
        self.password = newpassword
    
    def changeUserName(self, newusername):
        # MAYBE check if username already exists
        self.username = newusername

    def __str__(self):
        return f"User {self.first_name} {self.last_name} Joined in {self.date_joined}"

class Admin(User):
    def addInventory(vehicle) -> None:
        pass
    
    def removeInventory(vehicle) -> None:
        pass

    def __str__(self):
        return f"Admin {self.first_name} {self.last_name} Joined in {self.date_joined}"

class Customer(User):
    def __init__(self, vehicles=[], username='', password='', first_name='',last_name='', date_joined=None):
        self.vehicle_list = vehicles
        super().__init__(username, password, first_name, last_name, date_joined)

    def order(self,vehicle) -> None:
        # set vehicle status to ordered
        self.vehicle_list.append(vehicle)

    def __str__(self):
        return f"Customer {self.first_name} {self.last_name} Joined in {self.date_joined}"
