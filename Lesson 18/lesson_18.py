import turtle as t
from random import choice

colors = [(78, 96, 119), (248, 231, 194), (190, 157, 130), (36, 32, 24), (133, 145, 156), (31, 44, 62), (112, 102, 84), (231, 199, 132), (143, 152, 146), (97, 107, 103),
          (43, 62, 92), (115, 105, 111), (149, 138, 142), (26, 30, 27), (153, 147, 77), (114, 126, 146), (36, 32, 34), (148, 120, 113), (78, 74, 32), (209, 214, 221)]

dot_size = 10

t.colormode(255)
tortoise = t.Turtle()
tortoise.speed(0)
tortoise.up()
tortoise.hideturtle()

screen = t.Screen()
screen.setup(300, 300)

t_height = -(screen.window_height()/2) + 20
t_widht = -(screen.window_width()/2) + 20

tortoise.goto(t_widht, t_height)

while tortoise.ycor() < screen.window_height():
    while tortoise.xcor() < screen.window_width():
        tortoise.dot(dot_size, choice(colors))
        tortoise.forward(20)
    t_height += (dot_size * 2)
    tortoise.goto(-(screen.window_width()/2) + 20, t_height)

screen.exitonclick()
