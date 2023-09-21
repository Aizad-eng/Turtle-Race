#Turtle Race
import time
from turtle import Turtle, Screen
import random

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
colors  = ["red","blue","green","purple","orange","violet"]
choice = screen.textinput("Decide winner: ", "Which color turtle will win? ")
while choice not in colors:
    choice = screen.textinput("Decide winner: ", "Which color turtle will win? ")

turtles =[]

for i in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color((colors[i]))
    turtles.append(new_turtle)

print(screen.screensize())

def race_start():
    ycor = -180
    for turtle in turtles:
        turtle.penup()
        turtle.shapesize(2,2)
        turtle.goto(-450, ycor)
        ycor += 80

race_start()
screen.update()
race_not_finished = True

while race_not_finished:
    screen.update()
    for turtle in turtles:
        time.sleep(0.01)
        screen.update()
        for i in range(1):
            turtle.forward(random.randint(1, 30))
            if turtle.xcor()>=430:
                winner_turtle_color = turtle.pencolor()
                race_not_finished = False
                if choice.lower() == winner_turtle_color:
                    print("You won the bet")
                else:
                    print(f"You lost the bet, {winner_turtle_color} won!")



screen.exitonclick()