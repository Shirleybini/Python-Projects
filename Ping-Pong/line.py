# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:55:26 2020

@author: Shirley Sinha
"""

from turtle import Turtle
  
class Line(Turtle):
    def __init__(self,pos):
        super().__init__()
        
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.25,stretch_wid=1)
        self.color("white")
        self.goto(pos)
        
        