####################################################################################################################
'''
////////////////
PROGRAM vehicles:  define a class called Car with various attributes and methods to 
                   represent a vehicle in the PigeonBox system and manipulate its properties.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

////////////////
PURPOSE:
The purpose of the class is to provide a blueprint for creating car objects and defining their 
properties and behaviors.

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


////////////////
DATA STRUCTURES:
DataStructures:
- Dictionary: The class Car takes in several dictionaries as input parameters like info, performance, design, protection, and others.
- List: The class Car takes in several lists as input parameters like handling, comfort, entertainment, and others.

Attributes:
- vin (str): vehicle identification number
- info (dict): car information, containing keys: year, make, model, and mileage
- performance (dict): car performance information, containing keys: engine and transmission
- design (dict): car design information, containing keys: interior and exterior
- handling (list): a list of car handling features
- comfort (list): a list of car comfort features
- entertainment (list): a list of car entertainment features
- protection (dict): car protection information, containing keys: maintenance and warranty
- package (str): car package information
- status (Status): car availability status (enum type)
- price (int/float): car price

////////////////
ALGORITHM:
None

////////////////
ERROR HANDLING:
No explicit error handling.

////////////////
'''
####################################################################################################################

import locale
import PigeonBox.status as st
from PigeonBox.bcolors import bcolors



class Car ():
    """Class that represents a car with various attributes and methods."""

    def __init__(self, vin='', info={}, performance={}, design={}, handling=[], comfort=[], entertainment=[], protection={}, package='', status=None, price=0):
        """ A class constructor that initializes an object with various attributes such as vehicle information, performance, design, handling, comfort, entertainment, protection, package, status, and price."""
        self.vin = vin
        self.info = info
        self.performance = performance
        self.design = design
        self.handling = handling
        self.comfort = comfort
        self.entertainment = entertainment
        self.protection = protection
        self.package = package
        # Set default status to AVAILABLE if not provided
        if status is None:
            status = st.Status.AVAILABLE
        # Convert status string to Status enum if a string is provided
        if isinstance(status, str):
            status = st.strToStatus(status)
        self.status = status
        self.price = price

    def UpdateMileage(self, newMileage):
        """Update the mileage of a vehicle object."""
        self.info['mileage'] = newMileage

    def UpdateWarranty(self, newWarranty):
        """Update the warranty information of a car object."""
        self.protection['warranty'].append(newWarranty)

    def getVin(self):
        """Returns the vehicle identification number (VIN) of a vehicle object."""
        return self.vin
    
    def getStatus(self):
        """Returns the current status of a vehicle object."""
        return self.status
    
    def getStatusStr(self):
        """A method to get the string representation of the car's status"""
        return st.StatusToStr(self.status)
    
    def getCarInfo(self):
        """A method to get the string representation of the car's status."""
        return self.info

    def SetStatus(self, updated_status):
        """Sets the status of a car object either by passing in a Status enum or a string representation of a status."""
        if not isinstance(updated_status, str):
            self.status = updated_status
            return
        self.status = st.strToStatus(updated_status.lower())

    def to_dict(self):
        """"Convert object data to a dictionary format."""
        return {
            "vin": self.vin,
            "status": st.StatusToStr(self.status),
            "info": [self.info],
            "performance": [self.performance],
            "design": [self.design],
            "handling": self.handling,
            "comfort": self.comfort,
            "audio": self.entertainment,
            "protection": [self.protection],
            "package": self.package,
            "price": self.price
        }

    def serialize(car):
        """JSON serialization of Car object"""
        if isinstance(car, Car):
            return car.to_dict()
        raise TypeError("Object of type 'Car' is not JSON serializable")

    def isAvailable(self):
        """Checks if the car is available."""
        return self.status == st.Status.AVAILABLE
    
    def UpdatePrice(self, newprice):
        """"Update the price of a Car object."""
        self.price = newprice

    def getDetails(self):
        """Returns the details of a car object in a formatted string."""
        # Define a string containing the details of the car, including the VIN, package, performance, design, extras, and protection plans
        res = f"""\n{bcolors.BOLD}{self.vin}{bcolors.ENDC} with {self.package} package
        Performance
        Engine: {self.performance['engine']}, Transmission: {self.performance['transmission']}
        Mileage: {self.info['mileage']} miles
        {bcolors.BOLD}Design{bcolors.ENDC}
        Interior design: {self.design['interior']}
        Exterior design: {self.design['exterior']}
        {bcolors.BOLD}Extras{bcolors.ENDC}
        Comfort: {self.comfort}
        Entertainment {self.entertainment}
        {bcolors.BOLD}Protection plans{bcolors.ENDC}
        Maintenance {self.protection['maintenance']}
        Warranty plans {self.protection['warranty']}"""
        # Return the string representation of the car along with its details
        return self.__str__() + res
    
    def __eq__(self, __o: object) -> bool:
        """Compares two instances of the Car class for equality based on their VINs."""
        if isinstance(__o, Car):
            return self.vin == __o.vin
    
    def __str__(self) -> str:
        """Returns a string representation of a car object including its year, make, model, price, and status."""
        locale.setlocale( locale.LC_ALL, '' )
        return f"{self.info['year']} {bcolors.BOLD}{self.info['model']} {self.info['make']}{bcolors.ENDC} {bcolors.OKGREEN}{locale.currency(self.price, grouping=True )}{bcolors.ENDC} {bcolors.UNDERLINE}{self.status}{bcolors.ENDC}"

    def __repr__(self) -> str:
        """Returns a string representation of the car object including its model and make."""
        return f"{self.info['model']} {self.info['make']}"
