from turtle import Screen, Turtle
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("BreakOut")
screen.tracer(0)
screen.listen()


# paddle = Turtle("circle")
# paddle.color("white")
# paddle.penup()
# paddle.shapesize(stretch_len=3, stretch_wid=0.5)
# paddle.goto(0, -250)

paddle = Paddle((0, -280))

screen.onkey(paddle.go_right,"Right")
screen.onkey(paddle.go_left, "Left")

time.sleep(0.1)
screen.update()




screen.exitonclick()