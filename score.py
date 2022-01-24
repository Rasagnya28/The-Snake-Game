from turtle import Turtle
import score_list
import json
from score_list import score_list
class Scoreboard(Turtle):

    def __init__(self, player):
        super().__init__()
        self.score = 0
        self.player = player
        self.hideturtle()
        self.penup()
        self.color("white")
        self.display()

    def display(self):
        self.goto(260,250)
        self.write(f"Score : {self.score}",align= "right", font=("Courier", 16, "normal"))
        self.goto(-280,250)
        self.write(f"High Score : {max(score_list)}({score_list[max(score_list)]})", align="left", font=("Courier", 16, "normal"))

    def update_score(self):
        self.score+=1
        self.clear()
        self.display()

    def game_over(self):
        self.goto(0,0)
        self.color("red")

        file=open("score_list.py", "w")
        if self.score not in score_list:
            score_list[self.score] = self.player
        if self.score in score_list and self.player != score_list[self.score]:
            score_list[self.score]+=f" , {self.player}"
        file.write(f"score_list={json.dumps(score_list)}")
        file.close()
        self.write("GAME OVER", align="center",font=("Arial", 25, "bold"))
        self.goto(0,-50)
        self.color("dodger blue")
        self.write(f"Your Score : {self.score}", align="center",font=("Sans-Serif", 22, "normal"))



