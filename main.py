from art import logo

print(logo)
print("Welcome to the silent auction!")

bids = {}

def calc_highest_bid(bids):
    highest_amount = 0
    highest_bidder = ""

    for bidder in bids:
        if bids[bidder] > highest_amount: #if the amount offered is greater than the highest amount, the latter becomes the former
            highest_amount = bids[bidder]
            highest_bidder = bidder
    print(f"{highest_bidder} won with a bid of ${highest_amount}!")

quitting = False
while(not quitting):
    name = input("What's your name?: ")
    offer = int(input("What's your bid?: $"))
    bids[name] = offer

    exit = input("Is there another bidder? Type yes/no: ").lower()
    if exit == 'no':
        print("\033[H\033[J") # clears the screen, same in ln 31.
        print(logo)
        calc_highest_bid(bids)
        quitting = True
    else:
        print("\033[H\033[J")
    
