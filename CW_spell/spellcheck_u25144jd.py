import sys
import string
import os
import re

def spellChecker(text, outputFile):
    outputFile.write("u25144jd")
    outputFile.write("\nFormatting ###################")

    removedNumbersCount = 0
    removedPunctuationCount = 0
    removedUpperCaseCount = 0
    newString = ""
    # Checks for elipse, adds one to counter and then removes them from text
    if "..." in text:
        for i in re.findall("\.\.\.", text):
            removedPunctuationCount = removedPunctuationCount + 1
        text = text.replace("...", "")

    # Loops through every character in text and performs a certain action depending
    # on character
    for char in text:
        if char.isupper():
            newString = newString + char.lower()
            removedUpperCaseCount = removedUpperCaseCount + 1
        elif char.isdigit():
            removedNumbersCount = removedNumbersCount + 1
        elif char in ".?!,:;—-()[]{}'\"":
            removedPunctuationCount = removedPunctuationCount + 1
        else:
            newString = newString + char

    wordList = newString.split()

    outputFile.write("\nNumber of upper case letters changed: " + str(removedUpperCaseCount))
    outputFile.write("\nNumber of punctuations removed: " + str(removedPunctuationCount))
    outputFile.write("\nNumber of numbers removed: " + str(removedNumbersCount))

    wordCount = 0
    wordCorrectCount = 0
    wordIncorrectCount = 0

    outputFile.write("\nSpellchecking ###################")
    # Cycles through words in the word list created in formatting
    for word in wordList:
        if word in englishDictionairy:
            wordCorrectCount = wordCorrectCount + 1
        else:
            wordIncorrectCount = wordIncorrectCount + 1

    outputFile.write("\nNumber of words: " + str(len(wordList)))
    outputFile.write("\nNumber of correct words: " + str(wordCorrectCount))
    outputFile.write("\nNumber of incorrect words: " + str(wordIncorrectCount))

# Opens EnglishWords.txt and creates a list of words
inputFile1 = open(sys.argv[1], "r")
englishDictionairy = inputFile1.read().split()
# Creates a list of the inputs files
inputFiles = os.listdir(sys.argv[2])
# Cycles through input files, creates corresponding output file and excutes
# spellChecker for each input file
for inputFile in inputFiles:
    outputFile = open(sys.argv[3] + inputFile[:-4] + "_u25144jd.txt", "x")
    spellChecker(open(sys.argv[2] + inputFile, "r").read(), outputFile)
