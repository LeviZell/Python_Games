# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:04:25 2016

@author: LeviZ
"""

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2]
paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
acc = 5

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT /2]
ball_vel = [0,-1]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT /2]
    x = random.randrange(3,5)
    y = random.randrange(1, 3)

    ball_vel[0] = x
    if direction == False:
        ball_vel = [-x, -y]
    else:
        ball_vel = [x, -y]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(random.choice([RIGHT, LEFT]))
    paddle1_pos[1] = HEIGHT / 2
    paddle2_pos[1] = HEIGHT / 2
    score1 = 0
    score2 = 0
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel 

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]    
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
   
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos[1] + paddle1_vel[1]) <= (HALF_PAD_HEIGHT - acc) or (paddle1_pos[1] + paddle1_vel[1]) >= (HEIGHT - HALF_PAD_HEIGHT + acc):
        paddle1_vel[1] = 0
    else: 
        paddle1_pos[1] += paddle1_vel[1]
    if (paddle2_pos[1] + paddle2_vel[1]) <= (HALF_PAD_HEIGHT - acc)  or (paddle2_pos[1] + paddle2_vel[1]) >= (HEIGHT - HALF_PAD_HEIGHT + acc):
        paddle2_vel[1] = 0
    else: 
        paddle2_pos[1] += paddle2_vel[1]

    # draw paddles
    canvas.draw_line([paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT], 
                     [paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT], 
                     PAD_WIDTH, 'WHITE')
    canvas.draw_line([paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT], 
                     [paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT], 
                     PAD_WIDTH, 'WHITE')
    
    # determine whether paddle and ball collide    
    if ((ball_pos[1] + ball_vel[1]) <= BALL_RADIUS) or ((ball_pos[1] + ball_vel[1]) >= (HEIGHT - BALL_RADIUS)):
        ball_vel[1] = - ball_vel[1] 
        
    if (ball_pos[0] + ball_vel[0]) <= (BALL_RADIUS + PAD_WIDTH):
            if (ball_pos[1] + BALL_RADIUS >= (paddle1_pos[1] - HALF_PAD_HEIGHT)) and (ball_pos[1] <= (paddle1_pos[1] + HALF_PAD_HEIGHT)):
                ball_vel[0] = -1.15 * ball_vel[0]
            else: 
                score2 += 1
                spawn_ball(RIGHT)
    elif(ball_pos[0] + ball_vel[0] + BALL_RADIUS) >= (WIDTH - PAD_WIDTH):
            if (ball_pos[1] + BALL_RADIUS >= (paddle2_pos[1] - HALF_PAD_HEIGHT))  and (ball_pos[1] <= (paddle2_pos[1] + HALF_PAD_HEIGHT)):
                ball_vel[0] = -1.15 * ball_vel[0]
            else:        
                score1 += 1
                spawn_ball(LEFT)
                
    # draw scores
    canvas.draw_text(str(score1), [WIDTH * .22, HEIGHT/6], 48, "Green")
    canvas.draw_text(str(score2), [WIDTH * .72, HEIGHT/6], 48, "Green")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP["s"]:
            paddle1_vel[1] += acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] -= acc
        
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += acc
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0
        
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)

# register event handlers
frame.add_button("Restart", new_game, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
