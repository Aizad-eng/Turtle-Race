#Turtle Race

from turtle import Turtle, Screen
import random

screen = Screen()
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
    ycor = -80
    for turtle in turtles:
        turtle.penup()
        turtle.shapesize(3,3)
        turtle.goto(-450, ycor)
        ycor += 80

race_start()
race_not_finished = True

while race_not_finished:
    for turtle in turtles:
        for i in range(1):
            turtle.speed(random.randint(1, 20))
            turtle.forward(random.randint(1, 30))
            if turtle.xcor()>=430:
                index_of_winner_turtle = turtles.index(turtle)
                winner_turtle_color = colors[index_of_winner_turtle]
                print(f"{winner_turtle_color} Won!")
                race_not_finished = False
if choice.lower() == winner_turtle_color:
    print("You won the bet")
else:
    print("You lost the bet")



screen.exitonclick()