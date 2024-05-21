from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.color("black")
    self.penup()
    self.setheading(90)
    self.restart_car()
  
  def move_up(self):
    self.forward(MOVE_DISTANCE)
  
  def restart_car(self):
    self.goto(STARTING_POSITION)

  def finish_status(self):
    if self.ycor() > FINISH_LINE_Y:
      return True
    else:
      return False
    


  

  

  
    
