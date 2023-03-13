from status import *

class Car ():
    def __init__(self, vin, info={}, performance={}, design={}, handling=[], comfort=[], entertainment=[], protection={}, package='', status=None, price=0):
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
     
    def __str__(self) -> str:
        return f"{self.info['model']}"
