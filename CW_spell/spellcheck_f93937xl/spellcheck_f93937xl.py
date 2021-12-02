import argparse
import string
import os

parser = argparse.ArgumentParser(description='Spellchecker')
parser.add_argument('dictionary', type=str, help='A required string argument -- English dictionary')
parser.add_argument('input_path', type=str, help='A required string argument -- input path')
parser.add_argument('output_path', type=str, help='A required string argument -- output path')

args = parser.parse_args()

input_path = args.input_path
output_path = args.output_path
input_files = os.listdir(input_path)
output_files = os.listdir(output_path)

a = 0
while a < len(input_files):
    input_file = input_files[a]
    input_path_1 = input_path + "/" + input_file
    with open(args.dictionary, "r") as f1:
        dictionary = f1.read()
    with open(input_path_1, "r") as f2:
        input = f2.read()
    t1 = "f93937xl\nFormatting ###################\n"

    result = ""

    num_upper = 0
    num_punct = 0
    num_num = 0
    for i in range(0, len(input)):
        if input[i] in string.punctuation:
            num_punct += 1
        elif input[i].isdigit():
            num_num += 1
        elif input[i].isupper():
            num_upper += 1
            result += input[i].lower()
        else:
            result += input[i]
    t2 = "Number of upper case letters changed: " + str(num_upper) + "\n"
    t3 = "Number of punctuations removed: " + str(num_punct) + "\n"
    t4 = "Number of numbers removed: " + str(num_num) + "\n"

    t5 = "Spellchecking ###################" + "\n"

    list = result.split()
    dict = dictionary.split()
    num_wrong = 0
    for word in list:
        if word not in dict:
            num_wrong += 1
    t6 = "Number of words: " + str(len(list)) + "\n"
    t7 = "Number of correct words: " + str(len(list) - num_wrong) + "\n"
    t8 = "Number of incorrect words: " + str(num_wrong) + "\n"

    answer = t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8
    output_file = input_file[:-4] + "_f93937xl" + input_file[-4:]
    output_path_1 = output_path + "/" + output_file
    with open(output_path_1, "w+") as f:
         answer = f.write(answer)
    a += 1

f1.close()
f2.close()
