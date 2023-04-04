from vehicles import *
from users import *
import json 

def LoadInventory():
    cars = []
    with open('data/inventory.json', 'r') as file:
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
    with open('data/users.json', 'r') as usr_file:
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
    return employees, admins

def LoadCustomers():
    customers = []
    with open('data/customers.json', 'r') as customer_file:
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
       
def LoadOrders():
    # use username_to_User
    pass

def WriteJson(): # for orders and users
    pass

