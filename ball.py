from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.9,stretch_len=0.9)
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        # this will reverse the move direction of ball in same cordinates
        self.y_move *= -1

    def bounce_x(self):
        # this will reverse the move direction of ball in same cordinates
        self.x_move *= -1
        self.move_speed *=0.9

    def reset_position(self):
        # this will move ball again to home if paddle misses
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()

