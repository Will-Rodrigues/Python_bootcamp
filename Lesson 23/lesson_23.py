from turtle import Screen
from player import Player
from car import Car
from scoreboard import ScoreBoard
import time

is_on = True

screen = Screen()
screen.setup(500, 400)
screen.tracer(0)

scoreboard = ScoreBoard()
player = Player()
car = Car()

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

while is_on:
    screen.update()
    time.sleep(0.1)

    car.create_car()
    car.move()

    for car in car.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            is_on = False

    if player.ycor() > 180:
        player.reset_position()
        scoreboard.level_up()
        for car in car.all_cars:
            car.level_up()

screen.exitonclick()
