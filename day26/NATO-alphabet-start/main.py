student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("day26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
# print(data)
nato_alphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(nato_alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_valid_word = False
while not is_valid_word:
    try:
        user_input = input("Enter a word: ")
        phonetic_list = [nato_alphabet_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        is_valid_word = True
        print(phonetic_list)

# Alternative method
def generate_nato_alphabet():
    try:
        user_input = input("Enter a word: ")
        phonetic_list = [nato_alphabet_dict[letter.upper()]
                            for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_nato_alphabet()
    else:
        print(phonetic_list)
