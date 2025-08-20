from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        self.teleport(randint(-280, 280), randint(-280, 280))

    def refresh(self):
        self.teleport(randint(-280, 280), randint(-280, 280))

