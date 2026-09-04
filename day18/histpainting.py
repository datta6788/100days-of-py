import colorgram
import random
# palette=colorgram.extract(r'D:\python course\100days-of-py\day18\SABCAP.jpg', 30)
# ####first_color=palette[0]
# ####rgb=first_color.rgb
# ####hsl=first_color.hsl
# ####proportion=first_color.proportion
# ####red=rgb[0:10]
# ####saturation=hsl[1]
# colorcodes=[]
# for i in range(30):
#     fc=palette[i]
#     c=fc.rgb
#     colorcodes.append(c[0:])
# print(colorcodes)

#OR#

# for i in palette:
#     colorcodes.append(i.rgb[0:])
# print(colorcodes)
# print(palette[0].proportion)

extracted_colors_5=[(115, 101, 82), (168, 144, 128), (24, 39, 48), (52, 47, 33), (85, 97, 88)]

extracted_colors_30=[(115, 101, 82), (168, 144, 128), (24, 39, 48), (52, 47, 33), (85, 97, 88), (74, 102, 121), (31, 39, 34), (142, 164, 182), (183, 206, 225), (139, 130, 108), (73, 67, 46), (176, 147, 153), (156, 116, 107), (125, 84, 90), (134, 146, 139), (53, 70, 61), (41, 63, 93), (120, 132, 126), (38, 73, 83), (109, 126, 152), (177, 189, 210), (162, 200, 217), (106, 135, 144), (151, 113, 120), (89, 53, 46), (41, 35, 40), (86, 52, 57), (231, 226, 211), (215, 180, 180), (177, 197, 196)]

extracted_colors_19=[(198, 157, 131), (192, 1, 28), (228, 213, 196), (143, 90, 62), (75, 32, 17), (182, 104, 86), (226, 181, 160), (111, 42, 29), (216, 190, 163), (171, 122, 80), (89, 5, 10), (189, 41, 52), (219, 63, 75), (193, 159, 162), (89, 60, 35), (22, 23, 29), (232, 165, 169), (19, 24, 22), (238, 188, 191)]

extracted_colors_34=[(7, 13, 19), (24, 32, 30), (42, 29, 16), (154, 94, 21), (220, 170, 72), (221, 147, 8), (216, 74, 130), (249, 200, 85), (54, 15, 23), (223, 123, 166), (166, 55, 96), (147, 18, 39), (231, 213, 189), (67, 91, 118), (154, 161, 157), (105, 65, 11), (235, 162, 195), (152, 161, 170), (233, 202, 216), (17, 61, 121), (91, 100, 96), (209, 212, 217), (222, 85, 52), (142, 20, 16), (207, 213, 210), (232, 172, 162), (98, 126, 167), (57, 67, 61), (50, 69, 74), (183, 189, 204), (120, 132, 125), (118, 132, 134), (187, 194, 192), (183, 194, 196)]

import turtle

oogway=turtle.Turtle()
# oogway.dot(10)
# oogway.penup()
# oogway.forward(100)
# oogway.dot(10)
# row_dots=10
# j=row_dots
# k=0
# l=50
# oogway.penup()
# oogway.pensize(10)
# for i in range(100):
#     oogway.dot()
#     # oogway.penup()
#     oogway.forward(50)
#     if i+1==j:
#         oogway.teleport(k,l)
#         j+=row_dots
#         k+=1
#         l+=50
# oogway.hideturtle()

turtle.colormode(255)

def colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

# oogway.setposition(-50,-50)
# oogway.setheading(225)
# oogway.forward(100)
# oogway.setheading(0)


def histpainting(no_of_dots,dots_in_row):
    # oogway.speed("fastest")
    oogway.hideturtle()
    j=dots_in_row
    k=0
    l=50
    oogway.penup()
    for i in range(no_of_dots):
        oogway.color(extracted_colors_19[i%len(extracted_colors_19)])
        oogway.dot(20)
        oogway.forward(50)
        if i+1==j:
            oogway.teleport(k,l)
            j+=dots_in_row
            k+=1
            l+=50

histpainting(100,10)

screen=turtle.Screen()
screen.exitonclick()