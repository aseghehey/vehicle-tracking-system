####################################################################################################################
'''
////////////////
PROGRAM session:   Handle session management and authentication of users.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

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

    # One-line description: Initializes an object of the class with two private attributes containing employee and admin data from a JSON file.
    # General description: This is an initialization method of a class that loads employee and admin data from a JSON file and stores it in two private attributes.
    # Typical calling example: obj = ClassName()
    # Accessibility: This method is public.
    # Function prototype: It does not take any argument and returns None.
    def __init__(self) -> None:
        self.__employees__, self.__admins__ = readJson.LoadUsers()



    # One-line description: Return the list of employees.
    # General description: The ReturnEmployees function returns the list of employees stored in the instance variable
    #    __employees__.
    # Typical calling example:
    #   company = Company()
    #   employees = company.ReturnEmployees()
    # Accessibility: Public.
    # Function prototype:def ReturnEmployees(self) -> list:
    def ReturnEmployees(self):
        return self.__employees__
    


    # One-line description: Returns a list of administrator users.
    # General description: This function returns the list of administrator users that was previously loaded from
    #    a JSON file using the LoadUsers() function. The list is stored as a private attribute __admins__ of the class.
    # Typical calling examples:
    #   userManager = UserManager()
    #   admins = userManager.ReturnAdmins()
    #   print(admins)  # prints the list of administrator users
    # Accessibility: Public.
    # Function prototype: def ReturnAdmins(self) -> List[Dict[str, Any]]:
    def ReturnAdmins(self):
        return self.__admins__





#   Extends the Session class to add authentication functionality.
class Auth(Session):

    # One-line description: Initializes an object of a class and creates a combined list of employees and admins as a list of users.
    # General description: This function is a constructor method for a class that inherits from a parent class. It initializes an object of the child class and creates a list of users that contains the combined list of employees and admins.
    # Typical calling examples:
    #   obj = ChildClass()
    # Accessibility: Private
    # Function prototype: def __init__(self) -> None:
    def __init__(self) -> None:
        super().__init__()
        # Combines the lists of employees and admins into a single list of users
        self.__users__ = self.__employees__ + self.__admins__



    # One-line description: Authenticate a user with their username and password.
    # General description: This method searches through a list of users to find a matching username and
    #   password combination. If a match is found, the user object is returned.
    # Typical calling examples:
    #   auth = Authenticator()
    #   user = auth.Authenticate("john.doe", "password123")
    # Accessibility: Public method.
    # Function prototype': def Authenticate(self, username, password) -> Union[User, None]:
    def Authenticate(self, username, password):
        # Iterates over the list of users to find a matching username and password
        for user in self.__users__:
            if user.getUsername() == username and user.getPassword() == password:
                return user
    
