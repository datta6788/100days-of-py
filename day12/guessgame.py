import random
print("Welcome to the Number Guessing Game!\n"
"I'm thinking of a number between 1 and 100. ")
difficulty=(input("Choose a difficulty. Type 'easy' or 'hard':"))
def dif_type(difficulty):
    if difficulty=='easy':
        return 10
    else:
        return 5
number=random.randint(1,100)
def user():
    print(number)
    # print(lives)
    game=True
    lives=dif_type(difficulty)
    while game:
        user_choice=int(input("guess:"))
        if user_choice==number:
            print('you guessed it correctly')
            game=False
        elif user_choice<number:
            lives-=1
            if lives==0:
                print("You ran out of chances to guess, you lost the game!")
                game=False
            else:
                print("Too low, guess again!")
                print(f'you have {lives} chances left')
        else:
            lives-=1
            if lives==0:
                print("You ran out of chances to guess, you lost the game")
                game=False
            else:
                print("Too high, guess again!")
                print(f'you have {lives} chances left')
user()
