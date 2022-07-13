from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.up()
        self.seth(90)
        self.reset_position()

    def move_up(self):
        self.sety(self.ycor() + 10)
    
    def move_down(self):
        if self.ycor() > -180:
            self.sety(self.ycor() - 10)

    def reset_position(self):
        self.goto(0, -180)
