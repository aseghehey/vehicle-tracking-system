from PigeonBox.interface import *
from PigeonBox.session import Auth
from PigeonBox.bcolors import *
from PigeonBox.main import *
import unittest
from unittest.mock import patch

#testcase 1: customer buying a car (success expected)
class TestBuyCar(unittest.TestCase):
    def test_buy_car_success(self):
        self.assertEqual(1+1,2)
    
    def test_buy_car_fail(self):
        #testcode goes here
        pass


#testcase 2: adding a car to inventory
class TestAddCar(unittest.TestCase):
    def test_add_car_success(self):
        pass
    def test_add_car_fail(self):
        pass


#testcase 3: removing a car from inventory
class TestRemoveCar(unittest.TestCase):
    def test_remove_car_success(self):
        pass
    def test_remove_car_fail(self):
        pass


#testcase 4: managing employees
class TestManageEmployees:
    def test_add_employee(self):
        pass
    def test_remove_employee(self):
        pass


#testcase 5: managing customers
class TestManageCustomers:
    def test_add_customer(self):
        pass
    def test_remove_customer(self):
        pass

#testcase 6: Managing Orders
class TestManageOrders:
    def test_delete_order(self):
        pass

###################################################################################################################

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestBuyCar('test_buy_car_success'))
    suite.addTest(TestBuyCar('test_buy_car_fail'))  
    runner = unittest.TextTestRunner()
    runner.run(suite)

