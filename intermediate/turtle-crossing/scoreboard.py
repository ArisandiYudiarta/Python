from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.score = 0
        self.write(f"Score: {self.score}", font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", font=FONT)

    def game_over(self):
        self.goto(x=-90, y=0)
        self.write(f"GAME OVER", font=FONT)
