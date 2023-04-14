####################################################################################################################
'''
////////////////
PROGRAM vehicles:  define a class called Car with various attributes and methods to 
                   represent a vehicle in the PigeonBox system and manipulate its properties.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu

////////////////
VERSION 1: written [day] [month] 2023 by [firstInitial]. [lastName]
REVISION [revision# ex: 1.1]: [day] [month] 2023 by [firstInitial]. [lastName] to [purpose of revision]

////////////////
PURPOSE:
The purpose of the class is to provide a blueprint for creating car objects and defining their 
properties and behaviors.

Methods:
- UpdateMileage(newMileage): update the car's mileage
- UpdateWarranty(newWarranty): update the car's warranty
- getVin(): return the car's VIN
- getStatus(): return the car's status
- getStatusStr(): return the string representation of the car's status
- getCarInfo(): return the car's information dictionary
- SetStatus(updated_status): set the car's status based on a string or a Status object
- to_dict(): convert the car object to a dictionary
- serialize(car): serialize the car object to a JSON object
- isAvailable(): check if the car is available
- UpdatePrice(newprice): update the car's price
- getDetails(): return the car's details in a formatted string
- __eq__(__o: object) -> bool: compare two car objects based on their VINs
- __str__(): return a string representation of the car object
- __repr__(): return a string representation of the car object

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



#   Class that represents a car with various attributes and methods.
class Car ():
    # Constructor to initialize the car's attributes
    def __init__(self, vin='', info={}, performance={}, design={}, handling=[], comfort=[], entertainment=[], protection={}, package='', status=None, price=0):
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

    # Method to update the car's mileage
    def UpdateMileage(self, newMileage):
        self.info['mileage'] = newMileage

    # Method to update the car's warranty information
    def UpdateWarranty(self, newWarranty):
        self.protection['warranty'].append(newWarranty)

    # Getter method to retrieve the car's VIN
    def getVin(self):
        return self.vin
    
    # Getter method to retrieve the car's status as a Status enum
    def getStatus(self):
        return self.status
    
    # Getter method to retrieve the car's status as a string
    def getStatusStr(self):
        return st.StatusToStr(self.status)
    
    # Getter method to retrieve the car's information dictionary
    def getCarInfo(self):
        return self.info

    # Setter method to update the car's status
    def SetStatus(self, updated_status):
        if not isinstance(updated_status, str):
            self.status = updated_status
            return
        self.status = st.strToStatus(updated_status.lower())

    # Method to convert the car object to a dictionary
    def to_dict(self):
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

    # Method to serialize the car object to JSON
    def serialize(car):
        if isinstance(car, Car):
            return car.to_dict()
        raise TypeError("Object of type 'Car' is not JSON serializable")

    # Method to check if the car is available
    def isAvailable(self):
        return self.status == st.Status.AVAILABLE
    
    # Method to update the car's price
    def UpdatePrice(self, newprice):
        self.price = newprice

    # Method to retrieve the car's details as a string
    def getDetails(self):
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

    # Method to check if two car objects are equal based on their VINs
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Car):
            return self.vin == __o.vin
    
    # Method to get the string representation of the car object
    def __str__(self) -> str:
        locale.setlocale( locale.LC_ALL, '' )
        # Return the string representation of the car object including its year, make, model, price, and status
        return f"{self.info['year']} {bcolors.BOLD}{self.info['model']} {self.info['make']}{bcolors.ENDC} {bcolors.OKGREEN}{locale.currency(self.price, grouping=True )}{bcolors.ENDC} {bcolors.UNDERLINE}{self.status}{bcolors.ENDC}"

    # Method to get the string representation of the car object for debugging purposes
    def __repr__(self) -> str:
        # Return the string representation of the car object including its model and make
        return f"{self.info['model']} {self.info['make']}"
