from turtle import Turtle

FONT=("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(-200,260)
        self.color("white")
        self.penup()
        with open("D:/Study/100 Days of code/Turtle game/Snake Game/data/data.txt") as data:
            self.highScore=int(data.read())
        self.hideturtle()
        self.display_score()        

    def display_score(self):
        self.clear()
        self.color("green")
        self.write(arg=f"High Score ={self.highScore}     Score = {self.score}",font=FONT)

    def reset(self):
        self.score=0

    def scoreboard_update(self):
        self.score+=1
        self.clear()
        self.playerHighScore()
        self.display_score()

    def playerHighScore(self):
        if self.highScore<self.score:
            self.highScore=self.score
            with open("D:/Study/100 Days of code/Turtle game/Snake Game/data/data.txt",mode="w") as data:
                data.write(f"{self.highScore}")