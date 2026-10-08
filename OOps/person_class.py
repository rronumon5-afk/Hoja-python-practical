#class=blueprint

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    
    #method= function inside class
     
    def greet(self):
         print("Hello",self.name)
         
    #object crete from class
p=person("Arun",23)
p2=person("Ajay",25)
         
p.greet()
p2.greet()         