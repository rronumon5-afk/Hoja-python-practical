class shape:
    def area(self):
        return 0
class circle(shape):
    def area(self):
        return 3.14*2
class rectangle(shape):
    def area(self):
        return 5*4 
#polymorpshism
shapes=[circle(),rectangle()]
for s in shapes:
    print(s.area())       
        