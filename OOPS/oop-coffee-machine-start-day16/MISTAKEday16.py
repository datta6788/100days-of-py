# from turtle import * 
# turtle=Turtle()
# turtle.shape("turtle ")
# turtle.color("pink")
# turtle.forward(69)
# turtle.right(25)
# turtle.left(90)
# # turtle.forward(69)
# # turtle.backward(69)
# # turtle.forward(69)
# # turtle.backward(69)
# # turtle.forward(69)
# # turtle.backward(69)
# # turtle.forward(69)
# # turtle.backward(69)
# my_s=Screen()
# # print(my_s.canvheight)
# my_s.exitonclick()

# from prettytable import PrettyTable
# table=PrettyTable()
# table.add_column("STUDENT NAME",["Datta","Kuber","Keerthi","Vardhan","Krish","Deekshith"])
# table.add_column("COLLEGE NAME",["SVIT","SVIT","SVIT","SVIT","SVIT","Methodist"])
# # table.align='l'
# # table.valign='m' 
# print(table)
#################################################################################################
#################################################################################################
#################################################################################################
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import menu,money_machine,coffee_maker
coffeemaker=coffee_maker.CoffeeMaker()
coffeemenu=menu.Menu()
money=money_machine.MoneyMachine()
run=True
while run:
    user_input=input("What would you like? (espresso/latte/cappuccino/):").lower()
    if user_input=="report":
        coffeemaker.report()
        money.report()
    elif user_input=="off":
        run=False
    else:
        user_choice=coffeemenu.find_drink(user_input)
        if user_choice:
            if coffeemaker.is_resource_sufficient(user_choice):
                if money.make_payment(user_choice.cost):
                    coffeemaker.make_coffee(user_choice)












