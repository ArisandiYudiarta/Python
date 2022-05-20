from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.shape("turtle")


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_right():
    tim.right(10)


def move_left():
    tim.left(10)


def clearscreen():
    tim.clear()

screen.listen()

screen.onkeypress(key="Up", fun=move_forward)
screen.onkeypress(key="Left", fun=move_left)
screen.onkeypress(key="Right", fun=move_right)
screen.onkeypress(key="Down", fun=move_backwards)
screen.onkeypress(key="c", fun=clearscreen)


screen.exitonclick()
