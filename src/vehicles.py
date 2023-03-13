from status import *

class Car ():
    def __init__(self, vin, model, make, mileage, year, color, performance={}, design={}, handling=[], comfort=[], entertainment=[], protection={}, package='', price=0):
        self.vin = vin
        self.make = make
        self.mileage = mileage
        self.year = year
        self.color = color
        self.performance = performance
        self.design = design
        self.handling = handling
        self.comfort = comfort
        self.entertainment = entertainment
        self.protection = protection
        self.package = package
        self.price = price
    
    def __str__(self):
        return f"Car {self.make} {self.model} {self.year} ${self.price}"
    

if __name__ == "__main__":
    pass