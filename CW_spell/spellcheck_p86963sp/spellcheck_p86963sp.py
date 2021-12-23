import sys
import re

wordFile = sys.argv[1]
inputFile = sys.argv[2]
outputFile = sys.argv[3]

dictionary = open(wordFile, "r")
inputF = open(inputFile, "r")
outputF = open(outputFile, "w")

words = dictionary.readlines()
words = [s.strip("\n") for s in words]

string = inputF.read()
punctuation = re.sub(r'\W+', '', string)

numbersRemoved = 0
punctuationRemoved = 0
toLowerCase = 0
for i in string:
    if (i.isdigit()):
        string = string.replace(i, "", 1)
        numbersRemoved += 1
    if (i not in punctuation and i != " "):
        string = string.replace(i, "", 1)
        punctuationRemoved += 1
    if (i.isupper()):
        string = string.replace(i, i.lower(), 1)
        toLowerCase += 1

correctWords = 0
incorrectWords = 0
wordsOfString = string.split()

for word in wordsOfString:
    if word in words:
        correctWords += 1
    else:
        incorrectWords += 1

outputF.write("p86963sp")
outputF.write("\nFormatting ###################")
outputF.write("\nNumber of upper case words changed: " + str(toLowerCase))
outputF.write("\nNumber of punctuations removed:" + str(punctuationRemoved))
outputF.write("\nNumber of numbers removed:" + str(numbersRemoved))
outputF.write("\nSpellchecking ###################")
outputF.write("\nNumber of words:" + str(len(wordsOfString)))
outputF.write("\nNumber of correct words:" + str(correctWords))
outputF.write("\nNumber of incorrect words: " + str(incorrectWords))
