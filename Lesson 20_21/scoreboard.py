from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("lesson 20_21/data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"SCORE: {self.score} | HIGHSCORE {self.high_score}" , True,
                   align="center", font=('Arial', 12, 'bold'))

    def score_up(self):
        self.clear()
        self.score += 1
        self.goto(0, 280)
        self.write(f"SCORE: {self.score} | HIGHSCORE {self.high_score}" , True,
                   align="center", font=('Arial', 12, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("lesson 20_21/data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.goto(0, 280)
        self.write(f"SCORE: {self.score} | HIGHSCORE {self.high_score}" , True,
                   align="center", font=('Arial', 12, 'bold'))
