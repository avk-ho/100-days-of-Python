# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dict = {"key": "value",}
# value = a_dict{"not_key"}

# IndexError
# fruit_list = ["Apple", "Banana", "Orange"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 3)


# Managing errors
# try:
#     file = open("a_file.txt")
#     fruit_list = ["Apple", "Banana", "Orange"]
#     fruit = fruit_list[3]
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
# except IndexError as index_error:
#     print(f"Index {index_error} out of range")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height < 3:
#     raise ValueError("Cannot be over 3 meters")
# bmi = weight / height ** 2
# print(bmi)