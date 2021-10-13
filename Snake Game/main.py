from scoreboard import Scoreboard
from food import Food
import turtle
from snake import Snake
from scoreboard import Scoreboard
from white import White
import time

#Screen setup
#-------------------------------------------#
turtle_screen=turtle.Screen()
turtle_screen.setup(width=600,height=600)
turtle_screen.bgcolor("black")
turtle_screen.title("Snake")
turtle_screen.tracer(0)
#-------------------------------------------#
#Screen setup

#Objects for Snake Game
#-------------------------------------------#
snake=Snake()
snake_food=Food()
white=White()
scoreboard=Scoreboard()
#-------------------------------------------#

#Taking Screen inputs
#-------------------------------------------#
turtle_screen.listen()
turtle_screen.onkey(snake.up,"Up")
turtle_screen.onkey(snake.down,"Down")
turtle_screen.onkey(snake.left,"Left")
turtle_screen.onkey(snake.right,"Right")
#-------------------------------------------#

is_game_on=True

while is_game_on:

    turtle_screen.update()
    scoreboard.display_score()
    time.sleep(0.1)
    snake.move()

    #Detecting colision with food
    if snake.head.distance(snake_food)< 10:
        snake.extend()
        snake_food.refresh()
        scoreboard.scoreboard_update()

    #Detecting collision with wall
    if snake.head.xcor()>280 or snake.head.ycor()>255 or snake.head.xcor()<-280 or snake.head.ycor()<-290:
        scoreboard.reset()
        snake.head.goto(0,0)
        # is_game_on=False
        

    #Detecting collision with own body
    for segment in snake.all_segment[1:]:
        if snake.head.distance(segment)<10:      
            scoreboard.reset()
            snake.head.goto(0,0)
            # is_game_on=False
            

turtle_screen.exitonclick()