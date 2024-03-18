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
#github test vol2

def check_resources(choice):
    water = MENU[choice]["ingredients"].get("water", 0)
    milk = MENU[choice]["ingredients"].get("milk", 0)
    coffee = MENU[choice]["ingredients"].get("coffee", 0)

    if water > resources["water"]:
        return "water"
    elif milk > resources["milk"]:
        return "milk"
    elif coffee > resources["coffee"]:
        return "coffee"
    else:
        return "enough"


def process_payment(cost):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    change = total - cost
    return change


def make_coffee(choice):
    water = MENU[choice]["ingredients"]["water"]
    milk = MENU[choice]["ingredients"].get("milk", 0)
    coffee = MENU[choice]["ingredients"]["coffee"]
    cost = MENU[choice]["cost"]

    resource_check = check_resources(choice)
    if resource_check != "enough":
        print(f"There is not enough {resource_check}.")
        return False

    change = process_payment(cost)
    if change < 0:
        print("Not enough money. Money refunded.")
        return False

    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee
    print(f"Change is {change:.2f}. Enjoy your {choice}!")
    return True


def main():
    while True:
        choice = input('What would you like? (espresso/latte/cappuccino): ')

        if choice == "report":
            print(resources)
        elif choice in MENU:
            if make_coffee(choice):
                break
        else:
            print("Invalid choice! Please choose from 'espresso', 'latte', 'cappuccino', or 'report'.")


main()
