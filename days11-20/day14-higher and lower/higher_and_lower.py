# steps:
# import game data and check if you can use data from it
# import art and random module
# generate random pick from game data (as a first choice)
# extract specific keys from dictionary
# prepare outputs
# create if/else block - A vs B (check if B is not A) - global scope
# compare data (followers)
# add point to score / end game
# create while loop around whole game

import random
import art
from game_data import data


def getRandomPick():
    return random.choice(data)


def formatdata(account):
    """format output strings"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


print(art.logo)

account_a = getRandomPick()
account_b = getRandomPick()
score = 0
endOfTheGame = False


while not endOfTheGame:
    A_followers = account_b["follower_count"]
    B_followers = account_b["follower_count"]

    print(f"score: {score}")
    print(f"Compare A:", formatdata(account_a))
    print(f"Against B:", formatdata(account_b))
    userChoice = input("Who has more followers on instagram? Type 'A' or 'B' ").upper()

    if userChoice == 'A' and A_followers > B_followers:
        print("that's correct!")
        score += 1
        account_b = getRandomPick()
    elif userChoice == 'B' and B_followers > A_followers:
        print("That's correct")
        account_a = account_b
        account_b = getRandomPick()
        score += 1
    elif A_followers == B_followers:
        print("It's draw - but lets continue")
        account_a = account_b
        account_b = getRandomPick()
        score += 1
    else:
        endOfTheGame = True
        print(f"Sorry, that was wrong. Your final score was {score}")
