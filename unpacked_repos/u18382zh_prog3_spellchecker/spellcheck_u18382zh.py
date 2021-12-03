import argparse
import os
count1 = ""
count2 = ""
count3 = ""
parser = argparse.ArgumentParser()
parser.add_argument('words', type=str)
parser.add_argument('input', type=str)
parser.add_argument('output', type=str)
args = parser.parse_args()
another = ""

txt = args.words
path = args.input
line = args.output

word = ""
numbernumber = 0
punctuationnumber = 0
uppernumber = 0

Numberofwords = 0
Numberofcorrectwords = 0
Numberofincorrectwords = 0

normal = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
punctuation = '''.?!,:;-_(){}[]'"'''
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



test = os.listdir(path)

if path[-1] != "/":
    path += "/"
if line[-1] != "/":
    line += "/"

for x in test:
    word = ""
    numbernumber = 0
    punctuationnumber = 0
    uppernumber = 0

    Numberofwords = 0
    Numberofcorrectwords = 0
    Numberofincorrectwords = 0
    result = 0
    file = open(path + x, "r")
    Englishtxt = open(txt, "r")
    english = Englishtxt.read()
    w = file.read()
    for a in w:
        if a in normal:
            word += a
        else:
            if a == " ":
                word += a
            if a in letter:
                uppernumber += 1
                word += a
            if a in punctuation:
                punctuationnumber += 1

            if a in number:
                numbernumber += 1
        another += a
    dotnumber = 0
    for z in another:
        if dotnumber == 2 and z == ".":
            punctuationnumber = punctuationnumber - 2
            dotnumber = 0
        elif (z == "." and dotnumber < 2) :
            dotnumber += 1
        elif z != ".":
            dotnumber = 0





    word = word.lower()

    space_number = 0
    correct = ""
    for y in word:
        if y == " " and space_number < 1:
            space_number += 1
            correct += y
        elif y == "\n":
            correct = correct
        elif y != " ":
            space_number = 0
            correct += y
    # print(correct)
    correct = correct.split(" ")
    # print(correct)
    english = english.split("\n")
    for i in correct:
        if i == "" or i == "\n":
            Numberofwords = Numberofwords
        elif i in english:
            Numberofwords += 1
            Numberofcorrectwords += 1
        else:
            Numberofwords += 1
            Numberofincorrectwords += 1

    q = x[0:-4]
    f = open(str(line) + str(q) + "_u18382zh.txt", "w")
    z = '''u18382zh
Formatting################### 
Number of upper case words changed: %s
Number of punctuations removed: %s
Number of numbers removed: %s
Spellchecking ###################
Number of words: %s
Number of correct words: %s
Number of incorrect words: %s
''' % (uppernumber, punctuationnumber, numbernumber, Numberofwords, Numberofcorrectwords, Numberofincorrectwords)
    f.write(z)
    f.close()
    Englishtxt.close()
    file.close()

        








