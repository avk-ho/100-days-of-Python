# https://www.udemy.com/course/100-days-of-code/learn/lecture/20944498#overview

# Day 31 - Flashcard project

from tkinter import *
from tkinter import messagebox
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

### DATA ###
def fetch_learned_data():
    global learned_data, learned_data_dict
    try:
        learned_data = pandas.read_csv(
            "day31_flashcard-project/data/learned_french_words.csv")
    except FileNotFoundError:
        learned_data = pandas.DataFrame(
            {"French": [],
            "English": [],
            })
        learned_data.to_csv(
            path_or_buf="day31_flashcard-project/data/learned_french_words.csv", index=False)
    finally:
        learned_data_dict = learned_data.to_dict(orient="records")
        # print(learned_data)


def update_learned_list():
    global current_card
    # print(current_card)
    learned_card = pandas.DataFrame(current_card, index=[0])
    # print(learned_card)
    learned_card.to_csv(
        "day31_flashcard-project/data/learned_french_words.csv", mode="a", index=False, header=False)
    fetch_learned_data()

fetch_learned_data()
data = pandas.read_csv("day31_flashcard-project/data/french_words.csv")
to_learn = data.to_dict(orient="records")  # is a list of dicts
# print(to_learn)

### CARD SWAPPING ###
def swap_card_right():
    global current_card
    
    if len(learned_data_dict) == len(to_learn):
        messagebox.showinfo(
            title="Congratulations", message="No more cards to learn.")

    else:
        update_learned_list()
        current_card = random.choice(to_learn)

        while current_card in learned_data_dict:
            current_card = random.choice(to_learn)

        canvas.itemconfig(card_title, text="French")
        canvas.itemconfig(card_word, text=current_card["French"])


def swap_card_wrong():
    global current_card
    current_card = random.choice(to_learn)

    while current_card in learned_data_dict:
        current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])

### CARD FLIPPING ###
def flip_card():
    current_title = canvas.itemcget(card_title, 'text')
    # current_word = canvas.itemcget(card_word, 'text')

    if current_title == "French":
        canvas.itemconfig(current_card_bg, image=card_back_img)
        canvas.itemconfig(card_title, text="English")
        canvas.itemconfig(card_word, text=current_card["English"])
    else:
        canvas.itemconfig(current_card_bg, image=card_front_img)
        canvas.itemconfig(card_title, text="French")
        canvas.itemconfig(card_word, text=current_card["French"])

### USER INTERFACE ###
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
right_img = PhotoImage(file="day31_flashcard-project/images/right.png")
wrong_img = PhotoImage(file="day31_flashcard-project/images/wrong.png")
arrow_img = PhotoImage(file="day31_flashcard-project/images/curved-arrow.png")
card_front_img = PhotoImage(file="day31_flashcard-project/images/card_front.png")
card_back_img = PhotoImage(file="day31_flashcard-project/images/card_back.png")

# Buttons
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=swap_card_wrong)
wrong_btn.grid(row=1, column=0)
flip_btn = Button(image=arrow_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=flip_card)
flip_btn.grid(row=1, column=1)
right_btn = Button(image=right_img, highlightthickness=0, command=swap_card_right)
right_btn.grid(row=1, column=2)


# Canvas
canvas = Canvas(width=800, height=526)
current_card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

swap_card_wrong()

window.mainloop()