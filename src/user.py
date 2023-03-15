"""
####################################################################################################################
[replace text and delete in bracket]
PROGRAM [name]:  [purpose of code and function. brief]

PROGRAMMER: [firstName] [lastName] [email]

VERSION 1: written [day] [month] 2023 by [firstInitial]. [lastName]
REVISION [revision# ex: 1.1]: [day] [month] 2023 by [firstInitial]. [lastName] to [purpose of revision]


PURPOSE:
[general purpose of code and each functionality. thorough description]

DATA STRUCTURES:
[major data structures and variables]
[ex: variable LENGTH - integer]

ALGORITHM:
[brief description of logic flow]

ERROR HANDLING:
[brief description error handling]

####################################################################################################################
"""
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

    def changePassword(self, newpassword):
        # MAYBE add verifiers? 
        self.password = newpassword
        print('password changed successfully')
    
    def changeUserName(self, newusername):
        # MAYBE check if username already exists
        self.username = newusername
        print('username changed successfully')
        # write username to json

    def __eq__(self, __o):
        if isinstance(__o, User) or isinstance(__o, Admin) or isinstance(__o,Employee):
            return __o.username == self.username
        
    def __str__(self):
        return f"User {self.first_name} {self.last_name} Joined in {self.date_joined}"

class Admin(User): # can delete and add inventory
    def __str__(self):
        return f"Admin {self.first_name} {self.last_name} Joined in {self.date_joined}"

class Employee(User): # can sell cars
    def __str__(self):
        return f"Employee {self.first_name} {self.last_name} Joined in {self.date_joined}"