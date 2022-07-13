from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.6)
        self.up()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor()+ self.y_move)

    def hit_top_bottom(self):
        self.y_move *= -1

    def hit_left_right(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.clear()
        self.move_speed = 0.1
        self.goto(0, 0)
        self.hit_left_right()
