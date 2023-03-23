from status import *
import locale
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
        if not status: status = Status.AVAILABLE
        self.status = status
        self.price = price
    
    def isAvailable(self):
        return self.status == Status.AVAILABLE
        
    def SetStatus(self, updated_status):
        self.status = {'available':Status.AVAILABLE,
                       'ordered': Status.ORDERED,
                       'backorder':Status.BACKORDER,
                       'delivered': Status.DELIVERED}[updated_status.lower()]
    
    def UpdatePrice(self, newprice):
        self.price = newprice

    def Details(self):
        return self.__str__() + f"\nVIN: {self.vin}\nPerformance: {self.performance}\nInterior design: {self.design['interior']}\nExterior design: {self.design['exterior']}\nComfort: {self.comfort}\nPackage: {self.package}"

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Car): 
            return self.vin == __o.vin
    
    def __str__(self) -> str:
        locale.setlocale( locale.LC_ALL, '' )
        return f"{self.info['model']} {self.info['make']} {locale.currency(self.price, grouping=True )} year: {self.info['year']}"

    def __repr__(self) -> str:
        return f"{self.info['model']} {self.info['make']}"

