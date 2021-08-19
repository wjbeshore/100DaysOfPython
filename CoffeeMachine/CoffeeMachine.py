MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0.0
}


def get_payment():
    total_pay = 0.0
    total_pay += float(input("How many pennies do you have?:")) * 0.01
    total_pay += float(input("How many nickels do you have?:")) * 0.05
    total_pay += float(input("How many dimes do you have?:")) * 0.1
    total_pay += float(input("How many quarters do you have?:")) * 0.25
    return total_pay


def make_order(n):
    if n == "espresso":
        check_resources(n)
        update_resources(n)
    elif n == "latte":
        check_resources(n)
        update_resources(n)
    elif n == "cappuccino":
        check_resources(n)
        update_resources(n)
    else:
        new_order = input("Could you please repeat that?:")
        make_order(new_order)


def update_resources(drink):
    for each in MENU[drink]["ingredients"]:
        resources[each] -= MENU[drink]["ingredients"][each]
    resources["Money"] += MENU[drink]["cost"]
    print("Your change is: " + str(payment - MENU[drink]["cost"]))


def check_resources(ordered):
    if payment < MENU[ordered]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return

    for each in MENU[ordered]["ingredients"]:
        if resources[each] < MENU[ordered]["ingredients"][each]:
            print("Sorry there is not enough " + each + ".")
            return


order = input("What would you like? (espresso/latte/cappuccino):")
payment = get_payment()
make_order(order)
