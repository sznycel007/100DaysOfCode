import random
import art

print(art.logo)

# the player's possible attempts depend on the level of play
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

randomNumber = random.choice(range(1, 101))
print(f"Psst, the correct answer is {randomNumber}")

level = input("Choose a difficulty. Type 'easy or 'hard': ")


def gamelevel(difficulty):
    if difficulty == "easy":
        print(f"You have 10 attempts remaining to guess the number.")
        return 10
    elif difficulty == "hard":
        print(f"You have 5 attempts remaining to guess the number.")
        return 5


gamelives = gamelevel(level)


while gamelives != 0:
    userGuess = int(input("Make a guess: "))

    if userGuess > randomNumber:
        print("Too high")
    elif userGuess < randomNumber:
        print("Too low")
    elif gamelives == 0:
        print("You've run out of guesses, you lose.")
    elif userGuess == randomNumber:
        print(f"You got it! The answer was {randomNumber}")
        break

    gamelives += -1
    if gamelives > 0:
        print("Guess again")
        print(f"You have {gamelives} attempts remaining to guess the number.")

else:
    print("You've run out of guesses, you lose.")
