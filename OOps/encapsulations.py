class demo:
            def __init__(self):
                self.public_var="I am public"
                self._protected_var="I am protected"
                self.__private_var="I am private"

            def show(self):
                print(self.public_var)
                print(self._protected_var)
                print(self.__private_var)
            
            def get_private(self):
                return self.__private_var    

obj=demo()
print(obj.public_var)
print(obj._protected_var)
print(obj.get_private())
        


                
                
  