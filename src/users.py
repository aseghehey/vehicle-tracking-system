from datetime import date
from interface import *
from orders import *
from status import *
import bcolors
class User():
    def __init__(self, username='', password='', first_name='', last_name='', date_joined=None) -> None:
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        if not date_joined:
            date_joined = date.today()
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

    def UpdatePassword(self, newpassword):
        self.password = newpassword

    def UpdateUserName(self, newusername):
        self.username = newusername

    def __eq__(self, __o):
        if isinstance(__o, User) or isinstance(__o, Admin) or isinstance(__o, Employee):
            return __o.username == self.username

    def __str__(self):
        return f"User {self.first_name} {self.last_name} Joined in {self.date_joined}"

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Admin(User):  # can delete or add inventory, add or delete employees
    def __str__(self):
        return f"Admin {self.first_name} {self.last_name} Joined in {self.date_joined}"


class Employee(User):  # manages sales and can update inventory but cannot add or delete
    def __str__(self):
        return f"Employee {self.first_name} {self.last_name}"
    
    def Details(self):
        return f"Joined in {self.date_joined}"

class Customer:
    def __init__(self, first, last, card, email, addr, id=0) -> None:
        self.id = id
        self.fn = first
        self.ln = last
        self.card = card
        self.email = email
        self.address = addr
        self.orders = []

    def to_dict(self):
        return {
            "email": self.email,
            "name": [{ "first": self.fn, "last": self.ln }],
            "card": self.card,
            "address": self.address
        }

    def serialize(customer):
        if isinstance(customer, Customer):
            return customer.to_dict()
        raise TypeError("Object of type 'Customer' is not JSON serializable")

    def UpdateCard(self, new_card):
        self.card = new_card

    def UpdateAddress(self, new_address):
        self.address = new_address

    def UpdateEmail(self, new_email):
        self.email = new_email

    def Details(self):
        return f"\nEmail: {self.email} \nAddress: {self.address}\nList of all orders: {self.orders}"

    def __str__(self) -> str:
        return f"{self.ln}, {self.fn}"

    def __repr__(self) -> str:
        return f"{self.fn} {self.ln} ID {self.id}"

    def __eq__(self, value) -> bool:
        if isinstance(value, Customer):
            return value.id == self.id
        return False
