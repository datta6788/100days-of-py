import turtle
import random
# oogway=turtle.Turtle()
# oogway.shape("turtle")
screen=turtle.Screen()
# oogway2=turtle.Turtle()
# oogway2.shape("turtle")
# oogway3=turtle.Turtle("turtle")
# oogway4=turtle.Turtle("turtle")
# def fd():
#     oogway.color("red")
#     oogway.forward(10)

# def bd():
#     oogway.color("orange")
#     oogway.back(10)

# def right():
#     oogway.color("blue")
#     oogway.right(10)

# def left():
#     oogway.color("pink")
#     oogway.left(10)

# def clear():
#     oogway.clear()
#     oogway.reset()

# turtle.onkey(key="w",fun=fd)

# turtle.onkey(key="s",fun=bd)

# turtle.onkey(key="d",fun=right)

# turtle.onkey(key="a",fun=left)

# turtle.onkey(key="c",fun=clear)
# turtle.listen()
# oogway.penup(),oogway2.penup(),oogway3.penup(),oogway4.penup()
# screen.setup(1000,1000)
# oogway.goto(x=-450,y=0)
# oogway2.goto(x=-450,y=50)
# oogway3.goto(x=-450,y=-50)
# oogway4.goto(x=-450,y=-100)

ypos=[0,50,100,-50,-100]
turtles=[]
# def movement():

dialogbox=turtle.textinput("T1","WHO's GONNA WIN THE RACE?(red/yellow/blue/green/purple)").lower()
colors=["red","yellow","blue","green","purple"]

for i in range(5):
    shell=turtle.Turtle("turtle")
    shell.color(colors[i])
    shell.penup()
    shell.goto(x=-450,y=ypos[i])
    turtles.append(shell)
game=True

while game:
    for i in turtles:    
        i.forward(random.randint(0,10))
# for i in turtles:    
# i.forward(random.randint(0,10)) 
        if i.xcor()>470:
            game=False
            if dialogbox==i.pencolor():
                print("YOU WON THE BET!")
            else:
                print("FAHHHHHHHHHH")
            # screen.bye()

for i in range(5):
    turtles[i].forward(random.randint(0,10))



# screen.exitonclick()
