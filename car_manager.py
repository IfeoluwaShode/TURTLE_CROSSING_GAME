import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.create_car()
        self.car_speed = 0.1

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 2:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            position_y = random.randint(-250, 250)
            car.goto(300, position_y)
            self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            car.backward(STARTING_MOVE_DISTANCE)
