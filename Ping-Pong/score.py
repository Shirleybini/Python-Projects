# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 00:06:58 2020

@author: Shirley Sinha
"""

from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        
        self.hideturtle()
        #self.update_score()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        
        
    def update_score(self):
        self.goto(-100,250)
        self.write(self.l_score,align="center",font= ("Arial",30,"normal"))
        self.goto(100,250)
        self.write(self.r_score,align="center",font= ("Arial",30,"normal"))
        
    def l_point(self):
        self.l_score +=1
        self.clear()
        self.update_score()
        
    
    def r_point(self):
        self.r_score +=1
        self.clear()
        self.update_score()
    