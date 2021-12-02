import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("english_words")
parser.add_argument("input_folder")
parser.add_argument("output_folder")
args = parser.parse_args()
english_words_file_name = args.english_words
input_folder_name = args.input_folder
output_folder_name = args.output_folder

files_to_loop = os.listdir(input_folder_name)

for file in files_to_loop:
    input_file_name = file
    output_file_name = "{}_a08872aa.txt".format(input_file_name[:len(input_file_name)-4])
    if "/" in input_folder_name:
        input_file = open("{}/{}".format(input_folder_name, input_file_name), "r")
    else:
        input_file = open("{}/{}".format(input_folder_name, input_file_name), "r")
    text = input_file.read()

    legal_chars = list("abcdefghijklmnopqrstuvwxyz")
    nums = list("0123456789")
    i=0

    upper_count = 0
    num_count = 0
    punctuation_count = 0

    indvl_chars = set(text)
    for char in indvl_chars:
        current_len = len(text)
        if char in legal_chars or char == " ":
            next
        elif char.lower() in legal_chars:
            upper_count += text.count(char)
            text = text.replace(char, char.lower())
        elif char not in legal_chars and char in nums:
            text = text.replace(char, "")
            num_count += current_len - len(text)
        elif char not in legal_chars:
            text = text.replace(char, "")
            punctuation_count += current_len - len(text)

    words_in_text = text.split(" ")

    english_words = open(english_words_file_name, "r")
    word_list = english_words.read().split("\n")

    total_words = len(words_in_text)
    incorrect_words = 0
    for check in words_in_text: 
        if check not in word_list:
            incorrect_words +=1

    english_words.close()

    final_text = "a08872aa\nFormatting ###################\nNumber of upper case words transformed: {}\nNumber of punctuation’s removed: {}\nNumber of numbers removed: {}\nSpellchecking ###################\nNumber of words in file: {}\nNumber of correct words in file: {}\nNumber of incorrect words in file: {}".format(str(upper_count), str(punctuation_count), str(num_count), str(total_words), str(total_words-incorrect_words), str(incorrect_words))
    if "/" in output_folder_name:
        output_file = open("{}/{}".format(output_folder_name, output_file_name), "w")
    else:
        output_file = open("{}\{}".format(output_folder_name, output_file_name), "w")
    output_file.write(final_text)
    output_file.close()


