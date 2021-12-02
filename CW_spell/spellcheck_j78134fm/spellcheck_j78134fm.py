import os
import argparse
import re

def remove_blanks(lst):
    return [element for element in lst if element != ""]
def cleaning_numbers(word):
    word = re.sub("[0-9]", "", word)
    return word
def cleaning_punctuation(word):
    word = re.sub("[^a-zA-Z0-9\s]", "", word)
    return word

parser = argparse.ArgumentParser()
parser.add_argument("englishwords", help="The english words file")
parser.add_argument("inputfilepath", help="The input file path")
parser.add_argument("outputfilepath", help="The output file path")
args = parser.parse_args()

engwords = args.englishwords
inputdirectory = args.inputfilepath
outputdirectory = args.outputfilepath

for filename in os.listdir(inputdirectory):
    with open(os.path.join(inputdirectory, filename)) as inputfile:
        whole_string = inputfile.read()

    with open(engwords, "r") as file:
        words = [line.strip("\n") for line in file]

    whole_string_stripped = re.split('\s+', whole_string)

    list_of_words_in_string = []
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0

    lst = re.findall("[A-Z]", whole_string)
    count1 += len(lst)

    lst2 = re.findall("[0-9]", whole_string)
    count3 += len(lst2)

    lst3 = re.findall("[^a-zA-Z0-9#@\s]", whole_string)
    count2 += len(lst3)

    if re.search("\.\.\.", whole_string):
        lst4 = re.findall("\.\.\.", whole_string)
        count2 -= len(lst4)*3
        count2 += len(lst4)

    for word in whole_string_stripped:
        word = cleaning_numbers(word)
        word = cleaning_punctuation(word)
        word = word.lower()
        list_of_words_in_string += [word]

    list_of_words_in_string = remove_blanks(list_of_words_in_string)

    for word in list_of_words_in_string:
        if word in words:
            count4 += 1
        else:
            count5 += 1

    filename_split = filename.split(".")
    filename_split.insert(1, "_j78134fm.")
    filename_otpt = "".join(filename_split)
    filename_output = os.path.join(outputdirectory, filename_otpt)

    with open(filename_output, "w") as outputfile:
        outputfile.writelines("j78134fm\n")
        outputfile.writelines("Formatting ###################\n")
        outputfile.writelines("Number of upper case letters changed: " + str(count1) + "\n")
        outputfile.writelines("Number of punctuations removed: " + str(count2) + "\n")
        outputfile.writelines("Number of numbers removed: " + str(count3) + "\n")
        outputfile.writelines("Spellchecking ###################" + "\n")
        outputfile.writelines("Number of words: " + str(len(list_of_words_in_string)) + "\n")
        outputfile.writelines("Number of correct words: " + str(count4) + "\n")
        outputfile.writelines("Number of incorrect words: " + str(count5) + "\n")
