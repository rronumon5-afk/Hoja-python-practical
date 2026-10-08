class phone:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def onn(self):
        print(self.brand,self.model,"is onn")
        
p1=phone("apple","18pro")
p2=phone("samsung","s24")

p1.onn()
p2.onn()      
        
        
