from turtle import Screen
from scoreboard import ScoreBoard
from ball import Ball
from pong_bar import PlayerBar, ComputerBar
import time

# TODO: create computer bar
is_on = True

screen = Screen()
screen.setup(800, 600)
screen.title("Pong game")
screen.tracer(0)

scoreboard = ScoreBoard()
ball = Ball()
player_bar = PlayerBar()

computer_bar = ComputerBar()

screen.listen()
screen.onkeypress(player_bar.move_up, "Up")
screen.onkeypress(player_bar.move_down, "Down")

screen.onkeypress(computer_bar.move_up, "w")
screen.onkeypress(computer_bar.move_down, "s")


while is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.player_point()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.computer_point()
    elif ball.ycor() < -275 or ball.ycor() > 280:
        ball.hit_top_bottom()

    if ball.distance(computer_bar) < 50 and ball.xcor() > 358 or  ball.distance(player_bar) < 50 and ball.xcor() < -358:
        ball.hit_left_right()

screen.exitonclick()
