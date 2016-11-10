# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:02:38 2016

@author: LeviZ
"""

# template for "Stopwatch: The Game"
import simplegui

# define global variables
counter = 0
HEIGHT = 200
WIDTH = 300
wins = 0
tries = 0
a = 0
b = 0
c = 0
d = 0
in_progress = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(counter):
    global a, b, c, d 
    a = (counter //10)/60
    b = ((counter //10)%60)//10
    c = ((counter //10)%60)%10
    d = (counter)%10
    if a > 9:
        a = str(0)
    else:
        a = str(a)
    return str(a)+":"+str(b)+str(c)+"."+str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global in_progress
    in_progress = False
    timer.start()
    
def stop():
    global counter, tries, wins, in_progress
    wins
    if in_progress == False:
        if d == 0:
            wins +=1
            tries+=1
        else:
            wins+=0
            tries+=1
    in_progress = True
    timer.stop()

def reset():
    global counter, wins, tries, in_progress
    tries = 0
    wins = 0
    counter = 0
    in_progress = True
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1

# define draw handler
def counter_display(canvas):
    canvas.draw_text(format(counter), [WIDTH//2, HEIGHT //2], 48, "White")
    canvas.draw_text(str(wins)+"/"+str(tries), [WIDTH// 1.25, HEIGHT/6], 29, "Green")
    
# create frame and timer
frame = simplegui.create_frame("Stopwatch Game", WIDTH, HEIGHT)

# register event handlers
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)
frame.set_draw_handler(counter_display)
timer = simplegui.create_timer(100, tick)

# start frame and timer
frame.start()


# Please remember to review the grading rubric
