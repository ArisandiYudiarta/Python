from turtle import Turtle, Screen
import random


color = [
    (157, 116, 152),
    (30, 26, 51),
    (49, 46, 86),
    (115, 59, 61),
    (199, 111, 104),
    (56, 61, 115),
    (109, 99, 156),
    (116, 84, 109),
    (20, 22, 51),
    (242, 160, 159),
]


turt = Turtle()
screen = Screen()

turt.penup()
turt.setx(-250)
turt.sety(-250)
turt.speed("fastest")
turt.hideturtle()
screen.colormode(255)


y = -250
for i in range(10):
    y += 50
    for j in range(10):
        turt.pencolor(random.choice(color))
        turt.dot(20)
        turt.forward(50)
    turt.sety(y)
    turt.setx(-250)

screen.exitonclick()
