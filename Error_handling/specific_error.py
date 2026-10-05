try:
    number=int(input("enter a number: "))
    result=10/number
    print(result)
    
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("Something went wrong")        
