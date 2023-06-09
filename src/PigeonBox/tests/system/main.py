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

#run command: python3 -m PigeonBox.system_tests

# perform general tests as follows:
# - stress testing, i.e., pushing the system to its limits;
# - volume testing, i.e., testing the system with large volumes of data;
# - configuration testing, i.e., testing the system on various computer systems;
            #idk if we will be able to do this one
# - time testing, i.e., checking the speed of the system on typical data sets;


import unittest


#time testing: test the timing of the individual functionality

class TestTiming(unittest.TestCase):

    #adding and deleting an employee
    @mock.patch('builtins.input', create=True)
    def test_addUser(self, mocked_input):
        mocked_input.side_effect = ['test', 'test', '5', '2', 'pepelopez', 'testtest123!', 'pepe', 'lopez', 'n', 'j', 'q', 'q', 'n']
        t0 = time.time()
        run()
        t1 = time.time()
        total = t1-t0
        assert(total < 100)
    
    @mock.patch('builtins.input', create=True)
    def test_removeUser(self, mocked_input):
        mocked_input.side_effect = ['test', 'test', '5', '3', '18', 'y', 'j', 'q', 'q', 'n']
        t0 = time.time()
        run()
        t1 = time.time()
        total = t1-t0
        assert(total < 100)


    #adding a car
    @mock.patch('builtins.input', create=True)
    def test_addCar(self, mocked_input):
        mocked_input.side_effect = ['test', 'test', '3', '4', '1', '500500500', 'Ford, Fusion, 2015', '500, Grey', '100000', '4 Cylinder, Automatic', 'Fabric, Normal', 'Normal', 'Normal', 'Bluetooth', 'None', 'Base', '5 Years, Average', 'Available', 'j', 'q', 'q', 'n']
        t0 = time.time()
        run()
        t1 = time.time()
        total = t1-t0
        assert(total < 100)



    #adding and deleting an order
    @mock.patch('builtins.input', create=True)
    def test_addOrder(self, mocked_input):
        mocked_input.side_effect = ['test', 'test', '1', '1', '51', 'y', 'n', '5', 'j', 'q', 'q', 'n']
        t0 = time.time()
        run()
        t1 = time.time()
        total = t1-t0
        assert(total < 100)


    @mock.patch('builtins.input', create=True)
    def test_deleteOrder(self, mocked_input):
        mocked_input.side_effect = ['test', 'test', '1', '2', '6', 'y', 'j', 'q', 'q', 'n']
        t0 = time.time()
        run()
        t1 = time.time()
        total = t1-t0
        assert(total < 100)

    #delete the car
    @mock.patch('builtins.input', create=True)
    def test_removeCar(self, mocked_input):
        mocked_input.side_effect = ['test', 'test', '3', '4', '2', '51', 'y', 'j', 'q', 'q', 'n']
        t0 = time.time()
        run()
        t1 = time.time()
        total = t1-t0
        assert(total < 100)


if __name__ == '__main__':
    unittest.main()