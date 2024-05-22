from turtle import Turtle, Screen
import pandas as pd


df = pd.read_csv("50_states.csv")

screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")

image = "blank_states_img.gif"


screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's a state name?")
print(answer_state)

screen.mainloop()
