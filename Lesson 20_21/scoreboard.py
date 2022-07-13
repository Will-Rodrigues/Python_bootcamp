from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"SCORE: {self.score}", True,
                   align="center", font=('Arial', 12, 'bold'))

    def score_up(self):
        self.clear()
        self.score += 1
        self.goto(0, 280)
        self.write(f"SCORE: {self.score}", True,
                   align="center", font=('Arial', 12, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align="center", font=('Arial', 24, 'bold'))
