from turtle import Screen
from snake import *
from food import *
from scoreboard import *
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
while game :
    snake.move_snake()
    screen.update()
    time.sleep(0.1)

    #detect collision with food
    if snake.head().distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    #detect collision with wall
    if snake.head().xcor() > 280 or snake.head().xcor() < -280 or snake.head().ycor() > 280 or snake.head().ycor() < -280:
        game = False
        game_over = Scoreboard()
        game_over.game_over()

    #detect collision with snake body
    for body in snake.snakes[1:]:
        if snake.head().distance(body) < 10:
            game = False
            game_over = Scoreboard()
            game_over.game_over()







screen.exitonclick()
