import turtle
import random
class pong(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("red")
        self.x=10
        self.y=10
        self.startpos()

    def movement(self):
        # self.goto(self.xcor()+10,self.ycor()+10)
        nx=self.xcor()+self.x
        ny=self.ycor()+self.y
        self.goto(nx,ny)

    def bouncey(self):
        # self.x=xval
        # self.y=yval
        self.y*=-1
        # self.goto(self.xcor()+10,self.ycor()-10)

    def bouncex(self):
        self.x*=-1

    def startpos(self):
        self.goto(0,random.randint(-380,380))