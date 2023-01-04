# import turtle
# timmy = turtle.Turtle()

from turtle import Turtle, Screen

timmy = Turtle()

print(timmy)

timmy.color("YellowGreen")
timmy.shape("turtle")
timmy.forward(100)

my_screen = Screen()
# Screen is a class
# my_screen is object of Blueprint Screen and . it's a seperator for between object and attribute

print(my_screen.canvheight)

# call method exitonclick for my_screen object
my_screen.exitonclick()

