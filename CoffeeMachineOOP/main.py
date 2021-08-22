from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cmaker = CoffeeMaker()
mmachine = MoneyMachine()
m = Menu()

while True:
    user_input = input("What would you like? (espresso/latte/cappuccino):")

    if user_input == "off":
        break

    if user_input == "report":
        cmaker.report()
        mmachine.report()

    else:
        for each in m.menu:
            if each.name == user_input:
                if cmaker.is_resource_sufficient(each):
                    cmaker.make_coffee(each)