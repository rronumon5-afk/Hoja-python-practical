def password_strength(password):
    strength=0
    
    #check passsword strength
    #check length
    if len(password)>=8:
        strength+=1
    #check any number        
    if any(char.isdigit() for char in password):
        strength+=1
    #check for special characters
        special_chars="!@#$%^&*()?/=+_-"
        if any(char in special_chars for char in password):
            strength+=1
    #decide strength level
    if strength==3:
        return "STRONG!!" 
    elif strength==2:
        return "MEDIUM!!"
    elif strength==1:
        return "NORMAL!!"
    else:
        return "WEAK"
    
#main program
    
pwd= input("Enter your password :")
print("password_strength :",password_strength(pwd))                   