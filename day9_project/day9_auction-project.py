# Exercice Project : Blind auction program

# from replit import clear
# used to clear the screen in replit

# Solo attempt
from day9_auction_art import logo

print(logo)
print("Welcome to the blind auction program")

def add_new_bid(name, bid):
    new_bid = {
        "name": user_name,
        "bid": user_bid,
    }
    bid_list.append(new_bid)

def find_highest_bid(list):
    highest_bidder = ""
    highest_bid = 0
    for bidder in list:
        bidder_name = bidder["name"]
        bid = bidder["bid"]
        if bid > highest_bid:
            highest_bidder = bidder_name
            highest_bid = bid
    print(f"The winner is {highest_bidder} with a bid of €{highest_bid}.")


bid_list = []

auction_continue = True
while auction_continue:
    user_name = input("What is your name ? ")
    user_bid = float(input("What is your bid ? €"))
    
    add_new_bid(user_name, user_bid)

    other_bid = ""
    while other_bid != "no" and other_bid != "yes": # to ask for a new input in case of a wrong input
        other_bid = input("Are there any other bidders ? Type 'yes' or 'no': ")
        if other_bid == "yes":
            #clear()
            print("Screen cleared")
        elif other_bid == "no":
            auction_continue = False
        else:
           print("Wrong input.")

find_highest_bid(bid_list)