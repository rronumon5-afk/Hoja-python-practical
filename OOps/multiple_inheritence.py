class mother:
    def cook(self):
        print("cooking...")
class father:
    def driving(self):
        print("driving...")
class son(mother,father):
    def __init__(self,name):
        self.name=name
    def drawing(self):
        print(self.name,"drawing...")
        
s=son("arun")
s.cook() 
s.driving()
s.drawing()                       
        