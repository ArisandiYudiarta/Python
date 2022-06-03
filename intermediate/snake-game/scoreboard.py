from turtle import Turtle

TEXT_ALIGN = "center"
SCORE_FONT = ("Arial", 12, "normal")
GAME_OVER_FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=270)
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(
            f"Score : {self.score} High Score : {self.high_score}",
            align=TEXT_ALIGN,
            font=SCORE_FONT,
        )

    def add_score(self):
        self.score += 1

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.show_score()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"GAME OVER!", align=TEXT_ALIGN, font=GAME_OVER_FONT)
