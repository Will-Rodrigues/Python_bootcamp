from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake = []
        self.speed = 20

    def new_part(self, position):
        new_part = Turtle('square')
        new_part.up()
        new_part.goto(position)
        self.snake.append(new_part)

    def create_snake(self):
        for position in STARTING_POSITION:
            self.new_part(position)

    def reset(self):
        for _ in self.snake:
            _.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()

    def extend_snake(self):
        self.new_part(self.snake[-1].position())

    def move_forward(self):
        for part in range(len(self.snake) - 1, 0, -1):
            if part > 0:
                next_part = self.snake[part - 1]
                self.snake[part].goto(next_part.xcor(), next_part.ycor())
        self.snake[0].forward(self.speed)

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].seth(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].seth(270)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].seth(180)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].seth(0)
