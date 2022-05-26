from turtle import Turtle

TEXT_ALIGN = "center"
SCORE_FONT = ("Arial", 12, "normal")
GAME_OVER_FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(x=0, y=270)
        self.write(f"Score : {self.score}", align=TEXT_ALIGN, font=SCORE_FONT)

    def add_score(self):
        self.score += 1

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER!", align=TEXT_ALIGN, font=GAME_OVER_FONT)
