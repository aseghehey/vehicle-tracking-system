"""
####################################################################################################################
[replace text and delete in bracket]
PROGRAM [name]:  [purpose of code and function. brief]

PROGRAMMER: [firstName] [lastName] [email]

VERSION 1: written [day] [month] 2023 by [firstInitial]. [lastName]
REVISION [revision# ex: 1.1]: [day] [month] 2023 by [firstInitial]. [lastName] to [purpose of revision]


PURPOSE:
[general purpose of code and each functionality. thorough description]

DATA STRUCTURES:
[major data structures and variables]
[ex: variable LENGTH - integer]

ALGORITHM:
[brief description of logic flow]

ERROR HANDLING:
[brief description error handling]

####################################################################################################################
"""
from status import *

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
     
    def setStatus(self, updated_status):
        self.status = {'available':Status.AVAILABLE,
                       'ordered': Status.ORDERED,
                       'backorder':Status.BACKORDER,
                       'delivered': Status.DELIVERED}[updated_status.lower()]
    
    def updatePrice(self, newprice):
        self.price = newprice

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Car): 
            return self.vin == __o.vin
    
    def __str__(self) -> str:
        return f"{self.info['model']} {self.info['make']} priced at ${self.price}"

