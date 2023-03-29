import time
import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# screen setup
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor('Black')
screen.title('Snake Game')
screen.tracer(0)

scoreboard = Scoreboard()
food = Food()
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food and increasing score
    if snake.head.distance(food) < 15:
        food.refresh_location()
        snake.extend_snake()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # detecting tail collision
    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
