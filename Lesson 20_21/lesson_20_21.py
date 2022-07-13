from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
snake.create_snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_on = True

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

    if snake.snake[0].distance(food.pos()) < 15:
        food.new_location()
        scoreboard.score_up()
        snake.extend_snake()

    if snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280 or snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -280:
        is_on = False
        scoreboard.game_over()

    for part in snake.snake[1:]:
        if snake.snake[0].distance(part) < 10:
            is_on = False
            scoreboard.game_over()

screen.exitonclick()