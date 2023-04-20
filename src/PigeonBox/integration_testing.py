from PigeonBox.session import Auth
from PigeonBox.bcolors import *
from PigeonBox.main import *
import unittest
from unittest.mock import *
from unittest import mock
from unittest import TestCase
import time
from PigeonBox import session, status, orders, users, vehicles
from PigeonBox.interface import *   
import unittest
from parsers.readJson import *


#main menu: in integration testing we will be testing how the 5 main components work (i.e. all individual functions working together)
# 1. Customer Orders
# 2. Car Sales
# 3. Car Inventory
# 4. Manage Customers
# 5. Manage Employees
# A: Account settings

#3. Car Inventory
class TestCarInventory(unittest.TestCase):

    #add a car (we will use this car for some of the following test cases)
    @mock.patch('builtins.input', create=True)
    def test_addCar(self, mocked_input):
        mocked_input.side_effect = ['test', 'test', '3', '4', '1', '500500500', 'Ford, Fusion, 2015', '500, Grey', '100000', '4 Cylinder, Automatic', 'Fabric, Normal', 'Normal', 'Normal', 'Bluetooth', 'None', 'Base', '5 Years, Average', 'Available', 'j', 'q', 'q', 'n']
        run()
        

#4. Manage Customers
class TestManageCustomers(unittest.TestCase):

    #add a customer (we will use this customer for some of the following test cases)
    @mock.patch('builtins.input', create=True)
    def test_addCustomer(self, mocked_input):
        mocked_input.side_effect = ['test', 'test', '4', '2', 'Lia', 'Lopez', 'lialopez@gmail.com', '2222222222222222', '123 dog drive', 'j', 'q', 'q', 'n']
        run()

#1. Customer Orders
class TestCustomerOrders(unittest.TestCase):

    #adding an order for the customer we created above
    @mock.patch('builtins.input', create=True)
    def test_addOrder(self, mocked_input):
        mocked_input.side_effect = ['test', 'test', '1', '1', '51', 'y', 'n', '6', 'j', 'q', 'q', 'n']
        run()

    #delete the same order as above
    @mock.patch('builtins.input', create=True)
    def test_deleteOrder(self, mocked_input):
        mocked_input.side_effect = ['test', 'test', '1', '2', '6', 'y', 'j', 'q', 'q', 'n']
        run()


# 5. Manage Employees
class TestManageEmployees(unittest.TestCase):

    #adding an employee
    @mock.patch('builtins.input', create=True)
    def test_addUsesr(self, mocked_input):
        mocked_input.side_effect = ['test', 'test', '5', '2', 'pepelopez', 'testtest123!', 'pepe', 'lopez', 'n', 'j', 'q', 'q', 'n']
        run()
    
    #deleting an employee (the same one we added above)
    @mock.patch('builtins.input', create=True)
    def test_removeUser(self, mocked_input):
        mocked_input.side_effect = ['test', 'test', '5', '3', '18', 'y', 'j', 'q', 'q', 'n']
        run()


class TestManageCustomerDelete(unittest.TestCase):

    #delete the customer we made above for the tests
    @mock.patch('builtins.input', create=True)
    def test_deleteCustomer(self, mocked_input):
        mocked_input.side_effect = ['test', 'test', '4', '3', '6', 'y', 'j', 'q', 'q', 'n']
        run()

class TestManageInventoryDelete(unittest.TestCase):

    #delete the car we made above for the tests
    @mock.patch('builtins.input', create=True)
    def test_deleteCar(self, mocked_input):
        mocked_input.side_effect = ['test', 'test', '3', '4', '2', '51', 'y', 'j', 'q', 'q', 'n']
        run()