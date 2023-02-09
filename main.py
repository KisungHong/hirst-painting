# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 6)
# for color in colors:
#     r= color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
color_list = [(242, 226, 204), (201, 155, 116), (244, 219, 232), (216, 240, 226), (212, 225, 240), (135, 163, 186)]
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
