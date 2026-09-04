import turtle

class score(turtle.Turtle):
    s1=0
    s2=0
    def __init__(self):
        super().__init__()
        # self.teleport(-100,330)
        self.hideturtle()

    def updt(self):
        self.clear()
        self.teleport(100,330)
        self.write(f"{self.s1}",font=("Arial",24,"bold"))
        self.teleport(-100,330)
        self.write(f"{self.s2}",font=("Arial",24,"bold"))

    def s1increase(self):
        self.s1+=1
        self.updt()

    def s2increase(self):
        self.s2+=1
        self.updt()

    def gameover(self):
        self.teleport(0,0)
        self.write(arg="GAMEOVER",align="center",font=("Arial",24,"bold"))