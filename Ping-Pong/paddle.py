# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:03:26 2020

@author: Shirley Sinha
"""

from turtle import Turtle

#POSITIONS = [(-470,0),(470,0)]

class Paddle(Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)
        
    def go_up(self):
        #self.setheading(0)
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
        
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)