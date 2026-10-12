class vehicle:
    def start(self):
        print("Vehicle starting..")
class car (vehicle):
    def rev(self):
        print("rev")


class bike (vehicle):
    def roll(self):
        print("rolliing")

c=car()
c.start()
c.rev()

b=bike()
b.start()
b.roll()
        