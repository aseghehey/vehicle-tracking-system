from datetime import datetime

class User():
    def __init__(self, username='', password='', first_name='', last_name='', date_joined=None) -> None:
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        # validate date
        if not date_joined: 
            date_joined = datetime.today()
        else:
            date_joined = datetime.strptime(date_joined, "%Y-%m-%d")
        self.date_joined = date_joined

    def getFirstName(self):
        return self.first_name
    
    def getLastName(self):
        return self.last_name

    def UpdatePassword(self, newpassword):
        self.password = newpassword

    def UpdateUserName(self, newusername):
        self.username = newusername

    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password
    
    def serialize(user):
        if isinstance(user, User):
            return user.to_dict()
        raise TypeError("Object of type 'User' is not JSON serializable")


    def __eq__(self, __o):
        if isinstance(__o, User) or isinstance(__o, Admin) or isinstance(__o, Employee):
            return __o.username == self.username

    def __str__(self):
        return f"User {self.first_name} {self.last_name} Joined in {self.date_joined}"

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Admin(User):  # can delete or add inventory, add or delete employees
    def __init__(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Admin") -> None:
        super().__init__(username, password, first_name, last_name, date_joined)
        self.categoryType = categoryType

    def getCategory(self):
        return self.categoryType

    def __str__(self):
        return f"{self.categoryType} {self.first_name} {self.last_name}"
    
    def getDetails(self):
        date = self.date_joined.strftime("%Y-%m-%d")
        return f"Joined in {date}"
    
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "name": [{"firstName": self.first_name, "lastName": self.last_name}],
            "dateJoined": self.date_joined.strftime("%Y-%m-%d"),
            "type": self.categoryType # default
        }


class Employee(User):  # manages sales and can update inventory but cannot add or delete
    def __init__(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Employee") -> None:
        super().__init__(username, password, first_name, last_name, date_joined)
        self.categoryType = categoryType
        
    def __str__(self):
        return f"{self.categoryType} {self.first_name} {self.last_name}"
    
    def getDetails(self):
        date = self.date_joined.strftime("%Y-%m-%d")
        return f"Joined in {date}"
    
    def getCategory(self):
        return self.categoryType
    
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "name": [{"firstName": self.first_name, "lastName": self.last_name}],
            "dateJoined": self.date_joined.strftime("%Y-%m-%d"),
            "type": self.categoryType # default
        }

class Customer:
    def __init__(self, first, last, card, email, address) -> None:
        self.firstName = first
        self.lastName = last
        self.card = card
        self.email = email
        self.address = address
        self.orders = []

    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName

    def getEmail(self):
        return self.email

    def setCard(self, new_card):
        self.card = new_card

    def setAddress(self, new_address):
        self.address = new_address

    def setEmail(self, new_email):
        self.email = new_email

    def getDetails(self):
        return f"\nEmail: {self.email} \nAddress: {self.address}\nList of all orders: {self.orders}"

    def to_dict(self):
        return {
            "email": self.email,
            "name": [{ "first": self.firstName, "last": self.lastName }],
            "card": self.card,
            "address": self.address
        }

    def serialize(customer):
        if isinstance(customer, Customer):
            return customer.to_dict()
        raise TypeError("Object of type 'Customer' is not JSON serializable")
    
    def __str__(self) -> str:
        return f"{self.lastName}, {self.firstName}"

    def __repr__(self) -> str:
        return f"{self.email}"

    def __eq__(self, value) -> bool:
        if isinstance(value, Customer):
            return value.email == self.email
        return False