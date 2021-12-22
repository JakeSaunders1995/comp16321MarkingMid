import argparse
import os
files = []
sortedfiles = []
b = 0
parser = argparse.ArgumentParser()
parser.add_argument('docsfile')
parser.add_argument('inputpath')
parser.add_argument('outputpath')
args = parser.parse_args()
inputstream = args.inputpath
outputstream = args.outputpath
wordfile = args.docsfile
#print(args.inputpath)
outputfile = ""
username = "e11226oc"
numbersremoved = 0
punctuationremoved = 0
capitalsremoved = 0
wordsamount = 0
correctwords = 0
incorrectwords = 0
words = []
theWords = []
correct = False

for file in os.listdir(inputstream):
    files.append(os.path.join(inputstream, file))

sortedfiles = sorted(files)

file = open(wordfile , "r")
for line in file:
    line = line.rstrip()
    theWords.append(line)

for x in range(len(sortedfiles)):
    working = open(sortedfiles[x], "r")
    plaintext = working.read()

    for x in range(len(plaintext)):
        letter = plaintext[x]
        dec = ord(letter)
        if plaintext[x].isnumeric() == True:
            numbersremoved += 1
        elif plaintext[x] == "." or plaintext[x] == "?" or plaintext[x] == "!" or plaintext[x] == "," or plaintext[x] == ":" or plaintext[x] == ";" or plaintext[x] == "-" or plaintext[x] == "--" or plaintext[x] == "(" or plaintext[x] == ")" or plaintext[x] == "[" or plaintext[x] == "]" or plaintext[x] == "{" or plaintext[x] == "}" or plaintext[x] == "'":
            punctuationremoved += 1
        elif dec >= 65 and dec <= 90:
            capitalsremoved += 1
        elif plaintext[x] == '"':
            punctuationremoved += 2

    for y in range(len(plaintext)):
        letter = plaintext[y]
        dec = ord(letter)
        if plaintext[y].isnumeric() == True:
            plaintext = plaintext.replace(plaintext[y], " ")
        elif plaintext[y] == "." or plaintext[y] == "?" or plaintext[y] == "!" or plaintext[y] == "," or plaintext[y] == ":" or plaintext[y] == ";" or plaintext[y] == "-" or plaintext[y] == "--" or plaintext[y] == "(" or plaintext[y] == ")" or plaintext[y] == "[" or plaintext[y] == "]" or plaintext[y] == "{" or plaintext[y] == "}" or plaintext[y] == '"':
            plaintext = plaintext.replace(plaintext[y], " ")
        elif dec >= 65 and dec <= 90:
            dec += 32
            plaintext = plaintext.replace(plaintext[y], chr(dec))
        elif plaintext[y] == "#" or plaintext[y] == "@":
            plaintext = plaintext.replace(plaintext[y], " ")

    words = plaintext.split()
    wordsamount = len(words)

    for z in range(len(words)):
        correct = False
        for a in range(len(theWords)):
            if words[z] == theWords[a]:
                correctwords += 1
                correct = True
        if correct == False:
            incorrectwords += 1

    print(username)
    print("Formatting ###################")
    print("Number of uppercase words changed: " , capitalsremoved)
    print("Number of punctuations removed: " , punctuationremoved)
    print("Number of numbers removed: " , numbersremoved)
    print("Spellchecking ###################")
    print("Number of words: " , wordsamount)
    print("Number of correct words: " , correctwords)
    print("Number of incorrect words: " , incorrectwords)

    out1 = ('Formatting ###################')
    out2 = 'Number of uppercase words changed: ' + str(capitalsremoved)
    out3 = 'Number of punctuations removed: ' + str(punctuationremoved)
    out4 = 'Number of numbers removed: ' + str(numbersremoved)
    out5 = 'Spellchecking ###################'
    out6 = 'Number of words: ' + str(wordsamount)
    out7 = 'Number of correct words: ' + str(correctwords)
    out8 = 'Number of incorrect words: ' + str(incorrectwords)
    b += 1
    outputfile = str(outputstream)+'/test_file'+str(b)+'_e11226oc.txt'
    writeout = open(outputfile, "w")
    writeout.writelines(str(username))
    writeout.writelines("\n")
    writeout.writelines(str(out1))
    writeout.writelines("\n")
    writeout.writelines(str(out2))
    writeout.writelines("\n")
    writeout.writelines(str(out3))
    writeout.writelines("\n")
    writeout.writelines(str(out4))
    writeout.writelines("\n")
    writeout.writelines(str(out5))
    writeout.writelines("\n")
    writeout.writelines(str(out6))
    writeout.writelines("\n")
    writeout.writelines(str(out7))
    writeout.writelines("\n")
    writeout.writelines(str(out8))
    capitalsremoved = 0
    punctuationremoved = 0
    numbersremoved = 0
    wordsamount = 0
    correctwords = 0
    incorrectwords = 0
