import argparse
import os

parser = argparse.ArgumentParser(description = 'Path')
parser.add_argument('wordpath', type=str, help='englishword file path')
parser.add_argument('inputpath', type=str, help='input file path')
parser.add_argument('outputpath', type=str, help='output file path')
args = parser.parse_args()

WordPath = args.wordpath
InputPath = args.inputpath
OutputPath = args.outputpath
dirs1 = os.listdir(args.inputpath)

TheWords = []
file = open(WordPath, "r")
for line in file:
    line = line.rstrip()
    TheWords.append(line)
file.close

for filein in dirs1:
    f = open(InputPath + "/" + filein)
    text = f.read()
    upper = 0
    punctuation = 0
    number = 0
    total = 0
    correct = 0
    incorrect = 0
    ellipsis = 0
    
    Text = text.split()

    for i in range(len(text)):
        if ord(text[i]) >= 48 and ord(text[i]) <= 57:
            number += 1
        if ord(text[i]) >= 65 and ord(text[i]) <= 90:
            upper += 1
        if (ord(text[i]) >= 33 and ord(text[i]) <= 34) or (ord(text[i]) >= 39 and ord(text[i]) <= 41) or (ord(text[i]) >= 44 and ord(text[i]) <= 45) or (ord(text[i]) >= 58 and ord(text[i]) <= 59) or (ord(text[i]) == 63) or (ord(text[i]) == 91) or (ord(text[i]) == 93) or (ord(text[i]) == 123) or (ord(text[i]) == 125):
            punctuation += 1
        if i+4 <= len(text):
            if ord(text[i]) == 46 and ord(text[i+1]) == 46 and ord(text[i+2]) == 46:
                punctuation += 1
                ellipsis += 1
        if ord(text[i]) == 46:
            punctuation += 1
    punctuation -= 3*ellipsis

    for i in Text:
        message = ""
        for j in i:
            if ord(j) >= 65 and ord(j) <= 90:
                message = message + chr(ord(j) + 32)
            elif ord(j) >= 97 and ord(j) <= 122:
                message = message + j
            else:
                message = message
        if len(message) >= 1:
            if ord(message[0]) >= 97 and ord(message[0]) <= 122:
                total += 1
            if message in TheWords:
                correct += 1
            else:
                incorrect += 1
    
    ff = open(OutputPath + "/" + filein[:-4] + "_j95271zf.txt","a")
    ff.write("j95271zf")
    ff.write("\nFormatting ###################")
    ff.write("\nNumber of upper case letters changed: " + str(upper))
    ff.write("\nNumber of punctuations removed: " + str(punctuation))
    ff.write("\nNumber of numbers removed: " + str(number))
    ff.write("\nSpellchecking ###################")
    ff.write("\nNumber of words: " + str(total))
    ff.write("\nNumber of correct words: " + str(correct))
    ff.write("\nNumber of incorrect words: " + str(incorrect))
    ff.close()
    f.close()

