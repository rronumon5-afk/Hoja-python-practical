def get_password():
    password=input("Enter Your Password :")
    return password    
def check_length(password):
    if len(password)>=8:
        return True
    else:
        return False
def check_special_characters(password):
    special_characters="!@#$%^&()_-+=?/"
    for i in password:
        if i in special_characters:
            return True
    return False  
def check_numbers(password):
    for i in password:
        if i.isdigit():
            return True
    return False
def check_uppercase(password):
    for i in password:
        if i.upper():
            return True
    return False
def display_strength(length_ok,special_ok,numbers_ok,uppercase_ok):
    score=length_ok+special_ok+numbers_ok+uppercase_ok
    
    print("\n----------------PASSWORD EVALUATION-------------------")              
        
    if length_ok:
        print("length : PASS(8 or more characters )")
    else:
        print("length : FAILED(below 8 characters )")
    
    if special_ok:
        print("special : PASS(special charactes appeared)")
    else:
        print("special : FAIL(none found)")
    if numbers_ok:
        print("numbers: PASS(numbers appeared)")
    else:
        print("numbers:FAIL(none found)")
    if uppercase_ok:
        print("uppercase:PASS(uppercase is appeared)")
    else:
        print("uppercase:FAIL(none found)")
    
    print("\n password strength :",end='')
                               
    if score<=1:
        print("WEAK")
    elif score==2:
        print("MEDIUM")
    elif score==3:
        print("STRONG")
    else:
        print("VERY STRONG")
    print("Total checks passed :",score,"/4")
def main():
    
    password=get_password()
    length_ok=check_length(password)
    special_ok=check_special_characters(password)
    number_ok=check_numbers(password)
    uppercase_ok=check_uppercase(password)
    
    display_strength(length_ok,special_ok,number_ok,uppercase_ok)
    
if __name__=="__main__":
    main()    
                                    