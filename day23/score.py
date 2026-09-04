import turtle

class scoreboard(turtle.Turtle):
    level=1
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.teleport(-450,400)
        self.level_up()

    def level_up(self):
        self.clear()
        self.write(f"Level:{self.level}",font=("Times",24,"bold"))
        self.level+=1

    def game_over(self):
        self.teleport(-200,0)
        self.write(f"GAME OVER",font=("Arial",50,"bold"))