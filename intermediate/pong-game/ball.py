from turtle import Turtle, shape


class Ball(Turtle):
    #
    def __init__(self, cor) -> None:
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(cor)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def resetpos(self):
        self.x_move *= -1
        self.goto(0, 0)
