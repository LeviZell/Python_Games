# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:01:48 2016

@author: LeviZ
"""

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

def name_to_number(player_choice):

# convert the player's choice to player_number using the function name_to_number()
# converts name to number using if/elif/else
    if player_choice == "rock":
        player_number = 0
        return player_number
    elif player_choice == "Spock":
        player_number = 1
        return player_number
    elif player_choice == "paper":
        player_number = 2
        return player_number
    elif player_choice == "lizard":
        player_number = 3
        return player_number
    elif player_choice == "scissors":
        player_number = 4
        return player_number
#  assigns a number for determining invalid entry
    else:
        player_number = 6
        return player_number

#	converts number to a name using if/elif/else

def number_to_name(comp_number):
    # delete the following pass statement and fill in your code below	
    if comp_number == 0:
        comp_choice = "rock"
        return comp_choice
    elif comp_number == 1:
        comp_choice = "Spock"
        return comp_choice
    elif comp_number == 2:
        comp_choice = "paper"
        return comp_choice
    elif comp_number == 3:
        comp_choice = "lizard"
        return comp_choice
    elif comp_number == 4:
        comp_choice = "scissors"
        return comp_choice
    else:
        return     

def rpsls(player_choice): 
# 	prints out the message for the player's choice
    print "Player chooses " + player_choice
    
#	computes random guess for comp_number using random.randrange() 
    comp_number = random.randrange (0, 5)
    
#	convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name (comp_number)

#	prints out the message for computer's choice
    print "Computer chooses " + comp_choice
    
    player_number = name_to_number(player_choice)
    
#	computes difference of comp_number and player_number modulo five
#   or states if invalid entry
#	use if/elif/else to determine winner, print winner message

    if player_number == 6:
        print "Error: invalid entry - " + player_choice + " is not an option. Please choose either rock, paper, lizard, or Spock. (case-sensitive)"    
    elif (comp_number - player_number) % 5 == 1 or (comp_number - player_number) % 5 ==  2:
        print "Computer Wins!"
    elif (comp_number - player_number) % 5 == 3 or (comp_number - player_number) % 5 ==  4:
        print "Player Wins!"
    else:
        print "Player and Computer Tie!"
        
#    prints a blank line
    print""
    
# 	tests code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


