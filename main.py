from req import MENU
from req import resources


#github test









def makine():
    makinestart=True
    while makinestart:
        choice = input('What would you like? (espresso/latte/cappuccino): ')

        if choice == "report":
            print(resources)
            continue

        if choice not in MENU:
            print("Invalid choice! Please choose from 'espresso', 'latte', 'cappuccino', or 'report'.")
            continue
        water = MENU[choice]["ingredients"].get("water", 0)
        milk = MENU[choice]["ingredients"].get("milk", 0)
        coffee = MENU[choice]["ingredients"].get("coffee", 0)
        if water > resources["water"]:
            print("there is not enough water")
            makinestart = False

        elif milk > resources["milk"]:
            print("there is not enough milk")
            makinestart = False

        elif coffee > resources["coffee"]:
            print("there is not enough coffe")
            makinestart = False

        else:
            print("please insert coins")
            cost = MENU[choice]["cost"]
            quarters = int(input("how many quarters?:")) * 0.25
            dimes = int(input("how many dimes?:")) * 0.10
            nickles = int(input("how many nickles?:")) * 0.05
            pennies = int(input("how many pennies?:")) * 0.01
            total = quarters + dimes + nickles + pennies
            paraüstü = total - cost
            if total - cost < 0:
                print("not enough money")
            else:
                print(f"change is {paraüstü}")
                resources["coffee"] -= coffee
                resources["milk"] -= milk
                resources["water"] -= water
                print(f"enjoy your {choice}")
makine()


