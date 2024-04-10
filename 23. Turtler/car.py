from turtle import Turtle
import random

COLOR_LIST = ["red", "green", "yellow", "purple", "blue", "orange", "black", "brown", "pink"]
SPEED = 5
MOVE_INCREMENT = 10

class Car():

    def __init__(self):
        self.allCars = []

    def createCar(self):
        carHeight = random.randint(-250,250)
        randomCarSpawnChance = random.randint(0,6)
        if randomCarSpawnChance == 1 or randomCarSpawnChance == 2:
            newCar = Turtle()
            newCar.shape("square")
            newCar.color(COLOR_LIST[random.randint(0,8)])
            newCar.penup()
            newCar.shapesize(stretch_len=1.5, stretch_wid=.75)
            newCar.goto(300, carHeight)
            newCar.setheading(180)
            self.allCars.append(newCar)

    def moveCar(self):
        for car in self.allCars:
            car.forward(SPEED)

    def speedUp(self):
        global SPEED
        SPEED += MOVE_INCREMENT

    