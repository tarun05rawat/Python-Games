from turtle import Turtle


FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def scoring(self):
        self.penup()
        self.hideturtle()
        self.goto(-290,270)
        self.write(f"LEVEL: {self.score}",align="left",font=FONT)
    
    def increase_score(self):
        self.clear()
        self.score+=1
        self.scoring()
    





