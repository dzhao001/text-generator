'''
    File name: main.py
    Author: Daniel Zhao
    Date created: 11/24/2021
    Date last modified: 11/24/2021
    Python Version: 3.8.12
'''

import functions
import os
import sys

# sets path as a destination string of desired text file
path = os.path.join(os.getcwd(), "text", os.listdir("text")[0])

# opens text file and reads it into a string
file = open(path, mode = "r", encoding = "utf-8")
file_string = file.read()
file.close()

# passes text file string to function and creates a list of words
word_list = functions.string_to_list(file_string)

# creates another list of all unique words in original list
unique_list = []
for i in word_list:
    if i not in unique_list:
        unique_list.append(i)

# creates a dictionary where every letter that comes after another is tracked and given a frequency
dict_freq = functions.letter_weighed_dict(word_list)

# creates a dictionary where the letters that come after another letter is giving a chance
dict_chance = functions.number_weighed_dict(dict_freq)

# reads user input for how long the text should be, quits the program if the user provides "q" as input
while (True):
    user_input = input("Generate a random list of text! Type a number for text length, or q to quit: ")
    if (user_input.lower() == "q"):
        sys.exit()
    if (not user_input.isdigit()):
        print("Error: Incorrect input received")
        continue
    print(functions.generate_text(dict_chance, unique_list, int(user_input)))