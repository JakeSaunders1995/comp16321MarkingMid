import argparse
import re
from os import listdir
from os.path import join, isfile

def command_line_parser():
    '''Parse the command line arguments and return'''
    parser = argparse.ArgumentParser(description="Run a spellcheck on the given file")
    parser.add_argument("dict", metavar="D", type=str,
                        help="Dictionary file path", action="store")
    parser.add_argument("input", metavar="I", type=str,
                        help="Input file path", action="store")
    parser.add_argument("output", metavar="O", type=str,
                        help="Output file path", action="store")

    args = parser.parse_args()
    return args.dict, args.input, args.output

def get_words(dict_path):
    file = open(dict_path, "r")
    words_dict = file.read()
    file.close()
    return words_dict

def get_message(filepath):
    file = open(filepath, "r")
    text = file.read()
    file.close()
    return text

def strip_uppercase(string):
    upper_count = sum(1 for char in string if char.isupper())
    string = string.lower()
    return upper_count, string

def strip_punctuation(string):
    PUNCTUATION = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    punctuation_count = sum(1 for char in string if char in PUNCTUATION)
    new_string = ""
    for word in string:
        word = word.strip(PUNCTUATION)
        new_string += word
    return punctuation_count, new_string

def strip_numbers(string):
    numeric_count = sum(1 for char in string if char.isnumeric())
    string = re.sub(r"\d+", "", string)
    return numeric_count, string

def remove_double_whitespace(string):
    return re.sub(" +", " ", string)

def check_words(string, dictionary):
    correct_count = 0
    incorrect_count = 0
    for word in string.split(" "):
        if word in dictionary:
            #print(f"{word} is in dictionary")
            correct_count += 1
        else:
            #print(f"{word} is not in dictionary")
            incorrect_count += 1
    return correct_count, incorrect_count

def format_output(upper_count, punctuation_count, numeric_count,
                  word_count, correct_count, incorrect_count):
    final_string = f"j96409sb\nFormatting ###################\n"
    final_string += f"Number of upper case words changed: {upper_count}\n"
    final_string += f"Number of punctuations removed: {punctuation_count}\n"
    final_string += f"Number of numbers removed: {numeric_count}\n"
    final_string += "Spellchecking ###################\n"
    final_string += f"Number of words: {word_count}\n"
    final_string += f"Number of correct words: {correct_count}\n"
    final_string += f"Number of incorrect words: {incorrect_count}"
    return final_string

def write_file(path, filename, message):
    file = open(f"{path}/{filename}.txt", "w")
    file.write(message)
    file.close()
    
if __name__ == "__main__":
    dict_path, input_path, output_path = command_line_parser()
    ENGLISH_WORDS_STR = get_words(dict_path)
    ENGLISH_WORDS_LIST = ENGLISH_WORDS_STR.split("\n")
    files = [file for file in listdir(input_path) if isfile(join(input_path, file))]
    filecount = 0
    for file in files:
        filecount += 1
        message = get_message(f"{input_path}/{file}")
        up_count, message = strip_uppercase(message)
        num_count, message = strip_numbers(message)
        punc_count, message = strip_punctuation(message)
        message = remove_double_whitespace(message)
        word_count = len(message.split(" "))
        correct_count, incorrect_count = check_words(message, ENGLISH_WORDS_LIST)
        output_string = format_output(up_count, punc_count, num_count, word_count, correct_count, incorrect_count)
        write_file(output_path, f"test_file{filecount}_j96409sb", output_string)