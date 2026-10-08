

try:
    a=float(input("Enter a number1: "))
    b=float(input("Enter a number2: "))
    op=input("Enter an operator(+,-,*,/):")

    if op =='+':
        print("Result:",a+b)
    elif op =='-':
        print("Result:",a-b)
    elif op == '*':
        print("Result:",a*b)
    elif op =='/':
        print("Result:",a/b)
    else:
        raise ValueError("invalid operator")
except ValueError as e:
    print("error!",e)
except ZeroDivisionError:
    print("zero division is not allowed")
finally:
    print("Thank you for using")        
    
           
        