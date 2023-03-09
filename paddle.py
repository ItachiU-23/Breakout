from turtle import Turtle
MOVE_DISTANCE  = 10
START_POSITION = (0, -270)

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=3, stretch_wid=0.5)
        self.goto(START_POSITION)

    
    def go_right(self):
        if self.xcor() < 260:
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def go_left(self):
        if self.xcor() > -260:
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x, self.ycor())
            

        
        

