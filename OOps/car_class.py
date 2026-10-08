class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def start(self):
        print(self.brand,self.model ,"is starting..")
        
car1=car("BMW","m3")
car2=car("toyota","mk5")

car1.start() 
car2.start()       
            