from parsers import readJson, writeJson

""" Deals with auth and session logic"""
class Session:
    def __init__(self) -> None:
        self.__employees__, self.__admins__ = readJson.LoadUsers()
    
    def ReturnEmployees(self):
        return self.__employees__
    
    def ReturnAdmins(self):
        return self.__admins__

class Auth(Session):
    def __init__(self) -> None:
        super().__init__()
        self.__users__ = self.__employees__ + self.__admins__

    def Authenticate(self, username, password):
        for user in self.__users__:
            if user.getUsername() == username and user.getPassword() == password:
                return user
    
