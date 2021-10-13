from turtle import Turtle

class White(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=30,stretch_wid=2)
        self.penup()
        self.goto(-0,280)