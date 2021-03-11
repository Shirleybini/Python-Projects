import turtle as t
import colorgram
import random

t.colormode(255) 


WIDTH = 1000
HEIGHT = 600

tur = t.Turtle()
screen = t.Screen()
screen.setup(width = WIDTH, height = HEIGHT)
screen.title("My Hirst Painting")


rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)
    

tur.penup() 
tur.hideturtle()   
tur.setheading(225)
tur.forward(300)
tur.setheading(0)


number_of_dots = 100

for dot_count in range(1,number_of_dots+1):
    Color = random.choice(rgb_colors)
    C = (Color.r,Color.g,Color.b)
    tur.dot(20, C)
    tur.forward(50)
    #print(tur.position())
    
    if dot_count %10==0:
        tur.setheading(90)
        tur.forward(50)
        tur.setheading(180)
        tur.forward(500)
        tur.setheading(0)



screen.exitonclick()