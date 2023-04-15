####################################################################################################################
'''
////////////////
PROGRAM orders:   
The code defines a class called "Order" representing an order made by a buyer for a car,
containing information such as the buyer, car, salesperson, date of purchase, and order ID,
with various methods to manipulate and retrieve information about the order.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

////////////////
PURPOSE:
The purpose of the code is to implement a class Order that represents an order made by a buyer for a car,
containing information such as the buyer, car, salesperson, date of purchase, and order ID.
The class provides several methods to get the details of the order,
such as the buyer, car, salesperson, date of purchase, and order ID.

Methods:
- getUser(self): Returns the buyer of the order.
- getCar(self): Returns the car of the order.
- getSeller(self): Returns the salesperson of the order.
- getDate(self): Returns the date of the order.
- getId(self): Returns the ID of the order.
- getDateJoined(self): Returns the date of purchase in the YYYY-MM-DD format.
- to_dict(self): Converts the Order object into a dictionary.
- serialize(order): Serializes the Order object into a JSON serializable format.
- RemoveOrder(self): Removes the order from the buyer's orders list and sets the car status to available.
- orderDetails(self): Returns details of the order including car, salesperson, and customer.
- __str__(self): Returns a string representation of the order object.
- __eq__(self, value): Overriding the equality operator to compare two Order objects.
- __repr__(self): Return car object string representation.

////////////////
DATA STRUCTURES:
DataStructures:
- self.id: An integer variable used to store the unique ID of an order.
- self.car: An object variable of the Car class, used to store the details of the car ordered in the order.
- self.buyer: An object variable of the User class, used to store the details of the buyer who placed the order.
- self.salesBy: An object variable of the Employee class, used to store the details of the salesperson who made the sale.
- self.when: A datetime variable, used to store the date and time of the order.

Attributes:
- id: a unique identifier for the order.
- car: an object of the Car class representing the car ordered by the buyer.
- buyer: an object of the User class representing the buyer who placed the order.
- when: a datetime object representing the date and time when the order was made.
- salesBy: an object of the Employee class representing the salesperson who sold the car.

////////////////
ALGORITHM:
None

////////////////
ERROR HANDLING:
No explicit error handling.

////////////////
'''
####################################################################################################################



from datetime import datetime
from PigeonBox.bcolors import bcolors


#   A class representing an order made by a buyer for a car, containing information such as the buyer, car, salesperson,
#   date of purchase, and order ID.
class Order():

    # One-line description: Initializes an object of the Sale class with specified attributes including car, buyer, sales employee, and date of sale.
    # General description: This function initializes an object of the Sale class with the provided attributes including an ID, a car object that has been ordered, the buyer's user ID, the sales employee's user
    #   ID, and the date of sale. If a date is not provided, the date is set to today's date.
    # Typical calling examples:
    #   sale = Sale(1, car, buyer_id, employee_id)
    #   sale = Sale(2, car, buyer_id, employee_id, '2022-05-12')
    # Accessibility: This function can be accessed within the Sale class.
    # Function prototype:def __init__(self, id, car=None, buyer=None, dateBought=None, employee=None) -> None:
    """ Class represents orders made, works like a database one-to-one relationship with a buyer and a car"""
    def __init__(self, id, car=None, buyer=None, dateBought=None, employee=None) -> None:
        self.id = id 
        #  set car status to ordered
        if car:  car.SetStatus('ordered')
        self.car = car        
        self.buyer = buyer #the user id
        self.salesBy = employee

        # if a date is not specified, it will be set to today's date
        if not dateBought: dateBought = datetime.today()
        else: dateBought = datetime.strptime(dateBought, "%Y-%m-%d")
        self.when = dateBought



    # One-line description: Returns the ID of the user who bought the car.
    # General description: This method returns the ID of the user who bought the car.
    # Typical calling examples: sale.getUser()
    # Accessibility: Public
    # Function prototype: def getUser(self) -> str:
    def getUser(self):
        return self.buyer
    


    # One-line description: Returns the car associated with the order object.
    # General description: This method returns the car object associated with the current order object.
    # Typical calling examples:
    #   order1.getCar()
    #   order2.getCar()
    # Accessibility: Public
    # Function prototype: def getCar(self) -> Car: (assuming that the Car class is the type of the self.car attribute)
    def getCar(self):
        return self.car
    


    # One-line description: Returns the employee who sold the car in the order.
    # General description: This method returns the employee who sold the car in the order instance.
    # Typical calling example: order.getSeller()
    # Accessibility: Public method.
    # Function prototype: def getSeller(self) -> Employee
    def getSeller(self):
        return self.salesBy
    

    # One-line description: Returns the date when the car was bought.
    # General description: This method is part of a class that represents a car sale. 
    #   It returns the date when the car was bought, which was either passed as an argument during object instantiation or set  
    #   to the current date by default.
    # Typical calling examples:
    #   sale = CarSale(1234, car, buyer, '2022-03-25', salesperson)
    #   sale.getDate() # returns datetime.datetime(2022, 3, 25, 0, 0)
    # Accessibility: Public
    # Function prototype: def getDate(self) -> datetime.datetime:
    def getDate(self):
        return self.when
    


    # One-line description: Returns the ID of a car order.
    # General description: This method is a getter method for the ID of a car order object.
    # Typical calling examples:
    #   order1 = CarOrder(1, car1, user1, "2022-04-12", employee1)
    #   order1_id = order1.getId()  # 1
    # Accessibility: Public.
    # Function prototype: def getId(self) -> int:
    def getId(self):
        return self.id
    


    # One-line description: Returns the date the user joined in the format "YYYY-MM-DD".
    # General description: This function returns the date that a user joined the system in the format "YYYY-MM-DD".
    # Typical calling examples:
    #   user = User("John", "Doe", "johndoe@gmail.com", "password", "1985-02-14")
    #   user.getDateJoined() -> "2022-03-04"
    # Accessibility: Public.
    # Function prototype: def getDateJoined(self) -> str:
    def getDateJoined(self):
        return self.when.strftime("%Y-%m-%d")
    


    # One-line description: Convert the Order object to a dictionary format.
    # General description: This function takes an instance of the Order class and returns a dictionary containing information about the order,
    #   such as the ID of the order, the VIN of the car being purchased, the email of the buyer, the username of the employee who made the sale, and the date of the sale.
    # Typical calling examples:
    #   order = Order(123, car, buyer, "2022-04-13", employee)
    #   order_dict = order.to_dict()
    # Accessibility: This function is a method of the Order class, so it can be called on any instance of that class.
    # Function prototype: def to_dict(self):
    def to_dict(self):
        return {
            "id": self.id,
            "carVin": self.car.getVin(),
            "buyer": self.buyer.getEmail(),
            "soldBy": self.salesBy.getUsername(),
            "dateBought": self.when.strftime("%Y-%m-%d")
        }
    

    # One-line description: Serializes an Order object to a JSON-compatible format.
    # General description: This function takes an Order object and converts it into a dictionary that can be easily serialized into a JSON format. It does this by calling the Order object's to_dict method, which returns a dictionary representation of the object's attributes. If the provided object is not an instance of the Order class, a TypeError is raised.
    # Typical calling examples:
    #   order = Order(1, car, buyer, dateBought, employee)
    #   serialized_order = serialize(order)
    # Accessibility: This function is likely part of a larger program or module and can be accessed from other functions or scripts within that program or module.
    # Function prototype:def serialize(order):
    def serialize(order):
        if isinstance(order, Order):
            return order.to_dict()
        raise TypeError("Object of type 'Order' is not JSON serializable")



    # One-line description: Removes an order and sets the car status to available.
    # General description: This function removes the current order from the buyer's orders list and sets the car status to available
    #    indicating that the car is no longer reserved.
    # Typical calling examples:
    # Accessibility: This function is an instance method, which means it can only be called on an instance of a class.
    # Function prototype: def RemoveOrder(self):
    def RemoveOrder(self):
        self.buyer.orders.remove(self)
        self.car.SetStatus("available")
    


    # One-line description: Generates a string containing the details of the order.
    # General description: This function generates a string containing the details of the car being ordered, the employee who made the
    #   sale, and the customer who placed the order.
    # Typical calling example:
    #   order = Order("O001", car, customer, "2023-04-14", employee)
    #   details = order.orderDetails()
    #   print(details)
    # Accessibility: Public.
    # Function prototype:def orderDetails(self) -> str:
    def orderDetails(self):
        toret = f"\nCar:\n{self.car.getDetails()}\n\nSales by: {self.salesBy}\n\nCustomer {self.buyer.getDetails()}\n"
        return toret



    # One-line description: Returns a string representation of the order object.
    # General description: This function returns a string representation of the order object,
    #   containing the order ID, the name of the salesperson who made the sale, and the car make and model, as well as the name of the buyer.
    # Typical calling examples: print(order) where order is an instance of the Order class.
    # Accessibility: Public.
    # Function prototype: def __str__(self):
    def __str__(self):
        salesBy = self.salesBy.__str__()
        salesBy = " ".join(salesBy.split(" ")[:3])
        return f"Order #{self.id} {bcolors.BOLD}Made by {salesBy}{bcolors.ENDC}: {self.car.getCarInfo()['make']} {self.car.getCarInfo()['model']} for {bcolors.BOLD}{self.buyer.getLastName()}, {self.buyer.getFirstName()}{bcolors.ENDC}"
    


    # One-line description: Check equality of two Order objects.
    # General description: The function checks whether two Order objects are equal by comparing their IDs.
    # Typical calling example:
    #   order1 = Order(...)
    #   order2 = Order(...)
    #   if order1 == order2:
    #       print("The two orders are equal")
    # Accessibility: Public.
    # Function prototype: def __eq__(self, value) -> bool:.
    def __eq__(self, value) -> bool:
        if isinstance(value, Order):
            return value.id == self.id
        return False
    


    # One-line description: Returns the string representation of the car object.
    # General description: This function returns the string representation of the car object contained in the order.
    # Typical calling example: print(order.__repr__())
    # Accessibility: Public.
    # Function prototype: def __repr__(self) -> str:
    def __repr__(self) -> str:
        return f"{self.car}"
