import random
def bj():
    my_cards=random.choices(cards,k=2)
    comp_cards=random.choices(cards)
    score=sum(my_cards)
    comp_score=sum(comp_cards)
    print(f'Your cards:{my_cards}, Your current score:{score}')
    print(f"Computer's first card:{comp_cards}")
    game=True
    while game:
        if my_cards==[11,10] or my_cards==[10,11]:
            print("You scored BLACKJACK!, you win!")
            game=False
        else:
            another_card=input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card=='y':
                new_card=random.choice(cards)
                my_cards.append(new_card)
                score+=new_card
                print(f'Your cards:{my_cards}, Your current score:{score}')
                print(f"Computer's first card:{comp_cards}")
                if score>21:
                    print("You went over, you lose!")
                    new_match=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
                    if new_match=='y':
                        bj()
                    else:
                        break
            else:
                comp=True
                while comp:
                    if comp_score<17:
                        new_comp_card=random.choice(cards)
                        comp_cards.append(new_comp_card)
                        comp_score+=new_comp_card
                        if comp_cards==[11,10] or comp_cards==[10,11]:
                            print(f"Your final hand:{my_cards}, final score:{score}")
                            print(f"Computer's final hand:{comp_cards}, final score:{comp_score}")
                            print("Computer scored BLACKJACK!, you lost!")
                            comp=False
                            game=False       
                    else:
                        if comp_score>score and comp_score<=21:
                            print(f"Your final hand:{my_cards}, final score:{score}")
                            print(f"Computer's final hand:{comp_cards}, final score:{comp_score}")
                            print("You lose")
                            comp=False
                            game=False                      
                        elif comp_score>21:
                            print(f"Your final hand:{my_cards}, final score:{score}")
                            print(f"Computer's final hand:{comp_cards}, final score:{comp_score}")
                            print("Dealer went over, you win!")
                            comp=False
                            game=False                       
                        elif comp_score==score:
                            print(f"Your final hand:{my_cards}, final score:{score}")
                            print(f"Computer's final hand:{comp_cards}, final score:{comp_score}")
                            print("It's a draw!")
                            comp=False
                            game=False
                        elif comp_score<score:
                            print(f"Your final hand:{my_cards}, final score:{score}")
                            print(f"Computer's final hand:{comp_cards}, final score:{comp_score}")
                            print("You win!")
                            comp=False
                            game=False
blackjack=True
while blackjack:
    cards=[11,10]
    wanna_play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if wanna_play=='y':
        bj()
    else:
        blackjack=False

