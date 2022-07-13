from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.computer_score = 0
        self.hideturtle()
        self.reset_position()
        self.show_score()

    def reset_position(self):
        self.clear()
        self.draw_line()
        self.goto(0, 250)

    def show_score(self):
        self.write(f"{self.player_score}    {self.computer_score}",
                   True, align="center", font=("Courier", 36, "bold"))

    def player_point(self):
        self.reset_position()
        self.player_score += 1
        self.show_score()

    def computer_point(self):
        self.reset_position()
        self.computer_score += 1
        self.show_score()

    def draw_line(self):
        self.up()
        self.goto(0, -300)
        self.seth(90)
        for _ in range(15):
            self.down()
            self.forward(20)
            self.up()
            self.forward(20)
