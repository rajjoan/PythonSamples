import random

options=["Rock","Paper","Scissors"]

play_again_yes_no = True 

while (play_again_yes_no == True):
    user_input=input("Type Rock,Paper,Scissors  : ")
    computer_selection=options[random.randint(0,2)]
     
    print("You selected "+user_input) 
    print("Player2 selected "+computer_selection)

    if computer_selection == user_input:
        print("you both entered the same thing!!!")

    elif (user_input == "Rock" and computer_selection == "Scissors"):
        print("You Won!!!")

    elif (user_input == "Paper" and computer_selection == "Rock"):
        print("You Won!!!")
    
    elif (user_input == "Scissors" and computer_selection == "Paper"):
        print("You Won!!!")

    else:
       print("Player 2 wins!!!")
    
    play_again=input("Do you want to play again?(yes or no?)")
    

    if play_again ==  "yes":
       play_again_yes_no = True
    else:
       
       play_again_yes_no = False

print("Thanks for playing")    
    


    
