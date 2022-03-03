import turtle
from state import State
# python -m pip install pandas
# python uninstall pandas
# https://pandas.pydata.org/docs/
import pandas


screen = turtle.Screen()
screen.title("USA States Game")
image = "day25/us-states-game-start/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("day25/us-states-game-start/50_states.csv")
states_list = states_data["state"].to_list()
# print(states_list)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

answered_list = []
game_over = False
while not game_over:
    answer_state = screen.textinput(title=f"Guess the State ({len(answered_list)}/{len(states_list)})", prompt="Please input a State name").title()
    # print(answer_state)
    if answer_state == "Exit":
        break
    elif answer_state in states_list:
        if answer_state not in answered_list:
            state_row = states_data[states_data["state"] == answer_state].to_dict()
            # print(state_row)
            state = {}
            for col in state_row:
                # print(col)
                for key in state_row[col]:
                    # print(state_row[col])
                    state[col] = state_row[col][key]

            answered_list.append(answer_state)
            new_state = State(state["state"], state["x"], state["y"])

    if len(answered_list) == len(states_list):
        game_over = True

# states_to_learn = []
# for state in states_list:
#     if state not in answered_list:
#         states_to_learn.append(state)

states_to_learn = [state for state in states_list if state not in answered_list] # shorter version after day 26

new_csv = pandas.Series(states_to_learn)
new_csv.to_csv("day25/us-states-game-start/states_to_learn.csv")

# turtle.mainloop()
# screen.exitonclick()