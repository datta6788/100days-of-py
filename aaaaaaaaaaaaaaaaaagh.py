import menu
import money_machine
import coffee_maker

# menu_item=menu.MenuItem()
items=menu.Menu()
coffee=coffee_maker.CoffeeMaker()
price=money_machine.MoneyMachine( )
# print()
on=True
while on:
    user=input(f"WHAT WOULD YOU LIKE TO HAVE? {items.get_items()}:").lower()
    if user=="report":
        coffee.report()
        price.report()
    elif user=="off":
        on=False
    else:
        user_choice=items.find_drink(user)
        if print(coffee.is_resource_sufficient(user_choice)):
           print(price.make_payment(user_choice.cost)) 