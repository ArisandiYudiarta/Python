from hashlib import new
from mimetypes import init
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self) -> None:
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):

        for c in self.cars:
            c.forward(self.speed)

    def spawn(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.seth(180)
        new_car.penup()
        new_car.goto(200, random.randrange(-250, 250))
        self.cars.append(new_car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
