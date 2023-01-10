from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)

# colors = ["light sky blue", "dark cyan", "medium turquoise", "dark orange", "green", "papaya whip", "medium orchid",
#           "slate blue", "light slate gray", "medium purple"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]

tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen.exitonclick()
