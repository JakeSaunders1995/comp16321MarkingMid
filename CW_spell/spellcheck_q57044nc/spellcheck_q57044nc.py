import sys
import os
import string

bunchOfWords = sys.argv[1]
inputFolder = sys.argv[2]
outputFolder = sys.argv[3]

def checkSpelling(f):
    uncheckedWords = f.read()
    justUncheckedWords = uncheckedWords.rstrip()
    removedNum = 0
    noNum = ""
    for n in justUncheckedWords:
        if not n.isdigit():
            noNum += n
        elif n.isdigit():
            removedNum += 1
    removedPunct = 0
    noPunct = ""
    for char in noNum:
        if char in string.punctuation:
            noPunct += ""
            removedPunct += 1
        elif char not in string.punctuation:
            noPunct += char
    convertedUpperCase = sum(1 for alph in noPunct if alph.isupper())
    alphabetsAndSpace = noPunct.lower()
    splittedToWords = alphabetsAndSpace.split()
    numOfWords = len(splittedToWords)
    numCorrect = 0
    numIncorrect = 0
    listDictWords = []
    engDict = open(bunchOfWords, "r")
    lines = engDict.readlines()
    for line in lines:
        line = line.rstrip()
        listDictWords.append(line)
    for w in splittedToWords:
        if w in listDictWords:
            numCorrect += 1
        elif w not in listDictWords:
            numIncorrect += 1
    engDict.close()
    spellCheckedResult = "q57044nc \nFormatting ################### \nNumber of upper case letters changed: " + str(convertedUpperCase) + "\nNumber of punctuations removed: " + str(removedPunct) + "\nNumber of numbers removed: " + str(removedNum) + "\nSpellchecking ################### \nNumber of words: " + str(numOfWords) + "\nNumber of correct words: " + str(numCorrect) + "\nNumber of incorrect words: " + str(numIncorrect)
    with open(outputFilePath, "w") as o:
        print(spellCheckedResult, file = o)

for fileName in os.listdir(inputFolder):
    if fileName.endswith(".txt"):
        inputFilePath = os.path.join(inputFolder, fileName)
        outputFilePath = str(outputFolder) + "/" + str(fileName[:10]) + "_q57044nc" + str(fileName[10:])
        with open(inputFilePath, "r") as j:
            inputFileName = j
            checkSpelling(inputFileName)
