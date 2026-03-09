#JUST A LIL CATCH IN THE PROGRAM
from day14data import data
import random

def celeb(a,b):
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

def game():
    d=random.randint(0,49)
    b=data[d]
    score=0
    # print("")
    play=True
    while play:
        d=random.randint(0,49)
        a=b
        b=data[d]
        print(f"Current score!: {score}")
        celeb(a,b)
        fam=input("Who's got more followers on insta? A or B? ").upper()
        print('\n'*20)
        if fam=='A':
            if a['follower_count']>b['follower_count']:
                score+=1
                # print(score)
            else:
                print(f"You guessed it wrong! Final score is {score}")
                play=False
        elif fam=="B":
            if b['follower_count']>a['follower_count']:
                score+=1
            else:    
                print(f'You guessed it wrong! Final score is {score}')
                play=False

game()