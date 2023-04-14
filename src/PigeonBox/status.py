####################################################################################################################
'''
////////////////
PROGRAM status:   defines an Enum class to represent the status of a car(available, ordered, backoreded, delivered).
                  These are used to organize vehicles by their status.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu

////////////////
VERSION 1: written [day] [month] 2023 by [firstInitial]. [lastName]
REVISION [revision# ex: 1.1]: [day] [month] 2023 by [firstInitial]. [lastName] to [purpose of revision]

////////////////
PURPOSE:
The purpose of this code is to provide a convenient way to represent
and manipulate the status of cars in a car sales inventory system,
and to allow for easy conversion between string representations and enum values.

Methods:
- strToStatus(status: str): takes a string argument and returns the corresponding Status enum value. 
                            If the input string is not recognized as a valid status, the function returns None.
- StatusToStr(status: Status): takes a Status enum value and returns the corresponding string representation.

////////////////
DATA STRUCTURES:
DataStructures:
- Enum: to define the various status values of a car.
- Dictionary: to store the string representation of the status and its corresponding enum value.

Attributes:
None

////////////////
ALGORITHM:
None

////////////////
ERROR HANDLING:
No explicit error handling.

////////////////
'''
####################################################################################################################

from enum import Enum

#   Enum class that defines the status of a car, and two functions that convert 
#   between the string representation of a status and its corresponding enum value.
class Status(Enum):
    AVAILABLE = 1   # When a car is added to the inventory and is available for purchase
    ORDERED = 2     # When a customer orders a car and it is not yet delivered
    BACKORDER = 3   # when car is out of stock -- could be a customer ordered, then got removed, set car to backorder status rather than available
    DELIVERED = 4   # when a car is delivered to a customer #TODO: add this functionality in the car sales menu


STATUS_DICT = { "available": Status.AVAILABLE,
                "ordered": Status.ORDERED,
                "backorder": Status.BACKORDER,
                "delivered": Status.DELIVERED}

#   Converts a string representation of a status to its corresponding Status enum value.
def strToStatus(status: str):
    if status not in STATUS_DICT: return
    return STATUS_DICT[status]

#   Converts a Status enum value to its corresponding string representation.
def StatusToStr(status: Status):
    for key, value in STATUS_DICT.items():
        if value == status:
            return key
