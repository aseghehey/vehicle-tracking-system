from PigeonBox import vehicles, users, orders
from parsers.readJson import INVENTORY_PATH, ORDERS_PATH, CUSTOMER_PATH, USERS_PATH
import json
INDENTATION = 2

def writeJson(data):
    '''
    This function writes data to a json filePath, it will determine what kind of data is being loaded and write to 
    the appopriate json filePath with the proper formatting
    '''
# decide which filePath based on objct type in array
    dataType = None
    if isinstance(data[0], vehicles.Car):
        filePath = INVENTORY_PATH
        dataType = vehicles.Car
    elif isinstance(data[0], orders.Order):
        dataType = orders.Order
        filePath = ORDERS_PATH
    elif isinstance(data[0], users.Customer):
        dataType = users.Customer
        filePath = CUSTOMER_PATH
    elif isinstance(data[0], users.User):
        dataType = users.User
        filePath = USERS_PATH
    else:
        raise TypeError("Incorrect object list")

    #serialize the array and write it to the appropriate json filePath
    with open(filePath, 'w') as f:
        serialized = json.dumps(data, default=dataType.serialize, ensure_ascii=False, indent=INDENTATION)
        f.write(serialized)