from turtle import Turtle

MOVE=20
TURTLE_POS=[(0,0),(-20,0),(-40,0)]

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    """Creates snakes objects and stores them in a list"""

    def __init__(self):
        self.all_segment=[]
        self.create_snake()
        self.head=self.all_segment[0]

    def create_snake(self):
             
        for coordinate in TURTLE_POS:
            self.add_segment(coordinate)
            
    def add_segment(self,coordinate):
        new_segment=Turtle(shape="square")
        new_segment.color("yellow")
        new_segment.penup()
        new_segment.goto(coordinate)
        self.all_segment.append(new_segment)

    def extend(self):
        self.add_segment(self.all_segment[-1].position())
    

    def move(self):

        for pos in range(len(self.all_segment)-1,0,-1):
            x_value=self.all_segment[pos-1].xcor()
            y_value=self.all_segment[pos-1].ycor()
            self.all_segment[pos].goto(x_value,y_value)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)