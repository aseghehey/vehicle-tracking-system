from vehicles import *
from users import *
import json
from os import path

def LoadInventory():
    cars = []
    with open('src/data/inventory.json', 'r') as file:
        json_file = json.load(file)
        for car in json_file:
            current_car = Car(vin=car['vin'], info=car['info'][0], performance=car['performance'][0],
                              design=car['design'][0], handling=car['handling'], comfort=car['comfort'],
                              entertainment=car['audio'], protection=car['protection'][0], package=car['package'],
                              price=car['price'])
            cars.append(current_car)
    return cars

def LoadUsers():
    employees, admins = [], []
    with open('src/data/users.json', 'r') as usr_file:
        json_user = json.load(usr_file)
        for i in range(len(json_user)):
            cur = json_user[i]
            name = cur['name'][0]
            user = {0:'employee', 1:'admin'}[i % 2] # dividing them equally (temporary; for testing) -- useful if we add customer user
            if user == 'employee':
                employee = Employee(username=cur['username'], password=cur['password'],
                                first_name=name['firstName'], last_name=name['lastName'], 
                                date_joined=cur['dateJoined'])
                employees.append(employee)
            else:
                admin = Admin(username=cur['username'], password=cur['password'],
                                first_name=name['firstName'], last_name=name['lastName'], 
                                date_joined=cur['dateJoined'])
                admins.append(admin)
    return customer, admins
                
def loadOrders():
    orders = []
    with open('src/data/orders.json', 'r') as file:
        json_file = json.load(file)
        
        for order in json_file:
            # do we want to leave it like this? or make it so that the buyer is an actual instance of a user object?
            current_order = Order(car=order['vin'], buyer=order['buyer'], dateBought = order['dateBought'])
            orders.append(current_order)
    return orders


def writeJson(data):
    '''
    This function writes data to a json file, it will determine what kind of data is being loaded and write to 
    the appopriate json file with the proper formatting
    '''
    flag = False
    print(type(data[0]))
# decide which file based on objct type in array
    if isinstance(data[0], Car):
        file = 'src/data/inventory.json'
    elif isinstance(data[0], Order):
        file = 'src/data/orders.json'
    elif isinstance(data[0], list):
        if isinstance(data[0][0], Employee) and isinstance(data[0][1], Admin):
            flag = True
            file = 'data/users.json'
    else:
        file = ''
        print('Not a valid type given in array.')
        return
    if flag:
        with open('src/data/mock_data.json', 'w') as f:
            serialized = json.dumps(data[0], default=type(data[0][0]).serialize, ensure_ascii=False, indent=4)
            f.write(serialized)
            serialized = json.dumps(data[1], default=type(data[0][1]).serialize, ensure_ascii=False, indent=4)
            f.write(serialized)

    #serialize the array and write it to the appropriate json file
    with open('src/data/mock_data.json', 'w') as f:
            serialized = json.dumps(data, default=type(data[0]).serialize, ensure_ascii=False, indent=4)
            f.write(serialized)
            



    

