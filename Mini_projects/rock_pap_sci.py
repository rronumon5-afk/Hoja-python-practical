import random

def get_computer_choice():
    return random.choice(["rock","paper","scissors"])

def get_player_choice():
    choice= input("choose rock,paper,or scissors: ").lower()
    while choice not in ["rock","paper","scissors"]:
        choice=input("Invalid choice.Please choose rock,paper,or scissors:").lower()
    return choice
    
def check_winner(player,computer):
    if player==computer:
        return "its draw"
    elif (player=="rock" and computer=="scissors")or\
        (player=="scissors" and computer=="paper")or\
        (player=="paper"and computer=="rock") :
        return "You Win!!"
    else:
        return "You Lose!!"

def play_game():
    player=get_player_choice()
    computer=get_computer_choice()
    print(f"you choose:{player}")
    print(f"computer choose:{computer}")
    print(check_winner(player,computer))
    
def main():
    play_game()
    
if __name__=="__main__":
    main()
    
               
    
