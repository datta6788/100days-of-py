import turtle
import random
import colorgram
# oogway=turtle.Turtle()

# oogway.shape("turtle")

# for i in range(4):
#     oogway.forward(100)
#     oogway.left(90)

# for i in range(10):
#     oogway.pencolor("black")
#     oogway.forward(10)
#     oogway.pencolor("white")
#     oogway.forward(10)
# for i in range(40):
#     oogway.forward(10)
#     oogway.penup()
#     oogway.forward(10)
#     oogway.pendown()

# for i in range(3):
#     oogway.forward(100)
#     oogway.left(120)
#     oogway.forward(100)

#######################################################

# oogway.forward(100)
# oogway.left(120)    
# oogway.forward(100)
# oogway.left(120)
# oogway.forward(100)
# oogway.left(120)
# oogway.forward(100)
# oogway.left(90)
# oogway.forward(100)
# oogway.left(90)
# oogway.forward(100)
# oogway.left(90)
# oogway.forward(100)
# oogway.left(90)
# oogway.forward(100)

################################################################

# for i in range(3):
#     oogway.color("red")
#     oogway.forward(100)
#     oogway.left(120)

# for i in range(4):
#     oogway.color("green")
#     oogway.forward(100)
#     oogway.left(90)

# for i in range(5):
#     oogway.color("black")
#     oogway.forward(100)
#     oogway.left(72) 

# for i in range(6):
#     oogway.color("orange")
#     oogway.forward(100)
#     oogway.left(60)

# for i in range(7):
#     oogway.color("yellow")
#     oogway.forward(100)
#     oogway.left(51.43)

# for i in range(8):
#     oogway.color("blue")
#     oogway.forward(100)
#     oogway.left(45)

# for i in range(9):
#     oogway.color("pink")
#     oogway.forward(100)
#     oogway.left(40)

# for i in range(10):
#     oogway.color("purple")
#     oogway.forward(100)
#     oogway.left(36)
# oogway.forward(100)

############################################################################

colors=["red","orange","yellow","green","blue","indigo","violet"]
# def shapes(sides):
#     angle=360/sides
#     oogway.color(random.choice(colors))
#     for i in range(sides):
#         oogway.forward(100)
#         oogway.right(angle)
# for i in range(3,11):
#     shapes(i)

############################################################

# oogway.shape("circle")
# turtle.colormode(255)
# def colors():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     rgb=(r,g,b)
#     return rgb        
# movements=[0,90,180,270,360]
# oogway.pensize(15)

# for i in range(100):
#     oogway.color(colors())
#     oogway.forward(50)
#     oogway.setheading(random.choice(movements))
#     oogway.speed(10)

# oogway.teleport(100,500)

# oogway.circle(50)
# oogway.right(360)
# oogway.circle(50)
# oogway.speed("fastest")

# turtle.colormode(255)

# def cc():
#     red=random.randint(0,255)
#     blue=random.randint(0,255)
#     green=random.randint(0,255)
#     return (red,blue,green)        

# angle2=5
# for i in range(360//angle2):
#     oogway.color(cc())
#     oogway.circle(100)
#     oogway.right(angle2)

# def circles(angle):
#     for i in range(360//angle):
#         oogway.color(cc())
#         oogway.circle(100)
#         oogway.right(angle)
# circles(5)

########################################################

palette=colorgram.extract(r'D:\python course\100days-of-py\day18\rangers.jpg', 35)
# ####first_color=palette[0]
# ####rgb=first_color.rgb
# ####hsl=first_color.hsl
# ####proportion=first_color.proportion
# ####red=rgb[0:10]
# ####saturation=hsl[1]
colorcodes=[]
for i in range(34):
    fc=palette[i]
    c=fc.rgb
    colorcodes.append(c[0:])
print(colorcodes)

# print(len(palette))

extracted_colors_5=[(115, 101, 82), (168, 144, 128), (24, 39, 48), (52, 47, 33), (85, 97, 88)]

extracted_colors_30=[(115, 101, 82), (168, 144, 128), (24, 39, 48), (52, 47, 33), (85, 97, 88), (74, 102, 121), (31, 39, 34), (142, 164, 182), (183, 206, 225), (139, 130, 108), (73, 67, 46), (176, 147, 153), (156, 116, 107), (125, 84, 90), (134, 146, 139), (53, 70, 61), (41, 63, 93), (120, 132, 126), (38, 73, 83), (109, 126, 152), (177, 189, 210), (162, 200, 217), (106, 135, 144), (151, 113, 120), (89, 53, 46), (41, 35, 40), (86, 52, 57), (231, 226, 211), (215, 180, 180), (177, 197, 196)]

#OR#
# for i in palette:
#     colorcodes.append(i.rgb[0:])
# print(colorcodes)
# print(palette[0].proportion)

# oogway.dot(100,"blue")

##########################################################
# screen=turtle.Screen()
# screen.exitonclick()