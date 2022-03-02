import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        scoreboard.increase_score()

    #collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()





screen.exitonclick()