import turtle
import random
car_colors=["violet","indigo","blue","green","yellow","orange","red"]
car_speed=15
class CARS():
    def __init__(self):
        self.all_cars=[]
        self.gen_car()
        # self.is_off_screen()

    def gen_car(self):
        for _ in range(100):
            limcq=turtle.Turtle("square")
            limcq.color(random.choice(car_colors))
            limcq.setheading(180)
            limcq.shapesize(stretch_wid=1,stretch_len=2)
            limcq.penup()
            limcq.teleport(random.randint(520,5000),random.randint(-450,480))
            self.all_cars.append(limcq)

    def car_move(self):
        for cars in self.all_cars:
            cars.forward(car_speed)


    # def is_off_screen(self):
    #     if self.xcor()<-520:
    #         self.destroy()
    # def car_loop(self):
    #     for i in range(len(self.all_cars)):
    #         if self.all_cars[i].pos()<(-480,0):
    #             for i in self.all_cars:
    #                 i.teleport(random.randint(520,5000),random.randint(-480,480))

    # def moving(self):
    #     for cars in self.all_cars:
    #         cars.forward(1)