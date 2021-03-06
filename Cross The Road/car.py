# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:47:51 2020

@author: Shirley Sinha
"""

from turtle import Turtle
import random
import turtle as t


t.colormode(255) 

WIDTH = 1000
HEIGHT = 600

class Car:
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5
        
    def create_car(self):
        rand = random.randint(1,8)
        if rand == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid = 1,stretch_len=2)
            new_car.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            new_car.penup()
            new_car.goto(500,random.randint(-240,280))
            new_car.speed("slowest")
            self.all_cars.append(new_car)
            
        
       
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    
    def level_up(self):
        self.car_speed += 10
        