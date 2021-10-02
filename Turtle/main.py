from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from lanes import Lanes
from safezone import SafeZone
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")

screen.tracer(0)

start=SafeZone(0,-280,30,1.8,"green")
finish=SafeZone(0,280,30,2.8,"green")
finish_line=SafeZone(0,290,4,1.2,"white")

lanes=Lanes()
lanes.lane()

player=Player()
screen.listen()
screen.onkey(player.goup,"Up")
screen.onkey(player.godown,"Down")

car=CarManager()

game_is_on = True
score=Scoreboard()

while game_is_on:
    
    score.display_current_level()
    time.sleep(0.1)
    car.create_car()
    car.car_move()
    
    for single_car in car.all_cars:
        if player.distance(single_car)<20:
            game_is_on=False
            score.game_over()

        if player.finish_line():
            player.go_to_start()
            car.level_up()
            score.increase_level()
    
    
    screen.update()

screen.exitonclick()