from turtle import Turtle, Screen

tortoise = Turtle()
screen = Screen()

tortoise_heading = 0


def move_forwards():
    tortoise.forward(10)


def move_backwards():
    tortoise.backward(10)


def tilt_left():
    global tortoise_heading
    tortoise_heading += 10
    tortoise.setheading(tortoise_heading)


def tilt_right():
    global tortoise_heading
    tortoise_heading -= 10
    tortoise.setheading(tortoise_heading)


def clear():
    tortoise.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=tilt_left)
screen.onkey(key="d", fun=tilt_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
