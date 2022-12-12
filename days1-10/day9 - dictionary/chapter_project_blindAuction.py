from replit import clear
import art
print(art.logo)

bidding_finished = False
auction = {}
binders = {}
saves = []


def save_binding(name, bid):
    auction = {
        name: bid
    }
    binders.update(auction)


while not bidding_finished:

    print("Welcome to the secret auction program!")
    name = input("What is your name? ")
    bid = int(input("What's your bid?: $"))
    AnyOthers = input("Are there any others bidders? Type 'yes' or 'no': ")

    if AnyOthers == 'yes':
        clear()
        save_binding(name, bid)
    else:
        save_binding(name, bid)
        bidding_finished = True
        break

# write provided values to the array
for bid in binders:
    # print(bid, binders[bid])
    saves.append(binders[bid])

# save the highest value from saves to maxBid variable
maxBid = max(saves)

# print key (name) from dictionary that is equal to maxBid
for name, bind in binders.items():
    if bind == maxBid:
        print(f"The winner is {name} with a bid of ${maxBid}")
