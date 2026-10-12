from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass
class SIBATM(ATM):
    def withdraw(self):
        self.__verify_pin()
        self.__check_balance()
        self.__update_server()
        print("cash withdrawn successfully")
        
    def __verify_pin(self):
        print("verified pin")
    def __check_balance(self):
        print("balance checked")
    def __update_server(self):
        print("server Updated")     
atm=SIBATM()
atm.withdraw()            