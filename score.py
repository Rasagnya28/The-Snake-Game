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
        self.goto(250,250)
        self.write(f"Score : {self.score}",align= "right", font=("Arial", 25, "normal"))
        self.goto(-270,250)
        self.write(f"High Score : {max(score_list)} ({score_list[max(score_list)]})", align="left", font=("Arial", 20, "normal"))

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
        self.write("GAME OVER", align="center",font=("Arial", 25, "normal"))



