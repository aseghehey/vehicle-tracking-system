from PigeonBox.interface import *
from PigeonBox.session import Auth
from PigeonBox.bcolors import *
from PigeonBox.main import *
import unittest
from unittest.mock import patch
from unittest import TestCase, mock


#testcase 1: customer buying a car (success expected)
class TestBuyCar(unittest.TestCase):
    @mock.patch('PigeonBox.run', create=True)
    @mock.patch('PigeonBox.MakeOrder', create=True)
    
    def test_buy_car_success(self, mocked_input_1, action2):
        
        mocked_input_1 = "1"
        action1 = run()
        #self.assertEqual(action1, mocked_input_1)
        action2 = interface.MakeOrder
        assert action2.called()


        



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

