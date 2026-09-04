import turtle
class score(turtle.Turtle):
    I=0
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.teleport(0,300)
        self.write(align="center",font=("Arial",10,"bold"),arg=f"Score-{self.I}")

    def increase_score(self):
        self.I+=1
        # print(self.I)
        self.clear()
        self.write(align="center",font=("Arial",10,"bold"),arg=f"Score-{self.I}")

    def gameover(self):
        self.teleport(0,0)
        self.write(arg="GAMEOVER",align="center",font=("Arial",24,"bold"))


