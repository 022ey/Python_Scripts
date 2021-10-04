COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import time
import random

class CarManager:

    def __init__(self):
        self.all_cars=[]
        self.car_reserve = []
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):

        random_no=random.randint(1,4)
        
        if random_no==1:
            if self.car_reserve:
                new_car = self.car_reserve.pop()
            else:
                new_car=Turtle(shape="square")
                new_car.shapesize(stretch_len=2,stretch_wid=1)
                new_car.penup()
                new_car.color(random.choice(COLORS))
                # random_y=int(random.randint(-8, 8)*30)
                # new_car.goto(280,random_y)
                # self.all_cars.append(new_car)
            random_y = int(random.randint(-8, 8)*30)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)


    def car_move(self):
        
        for car in self.all_cars:
            
            car.backward(self.car_speed)
            if car.xcor() < -320:
                self.all_cars.remove(car)
                self.car_reserve.append(car)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT