try:
    number=int(input("Enter a number: "))
    result=10/number
    print(result)
    
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("Cannot divided by zero!!")
else:
    print("Calculation Successfully Completed")
                
