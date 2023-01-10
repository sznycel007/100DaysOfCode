# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('hirst_large.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = r, g, b
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


from turtle import Turtle, Screen
import random


tim = Turtle()
screen = Screen()
screen.colormode(255)

color_list = [
    (243, 235, 74), (211, 158, 93), (186, 12, 69), (112, 179, 208), (25, 116, 168), (173, 171, 31),
    (219, 129, 166), (161, 79, 35), (129, 185, 146), (9, 32, 76), (222, 62, 105), (235, 73, 42),
    (180, 45, 94), (30, 136, 81), (236, 164, 193), (78, 12, 63), (12, 54, 33), (234, 227, 7),
    (26, 165, 209), (16, 43, 132), (58, 166, 96), (134, 214, 229), (10, 101, 63), (133, 34, 20),
    (91, 27, 11), (159, 211, 188)
]


# 10 x 10 rows of dots
# each dot will be 20 at size (radiant)
# space between dots will be in 50 paces

tim.hideturtle()
tim.setheading(225)
tim.setheading(0)
tim.penup()
tim.speed(6)

x = -212.13
y = -212.13

for posY in range(10):
    for posX in range(10):
        randomColor = random.choice(color_list)
        tim.setposition(x, y)
        tim.dot(20, randomColor)
        x += 50
    x = -212.13
    tim.setposition(x, y)
    y += 50
    tim.dot(20, randomColor)

screen.exitonclick()
