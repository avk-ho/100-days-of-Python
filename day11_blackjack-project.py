# https://www.udemy.com/course/100-days-of-code/learn/lecture/19658862#overview

# Day 11 - Blackjack game

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Solo attempt

# If the player score is above 21, they lose ("bust")
# If the score of the dealer is < 17, they must take another card
# If in the end, the player and dealer have the same score, it's a draw
# Ace is counted as 11 below 21, or 1 if the count ends up above 21

# The player is given 2 cards
# The dealer has one card visible, another hidden to the player
# The player can ask to be given another card, or can stand (stop with their current score)
# The dealer reveal their second card, if score < 17, they must take another card, hidden unless the player did stand
# Repeat 2 previous phases

import random

def blackjack():

    def add_card(dict, nb):
        # Adds nb of cards to dict, and updates the status of dict
        hand = dict["cards"]
        hand.extend(random.choices(cards, k=nb))
        score = sum(hand)
        dict["score"] = score
        if score == 21:
            dict["blackjack"] = True

    def swap_ace(dict):
        # Swaps an Ace value of 11 to a 1 and updates the status of dict
        hand = dict["cards"]
        ace_index = hand.index(11) # After correction, not necessary, could be remplaced with a .remove(11)
        hand[ace_index] = 1  # then an .append(1)
        score = sum(hand)
        dict["score"] = score
        if score == 21:
            dict["blackjack"] = True

    def end_game(dict):
        # Checks whether the game continues or an end state is reached
        hand = dict["cards"]

        while True:
            score = dict["score"]
            if score > 21:
                contain_ace = False
                if 11 in hand:
                    contain_ace = True

                if contain_ace:
                    swap_ace(dict)
                else:
                    return True
            elif score == 21:
                return True
            else:
                return False

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    player = {
        "cards": [],
        "score": 0,
        "blackjack": False,
    }

    dealer = {
        "cards": [],
        "score": 0,
        "blackjack": False,
    }

    add_card(player, 2)
    add_card(dealer, 2)

    game_over = False  
    while not game_over:
        dealer_cards_copy = dealer["cards"].copy()
        dealer_cards_copy.pop()
        print(f"This is your hand: {player['cards']}")
        print(f"This is the dealer's hand: {dealer_cards_copy}")

        game_over = end_game(player) or end_game(dealer)
        if game_over:
            if player["score"] > 21:
                print("Your score is above 21. You lose.")
                return
            elif player["blackjack"] and dealer["blackjack"]:
                print(f"This is the dealer's hand: {dealer['cards']}")
                print("It's a draw.")
                return
            elif player["blackjack"]:
                # Some clarifications may be needed, can the dealer try to get a blackjack as well ?
                # if so, the code here should instead jump to the if player_stood part
                print(f"This is the dealer's hand: {dealer['cards']}")
                print("You win.")
                return
            elif dealer["blackjack"]:
                print(f"This is the dealer's hand: {dealer['cards']}")
                print("You lose.")
                return

        input_check = True
        player_stood = False
        while input_check:
            draw_more_input = input(
                "Type 'y' if you want to draw 1 more card, else type 'n' to stop with your current hand: ")
            if draw_more_input == "y":
                # Will loop back to the beginning until an end state or the player chooses to stand
                add_card(player, 1)
                end_game(player)
                input_check = False
            elif draw_more_input == "n":
                player_stood = True
                input_check = False
            else:
                print("Wrong input.")

        # Only active if the player decide to stand, passing the turn to the dealer
        if player_stood:
            while dealer["score"] < 17:
                add_card(dealer, 1)
                print(f"This is the dealer's hand: {dealer['cards']}")
                game_over = end_game(player) or end_game(dealer)
                if game_over:
                    if dealer["score"] > 21:
                        print("The dealer score is above 21. You win.")
                        return
                    elif dealer["blackjack"]:
                        print("You lose.")
                        return

            # Final score check
            game_over = True
            if player["score"] == dealer["score"]:
                print(f"This is your hand: {player['cards']}")
                print(f"This is the dealer's hand: {dealer['cards']}")
                print("It's a draw.")
                return
            elif player["score"] > dealer["score"]:
                print(f"This is your hand: {player['cards']}")
                print(f"This is the dealer's hand: {dealer['cards']}")
                print("You win.")
                return
            else:
                print(f"This is your hand: {player['cards']}")
                print(f"This is the dealer's hand: {dealer['cards']}")
                print("You lose.")
                return