import locale
import PigeonBox.status as st
from PigeonBox.bcolors import bcolors


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
        if status is None:
            status = st.Status.AVAILABLE
        if isinstance(status, str):
            status = st.strToStatus(status)
        self.status = status
        self.price = price

    def UpdateMileage(self, newMileage):
        self.info['mileage'] = newMileage

    def UpdateWarranty(self, newWarranty):
        self.protection['warranty'].append(newWarranty)

    def getVin(self):
        return self.vin
    
    def isDelivered(self):
        return True if self.status == st.Status.DELIVERED else False
    
    def getStatus(self):
        return self.status
    
    def getStatusStr(self):
        return st.StatusToStr(self.status)
    
    def getCarInfo(self):
        return self.info

    def SetStatus(self, updated_status):
        if not isinstance(updated_status, str):
            self.status = updated_status
            return
        self.status = st.strToStatus(updated_status.lower())

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


    def serialize(car):
        if isinstance(car, Car):
            return car.to_dict()
        raise TypeError("Object of type 'Car' is not JSON serializable")

    def isAvailable(self):
        return self.status == st.Status.AVAILABLE
        
    def UpdatePrice(self, newprice):
        self.price = newprice

    def getDetails(self):
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
        return self.__str__() + res

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Car):
            return self.vin == __o.vin
    
    def __str__(self) -> str:
        locale.setlocale( locale.LC_ALL, '' )
        return f"{self.info['year']} {bcolors.BOLD}{self.info['model']} {self.info['make']}{bcolors.ENDC} {bcolors.OKGREEN}{locale.currency(self.price, grouping=True )}{bcolors.ENDC} {bcolors.UNDERLINE}{self.status}{bcolors.ENDC}"

    def __repr__(self) -> str:
        return f"{self.info['model']} {self.info['make']}"
