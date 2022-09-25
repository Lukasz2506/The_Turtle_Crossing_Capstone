from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.step = STARTING_MOVE_DISTANCE
        self.car_list = []
        self.append_cars()


    def append_cars(self):
        is_car = randint(1, 6)
        if is_car == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.goto(300, randint(-255, 255))
            self.car_list.append(new_car)

    def move_car(self):
        self.append_cars()
        for car in self.car_list:
            car.backward(self.step)

    def next_level(self):
        self.step += MOVE_INCREMENT
