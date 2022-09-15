from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)  # This will turn of updating the screen ,so you won't see turtle being created
# Then you have to manually define the update program

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()

screen.onkey(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")

fullScore = 0

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    # Detecting the collision of Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detecting the collision of Walls
    if snake.head.xcor() < -300 or snake.head.xcor() > +300 or snake.head.ycor() > +300 or snake.head.ycor() < -300 :
        score.reset()
        snake.reset()

    # Detect the collision with Tail
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         score.end_game()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
