def get_password():
    password=input("Enter your password :")
    return password
def check_length(password):
    if len(password)>=8:
        return True
    else:
        return False
def check_special_character():
    special_character="!@#$%^&*()_-=+?/"
    for i in password:
        
        
              