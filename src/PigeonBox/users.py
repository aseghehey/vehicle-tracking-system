####################################################################################################################
'''
////////////////
PROGRAM users:   The purpose of the classes(User,Admin,employee,Customer) is to provide a framework for 
                 managing users(Admins,employees) and customers in the system.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

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


    # One-line description: Initializes a User object with a username, password, first name, last name, and date joined.
    # General description: This function creates a new instance of a User object with the specified username, password, first name, last name, and date joined.
    #   If no date is provided, today's date is used. The date is validated and converted to a datetime object.
    # Typical calling examples:
    #   user1 = User('jdoe', 'password', 'John', 'Doe', '2022-03-15')
    #   user2 = User('asmith', 'p@ssword', 'Alice', 'Smith')
    # Accessibility: Public
    # Function prototype: def __init__(self, username='', password='', first_name='', last_name='', date_joined=None) -> None:
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


    # One-line description: Returns the first name of the user.
    # General description: This method is part of a User class and returns the first name attribute of a user object.
    # Typical calling examples: user.getFirstName()
    # Accessibility: Public
    # Function prototype: def getFirstName(self) -> str:
    def getFirstName(self):
        return self.first_name
    

    # One-line description: Returns the last name of a user.
    # General description: This function is a getter method that returns the last name of a user object.
    # Typical calling examples:
    #   user1_last_name = user1.getLastName()
    # Accessibility: This function is a public method that can be accessed from anywhere within the class and outside of it.
    # Function prototype:def getLastName(self) -> str:
    def getLastName(self):
        return self.last_name


    # One-line description: Updates the password of the user.
    # General description: This method updates the password of the user with the given new password.
    # Typical calling examples:
    #   user1.UpdatePassword('newpassword123')
    # Accessibility: Public.
    # Fuction prototype:
    #   def UpdatePassword(self, newpassword: str) -> None:
    def UpdatePassword(self, newpassword):
        self.password = newpassword



    # One-line description: Updates the username attribute of a user object with a new username.
    # General description: This method updates the username attribute of a User object with a new username passed as an argument.
    # Typical calling examples:
    #   user1 = User('john_doe', 'password', 'John', 'Doe', '2022-01-01')
    #   user1.UpdateUserName('john_doe_123')
    # Accessibility: Public
    # Function prototype: def UpdateUserName(self, newusername: str) -> None:
    def UpdateUserName(self, newusername):
        self.username = newusername



    # One-line description: Returns the username of a user.
    # General description: This function returns the username of a user object.
    # Typical calling examples:
    #   user1.getUsername() -> returns the username of user1
    # Accessibility: Public
    # Function prototype: def getUsername(self) -> str:
    def getUsername(self):
        return self.username
    


    # One-line description: Returns the password of a User instance.
    # General description: This function returns the password attribute of a User object,
    #    which stores the password of the user.
    # Typical calling examples:
    #   user = User('john', 'pass123')
    #   password = user.getPassword()
    # Accessibility: Public
    # Function prototype: def getPassword(self) -> str:
    def getPassword(self):
        return self.password
    


    # One-line description:A function to serialize a User object to a JSON-serializable format.
    # General description:This function takes a User object as an argument and converts it to a dictionary format that can be JSON-serialized. 
    #   If the input object is not of type User, 
    #   it raises a TypeError with an appropriate error message.
    # Typical calling examples:
    #   user_json = serialize(user_object)
    # Accessibility:This function can be accessed from any module in the program where it is imported.
    # Function prototype:def serialize(user: User) -> Union[Dict, None]:
    def serialize(user):
        if isinstance(user, User):
            return user.to_dict()
        raise TypeError("Object of type 'User' is not JSON serializable")



    # One-line description: Determines whether two users are equal by comparing their usernames.
    # General description: This method compares the usernames of two user objects to determine if they represent the same user.
    # Typical calling examples:
    #   user1 == user2 - This will check if user1 and user2 have the same username and return True if they are equal and False if not.
    # Accessibility: Public
    # Function prototype: def __eq__(self, __o) -> bool:
    def __eq__(self, __o):
        if isinstance(__o, User) or isinstance(__o, Admin) or isinstance(__o, Employee):
            return __o.username == self.username



    # One-line description: Returns a string representation of a User object.
    # General description: The __str__ function returns a string representation of a User object.
    #   The string contains the user's first name, last name, and the date they joined.
    # Typical calling examples:
    #   user1 = User('john_doe', 'password', 'John', 'Doe')
    #   print(user1) # Output: "User John Doe Joined in 2023-04-14 00:00:00"
    # Accessibility: Public.
    # Function prototype: def __str__(self) -> str:
    def __str__(self):
        return f"User {self.first_name} {self.last_name} Joined in {self.date_joined}"


    # One-line description: Return a string representation of a User object.
    # General description: This function returns a string representation of a User object which includes the user's 
    #   first name and last name.
    # Typical calling examples:
    #   user = User("john", "doe")
    #   print(repr(user)) (Output: "john doe")
    # Accessibility: Public
    # Function prototype: def __repr__(self) -> str:
    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"





#   This class inherits from the User class and defines an Admin user type.
#   An Admin user can delete or add inventory, add or delete employees.
class Admin(User):


    # One-line description: Initializes an instance of the Admin class, inheriting from the User class and setting the category type to "Admin".
    # General description: This function creates an instance of the Admin class, setting its properties to the provided arguments or default values
    #    and initializing it as a subclass of the User class with an additional categoryType property set to "Admin".
    # Typical calling examples:admin1 = Admin("admin1", "password", "John", "Doe", "2022-01-01")
    # Accessibility: Public.
    # Function prototype:
    #   def __init__(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Admin") -> None:
    def __init__(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Admin") -> None:
        super().__init__(username, password, first_name, last_name, date_joined)
        self.categoryType = categoryType



    # One-line description: Returns the category type of an object.
    # General description: This method is used to get the category type of an object. It returns the category type of the object on which it is called.
    # Typical calling examples:
    #   admin = Admin("admin", "password", "John", "Doe", datetime.now(), "Admin")
    #   category = admin.getCategory()
    # Accessibility: Public method.
    # Function prototype: def getCategory(self) -> str:
    def getCategory(self):
        return self.categoryType


    # One-line description: Returns a string representation of an Admin instance.
    # General description: This function returns a formatted string representation of an Admin instance containing the category type,
    #   first name and last name of the Admin.
    # Typical calling examples:
    #   admin1 = Admin("user1", "password123", "John", "Doe", datetime.now(), "Senior")
    #   print(admin1) will output "Senior John Doe"
    # Accessibility: Public
    # Function prototype: def __str__(self) -> str:
    def __str__(self):
        return f"{self.categoryType} {self.first_name} {self.last_name}"
    

        
    # One-line description: Get user details.
    # General description: This method returns the date on which the user joined.
    # Typical calling examples:
    #   admin = Admin("admin", "password", "John", "Doe", categoryType="Admin")
    #   details = admin.getDetails()
    # Accessibility: Public method.
    # Function prototype: def getDetails(self) -> str:
    def getDetails(self):
        date = self.date_joined.strftime("%Y-%m-%d")
        return f"Joined in {date}"
    


    # One-line description: Returns a dictionary with user information.
    # General description: This function returns a dictionary containing the user's username, password, first and last name, date of joining, and 
    #   category type as key-value pairs.
    # Typical calling examples:
    #   user = User("johndoe", "password", "John", "Doe", datetime.datetime.now())
    #   user_dict = user.to_dict()
    #   admin = Admin("admin", "password", "Admin", "User", datetime.datetime.now())
    #   admin_dict = admin.to_dict()
    # Accessibility: Public method accessible outside the class.
    # Function prototype: def to_dict(self) -> dict:
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


    # One-line description: Initializes an Employee object with a specified username, password, first and last name, date joined, and category type.
    # General description: This function initializes an Employee object, which inherits from the User class. It sets the object's
    #   instance variables to the values provided in the function parameters, and also sets the object's categoryType to "Employee" by default.
    # Typical calling examples:
    #   employee1 = Employee(username='jdoe', password='password123', first_name='John', last_name='Doe', date_joined=datetime.date(2022, 4, 14))
    # Accessibility: This function is accessible from within the Employee class and any subclasses that inherit from it.
    # Function prototype:
    #   def init(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Employee") -> None:
    def __init__(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Employee") -> None:
        super().__init__(username, password, first_name, last_name, date_joined)
        self.categoryType = categoryType
    


    # One-line description: Returns a string representation of the Employee object including category, first name, and last name.
    # General description: This function returns a formatted string that represents an Employee object.
    #   The returned string includes the Employee's category, first name, and last name.
    # Typical calling examples:
    #   employee = Employee(username='jdoe', password='password', first_name='John', last_name='Doe')
    #   print(employee) # Output: "Employee John Doe"
    # Accessibility: This function is public and can be accessed from anywhere in the code.
    # Function prototype: def __str__(self) -> str:
    def __str__(self):
        return f"{self.categoryType} {self.first_name} {self.last_name}"
    


    # One-line description: Returns the details of the employee's joining date in a formatted string.
    # General description: This method returns the date on which an employee joined the organization in a formatted string. It takes the employee's date of
    #   joining as an instance variable and formats it using the strftime() method.
    # Typical calling examples:
    #   emp1 = Employee('johndoe', 'password', 'John', 'Doe', datetime.date(2021, 1, 1))
    #   print(emp1.getDetails()) # Output: Joined in 2021-01-01
    # Accessibility: This method is public, accessible outside the class.
    # Function prototype: def getDetails(self) -> str:
    def getDetails(self):
        date = self.date_joined.strftime("%Y-%m-%d")
        return f"Joined in {date}"
    


    # One-line description: Returns the category type of the user.
    # General description: This function is a method of the User class which returns the category type of the user.
    # Typical calling examples:
    #   user1.getCategory()
    # Accessibility: This method is accessible to instances of the User class and its subclasses.
    # Function prototype:def getCategory(self) -> str:
    def getCategory(self):
        return self.categoryType
    


    # One-line description: Returns a dictionary representation of the user object.
    # General description: The to_dict method returns a dictionary with the user's attributes as key-value pairs, including their username,
    #   password, first and last name, date joined, and category type. This method is commonly used to convert user objects to a format that can be easily serialized and stored, such as in a database or JSON file.
    # Typical calling examples:
    #   user = User('johndoe', 'password', 'John', 'Doe')
    #   user_dict = user.to_dict()
    #   print(user_dict)
    # Output: {'username': 'johndoe', 'password': 'password', 'name': [{'firstName': 'John', 'lastName': 'Doe'}], 'dateJoined': '2023-04-14', 'type': 'Employee'}
    # Accessibility: Public.
    # Function prototype: def to_dict(self) -> dict:
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


    # One-line description: Constructor for a Customer class with attributes such as first and last name, card, email, address and an empty list for orders.
    # General description: The function initializes a new object of the Customer class by setting values for first name, last name,
    #   card, email, address, and an empty list for orders.
    # Typical calling examples:
    #   customer1 = Customer("John", "Doe", "1234-5678-9012-3456", "johndoe@example.com", "123 Main St")
    #   customer2 = Customer("Alice", "Smith", "9876-5432-1098-7654", "alicesmith@example.com", "456 Oak St")
    # Accessibility: Public
    # Function prototype: def __init__(self, first: str, last: str, card: str, email: str, address: str) -> None:
    def __init__(self, first, last, card, email, address) -> None:
        self.firstName = first
        self.lastName = last
        self.card = card
        self.email = email
        self.address = address
        self.orders = []



    # One-line description: Returns the first name of a customer.
    # General description: This function returns the first name of a customer object created using the Customer class. 
    #   The first name is stored as an instance variable within the class.
    # Typical calling example:
    #   customer1 = Customer("John", "Doe", "1234567890", "johndoe@gmail.com", "123 Main St")
    #   print(customer1.getFirstName())  # output: John
    # Accessibility: Public
    # Function prototype: def getFirstName(self) -> str:
    def getFirstName(self):
        return self.firstName
    


    # One-line description: Get the last name of a customer.
    # General description: This method returns the last name of a customer instance.
    # Typical calling examples:
    #   customer.getLastName()
    # Accessibility: Public.
    # Function prototype: def getLastName(self) -> str:
    def getLastName(self):
        return self.lastName



    # One-line description: Returns the email of a customer.
    # General description: This function returns the email attribute of a customer object.
    # Typical calling examples:
    #   customer = Customer("John", "Doe", "1234-5678-9012-3456", "johndoe@gmail.com", "123 Main St")
    #   email = customer.getEmail()
    # Accessibility: Public.
    # Function prototype:def getEmail(self) -> str:
    def getEmail(self):
        return self.email



    # One-line description: Sets the value of the card attribute for the instance of the class.
    # General description: This method sets the value of the card attribute to a new value passed as an argument.
    #   The card attribute represents the credit/debit card number associated with the customer's account.
    # Typical calling examples:
    #   customer1 = Customer('John', 'Doe', '1234 5678 9012 3456', 'john.doe@email.com', '123 Main St')
    #   customer1.setCard('9876 5432 1098 7654')
    # Accessibility: Public method accessible to anyone who has an instance of the Customer class.
    # Function prototype: def setCard(self, new_card: str) -> None:. The method takes a string argument new_card representing the new card number and returns nothing (None).
    def setCard(self, new_card):
        self.card = new_card



    # One-line description: Method to set a new address for a user profile.
    # General description: This method sets a new address for the user profile.
    # Typical calling examples:
    #   user = UserProfile('John', 'Doe', '1234 5678 9012 3456', 'johndoe@example.com', '123 Main St')
    #   user.setAddress('456 Broad St')
    # Accessibility: Public method.
    # Function prototype: def setAddress(self, new_address: str) -> None
    def setAddress(self, new_address):
        self.address = new_address



    # One-line description: Setter function to update the email address of a user.
    # General description: This function updates the email address of a user with a new email address.
    # Typical calling examples:
    # user.setEmail('newemail@example.com')
    # Accessibility: Public
    # Function prototype: def setEmail(self, new_email):
    def setEmail(self, new_email):
        self.email = new_email



    # One-line description: Returns a string containing the user's email, address, and list of orders.
    # General description: This method returns a formatted string that contains the email, address, and list of orders for a user.
    # Typical calling example: user.getDetails()
    # Accessibility: Public
    # Function prototype: def getDetails(self) -> str:
    def getDetails(self):
        return f"\nEmail: {self.email} \nAddress: {self.address}\nList of all orders: {self.orders}"



    # One-line description: Returns the dictionary representation of the customer object.
    # General description: This method returns a dictionary representation of the customer object with attributes such as email, name, card, and address.
    # Typical calling examples:
    # customer = Customer("John", "Doe", "1234567890123456", "johndoe@example.com", "123 Main St.")
    # customer_dict = customer.to_dict()
    # Accessibility: Public
    # Function prototype: def to_dict(self) -> dict:
    def to_dict(self):
        return {
            "email": self.email,
            "name": [{ "first": self.firstName, "last": self.lastName }],
            "card": self.card,
            "address": self.address
        }



    # One-line description: Function that serializes a Customer object into a JSON serializable dictionary.
    # General description: The serialize() function takes a Customer object and returns its dictionary representation using the to_dict() method. The purpose of the function
    #   is to allow the Customer object to be easily serialized to JSON for data exchange or storage.
    # Typical calling examples:
    # Accessibility: The function is accessible within the same module or class where it is defined.
    # Function prototype:def serialize(customer: Customer) -> dict:
    def serialize(customer):
        if isinstance(customer, Customer):
            return customer.to_dict()
        raise TypeError("Object of type 'Customer' is not JSON serializable")
    


    # one-line Description: This method returns a string representation of the object instance.
    # General Description: This method is used to get a string representation of the object instance of the Customer class. It concatenates the last name and first name of the customer 
    #   with a comma in between and returns the resulting string.
    # Typical calling example: print(customer_obj) where customer_obj is an instance of the Customer class.
    # Accessibility: Public.
    # Function prototype: def __str__(self) -> str:
    def __str__(self) -> str:
        return f"{self.lastName}, {self.firstName}"



    # One-line description: Returns a string representation of the customer object.
    # General description: This function returns a string representation of the customer object that includes their email address.
    # Typical calling examples:
    #   customer = Customer("John", "Doe", "1234567890123456", "johndoe@example.com", "123 Main St")
    #   print(repr(customer))
    # Accessibility: Public.
    # Function prototype: def __repr__(self) -> str:
    def __repr__(self) -> str:
        return f"{self.email}"



    # One-line description: Check if two Customer objects are equal by comparing their email addresses.
    # General description: This function compares the email attribute of a Customer object with another object. 
    #   If the other object is also a Customer object, its email attribute is compared with the email attribute of the original Customer object.
    #   If the two email addresses match, the function returns True, otherwise it returns False.
    # Typical calling examples:
    # Accessibility: This function is accessible from within the Customer class and can be called on a Customer object.
    # Function prototype: def __eq__(self, value) -> bool:
    def __eq__(self, value) -> bool:
        if isinstance(value, Customer):
            return value.email == self.email
        return False
