////////////

Below are each script's function descriptions.
This includes descriptions for readJson.py, writeJson.py, bcolors.py, interface.py, main.py, orders.py, session.py, status.py, users.py, vehicles.py
This includes the function's one line description, general description, typical function call, prototype, accessibility.

///////////
#
#
#
#
#
#
bcolors.py
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Methods:
Name: PrintFormat()
    # One-line description: A function that prints formatted text in different colors.
    # General description: The function takes two parameters, the color status and the text to be printed, and prints the text in the specified color. 
    #   It works like the print()
    #   function but allows the user to select from different color and formatting options.
    # Typical calling examples: PrintFormat("Success", "The operation was successful.") would print "The operation was successful." in green text.
        PrintFormat("Important", "Please enter your credentials.")
    #   would print "Please enter your credentials." in bold text.
    # Accessibility: This function can be accessed from within the module where it is defined.
    # Function prototype: def PrintFormat(color_status, print_info)


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
#
#
#
interface.py
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Methods:
class InterfaceObjects:
Name: init: 
    # One-line description: Initializes an instance of a class with inventory, customers, employees, admins, and users.
    # General description: This function is an initializer method that creates an instance of a class 
    #   with various data attributes such as inventory, customers, 
    #   employees, admins, and users. It also loads the data using the readJson and session modules 
    #   to provide the required data to the instance.
    # Typical calling examples: An instance of the class is created using my_instance = ClassName()
    # Accessibility: Public
    # Function prototype: def __init__(self) -> None:

Name: usernameToUser:
    # One-line description: Converts a given username to a corresponding user object if it exists in the system.
    # General description: Searches the list of employees and admins in the system to match the given username to the user's username. 
    #   If found, it returns the user object. Otherwise, it returns None.
    # Typical calling examples: system.usernameToUser('john123')
    # Accessibility: Public method
    # Function prototype: def usernameToUser(self, username: str) -> Union[User, None]:

Name: vinToCar: 
    # One-line description: This function returns a Car object based on its Vehicle Identification Number (VIN).
    # General description: This function takes a VIN as input and searches the inventory for a car that matches the given VIN.
    #   Once found, it returns the Car object that matches the VIN. If no match is found, it returns None.
    # Typical calling examples:
    #   car = vinToCar('ABC123456789')
    # Accessibility: Public
    # Function prototype: def vinToCar(self, vin: str) -> Union[Car, None]:

Name: emailToCustomer:
    # One-line description: Get customer object by email address.
    # General description: This function searches the list of customers for the customer object that matches 
    #   the given email address and returns it.
    # Typical calling examples:
    #   customer = emailToCustomer('john.doe@example.com')
    # Accessibility: Public.
    # Function prototype: def emailToCustomer(self, emailAddress) -> Union[Customer, None]:

Name: getCustomerList:
    # One-line description: Returns the list of all customers.
    # General description: This method returns the list of all customers in the system.
    # Typical calling example: customer_list = my_system.getCustomerList()
    # Accessibility: Public.
    # Function prototype: def getCustomerList(self) -> List[Customer]:

Name: getEmployeeList: 
    # One-line description: Returns a list of all employees.
    # General description: This function returns a list of all employees. It gets the list of employees by 
    #   calling the ReturnEmployees() method from the session module.
    # Typical calling examples:
    #   inventory_system = InventorySystem()
    #   employee_list = inventory_system.getEmployeeList()
    # Accessibility: Public
    # Function prototype: def getEmployeeList(self) -> List[Employee]:

Name: isEmployee: 
    # One-line description: Checks whether the given user is an employee or not.
    # General description: The isEmployee function takes a user object as an argument and returns a boolean value indicating whether the user is an employee or not.
    #   It does this by checking if the given user is present in the list of employees stored in the object.
    # Typical calling examples:
    #   is_employee = obj.isEmployee(user)
    # Accesibility: Public.
    # Function prototype:def isEmployee(self, user) -> bool:

Name: ViewUsers: 
    # One-line description: Returns the list of all users in the system.
    # General description: This method returns the list of all users (both employees and admins) in the system.
    # Typical calling examples:
    #   user_list = ViewUsers(): returns the list of all users in the system.
    # Accessibility: This method is a public method and can be accessed from outside the class.
    # Function prototype: def ViewUsers(self) -> List[Union[Employee, Admin]]:. 
    #   The method takes no parameters and returns a list of Employee and Admin objects.

Name: vinExists: 
    # One-line description: Check if a VIN (Vehicle Identification Number) exists in the inventory.
    # General description: This function takes a VIN as input and checks if it exists in the inventory by iterating through each car object in the inventory
    #    list and comparing its VIN to the input VIN. If the VIN exists, it returns True; otherwise, it returns False.
    # Typical calling example: vinExists('12345678901234567')
    # Accessibility: Public.
    # Function prototype: def vinExists(self, vin: str) -> bool:

Name: inInventory: 
    # One-line description: Check if a car is in the inventory.
    # General description: This function takes in a car object or a VIN (a string) and checks if the car is in the inventory. 
    #   If a car object is given, it compares the object to each car in the inventory using the == operator. If a VIN is given, 
    #   it checks if there is a car in the inventory with that VIN. If the car is found in the inventory, it returns True, otherwise, it returns False.
    # Typical calling examples:
    #   in_inventory = inventory.inInventory(my_car)
    #   in_inventory = inventory.inInventory('1HGCM82633A004352')
    # Accessibility: Public.
    # Function prototype: def inInventory(self, car) -> bool:

Name: ViewByStatus: 
    # One-line description: Returns a list of vehicles filtered by their status.
    # General description: This function receives a string with a status to filter the inventory by (either "available", "rented" or "maintenance").
    #    It then checks if the status is "available", in which case it calls the ViewAvailableInventory() method. If the status is not "available",
    #    it converts the string to a status object, loops through the inventory and returns a list of vehicles whose status matches the desired one.
    # Typical calling example:
    #   inventory.ViewByStatus("available"): returns a list of available vehicles.
    #   inventory.ViewByStatus("maintenance"): returns a list of vehicles under maintenance.
    # Accessibility: Public.
    # Function prototype: def ViewByStatus(self, statusToViewBy: str) -> List[Vehicle]:

Name: GetInventory: 
    # One-line description: Get the inventory of the car dealership.
    # General description: This function returns a list of cars in the inventory of the car dealership.
    # Typical calling examples:
    #   dealer = CarDealership(): Create a CarDealership object.
    #   inventory = dealer.GetInventory(): Get the inventory of the car dealership.
    # Accessibility: Public.
    # Function prototype: def GetInventory(self) -> List[Car]:.

Name: searchInventory: 
    # One-line description: Search inventory by car model, make, and year and return car object if found.
    # General description: This function searches for a car in the inventory list by matching its model, 
    #   make, and year with the provided parameters. If a car is found, the function returns its object; otherwise, it returns None.
    # Typical calling example: searched_car = searchInventory('Sedan', 'Honda', '2021')
    # Accessibility: This function is accessible within the class it belongs to.
    # Function prototype: def searchInventory(self, model: str, make: str, year: str) -> Optional[Car]:

Name: ViewAvailableInventory: 
    # One-line description: Returns a list of available vehicles in the inventory.
    # General description: This function returns a list of all available vehicles in the inventory by checking their status.
    # Typical calling examples:
    # my_inventory.ViewAvailableInventory()
    # Accessibility: Public
    # Function prototype: def ViewAvailableInventory(self) -> List[Vehicle]:

Name: UserExists:
    # One-line description: Checks if a user exists in the list of users.
    # General description: This method checks if a user exists in the list of users, which can be either customers or employees.
    #    It returns True if the user exists and False otherwise.
    # Typical calling examples:
    #   userManagement.UserExists('username123') - Check if a user with the username 'username123' exists in the user list.
    #   userManagement.UserExists(employeeObj) - Check if an employee object exists in the user list.
    # Accessibility: Public
    # Function prototype: def UserExists(self, checkUser)

Name: UsernameExists:
    # One-line description: Checks if a username already exists in the list of users.
    # General description: This function iterates over the list of users, and returns 
    #   True if a user with the given username already exists in the list, and False otherwise.
    # Typical calling examples:
    #   if system.UsernameExists("johndoe"): print("Username already exists!")
    # Accessibility: This function is a method of a class and can be called from any instance of that class.
    # Function prototype: def UsernameExists(self, username: str) -> bool:


class Interface:
Name: init: 
    # One-line description: Initializes an object of the class and loads orders from a JSON file.
    # General description: Initializes an object of the class, loads orders from a JSON file 
    #   using the LoadOrders() method from the readJson module, and creates a list of orders.Order objects from the data read in.
    # Typical calling examples: myObject = MyClass().
    # Accessibility: Public.
    # Function prototype: def __init__(self) -> None:.

Name: changeCarStatus: 
    # One-line description: Change the status of a car and mark the inventory list as updated.
    # General description: This function takes a car object and a status as arguments, and updates 
    #   the status of the car to the provided status. The function also marks the inventory list as updated
    #    by setting the first element of isObjListUpdated to True.
    # Typical calling examples: carRental.changeCarStatus(carObject, "rented")
    # Accessibility: This function is accessible within the CarRental class.
    # Function prototype: def changeCarStatus(self, car: Car, status: str) -> None

Name: changeCarPrice:
    # One-line description: Update the price of a car and set a flag for the inventory list as updated.
    # General description: This function takes a car object and a new price as input, and calls the UpdatePrice
    #   method of the car object to update its price. It also sets a flag in the isObjListUpdated list indicating
    #   that the inventory list has been updated.
    # Typical calling examples:
    #   changeCarPrice(my_car, 15000) where my_car is a car object and 15000 is the new price.
    #   changeCarPrice(self.inventory[3], 12000) where self.inventory[3] is a car object and 12000 is the new price.
    # Accessibility: This function is accessible within the class where it is defined.
    # Function prototype: def changeCarPrice(self, car, newPrice):

Name: changeCarMileage:
    # One-line description: Update mileage of a car object and set isObjListUpdated flag to True.
    # General description: This function takes a car object and a new mileage as input,
    #   then updates the car's mileage with the new value and sets the isObjListUpdated flag for the inventory list to True.
    # Typical calling examples:
    #   changeCarMileage(car_object, 5000)
    #   changeCarMileage(car_object, 12000)
    # Accessibility: This function is an instance method and can be accessed within the class it belongs to.
    # Function prototype: def changeCarMileage(self, car, newMileage):

Name: changeCustomerEmail(self, customer, newEmail):
    # One-line Description: Update the email of a given customer object.
    # General Description: This function takes a customer object and a new email address as input parameters,
    #   and updates the customer's email to the new email address. It also sets the isObjListUpdated flag t
    #    True for the customer list.
    # Typical calling examples:
    #   dealership.changeCustomerEmail(customerObj, "newemail@example.com")
    # Accessibility: Public method
    # Function prototype: def changeCustomerEmail(self, customer, newEmail):

Name: changeCustomerCard(self, customer, newCard):
    # One-line description: Change a customer's credit card information
    # General description: This function updates a customer's credit card information with the newCard provided.
    #   It updates the customer object and sets the isObjListUpdated flag for customers to True, indicating that the
    #   customer list needs to be updated in the database.
    # Typical calling examples: changeCustomerCard(my_customer, "1234 5678 9101 1121")
    # Accessibility: This function is a method of a class and can be accessed by instances of that class.
    # Function prototype: def changeCustomerCard(self, customer, newCard):

Name: changeCustomerAddress(self, customer, newAddress):
    # One-line description: Updates the address of a customer and sets a flag to indicate that the customer list has been updated.
    # General description: This function takes a customer object and a new address as inputs, and updates the customer's
    #   address to the new one. It also sets a flag to indicate that the customer list has been updated.
    # Typical calling examples:
    #   changeCustomerAddress(customer_obj, '123 Main St.')
    # Accessibility: This function is a member of a class and can be accessed within the class.
    # Function prototype: def changeCustomerAddress(self, customer, newAddress):

Name: changeUserPassword(self, user, newPassword):
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

Name: changeUserUsername(self, user, newUsername):
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

Name: viewOrders(self):
    # One-line description: Returns the list of orders.
    # General description: This function returns the list of orders that have been loaded from a JSON file in the class constructor.
    # Typical calling examples:
    #   orderList = myDealer.viewOrders()
    #   for order in myDealer.viewOrders(): print(order)
    # Accessibility: Public
    # Function prototype: def viewOrders(self) -> List[Order]:

Name: getOrderslist(self):
    # One-line description: Returns the list of orders.
    # General description: This function returns the list of orders stored in the object.
    # Typical calling examples: order_list = object.getOrderslist()
    # Accessibility: Public
    # Function prototype: def getOrderslist(self) -> List[Order]:

Name: isCarOrdered(self, car) -> bool:
    # One-line description: Check if a car has been ordered by a customer.
    # General description: This method checks if a given car has been ordered by a customer by iterating through the 
    #   list of orders stored in the customer object and comparing the car to each order.
    # Typical calling examples: customer.isCarOrdered(car) where customer is an instance of the Customer class and car is an instance of the Car class.
    # Accessibility: This method is a member of the Customer class and can only be called on instances of that class.
    # Function prototype: def isCarOrdered(self, car) -> bool: where self refers to the instance of the Customer class on which 
        the method is being called, car is an instance of the Car class, and the method returns a boolean value.

Name: doesOrderExist(self, checkOrder) -> bool:
    # One-line description: Checks if a car has been ordered.
    # General description: This function takes a car object as an argument and iterates over all orders 
    #   to check if the given car is present in any of the orders.
    # Typical calling examples:
    #   car1_ordered = self.isCarOrdered(car1)
    # Accessibility: This function is a method of a class and can be accessed within the class or its instances.
    # Function prototype: def isCarOrdered(self, car) -> bool:

Name: MakeOrder(self, customer, vehicle, seller):
    # One-line description: Creates an order object for a given customer, vehicle, and seller and adds it to the order list.
    # General description: The MakeOrder function creates an order object for a given customer, vehicle, and seller, 
    #   hecks that the vehicle is available, adds the order to the order list, and updates the customer's order list.
    #   It also sets a flag indicating that the order list has been updated so that it can be written to a JSON file. 
    #   The function returns the created order object.
    # Typical calling examples:
    #   MakeOrder(customer, vehicle, seller): creates an order object for the given customer, vehicle, and seller and adds it to the order list.
    # Accessibility: This function is part of a class and can be accessed by an instance of the class.
    # Function prototype:def MakeOrder(self, customer, vehicle, seller):

Name: UndoOrder(self, order):
    # One-line description: Remove an order from the orders list and update the car status.
    # General description: This function removes an order from the orders list and updates the car status.
    #   It also removes the order from the users' order list and frees up the memory by deleting the order object.
    # Typical calling examples: car_dealership.UndoOrder(order).
    # Accessibility: This function is a method of a class, and it can be accessed by an instance of the class.
    # Function prototype: def UndoOrder(self, order).
    
Name: emailExists(self, email):
    # One-line description: Checks if an email exists in the customer list.
    # General description: This function takes an email as input and iterates through the list of customers in the object. 
    #   If it finds a customer with the same email as the input, it returns True. Otherwise, it returns False.
    # Typical calling examples:
    #   Checking if a customer with a particular email already exists in the customer list.
    # Accessibility: This function is a method of a class and can only be accessed by instances of the class.
    # Function prototype: def emailExists(self, email) -> bool:

Name: isCustomer(self, newCustomer):
    # One-line description: Check if a given customer exists in the list of customers.
    # General description: This function checks if a given input is a customer object or a string email address of a customer, 
    #   and then searches for the customer object in the list of customers. If the input is a string email address,
    #    it calls the emailExists function to determine if there is a customer with that email in the list of customers.
    # Typical calling examples:
    #   is_customer = dealership.isCustomer('customer1@gmail.com')
    #   is_customer = dealership.isCustomer(customer_obj)
    # Accessibility: This function is a method of a class, so it is accessible to any instance of that class.
    # Function prototype: def isCustomer(self, newCustomer) -> bool:

Name: AddCustomer(self, first, last, card, email, address):
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

Name: RemoveCustomer(self, customer):
    # One-line description: Removes a given customer and their orders from the system, and sets any ordered car that has not been delivered to backorder status.
    # General description: This function takes a customer object as an argument, and then removes the customer and any orders they have made from the
    #    system. If a car associated with the customer has not been delivered, its status is set to backorder. The function updates the customers list and isObjListUpdated flag accordingly.
    # Typical calling examples:
    #   system.RemoveCustomer(customer1) - Removes customer1 and their orders from the system.
    #    system.RemoveCustomer(system.customers[2]) - Removes the third customer in the customers list from the system.
    # Accessibility: This function is a method of a class, so it can be called on an instance of the class.
    # Function prototype: def RemoveCustomer(self, customer):

Name: LogOut(self):
    # One-line description: Saves changes to JSON files and logs the user out of the system.
    # General description: This function is responsible for saving any changes made to the JSON 
    #   files during the user's session and logging the user out of the system. It checks which JSON files 
    #   have been updated and calls the writeJson function to write the changes to the corresponding files.
    # Typical calling examples: LogOut()
    # Accessibility: This function can be accessed by any logged-in user.
    # Function prototype: def LogOut(self) -> None:

    
class AdminInterface(Interface)
Name: AddAdmin(self, username, passwd, fname, lname, dateJoined=None):
    # One-line description: Add a new admin user to the system.
    # General description: This function adds a new admin user to the system with the provided username, password, first and last name,
    #    and optional date joined. It first checks if the username already exists in the system, and if so, returns False. 
    #   Otherwise, it creates a new Admin object with the provided information, appends it to the admins list, sets the isObjListUpdated flag to True, and returns True.
    # Typical calling examples:
    #   addAdmin("admin1", "password", "John", "Doe")
    #   ddAdmin("admin2", "password", "Jane", "Doe", "2022-01-01")
    # Accessibility: This function is a method of a class and can be accessed within the class and its instances.
    # Function prototype: def AddAdmin(self, username, passwd, fname, lname, dateJoined=None) -> bool:

Name: AddEmployee(self, username, passwd, fname, lname, dateJoined=None) -> None:
    # One-line Description: Adds a new employee user to the system.
    # General Description: This function takes in the employee's username, password, first and last name, and optional date of joining as arguments.
    #   It creates a new Employee object with the provided information and appends it to the list of employees. 
    #   The function returns True if the operation is successful and False if the user already exists in the system.
    # Typical Calling Examples:
    #   dealership.AddEmployee("john.doe", "password123", "John", "Doe")
    #    dealership.AddEmployee("jane.smith", "password456", "Jane", "Smith", "2022-01-01")
    # Accessibility: Public.
    # Function Prototype: def AddEmployee(self, username: str, passwd: str, fname: str, lname: str, dateJoined: str = None) -> Union[bool, None]

Name: ordersMadeByUser(self, user):
    # One-line description: Returns a list of orders made by a given user.
    # General description: This function takes a user as input and iterates through all the orders in the inventory.
    #    For each order, it checks if the seller matches the given user. If it does, the order is appended to a list of orders. 
    #   Finally, the function returns the list of orders made by the user.
    # Typical calling examples: orders = inventory.ordersMadeByUser(user)
    # Accessibility: This function is a method of the Inventory class.
    # Function prototype: def ordersMadeByUser(self, user: Union[users.Customer, users.Employee, users.Admin]) -> List[orders.Order]:

Name: RemoveUser(self, userToRemove) -> bool:
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

Name: AddInventory(self, vin, info, performance, design, handling, comfort, entertainment, protection, package, price, status=None) -> bool:
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

Name: RemoveInventory(self, car) -> bool:
    # One-line Description: Removes a car from the inventory if it exists, along with any associated orders.
    # General Description: This method removes a car from the inventory, along with any associated orders. First, it checks if the car exists in the inventory. 
    #   If it does, it checks the status of the car. If it is ordered, the method also removes the order associated with the car.
    #    Once the order (if any) is removed, the method proceeds to remove the car from the inventory entirely.
    # Typical Calling Examples:
    #   dealership.RemoveInventory(car)
    #   dealership.RemoveInventory(dealership.inventory[0])
    # Accessibility: Public.
    # Function Prototype: def RemoveInventory(self, car) -> bool:


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
#
#
#
main.py
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Methods:
Name: displayData(data):
    # One-line Description: Display an array of data along with their index.
    # General Description: This function takes an array of data and displays each element in the array along with its index. It first checks whether the array is empty, and if it is, it prints a warning message. If the array is not empty,
    #   the function iterates through each element in the array and prints it along with its index.
    # Typical Calling Examples: displayData([1, 2, 3, 4, 5]) - displays each element in the array along with its index.
    #   displayData([]) - prints a warning message since the array is empty.
    # Accessibility: This function can be accessed from anywhere in the program as long as it has been imported.
    # Function Prototype: def displayData(data) -> None:

Name: StallUntilUserInput():
    # One-line description: Stalls the program and waits for the user to press Enter to continue execution.
    # General description: This function halts program execution until the user presses Enter. 
        It is typically used to pause the program after some output is displayed on the console,
        allowing the user to view the output before the program continues executing.
    # Typical calling examples: StallUntilUserInput()
    # Accessibility: This function can be accessed from anywhere in the program.
    # Function prototype: def StallUntilUserInput():

Name: isEmpty(arr):
    # One-line description: Checks if an array is empty and displays a warning message if it is.
    # General description: This function takes an array as an argument and checks if it is empty. If the array is empty, a warning message is displayed using the PrintFormat 
    #   function and the function returns True. Otherwise, the function returns False.
    # Typical calling examples: isEmpty([]): This will display a warning message saying "No data to display" and return True.
    #   isEmpty([1, 2, 3]): This will return False since the array is not empty.
    # Accessibility: This function can be accessed by any other function within the same module.
    # Function prototype: def isEmpty(arr) -> bool:

Name: validatePassword():
    # One-line description: Function to validate a new password entered by the user, with confirmation.
    # General description: This function prompts the user to enter a new password, and then prompts them to confirm it by entering it again. It then checks if the two passwords
    #   match and are not the same as the old password. If the new password is valid, it returns it.
    # Typical calling examples:newPassword = validatePassword()
    # Accessibility: This function can be accessed from within the program.
    # Function prototype:def validatePassword() -> str:

Name: ChangePasswordMenu():
    # One-line description: A function to change the password of a user through an interface.
    # General description: The function prompts the user to enter a new password, validates the input,
    #   and changes the password of the current user via the interface.
    # Typical calling examples: ChangePasswordMenu()
    # Accessibility: The function can be accessed through the module or script where it is defined.
    # Function prototype: def ChangePasswordMenu() -> None

Name: validateUsername():
    # One-line description: Validates user input for a new username and checks if it is already taken or the same as the old username.
    # General description: This function takes user input for a new username and performs validation to ensure that the input is not 
        empty and that the new username is not the same as the old username. It also checks if the new username is already taken by another user in the system.
    # Typical calling examples:
    # new_username = validateUsername()
    # Accessibility: This function can be accessed within the program where it is defined and can be called from other functions 
        or methods that require user input for a new username.
    # Function prototype:def validateUsername() -> str:

Name: ChangeUsernameMenu():
    # One-line description: Changes the username for a user by taking input from the user.
    # General description: This function presents a menu to the user to change their username. 
        It prompts the user to enter a new username and validates the input. If the input is empty, the function returns without making any changes.
        Otherwise, it calls the changeUserUsername function of the interface module to change the user's username and prints a success message.
    # Typical calling example: ChangeUsernameMenu()
    # Accessibility: This function can be called from any module in the program as long as the interface module is imported.
    # Function prototype: def ChangeUsernameMenu():

Name: ConfirmSelection(response={"y", "yes", "n", "no"}, msg=""):
    # One-line description: A function to confirm a user's selection through a prompt, returning a boolean value.
    # General description: This function displays a warning message with an optional custom message and prompts the user to confirm their selection by typing "y" or "n".
    #   It then returns a boolean value based on the user's response.
    # Typical calling examples:if ConfirmSelection("Are you sure you want to delete this file?"):,if ConfirmSelection(msg="Do you want to save your changes?"):
    # Accessibility: This function can be accessed from anywhere within the program.
    # Function prototype:def ConfirmSelection(response = {"y", "yes", "n", "no"}, msg="") -> bool:

Name: ValidateUserInput(action="action", isNum=False, isEmail=False)
    # One-line Description: Validates user input based on certain conditions like being a number or an email address.
    # General Description: This function validates user input based on certain conditions. 
        It takes in three parameters - action (string), isNum (boolean), and isEmail (boolean). The user is prompted to enter input and the function 
        validates it based on the specified conditions.
    #   If the input is invalid, an appropriate message is displayed and the user is prompted again.
    # Typical Calling Examples:ValidateUserInput(action="age", isNum=True),ValidateUserInput(action="email", isEmail=True)
    # Accessibility: This function can be accessed from anywhere in the code.
    # Function Prototype:def ValidateUserInput(action="action", isNum=False, isEmail=False):

Name: getAction(validSet={"1", "2", "3"}, msg="Enter action:")
    # One-line description: A function to get user input for a valid action from a set of options.
    # General description: The function prompts the user to enter an action and checks whether it is a valid option from a given set of valid actions.
    #   It keeps asking the user to enter a valid action until they do so or exit by entering 'q'.
    # Typical calling examples:action = getAction({"1", "2", "3"}, "Please select an option:"), choice = getAction({"y", "n"}, "Do you want to proceed?")
    # Accessibility: The function can be accessed from within the same module.
    # Function prototype:def getAction(validSet: set[str] = {"1", "2", "3"}, msg: str = "Enter action:") -> Union[str, None]:

Name: PickIndex(arr)
    # One-line description: Displays an array of elements and prompts the user to pick an index to select an element.
    # General description: This function takes an array as input and displays each element in the array with its corresponding index. 
        It then prompts the user to enter an index to select an element from the array.
    #   The function validates the user's input and returns the index of the selected element.
    # Typical calling examples: index = PickIndex(myArray) where myArray is an array of elements.
    # Accessibility: This function is likely to be accessible to all users, as it is a console-based
    #   function that uses simple text input and output.
    # Function prototype:def PickIndex(arr: list) -> int:

Name: SeparateInputToList(inpt)
    # One-line description: A function that takes a string and returns an array of substrings separated by commas after stripping whitespace.
    # General description: This function takes a string as input and splits it into an array of substrings using commas as a separator.
    #   It then removes any leading or trailing whitespace from each substring and returns the resulting array.
    # Typical calling example: input_str = "apple, banana, orange" , fruit_list = SeparateInputToList(input_str)
    # Accessibility: The function can be accessed from within the same module.
    # Function prototype: def SeparateInputToList(inpt: str) -> List[str]:

Name: GetObject(objectList)
    # One-line description: Function to select and return an object from a list based on user's input.
    # General description: This function takes a list of objects as input, calls the PickIndex function 
        to prompt the user to select an object from the list, and returns the selected object. If the user chooses to exit, 
        it returns None. It also prints a success message for the user.
    # Typical calling examples: selected_employee = GetObject(employee_list),selected_car = GetObject(car_list)
    # Accessibility: This function is accessible to anyone who has access to the module where it is defined.
    # Function prototype: def GetObject(objectList):

Name: updateCarStatus(car)
    # One-line description: Update the status of a car in the inventory.
    # General description: This function prompts the user to select a new status for a given car in the inventory,
        then calls the appropriate function from the interface module to update the status of that car.
    # Typical calling example: updateCarStatus("Toyota Camry")
    # Accessibility: This function can be accessed from within the program.
    # Function prototype: def updateCarStatus(car: str) -> None

Name: AddEmployee()
    # One-line description: Function to add a new employee with username, password, first name, and last name and grant admin privileges if desired.
    # General description: This function prompts the user to enter the necessary information to add a new employee to the system, including username, password, first name, and last name.
    #   It also gives the option to grant admin privileges. After validating the input, it calls the AddAdmin() or AddEmployee() function from the interface module to add the employee to the system.
    # Typical calling examples: AddEmployee()
    # Accessibility: This function is likely to be accessible to admin users of a system that uses the interface module.
    # Function prototype:def AddEmployee():

Name: RemoveEmployeeMenu()
    # One-line description: A menu function that allows the user to select an employee from a list and remove them after confirmation.
    # General description: This function displays a menu to the user that lists all employees and prompts the user to select an employee to delete.
         After the user selects an employee, they will be asked to confirm their selection before the employee is removed.
    #   If the user confirms, the function will remove the employee and notify the user of the success or failure.
    # Typical calling examples: RemoveEmployeeMenu()
    # Accessibility: This function is accessible to users who have permission to remove employees.
    # Function prototype: def RemoveEmployeeMenu() -> None

Name: displayStatusOptions()
    # One-line description: Displays the available status options for an inventory and prompts the user to choose one.
    # General description: This function displays a list of available status options for an inventory, such as "Available", "Ordered", "BackOrder", and "Delivered".
    #   It then prompts the user to choose one of the options.
    # Typical calling examples: After displaying the list of status options, this function is often called to obtain the user's selected status for filtering or viewing data.
    # Accessibility: This function appears to be accessible to all users.
    # Function prototype: def displayStatusOptions() -> Union[str, None]:

Name: CarSearch()
    # One-line description: A function that searches for a car in the inventory based on the model, make, and year entered by the user.
    # General description: The CarSearch() function allows the user to search for a car in the inventory by providing the model, make, and year of the car.
    #   The function takes the user's input and validates it before searching for a matching car in the inventory. If a matching car
    #   is found, the function returns the car's details; otherwise, it informs the user that the car was not found.
    # Typical calling examples: CarSearch() can be called when a user wants to search for a specific car in the inventory.
    # Accessibility: The function is accessible to any user of the system.
    # Function prototype: def CarSearch():

Name: filterByMenu()
    # One-line description: Displays a menu to filter cars by their status and displays the filtered data.
    # General description: The filterByMenu() function displays a menu that allows users to filter the car inventory by status,
        which includes available, ordered, backorder, and delivered. It takes user input to select a status, validates the input, and 
    #   then calls the ViewByStatus() function of the interface object to retrieve and display the filtered data.
    # Typical calling examples: filterByMenu() to display the filter menu and filter cars by their status.
    # Accessibility: This function can be accessed from any part of the program as long as the interface object is accessible.
    # Function prototype:def filterByMenu()

Name: modifyInventoryMenu()
    # One-line description: Allows an administrator to add or remove a car from the inventory.
    # General description: This function provides a menu that allows the user to select an action to perform on the inventory of cars.
        The user must be an administrator to use this function. The menu provides two options: add a car or remove a car.
        If the user selects the add car option, the AddCar() function is called.
    #   If the user selects the remove car option, the RemoveCar() function is called.
    # Typical calling examples: modifyInventoryMenu(), modifyInventoryMenu(isAdmin=True)
    # Accessibility: The user must be an administrator to access this function.
    # Function prototype:def modifyInventoryMenu():

Name: AddCustomer()
    # One-line Description: Adds a new customer with their personal and credit card details to the system.
    # General Description: This function prompts the user to input the customer's personal details, 
        including first and last name, email address, credit card number, and home address. It then validates the 
        input and adds the customer to the system using the 'interface.AddCustomer' method. If the customer already 
        exists or if the email address is already in use, the function returns an error message.
    #   If the customer is successfully added, the function returns the customer object.
    # Typical Calling Example: AddCustomer()
    # Accessibility: The function can be accessed from anywhere in the system.
    # Function Prototype:def AddCustomer()

Name: DeleteCustomerMenu(customerToDelete)
    # One-line description: Deletes a customer from the system.
    # General description: This function takes a customer object to delete as an argument, confirms the deletion with the user, 
        and removes the customer from the interface if the user confirms. If the customer has orders, the function will display 
        a message informing the user of this fact before confirming the deletion.
    # Typical calling examples: DeleteCustomerMenu(customer_object)
    # Accessibility: This function can be accessed by any user with appropriate privileges.
    # Function prototype: def DeleteCustomerMenu(customerToDelete)

Name: Login()
    # One-line description: This function handles the login page and returns the user object if the user is authenticated.
    # General description: The function takes care of the login page by prompting the user for their username and password.
    #   It uses the Auth() object to authenticate the user. If the user is authenticated, the function returns the user object, 
    #   and if the user fails to log in after three attempts, it prints a message indicating the failure.
    # Typical calling examples:user = Login()
    # Accessibility: The function can be accessed from anywhere in the program.
    # Function prototype:def Login():

Name: modifyCarMenu(car)
    # One-line description: Modifies car status, price, mileage, and warranty plans.
    # General description: This function allows the user to modify the status, price, mileage, and warranty plans of a car
        object passed as a parameter to the function. It presents a menu of options to the user, where they can select the desired action.
        The available options are changing the car status, price, mileage, or warranty plans.
    # Typical calling examples: modifyCarMenu(car1)
    # Accessibility: This function can be accessed by any user with access to the application.
    # Function prototype: def modifyCarMenu(car)

Name: SearchCarMenu(car=None):
    # One-line description: Function to handle searching for cars in the inventory and providing actions for the search result.
    # General description: This function prompts the user to search for a car if one is not provided and then presents the user with
        options to either order the car or modify its attributes. If the car is already ordered, the function informs the user and returns.
    # Typical calling examples: SearchCarMenu() or SearchCarMenu(carObj)
    # Accessibility: The function can be accessed by any user with access to the module that contains it.
    # Function prototype:def SearchCarMenu(car=None):

Name: InventoryMenu()
    # One-line description: Display an inventory menu with options to view car details, search, filter, make customer orders, and modify inventory (admin-only).
    # General description: This function displays an inventory menu with options to interact with the car inventory. It allows users to view car details, search
        for specific cars, filter cars based on certain criteria, create a customer order for a specific car, and modify the inventory (admin-only).
    # Typical calling examples: InventoryMenu()
    # Accessibility: This function can be accessed from the main menu of the program or through a specific action in the program.
    # Function prototype: def InventoryMenu():

Name: AddCar()
    # One-line description: Function to add a new car to the inventory with user input.
    # General description: The function prompts the user to enter various details of a new car such as VIN, make, model, year, color, mileage, price, engine,
    #   transmission, interior, external design, paint, handling, audio, comfort features, package, warranty, and maintenance.
        The user input is then validated and dictionaries are created for the entered details. Finally, the function adds the new car to the inventory.
    # Typical calling examples: AddCar()
    # Accessibility: The function can be accessed from within the program in which it is defined.
    # Function prototype: def AddCar()

Name: RemoveCar()
    # One-line description: Function to remove a car from the inventory.
    # General description: This function allows the user to remove a car from the inventory by selecting it from a list of available cars.
    #   The user is prompted to confirm their choice, and if confirmed, the car is removed from the inventory.
    # Typical calling examples: RemoveCar()
    # Accessibility: This function can be accessed by any user with the appropriate permissions.
# Function prototype: def RemoveCar()

Name: addOrderMenu(carToOrder, customers)
    # One-line Description: Allows the user to add a new order to the system by selecting a car and customer.
    # General Description: This function prompts the user to confirm if they want to order a particular car and asks for the customer information.
        It then uses the customer and car information to create an order using the interface's MakeOrder() function. 
        If the order is successful, it prints the order details. If the car is already ordered by someone else, it prompts the user to add the car to backorder instead.
    # Typical calling examples:
    # addOrderMenu(carToOrder, customers)
    # Accessibility: This function can be accessed by calling it from another function or module.
    # Function prototype:def addOrderMenu(carToOrder, customers):

Name: OrderMenu()
    #   One-line description: Prints the order menu and provides options to add, remove, or view orders.
    #   Description: Displays the Order Menu with options to add, remove, or view orders.
    #   Typical calling example: OrderMenu()
    #   Accessibility: Can be accessed from the main menu by selecting "Orders".
    #   Function prototype: def OrderMenu()

Name: ManageEmployeesMenu()
    #   Description: Displays employee management menu and provides options to view, add or remove employees.
    #       Only accessible by admins.
    #   Accessibility: Only accessible by admins.
    #   Function Prototype: def ManageEmployeesMenu():

Name: validateCreditCard()
    #   One-line description: Validates a credit card number.
    #   General description: This function prompts 
    #       the user to input a credit card number and validates that it contains 16 digits.
    #   Typical calling example: cardNumber = validateCreditCard()
    #   Accessibility: This function can be accessed from any module that imports the current module.
    #   Function prototype: def validateCreditCard() -> str:

Name: modifyCustomerDetails()
    #   One-line Description: Modify details of a customer.
    #   General Description: This function allows the user to modify the details of a customer such as home address, email address, and credit card details.
            If a customer object is not provided as input, it gets the customer object from the list of customers.
    #       It displays the available options to the user and takes the appropriate action based on the user's choice.
    #   Typical Calling Example: modifyCustomerDetails()
    #   Accessibility: This function can be accessed from anywhere within the program.
    #   Function Prototype: def modifyCustomerDetails(customer=None)

Name: ManageCustomersMenu()
    #   One-line Description: Displays a menu for managing customers and prompts for actions to perform.
    #   general description: This function displays a menu that lists all the customers, and allows the user to perform different actions,
    #        such as adding, removing, viewing, or modifying customer details.
    #   typical call example: ManageCustomersMenu()
    #   Accessibillity: This function can be accessed from any part of the program.
    #   function prototype: def ManageCustomersMenu():

Name: CarSalesMenu()
    # One-line description: Displays the car sales menu and allows the user to view the sale details of delivered cars.
    # General description: This function displays the car sales menu and allows the user to view the sale details of delivered cars.
        It retrieves the list of delivered orders from the interface and displays it using the displayData function.
        It then prompts the user to select an action and calls the corresponding function based on the user's input. 
        If the user selects the "View sale details" option, it prompts the user to select a specific sale to view and 
        displays the sale details along with its delivery date.
    # Typical calling example: CarSalesMenu()
    # Accessibility: This function can be accessed from anywhere within the program.
    # Function prototype: def CarSalesMenu():

Name: AccountSettingsMenu()
    #   One-line description: Account settings menu for changing password, username, and viewing account details.
    #   General description: This function presents a menu for users to change their account settings. 
    #       It offers three options: changing password, changing username, and viewing account details. 
    #       The function loops until the user chooses to exit the menu.
    #   Typical calling examples: This function is called when a user selects the "Account Settings" option from the main menu.
    #   Accessibility: This function can be accessed by any logged-in user.
    #   Function prototype: def AccountSettingsMenu():

Name: menu()
    #   One-line description: Main menu that allows the user to access different sub-menus and account settings.
    #   General description: This function presents a main menu to the user, displaying different options based on their user type,
            and calls other sub-menus based on the user's choice. It also allows users to access their account settings to change their password or username.
    #   Typical calling examples: This function is called when the program starts or when the user goes back to the main menu from any of the sub-menus.
    #   Accessibility: This function is accessible to all users.
    #   Function prototype: def menu():

Name: run()
    #   One-line description: Runs the main program by logging in the user, setting up the interface, and displaying the main menu.
    #   General description: The run() function is the main function of the program that runs the login process, sets up the interface, 
            and displays the main menu. It calls the Login() function to log in the user, and depending on the user's category, 
            it sets up either a regular interface or an admin interface. It then calls the menu() function to display the main menu, 
            and logs out the user at the end of the session. If the user chooses to log in again, it starts the login process again.
    #   Typical calling examples:run()
    #   Accessibility: This function is not accessible as it is part of the program's main code.
    #   Function prototype: No arguments or return value.


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
#
#
#
orders.py
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Methods:
Name: __init__(self, id, car=None, buyer=None, dateBought=None, employee=None) -> None:
    # General description: This function initializes an object of the Sale class with the provided attributes including an ID, 
        a car object that has been ordered, the buyer's user ID, the sales employee's user
    #   ID, and the date of sale. If a date is not provided, the date is set to today's date.
    # Typical calling examples:
    #   sale = Sale(1, car, buyer_id, employee_id)
    #   sale = Sale(2, car, buyer_id, employee_id, '2022-05-12')
    # Accessibility: This function can be accessed within the Sale class.
    # Function prototype:def __init__(self, id, car=None, buyer=None, dateBought=None, employee=None) -> None:


Name: getUser(self): 
    # General description: This method returns the ID of the user who bought the car.
    # Typical calling examples: sale.getUser()
    # Accessibility: Public
    # Function prototype: def getUser(self) -> str:

Name: getCar(self): 
    # One-line description: Returns the car associated with the order object.
    # General description: This method returns the car object associated with the current order object.
    # Typical calling examples:
    #   order1.getCar()
    #   order2.getCar()
    # Accessibility: Public
    # Function prototype: def getCar(self) -> Car: (assuming that the Car class is the type of the self.car attribute)

Name: getSeller(self): 
    # One-line description: Returns the employee who sold the car in the order.
    # General description: This method returns the employee who sold the car in the order instance.
    # Typical calling example: order.getSeller()
    # Accessibility: Public method.
    # Function prototype: def getSeller(self) -> Employee

Name: getDate(self):
    # One-line description: Returns the date when the car was bought.
    # General description: This method is part of a class that represents a car sale. 
    #   It returns the date when the car was bought, which was either passed as an argument during object instantiation or set  
    #   to the current date by default.
    # Typical calling examples:
    #   sale = CarSale(1234, car, buyer, '2022-03-25', salesperson)
    #   sale.getDate() # returns datetime.datetime(2022, 3, 25, 0, 0)
    # Accessibility: Public
    # Function prototype: def getDate(self) -> datetime.datetime:

Name: getId(self):
    # One-line description: Returns the ID of a car order.
    # General description: This method is a getter method for the ID of a car order object.
    # Typical calling examples:
    #   order1 = CarOrder(1, car1, user1, "2022-04-12", employee1)
    #   order1_id = order1.getId()  # 1
    # Accessibility: Public.
    # Function prototype: def getId(self) -> int:

Name: getDateJoined(self): 
    # One-line description: Returns the date the user joined in the format "YYYY-MM-DD".
    # General description: This function returns the date that a user joined the system in the format "YYYY-MM-DD".
    # Typical calling examples:
    #   user = User("John", "Doe", "johndoe@gmail.com", "password", "1985-02-14")
    #   user.getDateJoined() -> "2022-03-04"
    # Accessibility: Public.
    # Function prototype: def getDateJoined(self) -> str:

Name: to_dict(self): 
    # One-line description: Convert the Order object to a dictionary format.
    # General description: This function takes an instance of the Order class and returns a dictionary containing information about the order,
    #   such as the ID of the order, the VIN of the car being purchased, the email of the buyer, the username of the employee 
        who made the sale, and the date of the sale.
    # Typical calling examples:
    #   order = Order(123, car, buyer, "2022-04-13", employee)
    #   order_dict = order.to_dict()
    # Accessibility: This function is a method of the Order class, so it can be called on any instance of that class.
    # Function prototype: def to_dict(self):

Name: serialize(order): 
    # One-line description: Serializes an Order object to a JSON-compatible format.
    # General description: This function takes an Order object and converts it into a dictionary that can be easily serialized into a JSON format.
         It does this by calling the Order object's to_dict method, which returns a dictionary representation of the object's attributes.
         If the provided object is not an instance of the Order class, a TypeError is raised.
    # Typical calling examples:
    #   order = Order(1, car, buyer, dateBought, employee)
    #   serialized_order = serialize(order)
    # Accessibility: This function is likely part of a larger program or module and can be accessed from other functions or scripts within that program or module.
    # Function prototype:def serialize(order):

Name: RemoveOrder(self): 
    # One-line description: Removes an order and sets the car status to available.
    # General description: This function removes the current order from the buyer's orders list and sets the car status to available
    #    indicating that the car is no longer reserved.
    # Typical calling examples:
    # Accessibility: This function is an instance method, which means it can only be called on an instance of a class.
    # Function prototype: def RemoveOrder(self):

Name: orderDetails(self):
    # One-line description: Generates a string containing the details of the order.
    # General description: This function generates a string containing the details of the car being ordered, the employee who made the
    #   sale, and the customer who placed the order.
    # Typical calling example:
    #   order = Order("O001", car, customer, "2023-04-14", employee)
    #   details = order.orderDetails()
    #   print(details)
    # Accessibility: Public.
    # Function prototype:def orderDetails(self) -> str:

Name: __str__(self): 
    # One-line description: Returns a string representation of the order object.
    # General description: This function returns a string representation of the order object,
    #   containing the order ID, the name of the salesperson who made the sale, and the car make and model, as well as the name of the buyer.
    # Typical calling examples: print(order) where order is an instance of the Order class.
    # Accessibility: Public.
    # Function prototype: def __str__(self):

Name: __eq__(self, value):
    # One-line description: Check equality of two Order objects.
    # General description: The function checks whether two Order objects are equal by comparing their IDs.
    # Typical calling example:
    #   order1 = Order(...)
    #   order2 = Order(...)
    #   if order1 == order2:
    #       print("The two orders are equal")
    # Accessibility: Public.
    # Function prototype: def __eq__(self, value) -> bool:.

Name: __repr__(self): 
    # One-line description: Returns the string representation of the car object.
    # General description: This function returns the string representation of the car object contained in the order.
    # Typical calling example: print(order.__repr__())
    # Accessibility: Public.
    # Function prototype: def __repr__(self) -> str:


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
#
#
#
session.py
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Methods:
Name: __init__(self) -> None
    # One-line description: Initializes an object of the class with two private attributes containing employee and admin data from a JSON file.
    # General description: This is an initialization method of a class that loads employee and admin data from a JSON file and stores it in two private attributes.
    # Typical calling example: obj = ClassName()
    # Accessibility: This method is public.
    # Function prototype: It does not take any argument and returns None.

Name: ReturnEmployees(self)
    # One-line description: Return the list of employees.
    # General description: The ReturnEmployees function returns the list of employees stored in the instance variable
    #    __employees__.
    # Typical calling example:
    #   company = Company()
    #   employees = company.ReturnEmployees()
    # Accessibility: Public.
    # Function prototype:def ReturnEmployees(self) -> list:

Name: ReturnAdmins(self)
    # One-line description: Returns a list of administrator users.
    # General description: This function returns the list of administrator users that was previously loaded from
    #    a JSON file using the LoadUsers() function. The list is stored as a private attribute __admins__ of the class.
    # Typical calling examples:
    #   userManager = UserManager()
    #   admins = userManager.ReturnAdmins()
    #   print(admins)  # prints the list of administrator users
    # Accessibility: Public.
    # Function prototype: def ReturnAdmins(self) -> List[Dict[str, Any]]:

Name: __init__(self) -> None
    # One-line description: Initializes an object of a class and creates a combined list of employees and admins as a list of users.
    # General description: This function is a constructor method for a class that inherits from a parent class. It initializes 
        an object of the child class and creates a list of users that contains the combined list of employees and admins.
    # Typical calling examples:
    #   obj = ChildClass()
    # Accessibility: Private
    # Function prototype: def __init__(self) -> None:

Name: Authenticate(self, username, password)
    # One-line description: Authenticate a user with their username and password.
    # General description: This method searches through a list of users to find a matching username and
    #   password combination. If a match is found, the user object is returned.
    # Typical calling examples:
    #   auth = Authenticator()
    #   user = auth.Authenticate("john.doe", "password123")
    # Accessibility: Public method.
    # Function prototype': def Authenticate(self, username, password) -> Union[User, None]:


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
#
#
#
status.py
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Methods:
Name: strToStatus(status: str)
    # One-line description: Convert a string representation of car status to its corresponding enum value.
    # General description: This function takes a string representation of a car status, such as "available" or "ordered", 
        and returns the corresponding enum value from the predefined STATUS_DICT dictionary.
    #   If the input status string is not found in the dictionary, the function returns None.
    # Typical calling examples:
    #   strToStatus("available") returns Status.AVAILABLE.
    #   strToStatus("backorder") returns Status.BACKORDER.
    #   strToStatus("sold") returns None.
    # Accessibility: The function is defined globally and can be accessed from anywhere in the program.
    # Function prototype: def strToStatus(status: str) -> Union[Status, None]

Name: StatusToStr(status: Status)
    # One-line description: Converts a Status enum value to its string representation.
    # General description: This function takes in a Status enum value and returns its corresponding string representation based on
    #   the values defined in the STATUS_DICT dictionary.
    # Typical calling examples:
    #   StatusToStr(Status.AVAILABLE) returns "available"
    #   StatusToStr(Status.ORDERED) returns "ordered"
    # Accessibility: This function can be accessed anywhere within the codebase where the st module is imported.
    # Function prototype: def StatusToStr(status: Status) -> str:



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
#
#
#
users.py
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Methods:
Class User:
Name: init(self, username='', password='', first_name='', last_name='', date_joined=None)
    # One-line description: Initializes a User object with a username, password, first name, last name, and date joined.
    # General description: This function creates a new instance of a User object with the specified username, password, first name, last name, and date joined.
    #   If no date is provided, today's date is used. The date is validated and converted to a datetime object.
    # Typical calling examples:
    #   user1 = User('jdoe', 'password', 'John', 'Doe', '2022-03-15')
    #   user2 = User('asmith', 'p@ssword', 'Alice', 'Smith')
    # Accessibility: Public
    # Function prototype: def __init__(self, username='', password='', first_name='', last_name='', date_joined=None) -> None:

Name: getFirstName(self)
    # One-line description: Returns the first name of the user.
    # General description: This method is part of a User class and returns the first name attribute of a user object.
    # Typical calling examples: user.getFirstName()
    # Accessibility: Public
    # Function prototype: def getFirstName(self) -> str:

Name: getLastName(self)
    # One-line description: Returns the last name of a user.
    # General description: This function is a getter method that returns the last name of a user object.
    # Typical calling examples:
    #   user1_last_name = user1.getLastName()
    # Accessibility: This function is a public method that can be accessed from anywhere within the class and outside of it.
    # Function prototype:def getLastName(self) -> str:

Name: UpdatePassword(self, newpassword)
    # One-line description: Updates the password of the user.
    # General description: This method updates the password of the user with the given new password.
    # Typical calling examples:
    #   user1.UpdatePassword('newpassword123')
    # Accessibility: Public.
    # Fuction prototype:
    #   def UpdatePassword(self, newpassword: str) -> None:

Name: UpdateUserName(self, newusername)
    # One-line description: Updates the username attribute of a user object with a new username.
    # General description: This method updates the username attribute of a User object with a new username passed as an argument.
    # Typical calling examples:
    #   user1 = User('john_doe', 'password', 'John', 'Doe', '2022-01-01')
    #   user1.UpdateUserName('john_doe_123')
    # Accessibility: Public
    # Function prototype: def UpdateUserName(self, newusername: str) -> None:

Name: getUsername(self)
    # One-line description: Returns the username of a user.
    # General description: This function returns the username of a user object.
    # Typical calling examples:
    #   user1.getUsername() -> returns the username of user1
    # Accessibility: Public
    # Function prototype: def getUsername(self) -> str:

Name: getPassword(self)
    # One-line description: Returns the password of a User instance.
    # General description: This function returns the password attribute of a User object,
    #    which stores the password of the user.
    # Typical calling examples:
    #   user = User('john', 'pass123')
    #   password = user.getPassword()
    # Accessibility: Public
    # Function prototype: def getPassword(self) -> str:

Name: serialize(user)
    # One-line description:A function to serialize a User object to a JSON-serializable format.
    # General description:This function takes a User object as an argument and converts it to a dictionary format that can be JSON-serialized. 
    #   If the input object is not of type User, 
    #   it raises a TypeError with an appropriate error message.
    # Typical calling examples:
    #   user_json = serialize(user_object)
    # Accessibility:This function can be accessed from any module in the program where it is imported.
    # Function prototype:def serialize(user: User) -> Union[Dict, None]:

Name: eq(self, __o)
    # One-line description: Determines whether two users are equal by comparing their usernames.
    # General description: This method compares the usernames of two user objects to determine if they represent the same user.
    # Typical calling examples:
    #   user1 == user2 - This will check if user1 and user2 have the same username and return True if they are equal and False if not.
    # Accessibility: Public
    # Function prototype: def __eq__(self, __o) -> bool:

Name: str(self)
    # One-line description: Returns a string representation of a User object.
    # General description: The __str__ function returns a string representation of a User object.
    #   The string contains the user's first name, last name, and the date they joined.
    # Typical calling examples:
    #   user1 = User('john_doe', 'password', 'John', 'Doe')
    #   print(user1) # Output: "User John Doe Joined in 2023-04-14 00:00:00"
    # Accessibility: Public.
    # Function prototype: def __str__(self) -> str:

Name: repr(self) -> str
    # One-line description: Return a string representation of a User object.
    # General description: This function returns a string representation of a User object which includes the user's 
    #   first name and last name.
    # Typical calling examples:
    #   user = User("john", "doe")
    #   print(repr(user)) (Output: "john doe")
    # Accessibility: Public
    # Function prototype: def __repr__(self) -> str:

    
Class Admin(User):
Name: init(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Admin")
    # One-line description: Initializes an instance of the Admin class, inheriting from the User class and setting the category type to "Admin".
    # General description: This function creates an instance of the Admin class, setting its properties to the provided arguments or default values
    #    and initializing it as a subclass of the User class with an additional categoryType property set to "Admin".
    # Typical calling examples:admin1 = Admin("admin1", "password", "John", "Doe", "2022-01-01")
    # Accessibility: Public.
    # Function prototype:
    #   def __init__(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Admin") -> None:

Name: getCategory(self)
    # One-line description: Returns the category type of an object.
    # General description: This method is used to get the category type of an object. It returns the category type of the object on which it is called.
    # Typical calling examples:
    #   admin = Admin("admin", "password", "John", "Doe", datetime.now(), "Admin")
    #   category = admin.getCategory()
    # Accessibility: Public method.
    # Function prototype: def getCategory(self) -> str:

Name: str(self)
    # One-line description: Returns a string representation of an Admin instance.
    # General description: This function returns a formatted string representation of an Admin instance containing the category type,
    #   first name and last name of the Admin.
    # Typical calling examples:
    #   admin1 = Admin("user1", "password123", "John", "Doe", datetime.now(), "Senior")
    #   print(admin1) will output "Senior John Doe"
    # Accessibility: Public
    # Function prototype: def __str__(self) -> str:

Name: getDetails(self)
    # One-line description: Get user details.
    # General description: This method returns the date on which the user joined.
    # Typical calling examples:
    #   admin = Admin("admin", "password", "John", "Doe", categoryType="Admin")
    #   details = admin.getDetails()
    # Accessibility: Public method.
    # Function prototype: def getDetails(self) -> str:

Name: to_dict(self)
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


Class Employee(User):
Name: init(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Employee")
    # One-line description: Initializes an Employee object with a specified username, password, first and last name, date joined, and category type.
    # General description: This function initializes an Employee object, which inherits from the User class. It sets the object's
    #   instance variables to the values provided in the function parameters, and also sets the object's categoryType to "Employee" by default.
    # Typical calling examples:
    #   employee1 = Employee(username='jdoe', password='password123', first_name='John', last_name='Doe', date_joined=datetime.date(2022, 4, 14))
    # Accessibility: This function is accessible from within the Employee class and any subclasses that inherit from it.
    # Function prototype:
    #   def init(self, username='', password='', first_name='', last_name='', date_joined=None, categoryType="Employee") -> None:

Name: str(self)
    # One-line description: Returns a string representation of the Employee object including category, first name, and last name.
    # General description: This function returns a formatted string that represents an Employee object.
    #   The returned string includes the Employee's category, first name, and last name.
    # Typical calling examples:
    #   employee = Employee(username='jdoe', password='password', first_name='John', last_name='Doe')
    #   print(employee) # Output: "Employee John Doe"
    # Accessibility: This function is public and can be accessed from anywhere in the code.
    # Function prototype: def __str__(self) -> str:

Name: getDetails(self)
    # One-line description: Returns the details of the employee's joining date in a formatted string.
    # General description: This method returns the date on which an employee joined the organization in a formatted string. It takes the employee's date of
    #   joining as an instance variable and formats it using the strftime() method.
    # Typical calling examples:
    #   emp1 = Employee('johndoe', 'password', 'John', 'Doe', datetime.date(2021, 1, 1))
    #   print(emp1.getDetails()) # Output: Joined in 2021-01-01
    # Accessibility: This method is public, accessible outside the class.
    # Function prototype: def getDetails(self) -> str:

Name: getCategory(self)
    # One-line description: Returns the category type of the user.
    # General description: This function is a method of the User class which returns the category type of the user.
    # Typical calling examples:
    #   user1.getCategory()
    # Accessibility: This method is accessible to instances of the User class and its subclasses.
    # Function prototype:def getCategory(self) -> str:

Name: to_dict(self)
    # One-line description: Returns a dictionary representation of the user object.
    # General description: The to_dict method returns a dictionary with the user's attributes as key-value pairs, including their username,
    #   password, first and last name, date joined, and category type. This method is commonly used to convert user objects to a format
        that can be easily serialized and stored, such as in a database or JSON file.
    # Typical calling examples:
    #   user = User('johndoe', 'password', 'John', 'Doe')
    #   user_dict = user.to_dict()
    #   print(user_dict)
    # Output: {'username': 'johndoe', 'password': 'password', 'name': [{'firstName': 'John', 'lastName': 'Doe'}], 'dateJoined': '2023-04-14', 'type': 'Employee'}
    # Accessibility: Public.
    # Function prototype: def to_dict(self) -> dict:



Class Customer:
Name: init(self, first, last, card, email, address)
    # One-line description: Constructor for a Customer class with attributes such as first and last name, card, email, address and an empty list for orders.
    # General description: The function initializes a new object of the Customer class by setting values for first name, last name,
    #   card, email, address, and an empty list for orders.
    # Typical calling examples:
    #   customer1 = Customer("John", "Doe", "1234-5678-9012-3456", "johndoe@example.com", "123 Main St")
    #   customer2 = Customer("Alice", "Smith", "9876-5432-1098-7654", "alicesmith@example.com", "456 Oak St")
    # Accessibility: Public
    # Function prototype: def __init__(self, first: str, last: str, card: str, email: str, address: str) -> None:

Name: getFirstName(self)
    # One-line description: Returns the first name of a customer.
    # General description: This function returns the first name of a customer object created using the Customer class. 
    #   The first name is stored as an instance variable within the class.
    # Typical calling example:
    #   customer1 = Customer("John", "Doe", "1234567890", "johndoe@gmail.com", "123 Main St")
    #   print(customer1.getFirstName())  # output: John
    # Accessibility: Public
    # Function prototype: def getFirstName(self) -> str:

Name: getLastName(self)
    # One-line description: Get the last name of a customer.
    # General description: This method returns the last name of a customer instance.
    # Typical calling examples:
    #   customer.getLastName()
    # Accessibility: Public.
    # Function prototype: def getLastName(self) -> str:

Name: getEmail(self):
    # One-line description: Returns the email of a customer.
    # General description: This function returns the email attribute of a customer object.
    # Typical calling examples:
    #   customer = Customer("John", "Doe", "1234-5678-9012-3456", "johndoe@gmail.com", "123 Main St")
    #   email = customer.getEmail()
    # Accessibility: Public.
    # Function prototype:def getEmail(self) -> str:

Name: setCard(self, new_card):
    # One-line description: Sets the value of the card attribute for the instance of the class.
    # General description: This method sets the value of the card attribute to a new value passed as an argument.
    #   The card attribute represents the credit/debit card number associated with the customer's account.
    # Typical calling examples:
    #   customer1 = Customer('John', 'Doe', '1234 5678 9012 3456', 'john.doe@email.com', '123 Main St')
    #   customer1.setCard('9876 5432 1098 7654')
    # Accessibility: Public method accessible to anyone who has an instance of the Customer class.
    # Function prototype: def setCard(self, new_card: str) -> None:. The method takes a string argument new_card 
        representing the new card number and returns nothing (None).

Name: setAddress(self, new_address):
    # One-line description: Method to set a new address for a user profile.
    # General description: This method sets a new address for the user profile.
    # Typical calling examples:
    #   user = UserProfile('John', 'Doe', '1234 5678 9012 3456', 'johndoe@example.com', '123 Main St')
    #   user.setAddress('456 Broad St')
    # Accessibility: Public method.
    # Function prototype: def setAddress(self, new_address: str) -> None

Name: setEmail(self, new_email):
    # One-line description: Setter function to update the email address of a user.
    # General description: This function updates the email address of a user with a new email address.
    # Typical calling examples:
    # user.setEmail('newemail@example.com')
    # Accessibility: Public
    # Function prototype: def setEmail(self, new_email):

Name: getDetails(self):
    # One-line description: Returns a string containing the user's email, address, and list of orders.
    # General description: This method returns a formatted string that contains the email, address, and list of orders for a user.
    # Typical calling example: user.getDetails()
    # Accessibility: Public
    # Function prototype: def getDetails(self) -> str:

Name: to_dict(self):
    # One-line description: Returns the dictionary representation of the customer object.
    # General description: This method returns a dictionary representation of the customer object with attributes such as email, name, card, and address.
    # Typical calling examples:
    # customer = Customer("John", "Doe", "1234567890123456", "johndoe@example.com", "123 Main St.")
    # customer_dict = customer.to_dict()
    # Accessibility: Public
    # Function prototype: def to_dict(self) -> dict:

Name: serialize(customer):
    # One-line description: Function that serializes a Customer object into a JSON serializable dictionary.
    # General description: The serialize() function takes a Customer object and returns its dictionary representation using the to_dict() method. The purpose of the function
    #   is to allow the Customer object to be easily serialized to JSON for data exchange or storage.
    # Typical calling examples:
    # Accessibility: The function is accessible within the same module or class where it is defined.
    # Function prototype:def serialize(customer: Customer) -> dict:

Name: __str__(self) -> str:
    # one-line Description: This method returns a string representation of the object instance.
    # General Description: This method is used to get a string representation of the object instance of the Customer class. It concatenates the last name and first name of the customer 
    #   with a comma in between and returns the resulting string.
    # Typical calling example: print(customer_obj) where customer_obj is an instance of the Customer class.
    # Accessibility: Public.
    # Function prototype: def __str__(self) -> str:


Name: __repr__(self) -> str:
    # One-line description: Returns a string representation of the customer object.
    # General description: This function returns a string representation of the customer object that includes their email address.
    # Typical calling examples:
    #   customer = Customer("John", "Doe", "1234567890123456", "johndoe@example.com", "123 Main St")
    #   print(repr(customer))
    # Accessibility: Public.
    # Function prototype: def __repr__(self) -> str:

Name: __eq__(self, value) -> bool:
    # One-line description: Check if two Customer objects are equal by comparing their email addresses.
    # General description: This function compares the email attribute of a Customer object with another object. 
    #   If the other object is also a Customer object, its email attribute is compared with the email attribute of the original Customer object.
    #   If the two email addresses match, the function returns True, otherwise it returns False.
    # Typical calling examples:
    # Accessibility: This function is accessible from within the Customer class and can be called on a Customer object.
    # Function prototype: def __eq__(self, value) -> bool:


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
#
#
#
vehicles.py
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Methods:
Name: __init__(self, vin='', info={}, performance={}, design={}, handling=[], comfort=[], entertainment=[], protection={}, package='', status=None, price=0):
    # One-line description: A class constructor that initializes an object with various attributes such as vehicle information, performance, design, handling, comfort, entertainment, protection, package, status, and price.
    # General description: This is a constructor method for a Vehicle class that initializes an object with various attributes. The vin parameter specifies the vehicle identification number (VIN) for the vehicle.
    #   The info, performance, design, handling, comfort, entertainment, and protection parameters specify dictionaries containing various attributes related to the vehicle.
    #   The package parameter specifies the package name for the vehicle. The status parameter specifies the status of the vehicle. The price parameter specifies the price of the vehicle.
    # Typical calling examples:
    #   To create a new Vehicle object with default status and price:
    #   vehicle1 = Vehicle(vin='12345', info={}, performance={}, design={}, handling=[], comfort=[], entertainment=[], protection={}, package='')
    #   To create a new Vehicle object with custom status and price:
    #   vehicle2 = Vehicle(vin='12345', info={}, performance={}, design={}, handling=[], comfort=[], entertainment=[], protection={}, package='', status='AVAILABLE', price=25000)
    # Accessibility: The constructor is accessible within the Vehicle class and can be called from any method within the class.
    # Function prototype:def __init__(self, vin='', info={}, performance={}, design={}, handling=[], comfort=[], entertainment=[], protection={}, package='', status=None, price=0):

Name: UpdateMileage(newMileage):
    # One-line description: Update the mileage of a vehicle object.
    # General description: This function updates the mileage of a vehicle object by taking in a new mileage
    #   value and updating the corresponding value in the object's 'info' dictionary.
    # Typical calling examples: car1.UpdateMileage(50000)
    # Accessibility: This function is a method of the vehicle class and can only be accessed through an instance of the class.
    # Function prototype: def UpdateMileage(self, newMileage):
    
Name: UpdateWarranty(newWarranty):
    # One-line description: Update the warranty information of a car object.
    # General description: This method takes a new warranty and appends it to the list of warranties in the car object's protection dictionary.
    # Typical calling examples:
    #   car.UpdateWarranty("3 years, unlimited miles")
    #   car.UpdateWarranty("5 years, 100,000 miles")
    # Accessibility: This method is accessible from within the Car class.
    # Function prototype: def UpdateWarranty(self, newWarranty):

Name: getVin():
    # One-line description: Returns the vehicle identification number (VIN) of a vehicle object.
    # General description: This method is part of a vehicle class that stores information about a specific vehicle.
    #   The getVin method returns the VIN of the vehicle.
    # Typical calling examples:
    #   myVehicle.getVin()
    # Accessibility: This method is a public method of the vehicle class, so it can be called from
    #   anywhere in the program where the vehicle object is accessible.
    # Function prototype:
    #   def getVin(self) -> str:

Name: getStatus():
    # One-line description: Returns the current status of a vehicle object.
    # General description: This function is part of a vehicle class and returns the current status of an instance of the class. The status is determined by an enumerated
    #   type and is set when the object is instantiated.
    # Typical calling examples:
    #   car1 = Vehicle('123456789', {'make': 'Ford', 'model': 'Mustang', 'year': 2021}, {'0-60 mph': 5.2}, {'exterior color': 'red'}, [], [], [], {'warranty': ['5 years/60,000 miles']}, 'premium', 'AVAILABLE', 35000)
    # Accessibility: This function is accessible within the vehicle class and can also be accessed by calling it from an instance of the class.
    # Function prototype:def getStatus(self):

Name: getStatusStr():
    # One-line description: A method to get the string representation of the car's status.
    # General description: This method is a member function of a class representing a car. It returns a string representing the car's status,
    #   which is stored as an enumerated type in the class instance.
    # Typical calling examples:
    #   c ar.getStatusStr()
    # Accessibility: This method is a public member function of the car class and can be accessed
    #   from anywhere in the program where a car object is in scope.
    # Function prototype:def getStatusStr(self):

Name: getCarInfo():
    # One-line description: A method to get the string representation of the car's status.
    # General description: This method is a member function of a class representing a car. It returns a string representing the car's status,
    #   which is stored as an enumerated type in the class instance.
    # Typical calling examples:
    #   car.getStatusStr()
    # Accessibility: This method is a public member function of the car class and can be accessed
    #   from anywhere in the program where a car object is in scope.
    # Function prototype: def getStatusStr(self):

Name: SetStatus(updated_status):
    # One-line description: Sets the status of a car object either by passing in a Status enum or a string representation of a status.
    # General description: This function sets the status of a car object. It takes in an argument, 'updated_status', which can be either a Status enum or a string representation of a status. If it is not a string, it sets the status to the provided enum. If it is a string,
    #   it converts it to a Status enum using a helper function and then sets the status of the car object.
    # Tycical calling examples:
    #   car1.SetStatus(Status.SOLD)
    #    car2.SetStatus('maintenance')
    # Accessibility: Public.
    # Function prototype:.def SetStatus(self, updated_status)

Name: to_dict():
    # One-line description: Convert object data to a dictionary format.
    # General description: This function takes an object and converts it to a dictionary format. 
    #   It retrieves each attribute of the object and maps it to a key in the dictionary.
    # Typical calling examples:
    #   car = Car()
    #   car_dict = car.to_dict()
    # Accessibility: Public.
    # Function prototype: def to_dict(self) -> dict:

Name: serialize(car):
    # One-line description: JSON serialization of Car object
    # General description: This function takes a Car object as an argument and returns a JSON-serializable dictionary representation of the object. 
        It calls the to_dict() method of the Car object to obtain a dictionary representation of the object, which is then returned. 
        If the argument passed to the function is not an instance of the Car class, it raises a TypeError.
    # Typical calling examples:
    #   my_car = Car()
    #   serialized_car = serialize(my_car)
    # Accessibility: Public
    # Function prototype: def serialize(car: Car) -> dict

Name: isAvailable():
    # One-line description: Checks if the car is available.
    # General description: This method checks if the car's status is available and returns
    #   True if it is, or False otherwise.
    # Typical calling examples:
    #   car.isAvailable()
    #   if car.isAvailable():
    # Accessibility: Public
    # Function prototype: def isAvailable(self) -> bool:

Name: UpdatePrice(newprice):
    # One-line description: Update the price of a Car object.
    # General description: This method updates the price of a Car object to a new value.
    # Typical calling examples: car.UpdatePrice(25000), where 'car' is an instance of the Car class and 25000 is the new price value.
    # Accessibility: Public method accessible to the Car class and its instances.
    # Function prototype: def UpdatePrice(self, newprice):

Name: getDetails():
    # One-line description: Returns the details of a car object in a formatted string.
    # General description: The getDetails method returns a string containing the details of a car object.
    #   It includes information such as VIN, package, performance, design, extras, and protection plans.
    #   The method also utilizes a __str__ method to get the basic information about the car, such as its make and model.
    # Typical calling examples:
    #   car = Car("VIN123", "Ford", "Mustang", "sports car", {"engine": "V8", "transmission": "manual"}, {"interior": "leather", "exterior": "red"}, 25000, "luxury", 
    #   {"comfort": "heated seats", "entertainment": "Bluetooth"}, {"maintenance": ["oil change", "tire rotation"], "warranty": ["powertrain", "electronics"]})
    #   print(car.getDetails())
    # Accessibility: Public
    # Function prototype: def getDetails(self):

Name: __eq__(__o: object) -> bool:
    # One-line description: Compares two instances of the Car class for equality based on their VINs.
    # General description: This is a magic method in Python that is invoked when using the == operator to
    #   compare two objects. It checks whether the given object is an instance of the Car class, and if so,
    #   compares their VINs for equality.
    # Typical calling examples:
    # car1 == car2: compares two instances of the Car class car1 and car2 for equality.
    # Accessibility: Public
    # Function prototype: def __eq__(self, __o: object) -> bool:

Name: __str__():
    # One-line description: Returns a string representation of a car object including its year, make, model, price, and status.
    # General description: This method formats and returns a string representation of a car object. It displays the year, make, and model of the car, 
    #   its price in the local currency, and its status (which can be either AVAILABLE or UNAVAILABLE).
    # Typical calling examples:
    #   car1 = Car(vin="12345678901234567", make="Tesla", model="Model S", year=2020, price=79990, status=st.Status.AVAILABLE)
    #   print(car1) # prints "2020 Tesla Model S $79,990.00 AVAILABLE"
    # Accessibility: This method is a public instance method and can be called on any Car object.
    # Function prototype: def __str__(self) -> str:

Name: __repr__():
    # One-line description: Returns a string representation of the car object including its model and make.
    # General description: This function returns a string representation of the car object, which includes its model and make.
    # Typical calling examples:
    #   print(car1) where car1 is an instance of the Car class.
    # Accessibility: This function is accessible within the Car class and to objects of this class.
    # Function prototype: def __repr__(self) -> str:


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
#
#
#
readJson.py
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Methods:
Name:LoadInventory()
    # One-line description:Loads the car inventory data from a JSON file and creates a list of Car objects.
    # General description:The LoadInventory function reads car inventory data from a JSON file, 
    #     creates Car objects using the data, and returns a list of Car objects.
    # Typical calling examples:inventory = LoadInventory()
    # Accessibility: The function can be accessed by importing the module that it belongs to.
    # Function prototype:def LoadInventory() -> List[vehicles.Car]:

Name:LoadUsers()
    # One-line description: Loads user data from a JSON file and creates Employee and Admin objects accordingly.
    # General description: This function reads user data from a JSON file and creates Employee and Admin objects 
    #   based on the user type information in the file. The function returns two lists of Employee and Admin objects respectively.
    # Typical calling examples:
    #   employees, admins = LoadUsers()
    # Accessibility: This function is accessible within the module where it is defined.
    # Function prototype:def LoadUsers() -> Tuple[List[users.Employee], List[users.Admin]]:

Name:LoadOrders()
    # One-line description: Loads a list of orders from a JSON file.
    # General description: This function loads a list of orders from a JSON file and returns the list.
    # Typical calling examples:
    #    orders = LoadOrders()
    # Accessibility: This function can be accessed within the module it is defined in.
    # Function prototype:def LoadOrders() -> List[orders.Order]:

Name:LoadCustomers()
    # One-line description: Loads and returns a list of Customer objects from a JSON file.
    # Genera description: This function reads a JSON file containing customer data, creates 
    #   Customer objects for each customer record, and appends them to a list. The list of Customer objects is then returned.
    # Typical calling examples:
    #   customers = LoadCustomers()
    # Accessibility: This function is likely intended to be used within a larger system, but could be called from
    #    anywhere within the scope of the project as long as the necessary files are accessible.
    # Function prototype:def LoadCustomers() -> List[users.Customer]:
    


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
#
#
#
#
#
writeJson.py
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Methods:
Name: writeJson(data)
# One-line description: This function writes data to a json filePath, it will determine what kind of data is being loaded and write to 
#   the appopriate json filePath with the proper formatting.
# General description: This function writes data to a JSON file based on the object type in an array.
#    It determines the file path based on the object type and serializes the data using the object's serialization function before writing it to the file.
# Typical calling examples:
#    writeJson(inventory) to write the inventory list to the inventory JSON file.
#   writeJson(orders) to write the orders list to the orders JSON file.
# Accessibility: This function is accessible from anywhere within the program.
# Function prototype: def writeJson(data):


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
