from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ["light sky blue", "dark cyan", "medium turquoise", "dark orange", "green yellow", "papaya whip",
          "medium orchid", "slate blue", "light slate gray", "medium purple"]


def drawShape(numberOfAngels):

    degree = int(360/numberOfAngels)
    timcolor = random.choice(colors)
    tim.color(timcolor)
    colors.remove(timcolor)

    for line in range(numberOfAngels):

        tim.color(timcolor)
        tim.right(degree)
        tim.forward(100)


for numberOfAngels in range(3, 11):
    drawShape(numberOfAngels)


screen = Screen()
screen.exitonclick()
