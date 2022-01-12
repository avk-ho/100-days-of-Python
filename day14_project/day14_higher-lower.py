# https://www.udemy.com/course/100-days-of-code/learn/lecture/19846766#overview

# Day 14 - Higher/Lower project

# Solo attempt

import random
from day14_gamedata import data
from day14_art import logo
from day14_art import vs

def higherLower():
    print(logo)
    game_over = False
    two_pick = []
    score = 0
    while not game_over:
        if len(two_pick) == 0:
            two_pick = random.choices(data, k=2)
            while two_pick[0] == two_pick[1]:
                two_pick = random.choices(data, k=2)
        else:
            two_pick.append(random.choice(data))
            while two_pick[0] == two_pick[1] or two_pick[1] == old_pick:
                two_pick[1] = random.choice(data)

        pick_a = two_pick[0]
        pick_b = two_pick[1]
        print(
            f"Compare A: {pick_a['name']}, {pick_a['description']} from {pick_a['country']}.")
        print(vs)
        print(
            f"Against B: {pick_b['name']}, {pick_b['description']} from {pick_b['country']}.")
        
        answer = ""
        if pick_a["follower_count"] > pick_b["follower_count"]:
            answer = "A"
            old_pick = two_pick.pop(1)
        else:
            answer = "B"
            old_pick = two_pick.pop(0)

        input_check = True
        while input_check:
            user_answer = input("Who has more followers (on instagram)? Type 'A' or 'B': ")
            if user_answer == "A" or user_answer == "B":
                input_check = False
                if user_answer == answer:
                    score += 1
                    print(f"You're right! Current score: {score}.")
                    # clear() from replit

                else:
                    game_over = True
                    print(f"Sorry, that's wrong. Final score: {score}.")
                    return
            else:
                print("Wrong input.")

# Post correction
# from replit import clear

def higherLower():
    def format_data(account):
        """Takes an account and returns a string description"""
        account_name = account["name"]
        account_desc = account["description"]
        account_country = account["country"]
        return f"{account_name}, {account_desc} from {account_country}."

    print(logo)
    game_over = False
    two_pick = []
    score = 0
    while not game_over:
        if len(two_pick) == 0:
            two_pick = random.choices(data, k=2)
            while two_pick[0] == two_pick[1]:
                two_pick = random.choices(data, k=2)
        else:
            two_pick.append(random.choice(data))
            while two_pick[0] == two_pick[1] or two_pick[1] == old_pick:
                two_pick[1] = random.choice(data)

        pick_a = two_pick[0]
        pick_b = two_pick[1]
        print(
            f"Compare A: {format_data(pick_a)}")
        print(vs)
        print(
            f"Against B: {format_data(pick_b)}")

        answer = ""
        if pick_a["follower_count"] > pick_b["follower_count"]:
            answer = "A"
            old_pick = two_pick.pop(0)
        else:
            answer = "B"
            old_pick = two_pick.pop(0)

        input_check = True
        while input_check:
            user_answer = input(
                "Who has more followers (on instagram)? Type 'A' or 'B': ")
            if user_answer == "A" or user_answer == "B":
                input_check = False
                if user_answer == answer:
                    score += 1
                    print(f"You're right! Current score: {score}.")
                    # clear() from replit
                    # print(logo)

                else:
                    game_over = True
                    print(f"Sorry, that's wrong. Final score: {score}.")
                    return
            else:
                print("Wrong input.")
