import os
import argparse
import re

parser = argparse.ArgumentParser(description="Spell check")
parser.add_argument("WORDS_FILE")
parser.add_argument("IN_FOLDER")
parser.add_argument("OUT_FOLDER")

args = parser.parse_args()

ALPHAS = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "01234567890"
PUNCTUATION = ".?!,:;-[]{}()'\""

with open(args.WORDS_FILE, "r") as words_file:
    WORDS = words_file.read().splitlines()

for input_filename in os.scandir(args.IN_FOLDER):
    with open(input_filename, "r") as input_file:
        input_str = input_file.read()

    # replace ellipsis with full stop to make counting easier
    input_str = input_str.replace("...", ".")

    num_upper = 0
    num_punct = 0
    num_num = 0

    cleaned_input = ""
    for char in input_str:
        if char in " \n" or char in ALPHAS:
            cleaned_input += char
        elif char in ALPHAS.upper():
            cleaned_input += char.lower()
            num_upper += 1
        elif char in NUMBERS:
            num_num += 1
        elif char in PUNCTUATION:
            num_punct += 1
        else:
            raise Exception("Invalid input!")


    input_words = cleaned_input.split()
    print(input_words)

    num_words = len(input_words)
    correct_words = 0
    wrong_words = 0

    for word in input_words:
        if word in WORDS:
            correct_words += 1
        else:
            wrong_words += 1

    output_str = f"""c60952ti
Formatting ###################
Number of upper case letters changed: {num_upper}
Number of punctuations removed: {num_punct}
Number of numbers removed: {num_num}
Spellchecking ###################
Number of words: {num_words}
Number of correct words: {correct_words}
Number of incorrect words: {wrong_words}"""

    output_filename = os.path.join(
        args.OUT_FOLDER,
        os.path.splitext(
            os.path.basename(input_filename))[0] +
        "_c60952ti" +
        os.path.splitext(input_filename)[1])

    with open(output_filename, "w") as output_file:
        output_file.write(output_str)
