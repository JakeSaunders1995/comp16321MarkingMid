import sys
import os 
import re

inputFilePath = sys.argv[2]
outputFilePath = sys.argv[3]
englishWordsFilePath = sys.argv[1]

inputFiles = []
for file in os.listdir(inputFilePath):
    if file.endswith(".txt"):
        inputFiles.append(file.split(".")[0])
englishWords = []

def AddEnglishWords():
    global englishWords
    inputFile = open(englishWordsFilePath)
    for line in inputFile:
        line = line.rstrip()
        englishWords.append(line)
    inputFile.close()   
AddEnglishWords()

def spellChecker(fileName):
    inputLines = []
    inputFile = open(os.path.join(inputFilePath, fileName + ".txt"))
    for line in inputFile:
        line = line.rstrip()
        inputLines.append(line)
    inputFile.close()

    transformedWords = []

    noWords = 0
    noUpperCaseWords = 0
    noOfNumbers = 0
    noOfPunc = 0
    noIncorrectWords = 0
    noOfEllipsis = 0
    noOfFullStops = 0
    noOfCorrectPunc = 0

    for i in range(len(inputLines)):
        characters = list(inputLines[i])
        noOfEllipsis += inputLines[i].count("...")
        for j in range(len(characters)):
            if re.search("[0-9]", characters[j]):
                noOfNumbers += 1
            if re.search("[^A-Za-z0-9#@. ]", characters[j]): #doesnt look for full stops (.)
                noOfPunc += 1 
            if re.search("[\.]", characters[j]):
                noOfFullStops += 1
            if re.search("[A-Z]", characters[j]):
                noUpperCaseWords += 1
        formatedLine = re.sub("[^A-Za-z ]", "", inputLines[i])
        formattedWords = formatedLine.split(" ")
        for j in formattedWords:
            if j != "":
                transformedWords.append(str(j.lower()))

    noWords = len(transformedWords)    
    for i in transformedWords:
        if not(i in englishWords):
            noIncorrectWords += 1

    noOfCorrectPunc = noOfPunc + noOfEllipsis + (noOfFullStops - (3*noOfEllipsis))

    outputFile = open(os.path.join(outputFilePath, str(str(fileName) + "_v78643ld.txt")), "w")
    outputFile.write("v78643ld" + "\n")
    outputFile.write("Formatting ###################" + "\n")
    outputFile.write("Number of upper case letters changed: " + str(noUpperCaseWords) + "\n")
    outputFile.write("Number of punctuations removed: " + str(noOfCorrectPunc) + "\n")
    outputFile.write("Number of numbers removed: " + str(noOfNumbers) + "\n")
    outputFile.write("Spellchecking ###################" + "\n")
    outputFile.write("Number of words: " + str(noWords) + "\n")
    outputFile.write("Number of correct words: " + str(noWords - noIncorrectWords) + "\n")
    outputFile.write("Number of incorrect words: " + str(noIncorrectWords) + "\n")
    outputFile.close()

for i in inputFiles:
    spellChecker(i)
