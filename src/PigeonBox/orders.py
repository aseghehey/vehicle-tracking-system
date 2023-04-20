from datetime import datetime
from PigeonBox.bcolors import bcolors

class Order():
    """ Class represents orders made, works like a database one-to-one relationship with a buyer and a car"""
    def __init__(self, id, car=None, buyer=None, dateBought=None, employee=None, deliveryDate = None) -> None:
        self.id = id 
        
        if car and not deliveryDate:  
            car.SetStatus('ordered')  #  set car status to ordered

        self.car = car        
        self.buyer = buyer #the user id
        self.salesBy = employee
        # if a date is not specified, it will be set to today's date
        if not dateBought: dateBought = datetime.today()
        else: dateBought = datetime.strptime(dateBought, "%Y-%m-%d")
        self.when = dateBought

        if deliveryDate:
            deliveryDate = datetime.strptime(deliveryDate, "%Y-%m-%d")

        self.deliveryDate = deliveryDate
     
    def getUser(self):
        return self.buyer
    
    def getCar(self):
        return self.car
        
    def getSeller(self):
        return self.salesBy
    
    def getDate(self):
        return self.when
    
    def getId(self):
        return self.id
    
    def getDateJoined(self):
        return self.when.strftime("%Y-%m-%d")
    
    def to_dict(self):
        return {
            "id": self.id,
            "carVin": self.car.getVin(),
            "buyer": self.buyer.getEmail(),
            "soldBy": self.salesBy.getUsername(),
            "dateBought": self.when.strftime("%Y-%m-%d"),
            "deliveryDate": "" if not self.deliveryDate else self.deliveryDate.strftime("%Y-%m-%d"),
        }
    
    def updateDeliveryDate(self):
        today = datetime.today()
        self.deliveryDate = today

    def getDeliveryDate(self):
        return self.deliveryDate.strftime("%Y-%m-%d")

    def serialize(order):
        if isinstance(order, Order):
            return order.to_dict()
        raise TypeError("Object of type 'Order' is not JSON serializable")

    def RemoveOrder(self):
        """ Removes the order from the buyer's orders list and sets the car status to available"""
        self.buyer.orders.remove(self)
        self.car.SetStatus("available")
    
    def orderDetails(self):
        toret = f"\nCar:\n{self.car.getDetails()}\n\nSales by: {self.salesBy}\n\nCustomer {self.buyer.getDetails()}\n"
        return toret

    def __str__(self):
        salesBy = self.salesBy.__str__()
        salesBy = " ".join(salesBy.split(" ")[:3])
        # print(self.car.getStatus())
        # orderType = "Sale" if self.car.isDelivered() else "Order"

        return f"ID: #{self.id} {bcolors.BOLD}Made by {salesBy}{bcolors.ENDC}: {self.car.getCarInfo()['make']} {self.car.getCarInfo()['model']} for {bcolors.BOLD}{self.buyer.getLastName()}, {self.buyer.getFirstName()}{bcolors.ENDC}"
    
    """ Overriding the equality operator to compare two Order objects"""
    def __eq__(self, value) -> bool:
        if isinstance(value, Order):
            return value.id == self.id
        return False
    
    def __repr__(self) -> str:
        return f"{self.car}"
