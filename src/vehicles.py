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

    def setStatus(self, updated_status):
        self.status = {'available': Status.AVAILABLE,
                       'ordered': Status.ORDERED,
                       'backorder': Status.BACKORDER,
                       'delivered': Status.DELIVERED}[updated_status.lower()]

    def updatePrice(self, newprice):
        self.price = newprice

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Car):
            return self.vin == __o.vin

    def __str__(self) -> str:
        locale.setlocale(locale.LC_ALL, '')
        return f"{self.info['model']} {self.info['make']} {locale.currency(self.price, grouping=True )}"
