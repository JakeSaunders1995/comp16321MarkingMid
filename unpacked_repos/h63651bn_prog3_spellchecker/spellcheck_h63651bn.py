import argparse
import string
import os

# punctuation and digits are in between 33-57

numbers = "0123456789"
symbols = string.punctuation
symbols = symbols.replace("@", "")
symbols = symbols.replace("#", "")

def main(s):
    outputstring = ""
    s = s + " "
    words_list = []
    curr_word = ""
    count = 0

    outputstring += "h63651bn\n"
    outputstring += "Formatting ###################\n"

    nr_num = 0
    nr_upper = 0
    nr_symbols = 0

    for i in s:
        if i == " ":
            if curr_word != "":
                words_list.append(curr_word)
                curr_word = ""
        elif i in numbers:
            nr_num += 1
        elif i.isalpha():
            if ord(i) <= ord('Z'):  # it is an uppercase letter
                nr_upper += 1
                curr_word = curr_word + i.lower()
            else:
                curr_word = curr_word + i
        elif i in symbols:  # it is a symbol
            nr_symbols = nr_symbols + 1
            if i == ".":
                count += 1
                if count == 3:
                    nr_symbols -= 2
                    count = 0
                else:
                    count = 0

    outputstring += "Number of upper case words changed: " + str(nr_upper) + '\n'
    outputstring += "Number of punctuations removed: " + str(nr_symbols) + '\n'
    outputstring += "Number of numbers removed: " + str(nr_num) + '\n'

    nr_correct = 0
    nr_incorrect = 0

    outputstring += "Spellchecking ###################\n"
    outputstring += "Number of words: " + str(len(words_list)) + '\n'

    for word in words_list:
        if word in english_dic:
            nr_correct += 1
        else:
            nr_incorrect += 1

    outputstring += "Number of correct words: " + str(nr_correct) + '\n'
    outputstring += "Number of incorrect words:" + str(nr_incorrect) + '\n'
    return outputstring


parser = argparse.ArgumentParser()
parser.add_argument('dic_file')
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()

input_folder = args.input_folder
output_folder = args.output_folder
dic = args.dic_file
input_files = os.listdir(f"./{input_folder}")
english_dic = open(dic, "r")
english_dic = english_dic.read().replace("\n", " ")
english_dic = english_dic.split()

for file in input_files:
    f = open(f"{input_folder}/{file}", "r")
    k = file.find('.')
    output_file = file[0:k] + "_h63651bn" + file[k:]
    g = open(f"{output_folder}/{output_file}", "w")
    string = f.read().replace("\n", " ")
    string = string.strip()
    empty_string = ""
    g.write(main(string))
    f.close()
    g.close()

