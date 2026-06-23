from os import path
import random
import turtle
import colorgram

# path = path.dirname(path.abspath(__file__))

# colors = colorgram.extract(path + "\\sketch.jpg", 30)
# color_list = []
# for color in colors:
#     color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(color_list)


color_list = [
    (35, 19, 11),
    (17, 24, 33),
    (136, 82, 44),
    (216, 155, 84),
    (12, 16, 14),
    (24, 13, 17),
    (144, 30, 10),
    (249, 200, 83),
    (61, 84, 109),
    (201, 140, 36),
    (96, 63, 24),
    (248, 217, 165),
    (41, 60, 96),
    (188, 243, 251),
    (225, 78, 39),
    (211, 252, 250),
    (252, 201, 1),
    (117, 164, 192),
    (75, 94, 79),
    (96, 77, 85),
    (86, 46, 72),
    (98, 122, 168),
    (127, 219, 243),
    (140, 167, 144),
    (52, 72, 55),
    (186, 133, 164),
    (38, 71, 86),
    (190, 83, 135),
    (76, 143, 171),
    (251, 243, 248),
]
tim = turtle.Turtle()
tim.hideturtle()
turtle.colormode(255)
tim.speed("fastest")
tim.penup()
tim.setpos(-225, -225)

for i in range(10):
    for k in range(10):
        color = random.choice(color_list)
        tim.dot(14, color)
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
