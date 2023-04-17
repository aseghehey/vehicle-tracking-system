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
from vehicles import Car
import unittest
from PigeonBox import Interface, AdminInterface, users, vehicles

#main menu: in integration testing we will be testing how the 5 main components work (i.e. all individual functions working together)
# 1. Customer Orders
# 2. Car Sales
# 3. Car Inventory
# 4. Manage Customers
# 5. Manage Employees
# A: Account settings




class TestInterfaceIntegration(unittest.TestCase):

    def setUp(self):
        self.interface = Interface()
        self.admin_interface = AdminInterface()

        self.car_data = {
            'vin': '1234567890',
            'info': {'model': 'Model S', 'make': 'Tesla', 'year': 2022, 'color': 'red', 'mileage': 0},
            'performance': {},
            'design': {},
            'handling': {},
            'comfort': {},
            'entertainment': {},
            'protection': {},
            'package': {},
            'price': 80000
        }

        self.customer_data = {
            'first': 'John',
            'last': 'Doe',
            'card': '1234 5678 9012 3456',
            'email': 'johndoe@example.com',
            'address': '1234 Main St'
        }

    def tearDown(self):
        del self.interface
        del self.admin_interface

    def test_add_remove_inventory(self):
        # Test adding a car to the inventory
        added = self.admin_interface.AddInventory(**self.car_data)
        self.assertTrue(added)
        
        # Test removing a car from the inventory
        car = self.admin_interface.vinToCar(self.car_data['vin'])
        self.assertIsNotNone(car)
        
        removed = self.admin_interface.RemoveInventory(car)
        self.assertTrue(removed)

    def test_add_remove_customer(self):
        # Test adding a customer
        customer = self.interface.AddCustomer(**self.customer_data)
        self.assertIsNotNone(customer)
        
        # Test removing a customer
        customer = self.interface.emailToCustomer(self.customer_data['email'])
        self.assertIsNotNone(customer)
        
        self.interface.RemoveCustomer(customer)
        self.assertFalse(self.interface.isCustomer(customer))

    def test_add_remove_employee(self):
        # Test adding an employee
        employee_data = {'username': 'testemployee', 'passwd': 'testpassword', 'fname': 'Test', 'lname': 'Employee'}
        added = self.admin_interface.AddEmployee(**employee_data)
        self.assertTrue(added)

        # Test removing an employee
        employee = self.admin_interface.usernameToUser(employee_data['username'])
        self.assertIsNotNone(employee)
        
        removed = self.admin_interface.RemoveUser(employee)
        self.assertTrue(removed)

    def test_make_undo_order(self):
        # Test making an order
        self.admin_interface.AddInventory(**self.car_data)
        car = self.admin_interface.vinToCar(self.car_data['vin'])
        self.assertIsNotNone(car)
        
        customer = self.interface.AddCustomer(**self.customer_data)
        self.assertIsNotNone(customer)
        
        employee_data = {'username': 'testemployee', 'passwd': 'testpassword', 'fname': 'Test', 'lname': 'Employee'}
        self.admin_interface.AddEmployee(**employee_data)
        employee = self.admin_interface.usernameToUser(employee_data['username'])
        self.assertIsNotNone(employee)
        
        order = self.interface.MakeOrder(customer, car, employee)
        self.assertIsNotNone(order)
        
        # Test undoing an order
        self.interface.UndoOrder(order)
        self.assertFalse(self.interface.doesOrderExist(order))

if __name__ == '__main__':
    unittest.main()
