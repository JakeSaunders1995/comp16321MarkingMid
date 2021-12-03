import argparse
import os
import re

parser = argparse.ArgumentParser(description="I/O file path")
parser.add_argument("wordlist_path")
parser.add_argument("input_folder_path")
parser.add_argument("output_folder_path")
args = parser.parse_args()

punctuation = ".?!,;:-—_…[](){}“”'"


def ModifyFormat(text):
    global count
    global punctuation
    result = ""
    for i in text:
        if i == " " or i == "\n":
            result += " "  # Space detected
            continue
        elif i.isdigit():
            count[0] += 1  # Number detected
            continue
        elif i in punctuation:  # Punctuation detected
            count[1] += 1
            continue
        elif i.isupper():
            count[2] += 1
            result += i.lower()
            continue
        result += i
    result = re.sub(r"\s+", " ", result).rstrip()  # Remove redundant space
    return result


def WordCheck(text):
    global wordlist
    textword = text.split(" ")
    count[3] = len(textword)
    for word in textword:
        if not (word in wordlist):
            count[4] += 1


def WriteFile(filepath):
    global count
    file = open(filepath, "w")
    file.write("j36001zl\n")
    file.write("Formatting ###################\n")
    file.write(f"Number of upper case letters changed: {count[2]}\n")
    file.write(f"Number of punctuations removed: {count[1]}\n")
    file.write(f"Number of numbers removed: {count[0]}\n")
    file.write("Spellchecking ###################\n")
    file.write(f"Number of words: {count[3]}\n")
    file.write(f"Number of correct words: {count[3] - count[4]}\n")
    file.write(f"Number of incorrect words: {count[4]}")
    file.close()


wordfile = open(args.wordlist_path, "r")
wordlist = []
for line in wordfile:
    wordlist.append(line.strip('\n'))

for filename in os.listdir(args.input_folder_path):
    count = [0, 0, 0, 0, 0]  # 0 number, 1 punctuation, 2 uppercase, 3 total words, 4 incorrect words
    inputfile = open(f"{args.input_folder_path}/{filename}", "r")
    WordCheck(ModifyFormat(inputfile.read()))
    WriteFile(f"{args.output_folder_path}/{filename[:-4]}_j36001zl.txt")
    inputfile.close()
