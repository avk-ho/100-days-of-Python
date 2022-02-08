# https://www.udemy.com/course/100-days-of-code/learn/lecture/20532962#overview

# Day 24 - Files / Directories / Paths

# Opening and reading files
# Basic way
# file = open("day24/my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Second way (recommended)
# with open("day24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Writing
# This overwrite what is currently in the file
# with open("day24/my_file.txt", mode="w") as file:
#     file.write("New text.")
    
# Append
# This adds the new text after the current content of the file
with open("day24/my_file.txt", mode="a") as file:
    file.write("New text.")


# Mail merge project