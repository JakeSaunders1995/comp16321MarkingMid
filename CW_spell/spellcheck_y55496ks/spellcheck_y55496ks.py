import sys
import string
import re

spellCheckFile = sys.argv[1]
inputFile = sys.argv[2]
outputFile = sys.argv[3]

file = open(inputFile, "r")
for line in file:
    textFile = line
file.close()

numberOfPunc = 0
numberOfInt = 0
numberOfUpper = 0
numberOfWords = 0
numberOfCorrectW = 0
numberOfWrongW = 0
for i in range(len(textFile)):
    if textFile[i] in string.punctuation:
        numberOfPunc = numberOfPunc + 1
    if textFile[i].isdigit():
        numberOfInt = numberOfInt + 1
    if textFile[i].isupper():
        numberOfUpper = numberOfUpper + 1
textFile = textFile.translate(str.maketrans('', '', string.punctuation))
textFile = re.sub(r'[0-9]+', '', textFile)
textFile = textFile.lower()

checkString = textFile.split(" ")
try:
    while True:
        checkString.remove('')
except ValueError:
    pass


for i in range(len(checkString)):
    numberOfWords = numberOfWords + 1
    spelling = False
    file = open(spellCheckFile, "r")
    for line in file:
        if checkString[i].strip() == line.strip():
            spelling = True 
    file.close()
    if spelling == True:
        numberOfCorrectW = numberOfCorrectW + 1
    else:
        numberOfWrongW = numberOfWrongW + 1

file = open(outputFile, "w")
file.write("y55496ks" + '\n')
file.write("Formatting ###################" + '\n')
file.write("Number of upper case words changed: " + str(numberOfUpper) + '\n')
file.write("Number of punctuations removed: " + str(numberOfPunc) + '\n')
file.write("Number of numbers removed: " + str(numberOfInt) + '\n')
file.write("Spellchecking ###################" + '\n')
file.write("Number of words: " + str(numberOfWords) + '\n')
file.write("Number of correct words: " + str(numberOfCorrectW) + '\n')
file.write("Number of incorrect words: " + str(numberOfWrongW) + '\n')
file.close()
