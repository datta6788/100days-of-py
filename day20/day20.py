import random
import turtle
import time
import snake, food
import scoreboard
score=scoreboard.score()

# # print(random.randint(0,10))
# oogway=turtle.Turtle("square")
# oogway.shapesize(1,1)
# oogway.penup()
# oogway2=turtle.Turtle("square")
# oogway2.shapesize(1,1)
# oogway2.penup(),
# oogway2.goto(-20,0)
# oogway3=turtle.Turtle("square")
# oogway3.shapesize(1,1)
# oogway3.penup()
# oogway3.goto(-40,0)
# turtle.listen()

# def ri():
#     oogway.right(90)
# def le():
#     oogway.left(90)

# turtle.onkey(ri,"d")
# turtle.onkey(le,"a")

# move= True
# while move:
#     oogway.forward(10)
#     oogway2.forward(10)
#     oogway3.forward(10)

screen=turtle.Screen()
# screen.screensize(500,500)
# screen.tracer(0)
# oogway=turtle.Turtle("square")
# oogway.shapesize(1,1)
# oogway.penup()
# oogway2=turtle.Turtle("square")
# oogway2.shapesize(1,1)
# oogway2.penup(),
# oogway2.goto(-20,0)
# oogway3=turtle.Turtle("square")
# oogway3.shapesize(1,1)
# oogway3.penup()
# oogway3.goto(-40,0)
turtle.listen()
# screen.update()

# move= True
# while move:
#     screen.update()

#     # time.sleep()
#     oogway3.goto(oogway2.position())
#     # oogway.left(90)
#     oogway2.goto(oogway.position())
#     oogway.forward(10)
    
# screen.update()

# coordinates=[(0,0),(-20,0),(-40,0)]
# turtles=[]
# screen.tracer(0)
# for coor in coordinates:
#     oogway=turtle.Turtle("square")
#     oogway.penup()
#     oogway.goto(coor)
#     turtles.append(oogway)

# def ri():
#     turtles[0].right(90)
# def le():
#     turtles[0].left(90)

# turtle.onkey(ri,"d")
# turtle.onkey(le,"a")
# turtle.onkey(ri,"Right")
# turtle.onkey(le,"Left")

# dot=turtle.Turtle()
# dot.hideturtle()
# dot.teleport(100,100)
# dot.dot(10,"red")

# game=True
# while game:
#     screen.update()
#     time.sleep(0.1)
#     for i in range(len(turtles)-1,0,-1):
#         xpos=turtles[i-1].xcor()
#         ypos=turtles[i-1].ycor()
#         turtles[i].goto(xpos,ypos)
#     turtles[0].forward(20)

    # if turtles[0].distance(dot)<5:
    #     print("YES YES YES")
    #     game=False
# turtle.tracer(0)
turtle.tracer(0)
arboc=snake.Snake()
food_dot=food.Food()
game=True
turtle.listen()
screen.onkey(arboc.rk,"d")
screen.onkey(arboc.lk,"a")
screen.onkey(arboc.uk,"w")
screen.onkey(arboc.dk,"s")
while game:
    turtle.update()
    time.sleep(0.1)
    arboc.snake_movement()
    if arboc.oogways[0].distance(food_dot)<15:
        food_dot.food_teleport()
        score.increase_score()
        arboc.tail()
    if arboc.oogways[0].xcor()>470 or arboc.oogways[0].xcor()<-480 or arboc.oogways[0].ycor()>400 or arboc.oogways[0].ycor()<-400:
        print("FAHHHHH")
        score.gameover()
        game=False
    for pos in arboc.oogways[1:]:
        if arboc.oogways[0].distance(pos)<10:
            score.gameover()
            game=False
    
    # for pos in arboc.oogways:
    #     if pos==arboc.oogways[0]:
    #         pass
    #     elif arboc.oogways[0].distance(pos)<10:    
    #         game=False
screen.exitonclick()


