import sys
import os

args = sys.argv

def spell_check(raw_text):

    modified_text = ""

    upper_case = 0
    numbers = 0
    punctuation = 0

    upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    num = list("1234567890")
    punct = list(".?!,:;-_()[]{}'" + '"')

    elipse_count = 0

    for char in raw_text:

        if char in upper:
            upper_case += 1
            modified_text += char.lower()
        elif char in num:
            numbers += 1
        elif char in punct:
            if (char == '.' and elipse_count == 2):
                elipse_count = 0
                punctuation -= 1
            elif (char == '.'):
                punctuation += 1
                elipse_count += 1
            else:
                punctuation += 1
        else:
            modified_text += char

    word_list = modified_text.strip().split(" ")
    num_words = len(word_list)
    valid_words = 0
    invalid_words = 0

    valid_check = False

    for word in word_list:
        word = word.strip()
        valid_check = False
        for english_word in dictionary:
            if (word == english_word):
                valid_check = True
                break
        if (valid_check):
            valid_words += 1
        else:
            invalid_words += 1

    result =   ("y66466tl" +
                "\nFormatting ###################" +
                "\nNumber of upper case words changed: " + str(upper_case) +
                "\nNumber of punctuations removed: " + str(punctuation) +
                "\nNumber of numbers removed: " + str(numbers) +
                "\nSpellchecking ###################" +
                "\nNumber of words: " + str(num_words) +
                "\nNumber of correct words: " + str(valid_words) +
                "\nNumber of incorrect words: " + str(invalid_words))

    return result

input_dir = args[2]
output_dir = args[3]

for file_name in os.listdir(input_dir):
    input_file = open(os.path.join(input_dir, file_name), "r")
    output_file = open(os.path.join(output_dir,(file_name + "_y66466tl")), "w")
    dictionary = open(args[1], "r").read().splitlines()
    raw_text = input_file.read()
    result = spell_check(raw_text)
    output_file.write(result)
