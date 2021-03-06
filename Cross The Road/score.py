# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:38:16 2020

@author: Shirley Sinha
"""
FONT = ("Courier", 20, "normal")


from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-480,260)
        self.hideturtle()
        self.level = 1
        self.update_score()
        
    
    def update_score(self):
        self.write(f"Level: {self.level}",align="left",font= FONT)
        
    def increase_score(self):
        self.level +=1
        self.clear()
        self.update_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font= FONT)
        
    