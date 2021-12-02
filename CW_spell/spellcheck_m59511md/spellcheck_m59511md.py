import sys
import os

file_paths = sys.argv

english_words_file = open(file_paths[1], "r")
input_path = file_paths[2]
output_path = file_paths[3]

os.chdir(input_path)
files_in_directory = os.listdir()

ENGLISH_WORDS = english_words_file.read().split()
PUNCTUATION = [".", "?", "!", ",", ":", ";", "_", "-", "[", "]", "{", "}", "(", ")", "'", "…", '"']
NUMBERS = [str(i) for i in range(0, 10)]
UPPERCASE = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def spellcheck(input_file_string):

    os.chdir(input_path)
    input_file = open(input_file_string, "r")
    contents = input_file.read()

    no_of_nums = 0
    no_of_punc = 0
    no_of_caps = 0
    no_of_errs = 0

    for character in contents:
        if character in NUMBERS:
            no_of_nums += 1
        elif character in PUNCTUATION:
            no_of_punc += 1
        elif character in UPPERCASE:
            no_of_caps += 1

    for character in contents:
        if character in NUMBERS or character in PUNCTUATION:
            contents = contents.replace(character, "")
        elif character in UPPERCASE:
            contents = contents.replace(character, character.lower())

    words_in_contents = contents.split()
    no_of_words = len(words_in_contents)
    print(words_in_contents)
    print(contents)

    for word in words_in_contents:
        if word not in ENGLISH_WORDS:
            no_of_errs += 1

    output_file_name = input_file_string.replace(".txt", "") + "_m59511md.txt"

    os.chdir(output_path)
    output_file = open(output_file_name, "w")

    output_file.write("m59511md")
    output_file.write("\nFormatting ###################")
    output_file.write("\nNumber of upper case letters changed: " + str(no_of_caps))
    output_file.write("\nNumber of punctuations removed: " + str(no_of_punc))
    output_file.write("\nNumber of numbers removed: " + str(no_of_nums))
    output_file.write("\nSpellchecking  ###################")
    output_file.write("\nNumber of words: " + str(no_of_words))
    output_file.write("\nNumber of correct words: " + str(no_of_words - no_of_errs))
    output_file.write("\nNumber of incorrect words: " + str(no_of_errs))


for file in files_in_directory:
    spellcheck(file)
