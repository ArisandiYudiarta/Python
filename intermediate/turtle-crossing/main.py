import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
iteration = 0
while game_is_on:

    if iteration == 6:
        car.spawn()
        iteration -= 6
    car.move()
    iteration += 1

    # Detecting collitions with the cars
    for c in car.cars:
        if c.distance(player) < 22:
            game_is_on = False
            score.game_over()

    # Datecting if the player has finished the current level
    if player.ycor() >= player.goal:
        player.resetpos()
        car.increase_speed()
        score.add_score()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
