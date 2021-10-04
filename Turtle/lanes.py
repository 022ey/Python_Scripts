from turtle import Turtle


#Creating Center Line

class Lanes:
    def __init__(self):
        self.all_lanes=[]
        self.y_value=-260

    def lane(self):
        for _ in range(0,18):
            turtle=Turtle()
            turtle.penup()
            turtle.hideturtle()
            turtle.goto(0,self.y_value)
            turtle.pencolor("white")

            # turtle.setheading(270)
            turtle.backward(300) 

            for _ in range(16):
                # turtle.goto()
                turtle.pendown()
                turtle.forward(20)
                turtle.penup()
                turtle.forward(20)

            self.all_lanes.append(turtle)
            self.y_value+=30