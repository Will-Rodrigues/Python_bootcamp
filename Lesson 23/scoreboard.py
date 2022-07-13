from turtle import Turtle

FONT = ("Courier", 24, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.level = 1
        self.show_level()

    def show_level(self):
        self.goto(-235, 175)
        self.write(f"Level: {self.level}")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.show_level()
