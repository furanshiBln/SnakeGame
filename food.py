from turtle import Turtle
import random

#should inherit from Turtle class

class Food(Turtle):

    def __init__(self):
        super().__init__()
        #all of the following is happening everytime the class is called
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 275)
        random_y = random.randint(-280, 275)
        self.goto(random_x, random_y)