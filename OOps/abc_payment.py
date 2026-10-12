from abc import ABC,abstractmethod

class payment(ABC):
    def pay(self,amount):
        pass
class UPI(payment):
    def pay(self,amount):
        print("Paid",amount,"Using UPI")
        
class CARD(payment):
    def pay(self,amount):
        print("Paid",amount,"Using CARD")
        
p1=UPI()
c1=CARD()

p1.pay(2000)
c1.pay(4000)                    