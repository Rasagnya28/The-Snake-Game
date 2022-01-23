from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

scr=Screen()
scr.setup(600,600)
scr.bgcolor("black")
scr.title("Snake Game")

scr.tracer(0)

sn=Snake()
player=scr.textinput("Player Name", "Who's playing?").title()
sb= Scoreboard(player)
scr.listen()
scr.onkey(sn.Up, "Up")
scr.onkey(sn.Down, "Down")
scr.onkey(sn.Left,"Left")
scr.onkey(sn.Right,"Right")
food=Food()

while sn:
    scr.update()
    time.sleep(0.1)
    sn.movement()
    sn.walls()
    if sn.segments[0].distance(food) < 15:
        food.refresh()
        sb.update_score()
        sn.add_segment()
    for segment in sn.segments[1:]:
        if sn.segments[0].distance(segment) < 10:
            sb.game_over()
            scr.exitonclick()
            quit()
