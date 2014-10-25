# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    if(name=="rock"):
        return 0
    elif(name=="Spock"):
        return 1
    elif(name=="paper"):
        return 2
    elif(name=="lizard"):
        return 3
    elif(name=="scissors"):
        return 4

def number_to_name(number):
    if(number==0):
        return "rock"
    elif(number==1):
        return "Spock"
    elif(number==2):
        return "paper"
    elif(number==3):
        return "lizard"
    elif(number==4):
        return "scissors"


def rpsls(player_choice): 
    print("\n")
    str="Player chooses" + " " +player_choice
    print(str)
    player_num = name_to_number(player_choice)
    rand = random.randrange(0,5,1)
    comp_choice = number_to_name(rand)
    str1="Computer chooses" + " " +comp_choice
    print(str1)
    diff=(player_num - rand)
    diff%=5
    if(diff==1 or diff==2):
        print("Player wins!")        
    elif(diff==3 or diff==4):
        print("Computer wins!")      
    elif(diff==0):
        print("Player and computer tie!")
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
