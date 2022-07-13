from turtle import Turtle
from random import choice, randint

COLORS = ["blue", "red", "orange", "yellow", "purple"]
STARTING_SPEED = 5
SPEED_INCREMENT = 10


class Car:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_SPEED

    def create_car(self):
        if randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.up()
            new_car.shapesize(1, 2)
            new_car.seth(180)
            new_car.color(choice(COLORS))
            new_car.goto(300, randint(-140, 150))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            if car.xcor() > -280:
                car.forward(self.speed)
            else:
                car.goto(randint(300, 500), randint(-140, 150))

    def level_up(self):
        self.speed += SPEED_INCREMENT
