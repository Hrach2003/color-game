import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
              (176, 192, 209)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)

number_of_dots = 100
dots_per_line = 10
lines_to_print = 10
line_count = 0

while line_count < lines_to_print:
    for dot_count in range(1, dots_per_line + 1):
        tim.dot(20, random.choice(color_list))
        tim.forward(30)
        tim.pensize(30)

    line_count += 1

    if line_count < lines_to_print:
        tim.backward(30 * dots_per_line)
        tim.setheading(90)
        tim.forward(30)
        tim.setheading(0)
turtle_module.Screen().exitonclick()
