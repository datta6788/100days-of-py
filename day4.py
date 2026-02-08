import random
# a= ["datta","kuber","deekshith","vinay"]
# b=random.choice(a)
# print(b)

# a="datta"
# b="kuber"
# c="vinay"
# d=[a,b,c]
# e=random.randint(0,1)
# print(d[e])
# print(e)
# # print(random.choice(d))
##########ROCK PAPER SCISSOR############
a="rock"
b="paper"
c="scissor"
d=[a,b,c]
yourchoice=int(input("what do you choose?\n 0->rock\n 1->paper\n 2-scissors\n"))
if yourchoice==0:
    print(a)
elif yourchoice==1:
    print(b)
elif yourchoice==2:
    print(c)
    compchoice=random.randint(0,2)
    print(d[compchoice])
    if compchoice==yourchoice:
        print("its a tie")
    elif yourchoice==0:
        if compchoice==1:
            print("you loose")
        elif compchoice==2:
            print("you win")
    elif yourchoice==1:
        if compchoice==0:
            print("you win")
        elif compchoice==2:
            print("you loose")
    elif yourchoice==2:
        if compchoice==1:
            print("you win")
        else:
            print("you loose")
else:
    print("Invalid input")



