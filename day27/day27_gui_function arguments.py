# https://www.udemy.com/course/100-days-of-code/learn/lecture/20781124#search

# Day 27

# Tkinter
from tkinter import *

# window = Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady= 20) # modify padding around the border

# # Label
# my_label = Label(text="I am a label")
# my_label.grid(column=0, row=0)


# # Button
# def button_clicked():
#     user_input = entry.get()
#     my_label["text"] = user_input

# button = Button(text="Click me", command=button_clicked)
# button.grid(column=1, row=1)

# button2 = Button(text="Button 2")
# button2.grid(column=2, row=0)


# # Entry
# entry = Entry(width=10)

# entry.grid(column=3, row=2)


# window.mainloop()

# python advanced arguments
# unlimited arguments
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)
#     return sum

# add(1, 2, 3, 4, 5)


# Exercice project - Mile to km converter
window = Tk()
window.title("Mile to km converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)

def milesToKm():
    user_input = int(input.get())
    input_converted = round(user_input * 1.60934, 2)
    km_label = Label(text=input_converted)
    km_label.grid(column=1, row=1)

button = Button(text="Calculate", command=milesToKm)
button.grid(column=1, row=2)

text_label = Label(text="is equal to")
text_label.grid(column=0, row=1)

unit1_label = Label(text="Miles")
unit1_label.grid(column=2, row=0)

unit2_label = Label(text="Km")
unit2_label.grid(column=2, row=1)

window.mainloop()