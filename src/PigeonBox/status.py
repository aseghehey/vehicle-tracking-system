from enum import Enum

class Status(Enum):
    AVAILABLE = 1 # when cars are added
    ORDERED = 2 # when a customer orders a car
    BACKORDER = 3 # when car is out of stock -- could be a customer ordered, then got removed, set car to backorder status rather than available
    DELIVERED = 4 # when a car is delivered to a customer #TODO: add this functionality in the car sales menu

STATUS_DICT = { "available": Status.AVAILABLE,
                "ordered": Status.ORDERED,
                "backorder": Status.BACKORDER,
                "delivered": Status.DELIVERED}

def strToStatus(status: str):
    if status not in STATUS_DICT: return
    return STATUS_DICT[status]

def StatusToStr(status: Status):
    for key, value in STATUS_DICT.items():
        if value == status:
            return key