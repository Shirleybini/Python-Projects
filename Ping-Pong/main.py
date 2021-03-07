import time
from turtle import Screen

from line import Line
from paddle import Paddle
from ball import Ball
from score import Scoreboard

WIDTH = 1000
HEIGHT = 600
POSITIONS = [(-470, 0), (470, 0)]

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("PING PONG")
screen.tracer(0)

h = 0
while h < HEIGHT / 2:
    Line((0, h))
    Line((0, -h))
    h += 30

r_paddle = Paddle((470, 0))
l_paddle = Paddle((-470, 0))

my_ball = Ball()
my_score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "a")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.01)
    my_ball.move()

    if my_ball.ycor() > 280 or my_ball.ycor() < -280:
        my_ball.bounce_y()

    if (my_ball.distance(r_paddle) < 50 and my_ball.xcor() > 440) or (
            my_ball.distance(l_paddle) < 50 and my_ball.xcor() < -440):
        my_ball.bounce_x()

    if my_ball.xcor() > 480:
        my_ball.reset_position()
        my_score.l_point()

    if my_ball.xcor() < -480:
        my_ball.reset_position()
        my_score.r_point()

screen.exitonclick()
