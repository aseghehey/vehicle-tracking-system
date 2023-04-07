from PigeonBox import vehicles, users, orders
from parsers.readJson import INVENTORY_PATH, ORDERS_PATH, CUSTOMER_PATH, USERS_PATH
import json
INDENTATION = 2

def writeJson(data):
    '''
    This function writes data to a json filePath, it will determine what kind of data is being loaded and write to 
    the appopriate json filePath with the proper formatting
    '''
    isUser = False
# decide which filePath based on objct type in array
    if isinstance(data[0], vehicles.Car):
        filePath = INVENTORY_PATH
    elif isinstance(data[0], orders.Order):
        filePath = ORDERS_PATH
    elif isinstance(data[0], users.Customer):
        filePath = CUSTOMER_PATH
    elif isinstance(data[0][0], users.User):
        isUser = True
        filePath = USERS_PATH
    else:
        raise TypeError("Incorrect object list")

    if isUser:
        with open(filePath, 'w') as f:
            serialized = json.dumps(data[0], default=type(data[0][0]).serialize, ensure_ascii=False, indent=INDENTATION)
            f.write(serialized)
            serialized = json.dumps(data[1], default=type(data[0][1]).serialize, ensure_ascii=False, indent=INDENTATION)
            f.write(serialized)
    else:
        #serialize the array and write it to the appropriate json filePath
        with open(filePath, 'w') as f:
            serialized = json.dumps(data, default=type(data[0]).serialize, ensure_ascii=False, indent=INDENTATION)
            f.write(serialized)