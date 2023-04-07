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
            userType = cur["type"].lower()
            if userType == 'employee':
                employee = Employee(username=cur['username'], password=cur['password'],
                                first_name=name['firstName'], last_name=name['lastName'], 
                                date_joined=cur['dateJoined'])
                employees.append(employee)
            else:
                admin = Admin(username=cur['username'], password=cur['password'],
                                first_name=name['firstName'], last_name=name['lastName'], 
                                date_joined=cur['dateJoined'])
                admins.append(admin)
    return employees, admins
                
def loadOrders():
    orders = []
    with open('src/data/orders.json', 'r') as file:
        json_file = json.load(file)
        
        for i in range(len(json_file)):
            cur_order = json_file[i]
            id = cur_order['carVin']
            buyer = cur_order['buyer']
            salesBy = cur_order['soldBy']
            when = cur_order['dateBought'];
            order = Order(id, buyer, salesBy, when)
            orders.append(order)
    return orders

def LoadCustomers():
    customers = []
    with open('src/data/customers.json', 'r') as customer_file:
        json_customers = json.load(customer_file)
        for i in range(len(json_customers)):
            cur_json = json_customers[i]
            email = cur_json['email']
            name = cur_json['name'][0]
            fn, ln = name['first'], name['last']
            cc = cur_json['card']
            addy = cur_json['address']
            id = cur_json['id']
            
            customer = Customer(fn, ln, cc, email, addy, id)
            customers.append(customer)
    return customers

def writeJson(data):
    '''
    This function writes data to a json file, it will determine what kind of data is being loaded and write to 
    the appopriate json file with the proper formatting
    '''
    flag = False
# decide which file based on objct type in array
    if isinstance(data[0], Car):
        file = 'src/data/inventory.json'
    elif isinstance(data[0], Order):
        file = 'src/data/orders.json'
    elif isinstance(data[0], Customer):
        file = 'src/data/customers.json'
    elif isinstance(data[0][0], User):
        flag = True
        file = 'src/data/users.json'
    else:
        file = ''
        print('Not a valid type given in array.')
        return

    if flag:
        with open(file, 'w') as f:
            serialized = json.dumps(data[0], default=type(data[0][0]).serialize, ensure_ascii=False, indent=4)
            f.write(serialized)
            serialized = json.dumps(data[1], default=type(data[0][1]).serialize, ensure_ascii=False, indent=4)
            f.write(serialized)
    else:
        #serialize the array and write it to the appropriate json file
        with open(file, 'w') as f:
            serialized = json.dumps(data, default=type(data[0]).serialize, ensure_ascii=False, indent=4)
            f.write(serialized)



