from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super(Food, self).__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("White")
        self.speed(0)
        self.goto(x=random.randrange(-280, 280, 10), y=random.randrange(-280, 280, 10))
        self.refresh()

    def refresh(self):
        self.goto(x=random.randrange(-280, 280, 10), y=random.randrange(-280, 280, 10))
