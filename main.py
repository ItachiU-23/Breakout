from turtle import Screen, Turtle
from paddle import Paddle
from ball import  Ball
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("BreakOut")
# screen.tracer(0)
screen.listen()

dash = Paddle()
breaker = Ball()


screen.onkeypress(dash.go_right, "Right")
screen.onkeypress(dash.go_left, "Left")


# screen.update()

screen.exitonclick()