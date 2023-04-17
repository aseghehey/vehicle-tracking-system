# from PigeonBox.session import Auth
# from PigeonBox.bcolors import *
# from PigeonBox.main import *
# import unittest
# from unittest.mock import *
# from unittest import mock
# from unittest import TestCase
# import time
# from PigeonBox import session, status, orders, users, vehicles
# from PigeonBox.interface import *

# #run command: python3 -m PigeonBox.system_tests

# # perform general tests as follows:
# # - stress testing, i.e., pushing the system to its limits;
# # - volume testing, i.e., testing the system with large volumes of data;
# # - configuration testing, i.e., testing the system on various computer systems;
#             #idk if we will be able to do this one
# # - time testing, i.e., checking the speed of the system on typical data sets;


# import unittest


# #time testing: test the timing of the individual functionality

# class TestTiming(unittest.TestCase):
#     #im still figuring out how to use the patches to automate input

# #main menu
# # 1. Customer Orders
# # 2. Car Sales
# # 3. Car Inventory
# # 5. Manage Employees
# # A: Account settings

# #4. management of customers
#     @mock.patch('builtins.input', create=True)
#     def test_addUser(self, mocked_input):
#         mocked_input.side_effect = ['test', 'test', '5', '2', 'pepelopez', 'testtest123!', 'pepe', 'lopez', 'n', 'j', 'q', 'q', 'n']
#         #result = dictCreate(1)
#         t0 = time.time()
#         result = run()
#         t1 = time.time()
#         total = t1-t0
#         assert(total < 100)


#     @mock.patch('builtins.input', create=True)
#     def test_removeUser(self, mocked_input):
#         mocked_input.side_effect = ['test', 'test', '5', '3', '18', 'y', 'j', 'q', 'q', 'n']
#         result = run()


# #volume testing: test the system with large volumes of data




# if __name__ == '__main__':
#     unittest.main()