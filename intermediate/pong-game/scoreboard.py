from turtle import Turtle

TEXT_ALIGN = "center"
SCORE_FONT = ("Arial", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self, pos) -> None:
        super().__init__()
        self.color("white")
        self.ht()
        self.position = pos
        self.pu()
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(self.position)
        self.write(f"{self.score}", align=TEXT_ALIGN, font=SCORE_FONT)

    def add_score(self):
        self.score += 1
