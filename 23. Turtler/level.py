FONT = ("Courier", 24, "normal")
from turtle import Screen, Turtle
from car import Car
from player import  Player

car = Car()

class Level(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.updateLevel()


    def updateLevel(self):
        self.clear()
        self.goto(-230,200)
        self.write("Level: ", align="center", font= FONT)
        self.goto(-170,200)
        self.write(self.level, align="center", font= FONT)

    def addLevel(self):
        self.level += 1
        self.updateLevel()
        car.speedUp()

    def gameOver(self):
        self.goto(0,0)
        self.color("black")
        self.write("Game Over", align="center", font= ("Courier", 80, "normal"))