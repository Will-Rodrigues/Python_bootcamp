from turtle import Turtle


class PlayerBar(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape('square')
        self.shapesize(5, 1)
        self.goto(-380, 0)

    def move_up(self):
        if self.ycor() < 230:
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -230:
            self.sety(self.ycor() - 20)


class ComputerBar(PlayerBar):
    def __init__(self):
        super().__init__()
        self.goto(380, 0)
