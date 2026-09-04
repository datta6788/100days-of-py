import turtle
import random
# COLORS=["red","blue","green","pink","yellow","purple"]
SNAKES_POS=[(0,0),(-20,0),(-40,0)]
class Snake:

    def __init__(self): 
        self.oogways=[]
        self.snake_body()

    def snake_body(self):
        for snake in SNAKES_POS:
            oogway=turtle.Turtle("square")
            oogway.penup()
            oogway.goto(snake)
            self.oogways.append(oogway)
            # SNAKES_POS.a
        # self.oogways[len(self.oogways)-1].color("red")

    def snake_movement(self):
        for pos in range(len(SNAKES_POS)-1,0,-1):
            x=self.oogways[pos-1].xcor()
            y=self.oogways[pos-1].ycor()
            self.oogways[pos].goto(x,y)
        self.oogways[0].forward(20)
        self.oogways[0].color("red")        

    def tail(self):
        oogway2=turtle.Turtle("square")
        oogway2.penup()
        oogway2.goto(self.oogways[-1].position())
        self.oogways.append(oogway2)
        SNAKES_POS.append(oogway2.position())

    def rk(self):
        if self.oogways[0].heading()!=180:
            self.oogways[0].setheading(0)
        # turtle.onkey(self.rt,"d")

    def lk(self):
        if self.oogways[0].heading()!=0:
            self.oogways[0].setheading(180)

    def uk(self):
        if self.oogways[0].heading()!=270:
            self.oogways[0].setheading(90)

    def dk(self):
        if self.oogways[0].heading()!=90:
            self.oogways[0].setheading(270)

