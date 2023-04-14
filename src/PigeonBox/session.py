####################################################################################################################
'''
////////////////
PROGRAM session:   Handle session management and authentication of users.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu

////////////////
VERSION 1: written [day] [month] 2023 by [firstInitial]. [lastName]
REVISION [revision# ex: 1.1]: [day] [month] 2023 by [firstInitial]. [lastName] to [purpose of revision]

////////////////
PURPOSE:
The purpose of this code is to handle session management and authentication of users.

The Session class loads the users from a JSON file and initializes two lists to store employees and admins.
It also provides two functions to return the lists of employees and admins respectively.

The Auth class extends the Session class to add authentication functionality.
It combines the lists of employees and admins into a single list of users and provides a function Authenticate 
to authenticate user logged in with username and password.
The Authenticate function iterates over the list of users to find a matching username and password 
and returns the user object if found.

Methods:


////////////////
DATA STRUCTURES:
DataStructures:
- Lists: store the employees and admins data retrieved from a JSON file in the Session class, and 
         also to combine the employees and admins lists in the Auth class.
- Dictionaries: map string representations of status values to their corresponding enum values in the Status class.

Attributes:
- self.__employees__: A list attribute in the Session class that stores the employees loaded from a JSON file.
- self.__admins__: A list attribute in the Session class that stores the admins loaded from a JSON file.
- self.__users__: A list attribute in the Auth class that stores the combined list of employees and admins. 

////////////////
ALGORITHM:
None

////////////////
ERROR HANDLING:
No explicit error handling.
The calling code will raise these exceptions.

////////////////
'''
####################################################################################################################



from parsers import readJson, writeJson


#   handles the session management and authentication of users.
class Session:
    # Loads the users from a JSON file and initializes two lists to store employees and admins
    def __init__(self) -> None:
        self.__employees__, self.__admins__ = readJson.LoadUsers()

    # Returns the list of employees
    def ReturnEmployees(self):
        return self.__employees__
    
    # Returns the list of admins
    def ReturnAdmins(self):
        return self.__admins__

#   Extends the Session class to add authentication functionality.
class Auth(Session):
    def __init__(self) -> None:
        super().__init__()
        # Combines the lists of employees and admins into a single list of users
        self.__users__ = self.__employees__ + self.__admins__

    #   authenticates user logged in with username and password
    def Authenticate(self, username, password):
        # Iterates over the list of users to find a matching username and password
        for user in self.__users__:
            if user.getUsername() == username and user.getPassword() == password:
                return user
    
