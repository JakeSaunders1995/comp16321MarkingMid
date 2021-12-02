import argparse
import os
import re

parser = argparse.ArgumentParser()
parser.add_argument('english_words')
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()

input_directory = args.input_folder
output_directory = args.output_folder
english_words_file = args.english_words

for filename in sorted(os.listdir(input_directory)):

    output_file = filename.split(".")[0] + "_u08120fh.txt"

    with open(os.path.join(input_directory, filename), "r") as file:
        data = file.read()

        were_uppercase = []
        removed_numbers = []
        removed_punctuations = []

        punctuations = ['.', '?', '!', ',', ':', ';', '_', '-',
                        '[', ']', '{', '}', '(', ')', '\'', '\"', '...']

        for char in data:
            if char.isdigit() == True:
                removed_numbers.append(char)
            elif char.isupper() == True:
                were_uppercase.append(char)
            elif char in punctuations:
                removed_punctuations.append(char)

        count_upper = len(were_uppercase)
        count_nums = len(removed_numbers)
        count_puncs = len(removed_punctuations)

        with open(english_words_file, "r") as file:
            eng_words = file.read().splitlines()

        words = data.split()
        correct_words = []
        incorrect_words = []
        for word in words:
            new_word = re.sub('\W+', "", word)
            clean_word = re.sub(r'[0-9]', "", new_word)

            if len(clean_word) != 0:
                if clean_word.lower() not in eng_words:
                    incorrect_words.append(word)
                else:
                    correct_words.append(clean_word)

        correct = len(correct_words)
        incorrect = len(incorrect_words)
        total = correct + incorrect

        with open(os.path.join(output_directory, output_file), "w") as op:
            data = ["u08120fh", "\n"
                    "Formatting ###################", "\n"
                    "Number of upper case letters changed: ", str(
                        count_upper), "\n"
                    "Number of punctuations removed: ", str(
                        count_puncs), "\n"
                    "Number of numbers removed: ", str(count_nums), "\n"
                    "Spellchecking ###################", "\n"
                    "Number of words: ", str(total), "\n"
                    "Number of correct words: ", str(correct), "\n"
                    "Number of incorrect words: ", str(incorrect), "\n"
                    ]
            op.writelines(data)
