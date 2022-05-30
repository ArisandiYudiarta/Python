from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

# The line
line = Turtle("square")
line.color("white")
line.shapesize(stretch_wid=30, stretch_len=0.2)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
da_ball = Ball((0, 0))
r_score = Scoreboard((100, 240))
l_score = Scoreboard((-100, 240))

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_starts = True

while game_starts:
    time.sleep(0.05)
    screen.update()
    da_ball.move()

    # Detecting collotion with wall
    if da_ball.ycor() > 280 or da_ball.ycor() < -280:
        da_ball.bounce()

    # Detecting collition with paddle
    if (
        da_ball.distance(r_paddle) < 50
        and da_ball.xcor() > 320
        or da_ball.distance(l_paddle) < 50
        and da_ball.xcor() < -330
    ):
        da_ball.bounce_paddle()

    elif da_ball.xcor() > 400 or da_ball.xcor() < -400:
        if da_ball.xcor() > 400:
            r_score.add_score()
            r_score.update()
        elif da_ball.xcor() < -400:
            l_score.add_score()
            l_score.update()
        da_ball.resetpos()

screen.exitonclick()
