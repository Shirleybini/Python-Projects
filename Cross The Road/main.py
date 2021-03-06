
import time
from turtle import Screen
from my_turtle import MyTurtle
from car import Car
from score import Scoreboard

WIDTH = 1000
HEIGHT = 600

screen = Screen()
screen.setup(width = WIDTH, height = HEIGHT)
#screen.bgcolor("black")
screen.title("Cross The Road")
screen.tracer(0)


myturtle = MyTurtle()
my_car = Car()
my_score = Scoreboard()

screen.listen()
screen.onkey(myturtle.go,"Up")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    my_car.create_car()
    my_car.move()
    
    for car in my_car.all_cars:
        if car.distance(myturtle)<29:
            is_game_on = False
            my_score.game_over()
            

    if myturtle.reached():
        myturtle.start_again()
        my_car.level_up()
        my_score.increase_score()



screen.exitonclick()