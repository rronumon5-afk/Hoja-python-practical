class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name,"is eating")
class dog (Animal):
    def bark(self):
        print(self.name,"is Barking")
d=dog("doggy")
d.bark()
d.eat()                