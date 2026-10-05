import random

def generate_number():
    """Generate a random number between 1 and 100 """
    return random.randint(1,100)
def get_guess():
    """Ask the player for a guess"""
    return int(input("Enter your guess(1-100): "))

def check_guess(secret,guess):
    """Check the guess against the secret number"""
    if guess<secret:
        print("Too low!")
        return False
    elif guess>secret:
        print("Too High!")
        return False
    else:
        print("Correct!")
        return True
    
def play_game():
    secret_number=generate_number()
    attempts=6
    print("I have chosen number between 1 and 100.You have 10 attempts!")
    
    for attempts in range(1,attempts+ 1):
        guess=get_guess()
        if check_guess(secret_number,guess):
            print(f"You guessed it in {attempts} attempts!")
            break
    else:
        print(f"Sorry,you're out of attempts.The number was {secret_number}.")
        
def main():
    play_game()
    
if __name__=="__main__":
    main()    
    
    
               
