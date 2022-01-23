from turtle import Turtle
import random as r

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.refresh()

    def refresh(self):
        self.goto(r.randint(-280, 280), r.randint(-250, 250))


