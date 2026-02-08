import random
import hangman_words as hw
import hangman_art as ha
print(ha.logo)
dash=""
lives=len(ha.stages)-1
comp_choice=random.choice(hw.word_list)
print(comp_choice)
for d in comp_choice:
    dash+="_"
print(dash)
length=len(comp_choice)
show=""
display=''
correct=[]
for word in comp_choice:
    display+=word
while display!=show:
    showing=""
    user=input("guess a letter:")
    if user in correct:
        print(f"YOU HAVE ALREADY GUESSED THE LETTER {user}")    
    for index in range(length):
        if display[index]==user:
            showing+=user
            correct.append(user)
        elif display[index] in correct:
            showing+=display[index]
        else:
            showing+="_"
    print(showing)
    if showing==display:
        display=show
        print(ha.stages[lives],f"\nYOU WIN!")
    elif user not in display:
        lives-=1
        print(f"THE LETTER YOU HAVE GUESSED {user} IS NOT IN THE WORD!, YOU LOSE A LIFE") 
        if lives==0:
            display=show
            print(ha.stages[lives],f"\nYOU LOST, THE WORD WAS {comp_choice}!")
        else:
            print(ha.stages[lives],f"\nyou have {lives} lives remaining")
    else:
        print(ha.stages[lives],f"\nyou have {lives} lives remaining")
