from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE =  10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.clear()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.resetPosition()
        self.setheading(90)

    def moveUp(self):
        if self.ycor() < 280:
            self.forward(MOVE_DISTANCE)

    def moveDown(self):
        if self.ycor() > -201:
            self.backward(MOVE_DISTANCE)

    def finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
        
    def resetPosition(self):
        self.goto(STARTING_POSITION)