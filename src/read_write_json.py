from vehicles import *
from user import *
import json
from os import path


def loadInventory():
    # cars = {}
    # with open('data/inventory.json', 'r') as file:
    #     json_file = json.load(file)
    #     for car in json_file:
    #         current_car = Car(vin=car['vin'], info=car['info'][0], performance=car['performance'][0],
    #                           design=car['design'][0], handling=car['handling'], comfort=car['comfort'],
    #                           entertainment=car['audio'], protection=car['protection'][0], package=car['package'],
    #                           price=car['price'])
    #         cars.(current_car)
    # return cars

    with open('data/inventory.json', 'r') as file:
        inventory = json.load(file)
        return inventory


def loadUsers():
    customers, admins = [], []
    with open('data/users.json', 'r') as usr_file:
        json_user = json.load(usr_file)
        for i in range(len(json_user)):
            cur = json_user[i]
            name = cur['name'][0]
            user = {0:'employee', 1:'admin'}[i % 2] # dividing them equally (temporary; for testing) -- useful if we add customer user
            if user == 'employee':
                customer = Employee(username=cur['username'], password=cur['password'],
                                first_name=name['firstName'], last_name=name['lastName'], 
                                date_joined=cur['dateJoined'])
                customers.append(customer)
            else:
                admin = Admin(username=cur['username'], password=cur['password'],
                                first_name=name['firstName'], last_name=name['lastName'], 
                                date_joined=cur['dateJoined'])
                admins.append(admin)
    return customers, admins
                
def loadOrders():
    # use username_to_User
    pass

    with open('data/users.json', 'r') as file:
        users = json.load(file)
        return users


def loadOrders():
    '''
    Reads the orders from orders.json and formats 
    the objects into an array of type Order. Then,
    it returns the array of type Order
    '''
    # orders = []
    # with open('data/orders.json', 'r') as ord_file:
    #     json_order = json.load(ord_file)
    #     for i in range(len(json_order)):
    #         cur = json_order[i]
    #         current_order = Order(
    #             #I had to instantiate to a car object because the orders.py expects it as a car object
    #             car=Car(vin=cur['vin']), buyer=cur['user'],  dateBought=cur['dateBought'])
    #         orders.append(current_order)
    # return orders

    with open('data/orders.json', 'r') as file:
        orders = json.load(file)
        return orders


def writeJson(file):
    '''
    This function writes data to a json file, it will determine what kind of data is being loaded and write to 
    the appopriate json file
    '''

# if we are dealing with the car inventory
    if (file == 'data/inventory.json'):
        with open('data/mock_data.json', 'w') as f:
            newData = loadInventory()
            json.dump(newData, f, ensure_ascii=False, indent=4)

# if we are dealing with the users
    elif (file == 'data/users.json'):
        with open('data/mock_data.json', 'w') as f:
            newData = loadUsers()
            json.dump(newData, f, ensure_ascii=False, indent=4)

# if we are dealing with orders
    elif (file == 'data/orders.json'):
        with open('data/mock_data.json', 'w') as f:
            newData = loadOrders()
            json.dump(newData, f, ensure_ascii=False, indent=4)

    else:
        print("not a relevant json file")

'''
okay, so the two functions writeJson and updateInventory aren't really working together right now. I made
writeJson kinda how I think we talked about doing it, but after I coded it and was thinking of how the user
would go in and actually make the changes to the json files, I feel like the below implementation of
updateInventory might be easier?
We would have one of these update functions for each of the json files. so one for inventory, one for orders, and
one for users. In these functions the user can either add, delete, or update an existing object. 

I made a new json file for testing called mock_data.json. i just copied iventory.json into it.
'''

def updateInventory(file):
    # Check if file exists
    if path.isfile(file) is False:
        raise Exception("File not found")

    # Read JSON file
    with open(file) as f:
        listObj = json.load(f)

    # Verify existing list
    print(listObj)
    print(type(listObj))

    task = input("Do you want to add, delete, or update inventory?")

    if (task == "add"):
        # later we would make it so the user specifices what they want to add but for testing
        # im hardcoding a car object in here
        listObj.append({
            "vin": "TESTTESTTESTTESTTEST",
            "info": [
                {
                    "model": "1500",
                    "make": "Chevrolet",
                    "mileage": 6465,
                    "year": 1994,
                    "color": "Violet"
                }
            ],
            "performance": [{"engine": "Electric", "transmission": "CVT"}],
            "design": [
                {
                    "interior": [
                        "Side Airbags",
                        "Universal Garage Door Opener",
                        "Overhead Airbags",
                        "Power Locks",
                        "Power Seat(s)"
                    ],
                    "exterior": [
                        {
                            "paint": "Pearlescent",
                            "extra": [
                                "Alloy Wheels",
                                "Turbo Charged Engine",
                                "Power Hatch/Deck Lidis",
                                "ABS Brakes"
                            ]
                        }]
                }],
            "handling": ["Power Steering", "Anti-lock brakes"],
            "comfort": [
                "Front Seat Heaters",
                "Cross-Traffic Alert",
                "Skylight(s)",
                "Lane Departure Warning"
            ],
            "audio": [
                "SiriusXM Trial Available",
                "AM/FM Stereo",
                "Auxiliary Audio Input"
            ],
            "protection": [
                {
                    "maintenance": "every 10.000 mile maintenance",
                    "warranty": ["30 day money back guarantee (up to 1500 miles)"]
                }],
            "package": "Sports",
            "price": 172965
        })

        #dump newly updated information to json file
        with open(file, 'w') as json_file:
            json.dump(listObj, json_file, indent=4, separators=(',',': '))
        
        print('Successfully appended to the JSON file')

    elif (task == "delete"):
        # add functionality here
        return
    elif (task == "update"):
        # add functionality here
        return
    else:
        task = input(
            "input not correct, please enter one of the three options")
