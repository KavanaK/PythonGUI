# A simple game to start with

import turtle
import os


win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)


#Main game loop

#while True:
  #  win.update()

#setting score

score_a = 0
score_b = 0


#paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(10)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5 , stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

