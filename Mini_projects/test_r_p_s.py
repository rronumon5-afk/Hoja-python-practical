import random

def get_computer_choice():
    return random.choice(["rock","paper","scissors"]) 
def get_player_choice():
     choice=input("choose rock,paper,scissors: ").lower()
     while choice not in ["rock","paper","scissors"]:
         choice=input("Invalid choice.Please choose rock,paper,scissors").lower()
     return choice
def check_winner(player,computer):
    if player==computer:
        return "its a Draw!!"
    elif (player=="rock"and computer=="scissors")or\
        (player=="paper"and computer=="rock")or\
            (player=="scissors"and computer=="paper"):
        return "you winn!!"
    else:
        return"you lose!!"
    
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
            
    
       
                         
     
           