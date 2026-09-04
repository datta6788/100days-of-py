import turtle
import random
class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5)
        self.penup()
        self.food_teleport()

    def food_teleport(self):
        self.teleport(random.randint(0,100),random.randint(0,100))

        