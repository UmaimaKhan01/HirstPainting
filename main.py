from turtle import Turtle, Screen

is_race_on=False
tim=Turtle()
screen=Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race?enter a color: ")
colors=["red", "orange", "yellow", "green", "blue", "violet"]
y_position=[-70, -40, -10, 20, 50, 80]

for turtle_index in range(0,6):
    tim=Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_position[turtle_index])

if user_bet:
    is_race_on=True

while is_race_on:


screen.exitonclick()