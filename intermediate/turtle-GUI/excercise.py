from turtle import Screen, Turtle, color
import random

turt = Turtle()
screen = Screen()
turt.shape("classic")

# # circle turtle===========================================================
#     turt.forward(100)
#     turt.right(90)

# # Dashed line turtle======================================================
# for i in range(30):
#     turt.pd()
#     turt.fd(5)
#     turt.pu()
#     turt.fd(5)
#     turt.right(10)

# # many shapes turtle======================================================
# color = ["green", "yellow", "black", "red", "blue", "pink", "grey", "cyan"]
# k = 0
# for i in range(3, 11):
#     for l in range(i):
#         turt.color(color[k])
#         turt.forward(100)
#         turt.right(360 / i)
#     k += 1

# # random walk turtle======================================================

# # selected color
# # color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen",]

# # random color
# screen.colormode(255)


# direction = [0, 90, 180, 270]

# turt.pensize(10)
# turt.speed(100)


# for i in range(200):
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)

#     # turt.pencolor(random.choice(color))
#     turt.pencolor(r, g, b)

#     turt.forward(20)
#     turt.setheading(random.choice(direction))

turt.speed(100)
screen.colormode(255)


def draw_spirograph(gap_size):
    for i in range(int(360 / gap_size)):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turt.pencolor(r, g, b)

        turt.left(gap_size)
        turt.circle(100)


draw_spirograph(5)

screen.exitonclick()
