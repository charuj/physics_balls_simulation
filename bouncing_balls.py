from enum import auto
from p5 import *
import numpy as np 



class Ball:
    def __init__(self, width, height, radius, gravity ,friction, spring_constant, num_balls)-> None:
        self.width= width
        self.height= height
        self.radius= radius
        self.gravity =gravity 
        self.friction= friction
        self.spring= spring_constant
        self.position= Vector(np.random.randint(width), np.random.randint(height))
        self.velocity= Vector.random_2D()*7
        self.color= Color(np.random.randint(255), np.random.randint(255), np.random.randint(255))
        self.circle_size= radius*2
        self.num_balls= num_balls
 
        
    def collision(self, current, other):
        if current == other:
            return 
        dx= other.position.x - current.position.x # displacement along x-axis
        dy= other.position.y - current.position.y
        dis= (current.position).distance(other.position)
        if dis < self.radius*2:
            angle= atan2(dy ,dx)
            targetX= current.position.x + cos(angle) * self.radius*2
            targetY = current.position.y+ sin(angle) * self.radius*2
            ax = (targetX - other.position.x) * self.spring
            ay = (targetY - other.position.y) * self.spring
            current.velocity.x  -= ax
            current.velocity.y -= ay
            other.velocity.x  += ax 
            other.velocity.y  += ay   
   
    def move(self):
        self.velocity.y += self.gravity
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y 

        
        if self.position.x < self.radius:
            self.position.x= self.radius
            self.velocity.x *= self.friction
        
        if self.position.x > self.width - self.radius:
            self.position.x= self.width - self.radius
            self.velocity.x*= self.friction

        if self.position.y < self.radius:
            self.position.y= self.radius
            self.velocity.y*= self.friction 

        if self.position.y > self.height - self.radius:
            self.position.y= self.height - self.radius
            self.velocity.y *= self.friction


    def draw_ball(self):
        fill(self.color)
        stroke(self.color)
        circle((self.position.x, self.position.y), self.circle_size)

