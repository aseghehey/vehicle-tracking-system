####################################################################################################################
'''
////////////////
PROGRAM users:   The purpose of the classes(User,Admin,employee,Customer) is to provide a framework for 
                 managing users(Admins,employees) and customers in the system.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu

////////////////
VERSION 1: written [day] [month] 2023 by [firstInitial]. [lastName]
REVISION [revision# ex: 1.1]: [day] [month] 2023 by [firstInitial]. [lastName] to [purpose of revision]

////////////////
PURPOSE:
This code defines a User class that represents a user with basic information like username, password, and date joined.
It defines two classes Admin and Employee, both inherit from the User class and define their own functionalities.
It defines a Customer class with attributes first and last name, card, email, address, and orders.

Methods:
Class User:
- init(self, username='', password='', first_name='', last_name='', date_joined=None): Initializes the User class with given parameters.
- getFirstName(self): Returns the first name of the user.
- getLastName(self): Returns the last name of the user.
- UpdatePassword(self, newpassword): Updates the password of the user.
- UpdateUserName(self, newusername): Updates the username of the user.
- getUsername(self): Returns the username of the user.
- getPassword(self): Returns the password of the user.
- serialize(user): Static method that serializes the User object to a dictionary.
- eq(self, __o): Returns True if the given object has the same username as this User object.
- str(self): Returns a string representation of the User object.
- repr(self) -> str: Returns a string representation of the User object.

Class Admin(User):
- init(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Admin"): Initializes an Admin object.
- getCategory(self): Returns the category type of the user.
- str(self): Returns a string representation of the user.
- getDetails(self): Returns details about the user's join date.
- to_dict(self): Returns a dictionary representation of the user.

Class Employee(User):
- init(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Employee"): Initializes an Employee object.
- str(self): Returns a string representation of the user.
- getDetails(self): Returns details about the user's join date.
- getCategory(self): Returns the category type of the user.
- to_dict(self): Returns a dictionary representation of the user.

Class Customer:
- init(self, first, last, card, email, address): Initializes a Customer object.
- getFirstName(self): Returns the first name of the customer.
- getLastName(self): Returns the last name of the customer.

////////////////
DATA STRUCTURES:
DataStructures:
- Lists: Lists are used to store name information as a list of dictionaries in the to_dict() method of the Admin and Employee classes.
- Dictionaries: In the code, they are used to store information about users in the to_dict() method of the Admin and Employee classes. The Customer class also stores orders in a list of dictionaries.

Attributes:
- username: a string representing the username of the user.
- password: a string representing the password of the user.
- first_name: a string representing the first name of the user.
- last_name: a string representing the last name of the user.
- date_joined: a datetime object representing the date the user joined.
- categoryType: a string representing the type of user (Admin or Employee).
- firstName: a string representing the first name of the customer.
- lastName: a string representing the last name of the customer.
- card: a string representing the credit card information of the customer.
- email: a string representing the email address of the customer.
- address: a string representing the physical address of the customer.
- orders: a list of orders associated with the customer.

////////////////
ALGORITHM:
None

////////////////
ERROR HANDLING:
No explicit error handling.
Validation check in User for date_joined to make sure its a valid datetime object.

////////////////
'''
####################################################################################################################

from datetime import datetime


#   A class that represents a user with basic information like username, password, and date joined.
class User():
    #   Initializes the User class with given parameters.
    def __init__(self, username='', password='', first_name='', last_name='', date_joined=None) -> None:
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        # validate date. if date is not given, set it to today's date.
        if not date_joined: 
            date_joined = datetime.today()
        else:
            date_joined = datetime.strptime(date_joined, "%Y-%m-%d")
        self.date_joined = date_joined

    #   Returns the first name of the user.
    def getFirstName(self):
        return self.first_name
    
    #   Returns the last name of the user.
    def getLastName(self):
        return self.last_name

    #   Updates the password of the user
    def UpdatePassword(self, newpassword):
        self.password = newpassword

    #   Updates the username of the user
    def UpdateUserName(self, newusername):
        self.username = newusername

    #   Returns the username of the user
    def getUsername(self):
        return self.username
    
    #   Returns the password of the user
    def getPassword(self):
        return self.password
    
    #   Static method that serializes the User object to a dictionary
    def serialize(user):
        if isinstance(user, User):
            return user.to_dict()
        raise TypeError("Object of type 'User' is not JSON serializable")

    #   Returns True if the given object has the same username as this User object.
    def __eq__(self, __o):
        if isinstance(__o, User) or isinstance(__o, Admin) or isinstance(__o, Employee):
            return __o.username == self.username

    #   Returns a string representation of the User object
    def __str__(self):
        return f"User {self.first_name} {self.last_name} Joined in {self.date_joined}"

    #   Returns a string representation of the User object
    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"

#   This class inherits from the User class and defines an Admin user type.
#   An Admin user can delete or add inventory, add or delete employees.
class Admin(User):
    #   Initializes an Admin object
    def __init__(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Admin") -> None:
        super().__init__(username, password, first_name, last_name, date_joined)
        self.categoryType = categoryType

    #   Returns the category type of the user
    def getCategory(self):
        return self.categoryType

    #   Returns a string representation of the user
    def __str__(self):
        return f"{self.categoryType} {self.first_name} {self.last_name}"
    
    #   Returns details about the user's join date
    def getDetails(self):
        date = self.date_joined.strftime("%Y-%m-%d")
        return f"Joined in {date}"
    
    #   Returns a dictionary representation of the user
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "name": [{"firstName": self.first_name, "lastName": self.last_name}],
            "dateJoined": self.date_joined.strftime("%Y-%m-%d"),
            "type": self.categoryType # default
        }

#   This class inherits from the User class and defines an Employee user type.
#   An Employee user manages sales and can update inventory but cannot add or delete.
class Employee(User):
    #   Initializes an Employee object.
    def __init__(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Employee") -> None:
        super().__init__(username, password, first_name, last_name, date_joined)
        self.categoryType = categoryType
    
    #   Returns a string representation of the user.
    def __str__(self):
        return f"{self.categoryType} {self.first_name} {self.last_name}"
    
    #   Returns details about the user's join date.
    def getDetails(self):
        date = self.date_joined.strftime("%Y-%m-%d")
        return f"Joined in {date}"
    
    #   Returns the category type of the user.
    def getCategory(self):
        return self.categoryType
    
    #   Returns a dictionary representation of the user.
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "name": [{"firstName": self.first_name, "lastName": self.last_name}],
            "dateJoined": self.date_joined.strftime("%Y-%m-%d"),
            "type": self.categoryType # default
        }

#   Defines a Customer object.
class Customer:
    #   Initializes a Customer object
    def __init__(self, first, last, card, email, address) -> None:
        self.firstName = first
        self.lastName = last
        self.card = card
        self.email = email
        self.address = address
        self.orders = []

    #   Returns the first name of the customer.
    def getFirstName(self):
        return self.firstName
    
    #   Returns the last name of the customer.
    def getLastName(self):
        return self.lastName

    #   Returns the email of the customer.
    def getEmail(self):
        return self.email

    #   Sets the card number of the customer.
    def setCard(self, new_card):
        self.card = new_card

    #   Sets the address of the customer.
    def setAddress(self, new_address):
        self.address = new_address

    #   Sets the email of the customer.
    def setEmail(self, new_email):
        self.email = new_email

    #   Returns the details of the customer.
    def getDetails(self):
        return f"\nEmail: {self.email} \nAddress: {self.address}\nList of all orders: {self.orders}"

    #   Returns the dictionary representation of the customer object.
    def to_dict(self):
        return {
            "email": self.email,
            "name": [{ "first": self.firstName, "last": self.lastName }],
            "card": self.card,
            "address": self.address
        }

    #   Serializes the customer object.
    def serialize(customer):
        if isinstance(customer, Customer):
            return customer.to_dict()
        raise TypeError("Object of type 'Customer' is not JSON serializable")
    
    #   Returns the string representation of the customer object.
    def __str__(self) -> str:
        return f"{self.lastName}, {self.firstName}"

    #   Returns the email of the customer object.
    def __repr__(self) -> str:
        return f"{self.email}"

    #   Compares the email of the customer object with another object.
    def __eq__(self, value) -> bool:
        if isinstance(value, Customer):
            return value.email == self.email
        return False
