from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
#menu_item = MenuItem(name: )
"""
Coffee Machine
"""
is_on = True

while is_on:
    options = menu.get_items()
    order = input(f"What would you like to order? {options}: ")
    if order == "off":
        is_on = False
    elif order == "report":
         money_machine.report()
         coffee_maker.report()
    elif order =="latte" or order =="espresso" or order =="cappuccino":
        drink = menu.find_drink(order) 
        if coffee_maker.is_resource_sufficient(drink) is True:
            print("True if we have enough resources",coffee_maker.is_resource_sufficient(drink))
            print(drink)
            cost = drink.cost
            if money_machine.make_payment(cost) is True:
                print(f"Payment Sucess!!\nHere is your {order}")
        else:
            print("Resourse not suffficent")
    else:
        print("Invalid Input! Try Again")
