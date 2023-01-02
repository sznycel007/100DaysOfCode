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
    "Money $": 0,
}

COST = 0
MACHINEISON = True
IFRESOURCES = True


def whatToDo(userChoice):
    global MACHINEISON

    if userChoice == "report":

        print(f"Water: {resources['water']} ml")
        print(f"Milk:  {resources['milk']} ml")
        print(f"Coffee:{resources['coffee']} g")
        print(f"Money: {COST} $")

    elif userChoice == "off":
        MACHINEISON = False
        return MACHINEISON
    elif userChoice == "espresso":
        return checkResources("espresso")
    elif userChoice == "latte":
        return checkResources("latte")
    elif userChoice == "cappuccino":
        return checkResources("cappuccino")
    else:
        print("Wrong input")


def insertCoin():
    print("Please insert coins.")

    quarters = float(input("how many quarters:? ")) * 0.25
    dimes = float(input("how many dimes?: ")) * 0.10
    nickles = float(input("how many nickles?: ")) * 0.05
    pennies = float(input("how many pennies?: ")) * 0.01
    total = 0
    for i in quarters, dimes, nickles, pennies:
        total += i

    return total


def checkIfResources(kwargs):
    global IFRESOURCES
    IFRESOURCES = kwargs
    return IFRESOURCES


def checkResources(userChoice):
    global resources

    coffeeComponents = MENU[userChoice]["ingredients"]
    for ingredient in coffeeComponents:
        if (resources[ingredient] and coffeeComponents[ingredient]) and resources[ingredient] > 0 \
                and resources[ingredient] - coffeeComponents[ingredient] >= 0:
            resources[ingredient] -= coffeeComponents[ingredient]
            checkIfResources(True)
        else:
            checkIfResources(False)
            print(f"Sorry there is not enough {ingredient}")
            break
    return resources


def prepareCoffe(userChoice):
    global resources, COST, IFRESOURCES

    coffeeCost = MENU[userChoice]["cost"]
    usermoney = insertCoin()
    COST += coffeeCost

    if usermoney > coffeeCost:
        resources["Money $"] = COST
        print(f"Here is ${round(usermoney - coffeeCost, 2)} in change.")
        print(f"Here it's your ☕ {userChoice}. Enjoy! ")
    else:
        print("you don't have enough money")


while MACHINEISON:
    userChoice = input("What would you like? (espresso/latte/cappuccino): ")
    whatToDo(userChoice)

    if IFRESOURCES == True and userChoice != 'off' and userChoice != 'report':
        prepareCoffe(userChoice)
