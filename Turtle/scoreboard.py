from turtle import Turtle

FONT = ("Comic Sans MS", 18, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.player_level=1
        self.hideturtle()
        self.goto(-290,265)
        self.display_current_level()

    def increase_level(self):
        self.player_level+=1
        self.display_current_level()

    def display_current_level(self):
        self.clear()
        self.write(arg=f"Level- {self.player_level}",align="left",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER",align="center",font=FONT)