####################################################################################################################
'''
////////////////
PROGRAM status:   defines an Enum class to represent the status of a car(available, ordered, backoreded, delivered).
                  These are used to organize vehicles by their status.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

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


# One-line description: Convert a string representation of car status to its corresponding enum value.
# General description: This function takes a string representation of a car status, such as "available" or "ordered", and returns the corresponding enum value from the predefined STATUS_DICT dictionary.
#   If the input status string is not found in the dictionary, the function returns None.
# Typical calling examples:
#   strToStatus("available") returns Status.AVAILABLE.
#   strToStatus("backorder") returns Status.BACKORDER.
#   strToStatus("sold") returns None.
# Accessibility: The function is defined globally and can be accessed from anywhere in the program.
# Function prototype: def strToStatus(status: str) -> Union[Status, None]
def strToStatus(status: str):
    if status not in STATUS_DICT: return
    return STATUS_DICT[status]



# One-line description: Converts a Status enum value to its string representation.
# General description: This function takes in a Status enum value and returns its corresponding string representation based on
#   the values defined in the STATUS_DICT dictionary.
# Typical calling examples:
#   StatusToStr(Status.AVAILABLE) returns "available"
#   StatusToStr(Status.ORDERED) returns "ordered"
# Accessibility: This function can be accessed anywhere within the codebase where the st module is imported.
# Function prototype: def StatusToStr(status: Status) -> str:
def StatusToStr(status: Status):
    for key, value in STATUS_DICT.items():
        if value == status:
            return key
