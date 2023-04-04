from enum import Enum
class Status(Enum):
    AVAILABLE = 1 # when cars are added
    ORDERED = 2 # when a customer orders a car
    BACKORDER = 3 # when car is out of stock -- could be a customer ordered, then got removed, set car to backorder status rather than available
    DELIVERED = 4 # when a car is delivered to a customer #TODO: add this functionality in the car sales menu
