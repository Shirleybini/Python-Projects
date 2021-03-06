# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:35:47 2020

@author: Shirley Sinha
"""
FINISH = 290
MOVE_DISTANCE = 10
STARTING_POSITION = (0,-280)

from turtle import Turtle

class MyTurtle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.start_again()
        self.setheading(90)
    
    
    def start_again(self):
        self.goto(STARTING_POSITION)
        
        
    def go(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
        
    
    def reached(self):
        if self.ycor() == FINISH:
            return True
        else:
            return False