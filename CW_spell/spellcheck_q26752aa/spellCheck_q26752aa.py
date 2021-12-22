import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('englishwords', type=str)
parser.add_argument('input', type=str)
parser.add_argument('output', type=str)
args = parser.parse_args()

# renames original .txt file to include _q26752aa
def get_name(file_name):
    for i in range(len(file_name)):
        if file_name[i] == '.':
            output_name = file_name[0:i]
            return output_name + '_q26752aa.txt'
#-----------------------------------------------#
punctuation = '''\,<>.'"/?@#$%^&*_~!()-[]{};:'''
numbers = '0123456789'

os.chdir(args.input)
for file in os.listdir():
    #initialisation
    total_words = 0
    correct_words = 0
    incorrect_words = 0
    punc_removed = 0
    nums_removed = 0
    caps_removed = 0
    if file.endswith(".txt"):
        filepath = args.input + '/' + file
        f = open(filepath, "r")
        input = f.read()
        f.close()
    #removes numbers and punctuation
    for char in input:
        if char in punctuation:
            input = input.replace(char,"")
            punc_removed += 1
        if char in numbers:
            input = input.replace(char,"")
            nums_removed += 1
        if char.isupper() == True:
            input = input.replace(char,char.lower())
            caps_removed += 1

    f = open(args.englishwords,"r")
    englishwords = f.read().split()
    f.close()
    for word in input.split():
        if word in englishwords:
            correct_words += 1
        else:
            incorrect_words += 1
    total_words = correct_words + incorrect_words

    filepath = args.output + '/' + get_name(file)
    print(input.split())
    w = open(filepath, "w")
    w.write("q26752aa\n")
    w.write("Formatting ###################\n")
    w.write("Number of upper case words changed: "+str(caps_removed)+"\n")
    w.write("Number of punctuations removed: "+str(punc_removed)+"\n")
    w.write("Number of numbers removed: "+str(nums_removed)+"\n")
    w.write("Spellchecking ###################\n")
    w.write("Number of words: "+str(total_words)+"\n")
    w.write("Number of correct words: "+str(correct_words)+"\n")
    w.write("Number of incorrect words: "+str(incorrect_words)+"\n")
    w.close()
