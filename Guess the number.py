# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:03:15 2016

@author: LeviZ
"""

# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

#initialize random variables used in the game
num_range = 100
count = 0
secret_number = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range
    global count
    global secret_number
    
    secret_number = random.randrange(0, num_range)
  
    if num_range == 100:
        count = 7
    else:
        count = 9
    print "New game. Range is from 0 -", num_range 
    print "Number of remaining guesses is", count
    print ""
    return count

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global secret_number
    global count
    
    win = False 
    
    print "Guess was", guess
    count -= 1
    print "Number of remaining guesses is", count
    
    if int(guess) == secret_number:
        win = True   
    elif int(guess) >= num_range:
        outcome = "Guess is too high. Lose a turn. Try again."
    elif int(guess) < secret_number:
        outcome = "Higher!"
    else: 
        outcome = "Lower!"

        
    if win:
        print "Correct!"
        print""
        new_game()
        return
    elif count == 0:
        print "You ran out of guesses. The number was", secret_number
        print""
        new_game()
        return
    else:
        print outcome
        print""
        return
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame

frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess, then press enter", input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
