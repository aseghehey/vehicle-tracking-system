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


    #add a car (we will use this car for some of the following test cases)
    @mock.patch('builtins.input', create=True)
    def test_addCar(self, mocked_input):
        mocked_input.side_effect = ['test', 'test', '3', '4', '1', '500500500', 'Ford, Fusion, 2015', '500, Grey', '10000', '4 Cylinder, Automatic', 'Fabric, Normal', 'Normal', 'Normal', 'Bluetooth', 'None', 'Base', '5 Years, Average', 'Available', 'j', 'q', 'q', 'n']
        run()
        
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
