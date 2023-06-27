from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=420)

colors = ['red', 'green', 'blue', 'indigo', 'violet', 'yellow', 'orange']
y_positions = [-180, -120, -60, 0, 60, 120]
all_turtles = []

for index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput('USER BET', 'which color of turtle are you placing your bet on? ')

race_on = False

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            race_on = False
            turtle_color = turtle.pencolor()
            if user_bet == turtle_color:
                print(f'You won, {turtle_color} won the race')
            else:
                print(f'You lost, {turtle_color} won the race')
    
    
