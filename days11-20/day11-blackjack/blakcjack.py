import art
import random
from replit import clear

# rules:
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def getAnotherPick(player):
    pick = random.choice(cards)
    player.append(pick)
    return player


def collectInitialDeck(player):
    for i in range(0, 2):
        pick = random.choice(cards)
        player.append(pick)
        return player


def isblackjack():
    if sum(player2) == 21 or (sum(player1) == 21 and sum(player2) == 21):
        print("PC win with a Blackjack! ")
        return True
    elif sum(player1) == 21:
        print("User win with a Blackjack! ")
        return True
    elif sum(player1) > 21:
        print("You went over. You lose!")
        return True
    elif sum(player1) < 21:
        return False


gamestart = True

while gamestart:
    playerDeck = []
    pcDeck = []

    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == "n":
        gamestart = False
    else:
        clear()
        print(art.logo)
        collectInitialDeck(player=playerDeck)
        player1 = collectInitialDeck(playerDeck)

        collectInitialDeck(player=pcDeck)
        player2 = collectInitialDeck(pcDeck)

        isBlackJackLoop = False

        while isBlackJackLoop is False:

            if player1[0] == 11 and player1[1] == 11:
                player1[1] = 1

            if player2[0] == 11 and player2[1] == 11:
                player2[1] = 1

            isBlackJackLoop = isblackjack()

            if not isBlackJackLoop:

                userScore = sum(player1)
                pcScore = sum(player2)

                print(f"\tYour cards: {player1}, current score: {userScore} ")
                print(f"\tComputer's first card: {player2[0]}")
                anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")

                if anotherCard == "y":
                    getAnotherPick(player1)
                else:
                    while pcScore < 16:
                        getAnotherPick(player2)
                        break

                    print(f"Your final hand: {player1}, final score: {userScore}")
                    print(f"Computer's final hand: {player2}, final score {pcScore}")

                    if userScore < 21 and (userScore > pcScore):
                        print("You were closer to BlackJack - you win!")
                    elif pcScore < 21 and (pcScore > userScore):
                        print("PC were closer to BlackJack - you lose!")
                    elif userScore == userScore:
                        print("It's a draw but you lose!")
                    break
            else:
                print(f"Your final hand: {player1}, final score: {userScore}")
                print(f"Computer's final hand: {player2}, final score {pcScore}")

end = 'END GAME'
print(f'{end:.^20}')
