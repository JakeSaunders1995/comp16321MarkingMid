import argparse
import os
import string
parser = argparse.ArgumentParser()
parser.add_argument("word_list")
parser.add_argument("input_folder")
parser.add_argument("output_folder")
args = parser.parse_args()

english_words_file = open(args.word_list, "r")
english_words = english_words_file.read()

english_words_file.close()

all_words = english_words.split('\n')



for f in os.listdir(args.input_folder):
    num_upper_case = 0
    num_punctuation = 0
    num_numbers = 0

    correct_words = 0
    incorrect_words = 0

    file = open(args.input_folder + "/" + f, "r")
    text = file.read()

    file.close()
 
    i = 0
    while i < len(text):
        if text[i].isupper():
            num_upper_case += 1
        elif text[i].isdigit():
            num_numbers += 1
            text = text[:i] + text[i+1:]
            i -= 1
        elif text[i] in string.punctuation:
            num_punctuation += 1
            text = text[:i] + text[i+1:]
            i -= 1
        elif not text[i].isalpha() and text[i] != " ":
            text = text[:i] + text[i+1:]
            i -= 1
        i += 1

    text = text.lower()

    words = text.split(' ')
    words = list(filter(lambda a: a != '', words))

    for word in words:
        if word in all_words:
            correct_words += 1
        else:
            incorrect_words += 1

    output = "Formatting ###################" + "\n" + "Number of upper case words transformed: " + str(num_upper_case) + "\n" + "Number of punctuation’s removed: " + str(num_punctuation) + "\n" + "Number of numbers removed: " + str(num_numbers) + "\n" + "Spellchecking ###################" + "\n" + "Number of words in file: " + str(len(words)) + "\n" + "Number of correct words in file: " + str(correct_words) + "\n" + "Number of incorrect words in file: " + str(incorrect_words)

    file_write = open(args.output_folder + "/" + f[:-4] + "_r27125bw.txt", "w")
    file_write.write(output)
    file_write.close()
