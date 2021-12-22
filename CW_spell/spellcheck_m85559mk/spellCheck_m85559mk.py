import os
import argparse

def get_word_list(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

def remove_identical(input_string, disallowed_characters):
    output = ""
    amount_removed = 0
    for character in input_string:
        if character not in disallowed_characters:
            output += character
        else:
            amount_removed += 1 

    return output, amount_removed

#Returns the amount of correct words and incorrect words in a tuple
def spellcheck(word_list, input_string):
    input_string_words = input_string.split()
    correct_words = 0
    for word in input_string_words:
        if word in word_list:
            correct_words += 1

    return correct_words, len(input_string_words) - correct_words

def upper_to_lower(input_string):
    transformed = 0
    output_string = ''
    for character in input_string:
        if character != character.lower():
            transformed += 1
        output_string += character.lower()

    return output_string, transformed

#Returns a tuple of the input folder and the output folder
def get_io_folders():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument("english_words")
    my_parser.add_argument("input_folder")
    my_parser.add_argument("output_folder")
    args = my_parser.parse_args()

    return args.input_folder, args.output_folder, args.english_words

def get_output_filename(input_filename, username):
    txt_removed = input_filename.split(".")[0]
    return f'{txt_removed}_{username}.txt'


def main():
    input_folder, output_folder, english_words = get_io_folders()
    #Creates the output path if it does not already exist
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    word_list = get_word_list(english_words)
    for filename in os.scandir(input_folder):
        with open(filename.path, 'r') as f:
            input_string = f.read()
        output_file_path = os.path.join(output_folder, get_output_filename(filename.name, 'm85559mk'))
        with open(output_file_path, "w+") as f:
            without_numbers, numbers_removed = remove_identical(input_string, "1234567890")
            without_punctuation, punctuation_removed = remove_identical(without_numbers, '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
            without_uppercase, uppercase_removed = upper_to_lower(without_punctuation)
            correct_words, incorrect_words = spellcheck(word_list, without_uppercase)
            f.write("m85559mk\n")
            f.write("Formatting ###################\n")
            f.write(f"Number of upper case words changed: {uppercase_removed}\n")
            f.write(f"Number of punctuations removed: {punctuation_removed}\n")
            f.write(f"Number of numbers removed: {numbers_removed}\n")
            f.write("Spellchecking ###################\n")
            f.write(f"Number of words: {correct_words + incorrect_words}\n")
            f.write(f"Number of correct words: {correct_words}\n")
            f.write(f"Number of incorrect words: {incorrect_words}\n")

main()