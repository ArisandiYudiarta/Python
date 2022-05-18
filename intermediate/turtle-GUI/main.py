from turtle import Screen, Turtle, color

turt = Turtle()
turt.shape("turtle")
turt.color("green")

# # circle turtle
# for i in range(4):
#     turt.forward(100)
#     turt.right(90)

# # Dashed line turtle
# for i in range(30):
#     turt.pd()
#     turt.fd(5)
#     turt.pu()
#     turt.fd(5)
#     turt.right(10)

# many shapes turtle
color = ["green", "yellow", "black", "red", "blue", "pink", "grey", "cyan"]
k = 0
for i in range(3, 11):
    for l in range(i):
        turt.color(color[k])
        turt.forward(100)
        turt.right(360 / i)
    k += 1

screen = Screen()
screen.exitonclick()
