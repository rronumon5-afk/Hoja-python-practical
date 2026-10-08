balance=5000   
def show_menu():
    print("====ATM====")
    print("1.Check balance")
    print("2.deposit")
    print("3.Withdraw")
    print("4.Exit")
   
def check_balance(balance):
    print("Your balance is:",balance)
    
def deposit(balance):
    amount=float(input("Enter amount to deposit:"))
    if amount<=0:
        print("Amount should be greater than zero.")
    else:
      balance += amount
      print("Amount deposited successfully.")
    return balance
        
def withdraw(balance):
    amount=float(input("Enter amount to withdraw:"))
    if amount<=0:
        print("amount should be greater than zero.")
    elif amount >balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Amount withdrawn successfully.")
        return balance
                
while True:
    show_menu()
    choice= input("Enter your choice(1-4): ")
    if choice=="1":
        check_balance(balance)
    elif choice=="2":
        balance=deposit(balance)
    elif choice=="3":
       balance= withdraw(balance)
    elif choice=="4":
        print("Thank you for usin g our ATM.")
        break
    else:
        print("Invalid choice. Please try again.")