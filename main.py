import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

car = CarManager()
scoreboard = Scoreboard()
player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

screen.onkey(player.move, "Up")

game_on = True
while game_on:
    time.sleep(car.car_speed)
    screen.update()
    car.create_car()
    car.move()

    # DETECTS WHEN PLAYER REACHES FINISH LINE
    if player.ycor() == 280:
        player.restart()
        car.car_speed *= 0.009
        scoreboard.score += 1
        scoreboard.point()

    # DETECTS WHEN PLAYER COLLIDES WITH CAR
    for i in car.car_list:
        if player.distance(i) < 20:
            scoreboard.game_over()
            game_on = False
screen.exitonclick()
