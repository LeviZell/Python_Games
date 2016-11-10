# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:05:16 2016

@author: LeviZ
"""

# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global state, turns, cards, exposed, click_1, right_guess
    state = 0
    turns = 0
    card_index = 0
    right_guess = []
    cards = [n for n in range(0,8)*2]
    exposed = [False for n in range(0, 8)*2]
    random.shuffle(cards)
    label.set_text("Turns = "+str(turns))


# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, turns, exposed, card_index, click_1, click_2
    card_index = pos[0]//50
    if not exposed[pos[0]//50]:
        if state == 0:
            click_1 = card_index
            exposed[click_1] = True
            state = 1
            turns += 1
        elif state == 1:
            if not exposed[card_index]:
                click_2 = pos[0]//50
                exposed[click_2] = True
                state = 2
        else:
            if not exposed[card_index]:
                if cards[click_1] != cards [click_2]:
                    exposed[click_1] = False
                    exposed[click_2] = False
                turns += 1
                state=1
                click_1 = pos[0]//50
                exposed[click_1] = True
        label.set_text("Turns = "+str(turns))
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for n in range(len(cards)):
            card_pos = 50 * n
            if exposed[n]:
                canvas.draw_text(str(cards[n]), (card_pos+20, 100//2 ), 20, 'White')
                canvas.draw_polygon([(50*n, 0), (50*n, 100), (50*(n + 1), 100), (50*(n+1), 0)], 2,  'White') 
            else:
                canvas.draw_polygon([(50*n, 0), (50*n, 100), (50*(n + 1), 100), (50*(n+1), 0)], 2,  'White', 'Green') 
    if exposed.count(True) == 16:
        canvas.draw_text("Winner!  Winner!", (300, 90), 40, "Red") 

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric