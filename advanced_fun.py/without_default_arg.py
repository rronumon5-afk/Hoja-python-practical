def greet(name=None):
    if name is None:
        name = "Guest"
        
        print("hello", name)
        
greet()
greet("John")

        