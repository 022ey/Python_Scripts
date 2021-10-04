from turtle import Turtle

class SafeZone(Turtle):
    def __init__(self,x_cor,y_cor,length,width,colour):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=length,stretch_wid=width)
        self.color(colour)
        self.goto(x=x_cor,y=y_cor)