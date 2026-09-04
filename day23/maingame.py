import turtle,turtle_player
import time
import cars,score
scoreboard=score.scoreboard()
screen=turtle.Screen()
screen.setup(1000,1000)
screen.tracer(0)
oogway=turtle_player.OOGWAY()
turtle.listen()
turtle.onkey(oogway.move_fwd,"w")
turtle.onkey(oogway.move_bwd,"s")
game=True
lmq=cars.CARS()
# print(lmq.all_cars[0].pos())
while game:
    time.sleep(0.1)
    screen.update()
    lmq.car_move()
    for car in lmq.all_cars:
        if car.distance(oogway)<21:
            scoreboard.game_over()
            game=False

    if oogway.ycor()>480:
        scoreboard.level_up()
        oogway.teleport(0,-480)
        cars.car_speed+=5
        lmq.gen_car()
        print(cars.car_speed)



    # lmq.car_loop()
    # if lmq.all_cars[0].pos()<(0,0):
    #     print("yes")
    #     break




screen.exitonclick()