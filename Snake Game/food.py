from turtle import Turtle
import random

class Food(Turtle):
    """Creates a turtle food at random location"""
    
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x=random.randrange(-280,280,20)
        random_y=random.randrange(-280,250,20)
        self.goto(random_x,random_y)