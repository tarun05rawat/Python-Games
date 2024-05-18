from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True

while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  # Detect Collision with Wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  #Detect Collision with paddles
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()

  # Detect if Right Paddle misses
  if ball.xcor() > 380:       
    scoreboard.l_point()
    ball.restart()

  # Detect if Left Paddle misses
  if ball.xcor() < -380:
    scoreboard.r_point()
    ball.restart()

  



screen.exitonclick()


