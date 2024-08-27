from menu import MENU, resources
import sys

profit = 0


def is_sufficient(elements):
    """Return True when there is sufficient ingredients, or False"""
    for item in elements:
        is_enough = True
        if elements[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
        # elif resources[item] == 0:
        #     print("Machine is out of resources")
        #     sys.exit()
        return is_enough


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted , or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is Rs{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name , order_ingredients):
    """Reduce the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? expresso/latte/cappuccino:\n")
    if choice == "Off".lower():
        is_on = False
    elif choice == "report":
        print(f"Water:{resources['Water']}ml")
        print(f"Milk:{resources['Milk']}ml")
        print(f"Coffee:{resources['Coffee']}gm")
        print("\n")
        print(f"profit:{profit}Rs")
    else:
        drink = MENU[choice]
        # hkl= drink["ingredient"]
        # print(hkl)
        # print(drink)
        if is_sufficient(drink["ingredient"]):
            payment = int(input("Please insert Money.\nRs"))
            if is_transaction_successful(payment, drink["Cost"]):
                make_coffee(choice, drink["ingredient"])
