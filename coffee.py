def tran():
    coin = ['quarters', 'dimes', 'nickles', 'pennies']
    check = [float(input(f'How many{i}?')) for i in coin]
    return sum([i / 100 for i in [check[0] * 25, check[1] * 10, check[2] * 5, check[3]]])


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your  {drink_name}')


profit = 0


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change')
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough


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
}

is_on = True

Money = 0
# TODO: 1. Print report of  all coffee machine resources
while is_on:
    name = input("What would you like? (espresso/latte/cappuccino): ")
    if name == "off":
        is_on = False
    elif name == 'report':
        print(*[f'{i}:{resources[i]}' for i in resources], f'Money: ${payment}', sep='\n')
    else:
        drink = MENU[name]
        if is_resource_sufficient(drink['ingredients']):
            payment = tran()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(name, drink['ingredients'])
