import os, re, argparse
import string

parser = argparse.ArgumentParser(description = 'get i/o files')
parser.add_argument("input_path")
parser.add_argument("output_path")
args = parser.parse_args()

full_input_path = os.path.join(os.getcwd(), args.input_path)
input_files = os.listdir(full_input_path)

full_output_path = os.path.join(os.getcwd(), args.output_path)

inputs = [] # change per task
filenames_split = []
for input_filename in input_files:
    input_path = full_input_path + "/" + input_filename
    input_file = open(input_path, "r")
    inputs.append(input_file.read()) # change per task
    input_file.close

    temp_file_split = re.split(".txt", input_filename)
    filenames_split.append(temp_file_split[0])

english_words_file = open(os.path.join(os.getcwd(), "./EnglishWords.txt"), "r")
english_words = english_words_file.read()
english_words_file.close


file_num = 1
for unchecked in inputs:
    checked = ""
    num_count = 0
    punct_count = 0
    upper_count = 0
    for unchecked_char in unchecked:
        if unchecked_char.isnumeric():
            num_count = num_count + 1
        elif unchecked_char in string.punctuation:
            punct_count = punct_count + 1
        elif unchecked_char.isupper():
            upper_count - upper_count + 1
            checked = checked + unchecked_char.lower()
        else:
            checked = checked + unchecked_char
    
    checked_string = ""
    correct_count = 0
    incorrect_count = 0
    unchecked_words = re.split("\s", checked)
    for unchecked_word in unchecked_words:
        if unchecked_word in english_words:
            correct_count = correct_count + 1
        else:
            incorrect_count = incorrect_count + 1


    output_path = full_output_path + "/" + filenames_split[file_num - 1] + "_n72421tn.txt"

    checked_output = open(output_path, "w") 
    checked_output.write("Formatting ###################\nNumber of upper case words transformed: " + str(upper_count) + "\nNumber of punctuations removed " + str(punct_count) + "\nNumber of numbers removed " + str(num_count) + "\nSpellchecking ###################\nNumber of words in file " + str(incorrect_count + correct_count) + "\nNumber of correct words in file: " + str(correct_count) + "\nNumber of incorrect words in file: " + str(incorrect_count)) # change per task
    checked_output.close
    file_num = file_num + 1