from PigeonBox import vehicles, users, orders
import json

INVENTORY_PATH = "/Users/dariya/OneDrive - University of South Florida/University/3.2/CEN 4020/vehicle-tracking-system/src/data/inventory.json"
USERS_PATH = "/Users/dariya/OneDrive - University of South Florida/University/3.2/CEN 4020/vehicle-tracking-system/src/data/users.json"
ORDERS_PATH = "/Users/dariya/OneDrive - University of South Florida/University/3.2/CEN 4020/vehicle-tracking-system/src/data/orders.json"
CUSTOMER_PATH = "/Users/dariya/OneDrive - University of South Florida/University/3.2/CEN 4020/vehicle-tracking-system/src/data/customers.json"

def LoadInventory():
    cars = []
    with open(INVENTORY_PATH, 'r') as jsonFile:
        carsJson = json.load(jsonFile)
        for car in carsJson:
            current_car = vehicles.Car(vin=car['vin'], info=car['info'][0], performance=car['performance'][0],
                              design=car['design'][0], handling=car['handling'], comfort=car['comfort'],
                              entertainment=car['audio'], status= car['status'], protection=car['protection'][0], package=car['package'],
                              price=car['price'])
            cars.append(current_car)
    return cars

def LoadUsers():
    employees, admins = [], []
    with open(USERS_PATH, 'r') as jsonFile:
        usersJson = json.load(jsonFile)
        for i in range(len(usersJson)):
            currentUser = usersJson[i]
            name = currentUser['name'][0]
            userType = currentUser["type"].lower()
            if userType == 'employee':
                employee = users.Employee(username=currentUser['username'], password=currentUser['password'],
                                first_name=name['firstName'], last_name=name['lastName'], 
                                date_joined=currentUser['dateJoined'])
                employees.append(employee)
            else:
                admin = users.Admin(username=currentUser['username'], password=currentUser['password'],
                                first_name=name['firstName'], last_name=name['lastName'], 
                                date_joined=currentUser['dateJoined'])
                admins.append(admin)
    return employees, admins
                
def LoadOrders():
    orderList = []
    with open(ORDERS_PATH, 'r') as jsonFile:
        ordersJson = json.load(jsonFile)
        for i in range(len(ordersJson)):
            currentOrder = ordersJson[i]
            # order = orders.Order(id=id, car=car, buyer=buyer, employee=sellingUser, dateBought=when)
            orderList.append(currentOrder)
    return orderList

def LoadCustomers():
    customers = []
    with open(CUSTOMER_PATH, 'r') as jsonFile:
        customersJson = json.load(jsonFile)
        for i in range(len(customersJson)):
            currentCustomer = customersJson[i]
            emailAddress = currentCustomer['email']
            name = currentCustomer['name'][0]
            firstName, lastName = name['first'], name['last']
            creditCard = currentCustomer['card']
            homeAddress = currentCustomer['address']
            # add customer
            customer = users.Customer(firstName, lastName, creditCard, emailAddress, homeAddress)
            customers.append(customer)
    return customers
