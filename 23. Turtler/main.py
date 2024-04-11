from turtle import Screen
from car import Car
import time
from player import Player
from level import Level

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.title("Turtler")
screen.tracer(0)
player = Player()
car = Car()
level = Level()

screen.listen()
screen.onkey(player.moveUp, "Up")
screen.onkey(player.moveDown, "Down")

gameStatus = True
while gameStatus:
    time.sleep(0.1)
    screen.update()

    car.createCar()
    car.moveCar()

    for carObj in car.allCars:
        if carObj.distance(player) < 20:
            level.gameOver()
            gameStatus = False
    
    if player.finish():
        level.addLevel()
        player.resetPosition()


screen.exitonclick()
