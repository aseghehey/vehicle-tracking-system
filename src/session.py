# keep list of admins, customers, cars and where they are etc...
from read_write_json import *
from status import *
from users import *
from orders import *
from typing import Type

class Session:
    def __init__(self) -> None:
        self.__employees__, self.__admins__ = LoadUsers()
    
    def ReturnEmployees(self):
        return self.__employees__
    
    def ReturnAdmins(self):
        return self.__admins__

class Auth(Session):
    def __init__(self) -> None:
        super().__init__()
        self.__all_users__ = self.__employees__ + self.__admins__

    def Authenticate(self, entered_username, entered_password):
        for user in self.__all_users__:
            if user.username == entered_username and user.password == entered_password:
                return user
        return
    
class EndSession(Session):
    def __init__(self, update_flag: list[bool], inventory: list[Type[Car]], orders: list[Type[Order]]) -> None:
        super().__init__()
        self.update_flag = update_flag
        self.inventory = inventory
        self.orders = orders
    
    def Terminate(self):
        if self.update_flag[0]: WriteJson(self.inventory)
        if self.update_flag[1]: WriteJson(self.orders)
        if self.update_flag[2]: WriteJson(self.__employees__)

#  Testing 
if __name__ == "__main__":
    auth = Auth() # gkubach0 2nBztx3qzXV
    print(auth.Authenticate("gkubach0", "2nBztx3qzXV"))
