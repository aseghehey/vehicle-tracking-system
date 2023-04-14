####################################################################################################################
'''
////////////////
PROGRAM orders:   
The code defines a class called "Order" representing an order made by a buyer for a car,
containing information such as the buyer, car, salesperson, date of purchase, and order ID,
with various methods to manipulate and retrieve information about the order.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu

////////////////
VERSION 1: written [day] [month] 2023 by [firstInitial]. [lastName]
REVISION [revision# ex: 1.1]: [day] [month] 2023 by [firstInitial]. [lastName] to [purpose of revision]

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

     # Returns the buyer of the order
    def getUser(self):
        return self.buyer
    
    # Returns the car of the order
    def getCar(self):
        return self.car
    
    # Returns the salesperson of the order
    def getSeller(self):
        return self.salesBy
    
    # Returns the date of the order
    def getDate(self):
        return self.when
    
    # Returns the ID of the order
    def getId(self):
        return self.id
    
    # Returns the date of purchase in the YYYY-MM-DD format
    def getDateJoined(self):
        return self.when.strftime("%Y-%m-%d")
    
    # Converts the Order object into a dictionary
    def to_dict(self):
        return {
            "id": self.id,
            "carVin": self.car.getVin(),
            "buyer": self.buyer.getEmail(),
            "soldBy": self.salesBy.getUsername(),
            "dateBought": self.when.strftime("%Y-%m-%d")
        }
    
    # Serializes the Order object into a JSON serializable format
    def serialize(order):
        if isinstance(order, Order):
            return order.to_dict()
        raise TypeError("Object of type 'Order' is not JSON serializable")

    # Removes the order from the buyer's orders list and sets the car status to available
    def RemoveOrder(self):
        self.buyer.orders.remove(self)
        self.car.SetStatus("available")
    
    # Returns details of the order including car, salesperson, and customer
    def orderDetails(self):
        toret = f"\nCar:\n{self.car.getDetails()}\n\nSales by: {self.salesBy}\n\nCustomer {self.buyer.getDetails()}\n"
        return toret

    # Returns a string representation of the order object
    def __str__(self):
        salesBy = self.salesBy.__str__()
        salesBy = " ".join(salesBy.split(" ")[:3])
        return f"Order #{self.id} {bcolors.BOLD}Made by {salesBy}{bcolors.ENDC}: {self.car.getCarInfo()['make']} {self.car.getCarInfo()['model']} for {bcolors.BOLD}{self.buyer.getLastName()}, {self.buyer.getFirstName()}{bcolors.ENDC}"
    
    # Overriding the equality operator to compare two Order objects
    def __eq__(self, value) -> bool:
        if isinstance(value, Order):
            return value.id == self.id
        return False
    
    # return car object string representation
    def __repr__(self) -> str:
        return f"{self.car}"
