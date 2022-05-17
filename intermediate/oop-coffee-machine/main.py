from re import M
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menus = Menu()
money = MoneyMachine()
coffee_maker = CoffeeMaker()

end = False
while not end:
    options = menus.get_items()
    order = input(
        f"What coffe would you like to make? ({options}) : ")
    if order == "off":
        end = True
    elif order == "report":
        coffee_maker.report()
        money.report()
    else:
        drink = menus.find_drink(order)
        print(drink.cost)
        if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
