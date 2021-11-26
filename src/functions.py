'''
    File name: functions.py
    Author: Daniel Zhao
    Date created: 11/24/2021
    Date last modified: 11/24/2021
    Python Version: 3.8.12
'''
import random
import re

# parses a text file of all the words of the english language and turns it into a string
word_file = open("wordlist.txt")
word_list = word_file.read().split("\n")
word_file.close()

# this function takes a string seperated by spaces and turns it into a list of words, removing all symbols and numbers
def string_to_list(a_string):
    word_list = a_string.split()
    completed_list = [re.sub('[^a-zA-Z]+', '', i).lower() for i in word_list]
    return completed_list

# this function takes a word and tracks every letter and the preceeding one to return the dict its given with the
# freq of that letter appearing after another letter tracked. if it is the last letter, " " will be counted instead
def weigh_word(a_word, a_dict):
    for i in range(len(a_word)):
        if i + 1 >= len(a_word):
            if " " not in a_dict[a_word[i]]:
                a_dict[a_word[i]][" "] = 1
                return a_dict
            else:
                a_dict[a_word[i]][" "] += 1
                return a_dict
        if a_word[i + 1] not in a_dict[a_word[i]]:
            a_dict[a_word[i]][a_word[i + 1]] = 1
        else:
            a_dict[a_word[i]][a_word[i + 1]] += 1
    return a_dict

# this function takes a list and returns a dict where the frequency of one letter coming after another letter is tracked, 
# calls weigh word function
def letter_weighed_dict(a_list):
    my_dict = {}
    for i in "abcdefghijklmnopqrstuvwxyz":
        my_dict[i] = {}
    for i in a_list:
        my_dict = weigh_word(i, my_dict)
    return my_dict

# this function takes a dict weighed by frequency and returns a sorted dict based on probability
def number_weighed_dict(a_dict):
    my_dict = {}
    for i in "abcdefghijklmnopqrstuvwxyz":
        my_dict[i] = {}
    for i in a_dict:
        num_total = 0
        for j in a_dict[i]:
            num_total += a_dict[i][j]
        for j in a_dict[i]:
            num = a_dict[i][j]/num_total
            my_dict[i][j] = num
    for i in my_dict:
        my_dict[i] = dict(sorted(my_dict[i].items(), key = lambda t: t[1])) 
    return my_dict

# generates a random letter of the alphabet
def generate_letter():
    ran = int(random.uniform(97, 123))
    return chr(ran)

# calculates what letter should come after the letter given based on a reference dictionary and chance and returns that next letter
def calculate_next_letter(letter, ref_dict):
    ran = random.random()
    total = 0.0
    for i in ref_dict[letter]:
        total += ref_dict[letter][i]
        if ran < total:
            return i

# returns a single word given a letter to start and an english word list to check if word is valid
def generate_word(letter, ref_dict, english_list):
    str = ""
    formed_str = letter
    next_letter = letter
    while(True):
        temp_str = formed_str
        temp_list = [i[0:len(formed_str) + 1] for i in english_list]
        temp_letter = next_letter
        next_letter = calculate_next_letter(next_letter, ref_dict)
        if (str != "" and next_letter == " "):
            return str
        if (next_letter == " "):
            next_letter = temp_letter
            continue
        temp_str += next_letter
        if temp_str in temp_list:
            formed_str = temp_str
            if formed_str in english_list:
                str = formed_str

# returns a list of words based on a starting letter, default amount of words generated is 10
def generate_text(ref_dict, english_list, num_words = 10, letter = generate_letter()):
    text_list = []
    current_letter = letter
    i = 0
    while (i < num_words):
        word = generate_word(current_letter, ref_dict, english_list)
        if word in word_list:
            text_list.append(word)
            current_letter = text_list[-1][-1]
            i += 1
    return " ".join(text_list)
