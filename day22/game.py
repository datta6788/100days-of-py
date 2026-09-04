import players,scoreboard
import time
import pong
import turtle
points=scoreboard.score()
turtle.update()
turtle.tracer(0)
screen=turtle.Screen()
screen.setup(1000,800)
p=pong.pong()
base1=players.player1(480,0)
base2=players.player1(-480,0)
# player3=players.oogway(-50,-50)
# player4=players.oogway(50,-50)
# base1.teleport(480,-0)
# base2.teleport(-480,-0)
dots=turtle.Turtle()
dots.setheading(90)
dots.teleport(0,-400)
dots.pensize(5)
for i in range(800):
    dots.forward(10)
    dots.penup()
    dots.forward(10)
    dots.pendown()
turtle.listen()
turtle.onkey(base2.up,"w")
turtle.onkey(base2.dn,"s")
turtle.onkey(base1.up,"Up")
turtle.onkey(base1.dn,"Down")
# turtle.onkey(player3.up,"8")
# turtle.onkey(player3.dn,"2")
# turtle.onkey(player4.up,"6")
# turtle.onkey(player4.dn,"4")
points.updt()
i=0.07
game=True
while game:
    # print(base2.position())
    # print(p.position())
    screen.update()
    time.sleep(i)
    p.movement()
    if p.ycor()>380 or p.ycor()<-380:
        p.bouncey()
        # base1.loc()
        # print(base2.position())
        # player3.loc()
        # player4.loc()
        # p.movement()
        # game=False
    if p.xcor()>450 and base1.distance(p)<50 or p.xcor()<-450 and base2.distance(p)<50:
        p.bouncex()
        i-=0.0025

    if p.xcor()<-510:
        # or p.xcor()<-510:
        i=0.07
        points.s1increase()
        p.startpos()
        if points.s1==10:
            points.gameover()
            game=False
    if p.xcor()>510:
        i=0.07
        points.s2increase()
        p.startpos()
        if points.s2==10:
            points.gameover()
            game=False

screen.exitonclick()
