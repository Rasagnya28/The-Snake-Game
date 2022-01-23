from turtle import Turtle, Screen
move = 20
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        start = 0
        for i in range(3):
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(start, 0)
            start -= 20
            self.segments.append(segment)
    def add_segment(self):
        new_seg= Turtle("square")
        new_seg.penup()
        new_seg.color("white")
        new_seg.goto(self.segments[-1].position())
        self.segments.append(new_seg)
    def movement(self):
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto(self.segments[index - 1].xcor(), self.segments[index - 1].ycor())
        self.segments[0].forward(move)

    def walls(self):
        if self.segments[0].xcor() > 300:
            self.segments[0].goto(-300, self.segments[0].ycor())
        elif self.segments[0].xcor() < -300:
            self.segments[0].goto(300, self.segments[0].ycor())
        elif self.segments[0].ycor() > 300:
            self.segments[0].goto(self.segments[0].xcor(), -300)
        elif self.segments[0].ycor() < -300:
            self.segments[0].goto(self.segments[0].xcor(), 300)
    def Up(self):
        if self.segments[0].heading()!=270 and -300<=self.segments[0].xcor()<=300:
            self.segments[0].setheading(90)
    def Down(self):
        if self.segments[0].heading()!=90 and -300<=self.segments[0].xcor()<=300:
            self.segments[0].setheading(270)
    def Left(self):
        if self.segments[0].heading()!=0 and -300<=self.segments[0].ycor()<=300:
            self.segments[0].setheading(180)
    def Right(self):
        if self.segments[0].heading()!=180 and -300<self.segments[0].ycor()<300:
            self.segments[0].setheading(0)
