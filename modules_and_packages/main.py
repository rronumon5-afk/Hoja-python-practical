import utility
from my_packages import greeter,calculator

print(utility.greet("Muhammed"))
print(utility.add(223,4564))


print(greeter.say_hello("Muhammed"))

added=calculator.add(463,758)
print("Added:",added)

subtracted=calculator.subtract(added,733)
print("Subtracted:",subtracted)
