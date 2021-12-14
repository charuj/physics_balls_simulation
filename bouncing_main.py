from p5 import * 
import numpy as np 
from numpy import random
from bouncing_balls import Ball 

width= 700
height= 700
num_balls=10
gravity = 0.75
friction = -0.9
spring_constant= 0.1
balls=[]




def setup():
    size(width, height) 
    for i in range(num_balls):
        balls.append(Ball(width=width, height= height, radius=30,gravity=gravity, friction= friction,spring_constant= spring_constant, num_balls= num_balls))

def draw():
    background(184, 234, 252) 
    global balls

    for i in range(len(balls)):
        for j in range(0, i):
            balls[i].collision(balls[i], balls[j])

    for k in balls:
        k.move()
        k.draw_ball()
    # save_frame()

    
run()

