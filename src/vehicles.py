from status import *
import locale
from bcolors import bcolors
class Car ():
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
        if not status:
            status = Status.AVAILABLE
        self.status = status
        self.price = price

    def to_dict(self):
        return {
            "vin": self.vin,
            "info": self.info,
            "performance": self.performance,
            "design": self.design,
            "handling": self.handling,
            "comfort": self.comfort,
            "entertainment": self.entertainment,
            "protection": self.protection,
            "package": self.package,
            "status": self.status.value,
            "price": self.price
        }


    def serialize(car):
        if isinstance(car, Car):
            return car.to_dict()
        raise TypeError("Object of type 'Car' is not JSON serializable")

    def isAvailable(self):
        return self.status == Status.AVAILABLE
        
    def SetStatus(self, updated_status):
        if not isinstance(updated_status, str):
            self.status = updated_status
            return
        self.status = {'available':Status.AVAILABLE,
                       'ordered': Status.ORDERED,
                       'backorder': Status.BACKORDER,
                       'delivered': Status.DELIVERED}[updated_status.lower()]
    
    def UpdatePrice(self, newprice):
        self.price = newprice

    def Details(self):
        return self.__str__() + f"\nVIN: {self.vin}\nPerformance: {self.performance}\nInterior design: {self.design['interior']}\nExterior design: {self.design['exterior']}\nComfort: {self.comfort}\nPackage: {self.package}\nEntertainment {self.entertainment}"

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Car):
            return self.vin == __o.vin
    
    def __str__(self) -> str:
        locale.setlocale( locale.LC_ALL, '' )
        return f"{self.info['year']} {bcolors.BOLD}{self.info['model']} {self.info['make']}{bcolors.ENDC} {bcolors.OKGREEN}{locale.currency(self.price, grouping=True )}{bcolors.ENDC} {bcolors.UNDERLINE}{self.status}{bcolors.ENDC}"

    def __repr__(self) -> str:
        return f"{self.info['model']} {self.info['make']}"
