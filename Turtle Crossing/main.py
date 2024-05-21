import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 30, "normal")

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()
game_over = Turtle()
game_over.hideturtle()

screen.listen()
screen.onkey(player.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.scoring()

    car_manager.create_car()
    car_manager.move_car()

    # DETECT CRASHES WITH CAR
    for car in car_manager.all_cars:    
        if car.distance(player) < 20:
            game_over.penup()
            game_over.hideturtle()
            game_over.write(f"GAME OVER",align="center",font=GAME_OVER_FONT)
            game_is_on = False
            
    
    # DETECT LEVEL FINISH
    if player.finish_status():
        player.restart_car()
        car_manager.level_up()
        score.increase_score()





    
screen.exitonclick()


    
