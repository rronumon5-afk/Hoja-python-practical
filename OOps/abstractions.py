from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class cat(animal):
    def sound(self):
        return "meow!!"
    
class dog(animal):
    def sound(self):
        return "boww!!" 
    
d=dog()
c=cat()

print(d.sound())
print(c.sound())          