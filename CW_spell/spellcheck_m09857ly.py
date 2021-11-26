from argparse import ArgumentParser
import os


parser = ArgumentParser(description="Take in files")
parser.add_argument("words", help="Take in words file.")
parser.add_argument("input", help="Take in input folder.")
parser.add_argument("output", help="Take in output folder.")
args = parser.parse_args()
folders = args

def checker(filename):
    f = open(f'{folders.input}/{filename}', "r")
    line = f.readlines()
    temp = []
    for element in line:
        temp.append(element.replace("\n", ""))
    line = "".join(temp)
    f2 = open(folders.words, "r")
    words = [line.rstrip() for line in f2]
    numbers = "0123456789"
    alphabet = "abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    text = ""
    p_count = 0
    n_count = 0
    trans_count = 0
    correct = 0
    incorrect = 0
    check = 0
    for char in line:
        if char in numbers:
            n_count += 1
            check = 0
        elif char not in alphabet:
            if char == ".":
                check += 1
                if check == 3:
                    check = 0
                    p_count -= 2
            else:
                check = 0
            p_count += 1
        else:
            check = 0
            text += char

    text = text.split()
    for i in range(len(text)):
        if (not text[i].islower() and not text[i].isupper()) or text[i].isupper():
            for char in text[i]:
                if char in alphabet[26:-1]:
                    trans_count += 1
            text[i] = text[i].lower()
            

    word_count = len(text)

    for word in text:
        if word in words:
            correct += 1
        else:
            incorrect += 1

    text_output = f'm09857ly\nFormatting ###################\nNumber of upper case letters changed: {trans_count}\nNumber of punctuations removed: {p_count}\n'
    text_output += f'Number of numbers removed: {n_count}\nSpellchecking ###################\nNumber of words: {word_count}\n'
    text_output += f'Number of correct words: {correct}\nNumber of incorrect words: {incorrect}'

    with open(f'{folders.output}/{filename[:-4]}_m09857ly.txt', "w") as output:
        output.write(text_output)
        output.close()
try:
    os.mkdir(folders.output)
except:
    pass

for file in os.listdir(folders.input):
    checker(file)
