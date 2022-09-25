import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from roadways import Roadways

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# TODO 1. Create a player (turtle).
player = Player()

# TODO 2. Create a traffic.
car_manager = CarManager()

# TODO 5. Create a scoreboard
score = Scoreboard()
roadways = Roadways()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_car()
    # TODO 4. Detect when the turtle reaches the other side.
    if player.ycor() == 290:
        player.starting_pos()
        car_manager.next_level()
        score.level_up()
    # TODO 3. Detect collision with the car.
    for car in car_manager.car_list:
        if player.distance(car) <= 25:
            score.game_over()
            game_is_on = False

screen.exitonclick()