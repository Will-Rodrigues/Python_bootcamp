from turtle import Turtle, Screen, width
from random import randint

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Choose the winner", colors)

height = -100
width = -230

tortoises = []

for _ in range(6):
    tortoise = Turtle('turtle')
    tortoise.color(colors[_])
    tortoise.up()
    tortoise.goto(width, height)
    height += 40
    tortoises.append(tortoise)

if user_bet:
    is_on = True

while is_on:
    for tortoise in tortoises:
        if tortoise.xcor() > 230:
            is_on = False
            winning_color = tortoise.pencolor()
            if winning_color == user_bet:
                print("You win")
            else:
                print(f"You lost, the winner is the {winning_color} turtle.")
        tortoise.forward(randint(0, 11))

screen.exitonclick()
