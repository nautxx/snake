from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# initialize
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snaaaaaaaaake")
screen.tracer(0)

# creates objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# listen for keypresses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# main
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15: # 10x10 cirlce size
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    # If head collides with any segment in the tail:
        # trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.reset()

screen.exitonclick()