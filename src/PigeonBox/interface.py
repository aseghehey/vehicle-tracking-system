####################################################################################################################
'''
////////////////
PROGRAM interface:   contains classes and functions to manage the car dealership's interface,
                     allowing employees and admins to view, manage, and 
                     update car inventory, customers, orders, and user accounts.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

////////////////
PURPOSE:
- InterfaceObjects is a base class that manages the interface objects and mapping functions.

- Interface is a subclass of InterfaceObjects and contains all the methods for managing the 
  system's car, customer, users, and orders. 

Methods:
-InterfaceObjects:
- init: Initializes the interface object and loads the orders from json.
- usernameToUser: Maps a username to a user.
- vinToCar: Maps a VIN to a vehicle.
- emailToCustomer: Maps an email address to a customer.
- getCustomerList: Returns the customer list.
- getEmployeeList: Returns the employee list.
- isEmployee: Returns whether the user is an employee.
- ViewUsers: Returns all users.
- vinExists: Returns whether the given VIN is in the inventory.
- inInventory: Returns whether the given vehicle is in the inventory.
- ViewByStatus: Returns the list of vehicles with the given status.
- GetInventory: Returns the inventory list.
- searchInventory: Given relevant info, finds and returns a car object.
- ViewAvailableInventory: Returns the list of available vehicles.
- UserExists: Returns whether the given user exists.
- UsernameExists: Returns whether the given username exists.

-Interface:
- init: Initializes the interface object and loads the orders from json.
- changeCarStatus: Changes the status of a car.
- changeCarPrice: Changes the price of a car.
- changeCarMileage: Changes the mileage of a car.

////////////////
DATA STRUCTURES:
DataStructures:
- Lists: uses lists to store data such as inventory, orders, customers, employees, and admins.
- Dictionaries: uses dictionaries to store orders, with the order ID as the key 
                and the order details as the value.
- Tuples: uses tuples to store information such as the make, model, and year of a car.

Attributes:
No explicit attributes
- self.inventory: a list of vehicle objects representing the current inventory.
- self.customers: a list of customer objects representing the current customers.
- self.employees: a list of employee objects representing the current employees.
- self.admins: a list of admin objects representing the current admins.
- self.__users__: a list of all users (i.e., employees and admins), used as a helper.
- self.ordersDict: a dictionary representing the current orders (loaded from JSON).
- self.orders: a list of order objects representing the current orders.
- self.isObjListUpdated: a list of boolean values indicating whether a certain object list 
                         has been updated (e.g., the inventory, orders, etc.).
                         The list is indexed as follows: 0 = inventory, 1 = orders, 2 = users, 3 = customers.

////////////////
ALGORITHM:
algorithms used are simple. focused more on implementing logic for the system.
- Linear Search Algorithm: usernameToUser, vinToCar, emailToCustomer, searchInventory.
- Conditional Statemetns: ViewByStatus, inInventory, UserExists, UsernameExists, vinExists.
- Iteration: ViewAvailableInventory, getCustomerList, getEmployeeList, ViewUsers.

////////////////
ERROR HANDLING:
No explicit error handling.

////////////////
'''
####################################################################################################################

from parsers import *
from PigeonBox import session, status, orders, users, vehicles




#   A class for managing the interface objects and mapping functions.
class InterfaceObjects():


    # One-line description: Initializes an instance of a class with inventory, customers, employees, admins, and users.
    # General description: This function is an initializer method that creates an instance of a class 
    #   with various data attributes such as inventory, customers, 
    #   employees, admins, and users. It also loads the data using the readJson and session modules 
    #   to provide the required data to the instance.
    # Typical calling examples: An instance of the class is created using my_instance = ClassName()
    # Accessibility: Public
    # Function prototype: def __init__(self) -> None:
    def __init__(self) -> None:
        self.inventory = readJson.LoadInventory()
        self.customers = readJson.LoadCustomers()
        self.employees = session.Session().ReturnEmployees()
        self.admins = session.Session().ReturnAdmins()
        self.__users__ = self.employees + self.admins # helper


    '''mapper functions'''
    # One-line description: Converts a given username to a corresponding user object if it exists in the system.
    # General description: Searches the list of employees and admins in the system to match the given username to the user's username. 
    #   If found, it returns the user object. Otherwise, it returns None.
    # Typical calling examples: system.usernameToUser('john123')
    # Accessibility: Public method
    # Function prototype: def usernameToUser(self, username: str) -> Union[User, None]:
    def usernameToUser(self, username):
        for user in self.__users__:
            if user.getUsername() == username:
                return user
    


    # One-line description: This function returns a Car object based on its Vehicle Identification Number (VIN).
    # General description: This function takes a VIN as input and searches the inventory for a car that matches the given VIN.
    #   Once found, it returns the Car object that matches the VIN. If no match is found, it returns None.
    # Typical calling examples:
    #   car = vinToCar('ABC123456789')
    # Accessibility: Public
    # Function prototype: def vinToCar(self, vin: str) -> Union[Car, None]:
    def vinToCar(self, vin):
        for car in self.inventory:
            if car.getVin() == vin:
                return car
    


    # One-line description: Get customer object by email address.
    # General description: This function searches the list of customers for the customer object that matches 
    #   the given email address and returns it.
    # Typical calling examples:
    #   customer = emailToCustomer('john.doe@example.com')
    # Accessibility: Public.
    # Function prototype: def emailToCustomer(self, emailAddress) -> Union[Customer, None]:
    def emailToCustomer(self, emailAddress):
        for customer in self.customers:
            if customer.getEmail() == emailAddress:
                return customer
    


    # One-line description: Returns the list of all customers.
    # General description: This method returns the list of all customers in the system.
    # Typical calling example: customer_list = my_system.getCustomerList()
    # Accessibility: Public.
    # Function prototype: def getCustomerList(self) -> List[Customer]:
    def getCustomerList(self):
        return self.customers
    


    # One-line description: Returns a list of all employees.
    # General description: This function returns a list of all employees. It gets the list of employees by 
    #   calling the ReturnEmployees() method from the session module.
    # Typical calling examples:
    #   inventory_system = InventorySystem()
    #   employee_list = inventory_system.getEmployeeList()
    # Accessibility: Public
    # Function prototype: def getEmployeeList(self) -> List[Employee]:
    def getEmployeeList(self):
        return self.employees


    # One-line description: Checks whether the given user is an employee or not.
    # General description: The isEmployee function takes a user object as an argument and returns a boolean value indicating whether the user is an employee or not.
    #   It does this by checking if the given user is present in the list of employees stored in the object.
    # Typical calling examples:
    #   is_employee = obj.isEmployee(user)
    # Accesibility: Public.
    # Function prototype:def isEmployee(self, user) -> bool:
    def isEmployee(self, user):
        return user in self.employees


    # One-line description: Returns the list of all users in the system.
    # General description: This method returns the list of all users (both employees and admins) in the system.
    # Typical calling examples:
    #   user_list = ViewUsers(): returns the list of all users in the system.
    # Accessibility: This method is a public method and can be accessed from outside the class.
    # Function prototype: def ViewUsers(self) -> List[Union[Employee, Admin]]:. 
    #   The method takes no parameters and returns a list of Employee and Admin objects.
    def ViewUsers(self):
        return self.__users__
    


    # One-line description: Check if a VIN (Vehicle Identification Number) exists in the inventory.
    # General description: This function takes a VIN as input and checks if it exists in the inventory by iterating through each car object in the inventory
    #    list and comparing its VIN to the input VIN. If the VIN exists, it returns True; otherwise, it returns False.
    # Typical calling example: vinExists('12345678901234567')
    # Accessibility: Public.
    # Function prototype: def vinExists(self, vin: str) -> bool:
    def vinExists(self, vin):
        for car in self.inventory:
            if car.getVin() == vin:
                return True
        return False
    


    # One-line description: Check if a car is in the inventory.
    # General description: This function takes in a car object or a VIN (a string) and checks if the car is in the inventory. 
    #   If a car object is given, it compares the object to each car in the inventory using the == operator. If a VIN is given, 
    #   it checks if there is a car in the inventory with that VIN. If the car is found in the inventory, it returns True, otherwise, it returns False.
    # Typical calling examples:
    #   in_inventory = inventory.inInventory(my_car)
    #   in_inventory = inventory.inInventory('1HGCM82633A004352')
    # Accessibility: Public.
    # Function prototype: def inInventory(self, car) -> bool:
    def inInventory(self, car):
        if isinstance(car, str):
            return self.vinExists(car)

        for vehicle in self.inventory:
            if vehicle == car:
                return True
        return False 
    


    # One-line description: Returns a list of vehicles filtered by their status.
    # General description: This function receives a string with a status to filter the inventory by (either "available", "rented" or "maintenance").
    #    It then checks if the status is "available", in which case it calls the ViewAvailableInventory() method. If the status is not "available",
    #    it converts the string to a status object, loops through the inventory and returns a list of vehicles whose status matches the desired one.
    # Typical calling example:
    #   inventory.ViewByStatus("available"): returns a list of available vehicles.
    #   inventory.ViewByStatus("maintenance"): returns a list of vehicles under maintenance.
    # Accessibility: Public.
    # Function prototype: def ViewByStatus(self, statusToViewBy: str) -> List[Vehicle]:
    def ViewByStatus(self, statusToViewBy):
        statusToViewBy = statusToViewBy.lower()

        if (statusToViewBy == 'available'):
            return self.ViewAvailableInventory()

        viewStatus = status.strToStatus(statusToViewBy)
        filteredByStatus = []
        for car in self.inventory:
            if car.getStatus() == viewStatus:
                filteredByStatus.append(car)

        return filteredByStatus
    

    # One-line description: Get the inventory of the car dealership.
    # General description: This function returns a list of cars in the inventory of the car dealership.
    # Typical calling examples:
    #   dealer = CarDealership(): Create a CarDealership object.
    #   inventory = dealer.GetInventory(): Get the inventory of the car dealership.
    # Accessibility: Public.
    # Function prototype: def GetInventory(self) -> List[Car]:.
    def GetInventory(self):
        return self.inventory
    


    # One-line description: Search inventory by car model, make, and year and return car object if found.
    # General description: This function searches for a car in the inventory list by matching its model, 
    #   make, and year with the provided parameters. If a car is found, the function returns its object; otherwise, it returns None.
    # Typical calling example: searched_car = searchInventory('Sedan', 'Honda', '2021')
    # Accessibility: This function is accessible within the class it belongs to.
    # Function prototype: def searchInventory(self, model: str, make: str, year: str) -> Optional[Car]:
    def searchInventory(self, model, make, year):
        """ Given relevant info, finds and returns a car object"""
        for car in self.inventory:
            info = car.getCarInfo()
            if model == info['model'] and make == info['make'] and year == info['year']:
                return car
    


    # One-line description: Returns a list of available vehicles in the inventory.
    # General description: This function returns a list of all available vehicles in the inventory by checking their status.
    # Typical calling examples:
    # my_inventory.ViewAvailableInventory()
    # Accessibility: Public
    # Function prototype: def ViewAvailableInventory(self) -> List[Vehicle]:
    def ViewAvailableInventory(self):
        available = []
        for vehicle in self.inventory:
            if vehicle.getStatus() == status.Status.AVAILABLE:
                available.append(vehicle)
        return available
    


    # One-line description: Checks if a user exists in the list of users.
    # General description: This method checks if a user exists in the list of users, which can be either customers or employees.
    #    It returns True if the user exists and False otherwise.
    # Typical calling examples:
    #   userManagement.UserExists('username123') - Check if a user with the username 'username123' exists in the user list.
    #   userManagement.UserExists(employeeObj) - Check if an employee object exists in the user list.
    # Accessibility: Public
    # Function prototype: def UserExists(self, checkUser)
    def UserExists(self, checkUser):
        """ Useful for when we want to add or remove an employee"""
        if (isinstance(checkUser, str)):
            return self.UsernameExists(checkUser)
        
        for user in self.__users__:
            if user == checkUser:
                return True
        return False
    


    # One-line description: Checks if a username already exists in the list of users.
    # General description: This function iterates over the list of users, and returns 
    #   True if a user with the given username already exists in the list, and False otherwise.
    # Typical calling examples:
    #   if system.UsernameExists("johndoe"): print("Username already exists!")
    # Accessibility: This function is a method of a class and can be called from any instance of that class.
    # Function prototype: def UsernameExists(self, username: str) -> bool:
    def UsernameExists(self, username):
        for user in self.__users__:
            if user.getUsername() == username:
                return True
        return False



#   Interface is the class that contains all the methods for managing the system's car, customer, users, and orders.
class Interface(InterfaceObjects):


    # One-line description: Initializes an object of the class and loads orders from a JSON file.
    # General description: Initializes an object of the class, loads orders from a JSON file 
    #   using the LoadOrders() method from the readJson module, and creates a list of orders.Order objects from the data read in.
    # Typical calling examples: myObject = MyClass().
    # Accessibility: Public.
    # Function prototype: def __init__(self) -> None:.
    def __init__(self) -> None:
        super().__init__()
        #   loads orders from json
        self.ordersDict = readJson.LoadOrders() # have to pass customers and car functionality to correctly add to buyers list and such
        self.orders = []
        for order in self.ordersDict:
            self.orders.append(orders.Order(id=order['id'], 
                                            car=self.vinToCar(order['carVin']), 
                                            buyer=self.emailToCustomer(order['buyer']), 
                                            employee=self.usernameToUser(order['soldBy']), 
                                            dateBought=order['dateBought']))
        # 0: inv, 1: order, 2: users, 3: customer
        self.isObjListUpdated = [False] * 4
        # loading customer orders if there's any
        for order in self.orders:
            currentCustomer = order.getUser()
            for customer in self.customers:
                if customer == currentCustomer:
                    customer.orders.append(order)



    # One-line description: Change the status of a car and mark the inventory list as updated.
    # General description: This function takes a car object and a status as arguments, and updates 
    #   the status of the car to the provided status. The function also marks the inventory list as updated
    #    by setting the first element of isObjListUpdated to True.
    # Typical calling examples: carRental.changeCarStatus(carObject, "rented")
    # Accessibility: This function is accessible within the CarRental class.
    # Function prototype: def changeCarStatus(self, car: Car, status: str) -> None
    def changeCarStatus(self, car, status):
        car.SetStatus(status)
        self.isObjListUpdated[0] = True



    # One-line description: Update the price of a car and set a flag for the inventory list as updated.
    # General description: This function takes a car object and a new price as input, and calls the UpdatePrice
    #   method of the car object to update its price. It also sets a flag in the isObjListUpdated list indicating
    #   that the inventory list has been updated.
    # Typical calling examples:
    #   changeCarPrice(my_car, 15000) where my_car is a car object and 15000 is the new price.
    #   changeCarPrice(self.inventory[3], 12000) where self.inventory[3] is a car object and 12000 is the new price.
    # Accessibility: This function is accessible within the class where it is defined.
    # Function prototype: def changeCarPrice(self, car, newPrice):
    def changeCarPrice(self, car, newPrice):
        car.UpdatePrice(newPrice)
        self.isObjListUpdated[0] = True
    

    # One-line description: Update mileage of a car object and set isObjListUpdated flag to True.
    # General description: This function takes a car object and a new mileage as input,
    #   then updates the car's mileage with the new value and sets the isObjListUpdated flag for the inventory list to True.
    # Typical calling examples:
    #   changeCarMileage(car_object, 5000)
    #   changeCarMileage(car_object, 12000)
    # Accessibility: This function is an instance method and can be accessed within the class it belongs to.
    # Function prototype: def changeCarMileage(self, car, newMileage):
    def changeCarMileage(self, car, newMileage):
        car.UpdateMileage(newMileage)
        self.isObjListUpdated[0] = True



    # One-line Description: Update the email of a given customer object.
    # General Description: This function takes a customer object and a new email address as input parameters,
    #   and updates the customer's email to the new email address. It also sets the isObjListUpdated flag t
    #    True for the customer list.
    # Typical calling examples:
    #   dealership.changeCustomerEmail(customerObj, "newemail@example.com")
    # Accessibility: Public method
    # Function prototype: def changeCustomerEmail(self, customer, newEmail):
    def changeCustomerEmail(self, customer, newEmail):
        customer.setEmail(newEmail)
        self.isObjListUpdated[3] = True



    # One-line description: Change a customer's credit card information
    # General description: This function updates a customer's credit card information with the newCard provided.
    #   It updates the customer object and sets the isObjListUpdated flag for customers to True, indicating that the
    #   customer list needs to be updated in the database.
    # Typical calling examples: changeCustomerCard(my_customer, "1234 5678 9101 1121")
    # Accessibility: This function is a method of a class and can be accessed by instances of that class.
    # Function prototype: def changeCustomerCard(self, customer, newCard):
    def changeCustomerCard(self, customer, newCard):
        customer.setCard(newCard)
        self.isObjListUpdated[3] = True
    


    # One-line description: Updates the address of a customer and sets a flag to indicate that the customer list has been updated.
    # General description: This function takes a customer object and a new address as inputs, and updates the customer's
    #   address to the new one. It also sets a flag to indicate that the customer list has been updated.
    # Typical calling examples:
    #   changeCustomerAddress(customer_obj, '123 Main St.')
    # Accessibility: This function is a member of a class and can be accessed within the class.
    # Function prototype: def changeCustomerAddress(self, customer, newAddress):
    def changeCustomerAddress(self, customer, newAddress):
        customer.setAddress(newAddress)
        self.isObjListUpdated[3] = True



    # One-line description: Changes the password of an admin or employee user.
    # General description: This function takes a user object and a new password as input and changes 
    #   the password of the user if they are an admin or employee user.
    #   If the user is an admin or employee, their password is updated with the new password, 
    #   and the corresponding flag in isObjListUpdated is set to true.
    # Typical calling examples:
    #   changeUserPassword(admin_user, "new_password")
    #   changeUserPassword(employee_user, "new_password")
    # Accessibility: This function is accessible within the class where it is defined.
    # Function prototype: def changeUserPassword(self, user, newPassword):
    def changeUserPassword(self, user, newPassword):
        for admin in self.admins:
            if admin == user:
                admin.UpdatePassword(newPassword)
                self.isObjListUpdated[2] = True
                return
        
        for employee in self.employees:
            if employee == user:
                employee.UpdatePassword(newPassword)
                self.isObjListUpdated[2] = True
                return
            


    # One-line description: A function to change the username of an admin or an employee in a car dealership system.
    # General description: This function takes two parameters, a user object and a new username string, and changes the username of the user object to the new username. 
    #   The user object can be an admin or an employee, and the function checks which one it is by iterating through the list of admins and employees.
    #   If the user object is found in either list, the function updates the username of the user object and sets the corresponding index of the isObjListUpdated list to True.
    # Typical calling examples:
    #   changeUserUsername(admin_object, "new_username")
    #   changeUserUsername(employee_object, "new_username")
    # Accessibility: This function can be accessed by any part of the program that has access to the object it needs to update, 
    #   as well as the dealership object that contains the lists of admins and employees.
    # Function prototype:def changeUserUsername(self, user: Union[Admin, Employee], newUsername: str) -> None:
    def changeUserUsername(self, user, newUsername):
        for admin in self.admins:
            if admin == user:
                admin.UpdateUserName(newUsername)
                self.isObjListUpdated[2] = True
                return
        
        for employee in self.employees:
            if employee == user:
                employee.UpdateUserName(newUsername)
                self.isObjListUpdated[2] = True
                return
    

    # One-line description: Returns the list of orders.
    # General description: This function returns the list of orders that have been loaded from a JSON file in the class constructor.
    # Typical calling examples:
    #   orderList = myDealer.viewOrders()
    #   for order in myDealer.viewOrders(): print(order)
    # Accessibility: Public
    # Function prototype: def viewOrders(self) -> List[Order]:
    def viewOrders(self):
        return self.orders
    


    # One-line description: Returns the list of orders.
    # General description: This function returns the list of orders stored in the object.
    # Typical calling examples: order_list = object.getOrderslist()
    # Accessibility: Public
    # Function prototype: def getOrderslist(self) -> List[Order]:
    def getOrderslist(self):
        return self.orders
    


    #   Returns True if the car is already ordered.
    def isCarOrdered(self, car) -> bool:
        for order in self.orders:
            if order.getCar() == car:
                return True
        return False
    


    # One-line description: Checks if a car has been ordered.
    # General description: This function takes a car object as an argument and iterates over all orders 
    #   to check if the given car is present in any of the orders.
    # Typical calling examples:
    #   car1_ordered = self.isCarOrdered(car1)
    # Accessibility: This function is a method of a class and can be accessed within the class or its instances.
    # Function prototype: def isCarOrdered(self, car) -> bool:
    def doesOrderExist(self, checkOrder) -> bool:
        for order in self.orders:
            if order == checkOrder:
                return True
        return False
    


    # One-line description: Creates an order object for a given customer, vehicle, and seller and adds it to the order list.
    # General description: The MakeOrder function creates an order object for a given customer, vehicle, and seller, 
    #   hecks that the vehicle is available, adds the order to the order list, and updates the customer's order list.
    #   It also sets a flag indicating that the order list has been updated so that it can be written to a JSON file. 
    #   The function returns the created order object.
    # Typical calling examples:
    #   MakeOrder(customer, vehicle, seller): creates an order object for the given customer, vehicle, and seller and adds it to the order list.
    # Accessibility: This function is part of a class and can be accessed by an instance of the class.
    # Function prototype:def MakeOrder(self, customer, vehicle, seller):
    def MakeOrder(self, customer, vehicle, seller):
        # check that a vehicle is available before making an order
        if not vehicle.isAvailable(): return
        id = self.orders[-1].getId() + 1 if self.orders else 1
        order = orders.Order(id, vehicle, customer, employee=seller) # create order object
        # add order to order list and deal with the customer dependency
        self.orders.append(order)
        customer.orders.append(order)
        self.isObjListUpdated[1] = True # to write to json -- orders have been updated
        return order
    


    # One-line description: Remove an order from the orders list and update the car status.
    # General description: This function removes an order from the orders list and updates the car status.
    #   It also removes the order from the users' order list and frees up the memory by deleting the order object.
    # Typical calling examples: car_dealership.UndoOrder(order).
    # Accessibility: This function is a method of a class, and it can be accessed by an instance of the class.
    # Function prototype: def UndoOrder(self, order).
    def UndoOrder(self, order):
        # will remove an order from the orders list and update the car status
        # also removes order from the users.orders list
        if not self.doesOrderExist(order): 
            return
        
        self.orders.remove(order)
        order.RemoveOrder()
        del order # delete order object and free up memory

        self.isObjListUpdated[1] = True



    # One-line description: Checks if an email exists in the customer list.
    # General description: This function takes an email as input and iterates through the list of customers in the object. 
    #   If it finds a customer with the same email as the input, it returns True. Otherwise, it returns False.
    # Typical calling examples:
    #   Checking if a customer with a particular email already exists in the customer list.
    # Accessibility: This function is a method of a class and can only be accessed by instances of the class.
    # Function prototype: def emailExists(self, email) -> bool:
    def emailExists(self, email):
        for customer in self.customers:
            if customer.getEmail() == email:
                return True
        return False



    # One-line description: Check if a given customer exists in the list of customers.
    # General description: This function checks if a given input is a customer object or a string email address of a customer, 
    #   and then searches for the customer object in the list of customers. If the input is a string email address,
    #    it calls the emailExists function to determine if there is a customer with that email in the list of customers.
    # Typical calling examples:
    #   is_customer = dealership.isCustomer('customer1@gmail.com')
    #   is_customer = dealership.isCustomer(customer_obj)
    # Accessibility: This function is a method of a class, so it is accessible to any instance of that class.
    # Function prototype: def isCustomer(self, newCustomer) -> bool:
    def isCustomer(self, newCustomer):

        if isinstance(newCustomer, str):
            return self.emailExists(newCustomer)

        for customer in self.customers:
            if customer == newCustomer:
                return True
        return False



    # One-line description: Adds a new customer to the list of customers.
    # General description: This function adds a new customer to the list of customers in the system. It first checks if the customer with the given email 
    #   already exists in the system using the isCustomer function. If the customer exists, the function returns without making any changes. 
    #   If the customer doesn't exist, the function creates a new Customer object using 
    #   the provided first name, last name, card number, email, and address, and appends it to the list of customers.
    #    It also sets the isObjListUpdated flag to True, indicating that the list of customers has been updated.
    # Typical calling examples:
    #   AddCustomer("John", "Doe", "1234567890", "john.doe@example.com", "123 Main St.")
    # Accessibility: Public.
    # Function prototype:def AddCustomer(self, first: str, last: str, card: str, email: str, address: str) -> Optional[users.Customer]:
    def AddCustomer(self, first, last, card, email, address):
        if self.isCustomer(email):
            return
        newCustomer = users.Customer(first, last, card, email, address)
        self.customers.append(newCustomer)
        self.isObjListUpdated[3] = True
        return newCustomer



    # One-line description: Removes a given customer and their orders from the system, and sets any ordered car that has not been delivered to backorder status.
    # General description: This function takes a customer object as an argument, and then removes the customer and any orders they have made from the
    #    system. If a car associated with the customer has not been delivered, its status is set to backorder. The function updates the customers list and isObjListUpdated flag accordingly.
    # Typical calling examples:
    #   system.RemoveCustomer(customer1) - Removes customer1 and their orders from the system.
    #    system.RemoveCustomer(system.customers[2]) - Removes the third customer in the customers list from the system.
    # Accessibility: This function is a method of a class, so it can be called on an instance of the class.
    # Function prototype: def RemoveCustomer(self, customer):
    def RemoveCustomer(self, customer):
        """delete from orders if they exist AND set car to available if customer has been deleted """
        # grab customer orders
        customerOrders = []
        for order in self.orders:
            if order.getUser() == customer:
                customerOrders.append(order)
                if order.getCar().getStatus() != status.Status.ORDERED: # if car has not been delivered yet
                    order.getCar().setStatus(status.Status.BACKORDER)
        # delete orders for customers:
        while customerOrders:
            order = customerOrders.pop()
            self.UndoOrder(order)
        # delete customer
        self.customers.remove(customer)
        del customer
        self.isObjListUpdated[3] = True


    # One-line description: Saves changes to JSON files and logs the user out of the system.
    # General description: This function is responsible for saving any changes made to the JSON 
    #   files during the user's session and logging the user out of the system. It checks which JSON files 
    #   have been updated and calls the writeJson function to write the changes to the corresponding files.
    # Typical calling examples: LogOut()
    # Accessibility: This function can be accessed by any logged-in user.
    # Function prototype: def LogOut(self) -> None:
    def LogOut(self):
        if self.isObjListUpdated[0]:
            writeJson.writeJson(self.inventory)
        if self.isObjListUpdated[1]:
            writeJson.writeJson(self.orders)
        if self.isObjListUpdated[2]:
            allUsers = self.admins + self.employees
            writeJson.writeJson(allUsers)
        if self.isObjListUpdated[3]:
            writeJson.writeJson(self.customers)





#   AdminInterface is a subclass of Interface and allows an admin to perform additional operations such as adding or removing employees
#   and adding or removing cars from inventory.
class AdminInterface(Interface):
    """ Admin can do everything an employee can do and MORE, hence why it has its own class, which inherits all the methods from Interface
        but an admin can add and remove employees, and add and remove cars from inventory """



    # One-line description: Add a new admin user to the system.
    # General description: This function adds a new admin user to the system with the provided username, password, first and last name,
    #    and optional date joined. It first checks if the username already exists in the system, and if so, returns False. 
    #   Otherwise, it creates a new Admin object with the provided information, appends it to the admins list, sets the isObjListUpdated flag to True, and returns True.
    # Typical calling examples:
    #   addAdmin("admin1", "password", "John", "Doe")
    #   ddAdmin("admin2", "password", "Jane", "Doe", "2022-01-01")
    # Accessibility: This function is a method of a class and can be accessed within the class and its instances.
    # Function prototype: def AddAdmin(self, username, passwd, fname, lname, dateJoined=None) -> bool:
    def AddAdmin(self, username, passwd, fname, lname, dateJoined=None):
        if self.UserExists(username):
            return False
        
        newAdmin = users.Admin(username, passwd, fname, lname, date_joined=dateJoined)
        self.admins.append(newAdmin)
        self.isObjListUpdated[2] = True
        return True



    # One-line Description: Adds a new employee user to the system.
    # General Description: This function takes in the employee's username, password, first and last name, and optional date of joining as arguments.
    #   It creates a new Employee object with the provided information and appends it to the list of employees. 
    #   The function returns True if the operation is successful and False if the user already exists in the system.
    # Typical Calling Examples:
    #   dealership.AddEmployee("john.doe", "password123", "John", "Doe")
    #    dealership.AddEmployee("jane.smith", "password456", "Jane", "Smith", "2022-01-01")
    # Accessibility: Public.
    # Function Prototype: def AddEmployee(self, username: str, passwd: str, fname: str, lname: str, dateJoined: str = None) -> Union[bool, None]
    def AddEmployee(self, username, passwd, fname, lname, dateJoined=None) -> None:
        if self.UserExists(username):
            return False
        
        newEmployee = users.Employee(username, passwd, fname, lname, date_joined=dateJoined)
        self.employees.append(newEmployee)
        self.isObjListUpdated[2] = True
        return True
    


    # One-line description: Returns a list of orders made by a given user.
    # General description: This function takes a user as input and iterates through all the orders in the inventory.
    #    For each order, it checks if the seller matches the given user. If it does, the order is appended to a list of orders. 
    #   Finally, the function returns the list of orders made by the user.
    # Typical calling examples: orders = inventory.ordersMadeByUser(user)
    # Accessibility: This function is a method of the Inventory class.
    # Function prototype: def ordersMadeByUser(self, user: Union[users.Customer, users.Employee, users.Admin]) -> List[orders.Order]:
    def ordersMadeByUser(self, user):
        orders = []
        for order in self.orders:
            if order.getSeller() == user:
                orders.append(order)
        return orders



    # One-line description: Removes a user from the system and all orders made by that user.
    # General Description: This function takes a user object as input and removes the user from the system.
    #   It also removes all orders made by that user. The function returns True if the user is successfully 
    #   removed, otherwise it returns False.
    # Typical calling examples:
    #   RemoveUser(admin) # Removes the given admin from the system
    #   RemoveUser(employee) # Removes the given employee from the system
    #   RemoveUser(customer) # Removes the given customer from the system
    # Accessibility: Public
    # Function prototype:def RemoveUser(self, userToRemove) -> bool:
    def RemoveUser(self, userToRemove) -> bool:
        if not self.UserExists(userToRemove):
            return False

        # remove all orders made by that user
        userOrders = self.ordersMadeByUser(userToRemove)
        if userOrders:
            for order in userOrders:
                self.UndoOrder(order)

        if (isinstance(userToRemove, users.Admin)):
            self.admins.remove(userToRemove)
        else:
            self.employees.remove(userToRemove)

        self.__users__.remove(userToRemove)
        self.isObjListUpdated[2] = True
        return True



    # One-line description: Add a new car to the inventory if it doesn't already exist.
    # General description: This function adds a new car to the inventory if it doesn't already exist. It first checks if the car already exists
    #    in the inventory, and if it does, it returns False.
    #   If the car does not exist in the inventory, it creates a new instance of the Car class and appends it to the inventory list. 
    #   The function then sets the isObjListUpdated flag to True to indicate that the inventory list has been updated.
    # Typical calling examples:
    #   car_dealer.AddInventory('123456789', '2023 Toyota Camry', 8, 9, 7, 8, 9, 9, 'Platinum Package', 35000)
    #   car_dealer.AddInventory('987654321', '2023 Honda Accord', 9, 8, 7, 9, 8, 8, 'Touring Package', 32000, status.Status.BACKORDER)
    # Accessibility: This function is a method of a CarDealer class object and can be called by an instance of the class.
    # Function prototype:def AddInventory(self, vin: str, info: str, performance: int, design: int, handling: int, comfort: int, 
    #                  entertainment: int, protection: int, package: str, price: float, status: status.Status = None) -> bool:
    def AddInventory(self, vin, info, performance, design, handling, comfort, entertainment, protection, package, price, status=None) -> bool:
        """ checks if car already exist, if it doesn't, adds it to the inventory"""
        if self.inInventory(vin): 
            return False 
        
        newCar = vehicles.Car(vin=vin, info=info, performance=performance, design=design, handling=handling, comfort=comfort, entertainment=entertainment, protection=protection, package=package, price=price, status=status)
        self.inventory.append(newCar) 
        self.isObjListUpdated[0] = True 
        return True 



    # One-line Description: Removes a car from the inventory if it exists, along with any associated orders.
    # General Description: This method removes a car from the inventory, along with any associated orders. First, it checks if the car exists in the inventory. 
    #   If it does, it checks the status of the car. If it is ordered, the method also removes the order associated with the car.
    #    Once the order (if any) is removed, the method proceeds to remove the car from the inventory entirely.
    # Typical Calling Examples:
    #   dealership.RemoveInventory(car)
    #   dealership.RemoveInventory(dealership.inventory[0])
    # Accessibility: Public.
    # Function Prototype: def RemoveInventory(self, car) -> bool:
    def RemoveInventory(self, car) -> bool:
        """ checks if car exists, if it does, checks the status of the car, if it is ordered then it also removes the order
        then proceeds by removing the car entirely from the system"""
        if not self.inInventory(car): return False
        if car.getStatus() == status.Status.ORDERED:
            currentOrder = None
            for order in self.orders:
                if order.getCar() == car: 
                    currentOrder = order 
                    break
            if currentOrder: self.UndoOrder(currentOrder)
        self.inventory.remove(car)
        self.isObjListUpdated[0] = True
        return True
