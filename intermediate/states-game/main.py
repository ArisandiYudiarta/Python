import turtle
import pandas as pd

screen = turtle.Screen()
screen.screensize()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
print(type(all_states))

correct_guess = []

game_running = True
while game_running:
    score = len(correct_guess)
    answer_state = screen.textinput(
        title=f"Guess the States    Score : {score}/50 ",
        prompt="What's another state's name?                 ",
    ).title()

    if answer_state == "Exit":
        game_running = False
    if answer_state in all_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, font=("Arial", 8, "normal"))
        correct_guess.append(answer_state)
    if score == 50:
        game_running = False

# check the unanswered states and export it into a csv file
unanswered_states = list(set(all_states) - set(correct_guess))
us = pd.DataFrame(unanswered_states)
us.to_csv("unanswered_states.csv")

turtle.exitonclick()
