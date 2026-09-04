import turtle

class player1(turtle.Turtle):
    def __init__(self,xaxis,yaxis):
        super().__init__()
        # turtle.update()
        self.penup()
        self.shape("square") 
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.teleport(xaxis,yaxis)
        # self.loc()

    def up(self):
        self.goto(self.xcor(),self.ycor()+30)

    def dn(self):
        self.goto(self.xcor(),self.ycor()-30)

    def loc(self):
        print(self.position())

# class oogway(turtle.Turtle):
#         def __init__(self,x,y):
#             super().__init__()
#             self.shape("circle")
#             self.penup()
#             self.teleport(x,y)
#         def up(self):
#                 self.goto(self.xcor(),self.ycor()+20)
        
#         def dn(self):
#             self.goto(self.xcor(),self.ycor()-20)
        
#         def loc(self):
#             print(self.position())
# turtle.listen()
# turtle.onkey(up,"Up")
# turtle.onkey(dn,"Down")