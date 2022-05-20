from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(
    title="Make Your Bet!", prompt="Which turtle will win the race? Enter a color: "
)

all_turtle = []
color = ["red", "orange", "yellow", "green", "blue", "purple"]
start_race = False

y_pos = 100
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos)
    y_pos -= 40
    """everytime a new turtle is generated, immediately appended into a list"""
    all_turtle.append(new_turtle)

if user_bet:
    start_race = True

while start_race:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            start_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! {winning_color} is the winner!")
            else:
                print(f"You lost.... {winning_color} is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
