#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Getting the names
with open("Input/Names/invited_names.txt", mode="r") as invited_names:
    names_list = invited_names.readlines()

# Getting the letter template
with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    template = starting_letter.read()

# print(names_list)

# Writing the letters in the Output
for name in names_list:
    name = name.strip()
    formatted_name = name.replace(" ", "_")
    # print(name)
    # print(formatted_name)
    modified_template = template.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{formatted_name}.txt", mode="w") as letter:
        letter.write(modified_template)
