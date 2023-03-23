from datetime import date
from interface import *
from orders import *
from status import *
class User():
    def __init__(self, username='', password='', first_name='',last_name='', date_joined=None) -> None:
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        if not date_joined: date_joined = date.today()
        self.date_joined = date_joined

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_joined": self.date_joined
        }


    def serialize(user):
        if isinstance(user, User):
            return user.to_dict()
        raise TypeError("Object of type 'User' is not JSON serializable")
    '''
    def changePassword(self, newpassword):
        self.password = newpassword
    
    def changeUserName(self, newusername):
        self.username = newusername
    '''
    def __eq__(self, __o):
        if isinstance(__o, User) or isinstance(__o, Admin) or isinstance(__o,Employee):
            return __o.username == self.username
        
    def __str__(self):
        return f"User {self.first_name} {self.last_name} Joined in {self.date_joined}"

class Admin(User): # can delete or add inventory, add or delete employees
    def __str__(self):
        return f"Admin {self.first_name} {self.last_name} Joined in {self.date_joined}"

class Employee(User): # manages sales and can update inventory but cannot add or delete
    def __str__(self):
        return f"Employee {self.first_name} {self.last_name} Joined in {self.date_joined}"