def password_strength(password):
    strength=0
    
    #length of the pass
    if len(password)>=8:
        strength+=1
    #numbers in password
    if any(char.isdigit() for char in password):
        strength+=1
    #special chars
    special_chars="!@#$%^*()_-=+&/?"
    if any(char in special_chars for char in password):
        strength+=1
    #decide strength
    if strength==3:
        print ("STRONG!!")
    elif strength==2:
        print ("MEDIUM!!")
    elif strength==1:
        print ("NORMAL!!")
    else:
        print("WEAK!!")
#main prog
pwd=input("Enter Your Password :")
print("password strength :",password_strength(pwd))    
    
    
                