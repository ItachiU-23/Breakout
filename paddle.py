from turtle import Turtle
MOVE_DISTANCE = 20

class Paddle():

    def __inti__(self, pos):
        self.paddle = Turtle("circle")
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.shapesize(stretch_len=3, stretch_wid=0.5)
        self.paddle.goto(pos)

    def go_right(self):
        self.paddle.fd(MOVE_DISTANCE)

    def go_left(self):
        self.paddle.backward(MOVE_DISTANCE)
