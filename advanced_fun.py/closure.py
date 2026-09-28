def outer_function(x):
    
    def inner_function(y):
        return x + y
    return inner_function
add5=outer_function(5)
print(add5(10))
