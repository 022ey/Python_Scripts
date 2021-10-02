import turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("brown")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def goup(self):
        self.forward(MOVE_DISTANCE)

    def godown(self):
        if self.ycor()>-280:
            self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor()>=280:
            return True
        else:
            return False