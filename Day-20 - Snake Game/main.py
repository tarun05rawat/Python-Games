from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random

def main():
  screen = Screen()
  screen.setup(width=600,height=600)
  screen.bgcolor("black")
  screen.title("Tarun's Snake Game")
  screen.tracer(0)


  snake = Snake()
  food = Food()
  scoreboard = Scoreboard()





  screen.listen()
  screen.onkey(snake.up, "Up")
  screen.onkey(snake.down, "Down")
  screen.onkey(snake.left, "Left")
  screen.onkey(snake.right, "Right")



    

  game_is_on = True

  while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    if snake.head.distance(food) < 15:      #DETECT COLLISION WITH FOOD
      food.refresh()
      snake.extend()
      scoreboard.newscore()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:        # DETECT COLLISION WITH WALLS
      game_is_on = False
      scoreboard.game_over()
    
    for segment in snake.segments:              # DETECT COLLISION WITH TAIL
      if segment == snake.head:
        pass
      elif snake.head.distance(segment) < 10:
        game_is_on = False
        scoreboard.game_over()
      
  screen.update()
  play_again = screen.textinput("Game Over", "Play again? Type Yes or No: ")

  if play_again.lower() == 'yes':
    screen.clearscreen()
    main()
  else:
    screen.bye()
  

  screen.exitonclick()

main()