# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 22:53:46 2020

@author: Shirley Sinha
"""

from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("pink")
        #self.speed("slowest")
        self.x_move = random.randint(0,21)
        self.y_move = random.randint(0,21)
        
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        
    
    def bounce_y(self):
        self.y_move *=-1
            
        
    def bounce_x(self):
        self.x_move *= -1
        
        
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        