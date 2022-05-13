from res import MENU, resources

# TODO 5 make report function which prints.
def report(money, w, m, c):
    print(f"Water = {w}\nMilk = {m}\nCoffee = {c}\nMoney = {money}")


# TODO 2 function to Check the resources, if enough go to the next step, if not tell its not enough.
def checkres(coffee, curr_water, curr_milk, curr_coffee):
    req_water = MENU[coffee]['ingredients']['water']
    if coffee != "espresso":
        req_milk = MENU[coffee]['ingredients']['milk']
    else:
        req_milk = 0
    req_coffee = MENU[coffee]['ingredients']['coffee']

    if curr_water < req_water:
        print("Sorry there's not enough water")
        return req_water, req_milk, req_coffee, False
    if curr_milk < req_milk :
        print("Sorry there's not enough milk")
        return req_water, req_milk, req_coffee, False
    if curr_coffee < req_coffee:
        print("Sorry there's not enough coffee")
        return req_water, req_milk, req_coffee, False
        
    # TODO 7 Remove recources needed then print drink served and repeat the function.

    return req_water, req_milk, req_coffee, True
    
# TODO 3 Print input the money, quarter, dime, nickle, penny.
def check_money(price, money):
    quarter = (0.25 * int(input("Insert quarter : ")))
    dime = (0.10 * int(input("Insert dime : ")))
    nickle = (0.05 * int(input("Insert nickle : ")))
    penny = (0.01 * int(input("Insert penny : ")))

    # TODO 4 Calculate the money then compare to the corresponding drink's price, if its NOT enough refund the money and repeat todo 1.
    total = round(quarter + dime + nickle + penny, 2)

    if total < price:
        print("Sorry that's not enough money, money refunded")
        return False
    # TODO 6 if the money is more than the drink's price subtract the money, add to the data, then return the change.
    elif total > price:
        money += money
        return total - price
    else:
        return 0


# TODO 1 Print output what user would like to drink.
def run():
    curr_water = resources['water']
    curr_milk = resources['milk']
    curr_coffee = resources['coffee']
    money = 0
    
    stop = False

    while not stop:
        report(money, curr_water, curr_milk, curr_coffee)
        drink = input("What coffe would you like to make? (espresso/latte/cappuccino) : ")
        if drink.lower() == "report":
            report(money, curr_water, curr_milk, curr_coffee)
            continue
        water, milk, coffee, res = checkres(drink.lower(), curr_water, curr_milk, curr_coffee)
        if res == False:
            continue
        change = int(check_money(MENU[drink.lower()]['cost'], money))
        if change > 0:
            print(f"Here's ${change} in change")
            curr_water -= water
            curr_milk -= milk
            curr_coffee -= coffee
        elif change == False:
            continue
        else:
            curr_water -= water
            curr_milk -= milk
            curr_coffee -= coffee
        if res == True:
            print(f"Here's your {drink}, enjoy!")

        status = input("Would you like another drink? 'y' or 'n' : ")
        if status.lower() == "n":
            print("Program Ended!")
            stop = True
    
run()
