import sys
import re
import os

def getArguments():
    arguments = sys.argv
    words = arguments[1]
    source = arguments[2]
    destination = arguments[3]
    return words, source, destination

def readFile(fileName):
    file = open(fileName)
    content = file.readlines()
    file.close()
    return content

def readWords(path):
    os.chdir(path)
    file = open("EnglishWords.txt")
    content = file.readlines()
    file.close()
    return content

def format(text):
    formatedText = ""
    digitsRemoved = 0
    puncRemoved = 0
    upCaseLowered = 0
    for letter in text:
        change = False
        aVal = ord(letter)
        if (letter.isdigit()):
            # numbers
            digitsRemoved += 1
            change = True
            ()
        if ((aVal == 33) or (aVal == 34) or (aVal >= 39 and aVal <= 41) or (aVal >= 44 and aVal <= 46) or (aVal == 58) or (aVal == 59) or (aVal == 63) or (aVal == 91) or (aVal == 93) or (aVal == 123) or (aVal == 125)):
            # puncuation
            puncRemoved += 1
            change = True
        if (aVal >= 65 and aVal <= 90):
            # uppercase letters changed to lowercase
            upCaseLowered += 1
            formatedText += chr(aVal + 32)
            change = True
        if (not change):
            formatedText += letter
    return formatedText, digitsRemoved, puncRemoved, upCaseLowered

def wordAnalysis(engWords, text):
    wordList = text.split()
    wordCount = len(wordList)
    correctWords = 0
    incorrectWords = 0
    engList = []
    # removes \n from all words in english dictionary
    for element in engWords:
        engList.append(element.replace("\n",""))

    for word in wordList:
        if (engList.count(str(word)) != 0):
            correctWords += 1
        else:
            incorrectWords += 1
    return wordCount, correctWords, incorrectWords

def formatResults(uppercaseTransformed, puncuationRemoved, numbersRemoved, wordCount, correctWords, incorrectWords):
    return ["f18903ls", "Formatting ###################", "Number of upper case letters changed: " + str(uppercaseTransformed), "Number of puncuations removed: " + str(puncuationRemoved), "Number of numbers removed: " + str(numbersRemoved), "Spellchecking ###################", "Number of words: " + str(wordCount), "Number of correct words: " + str(correctWords), "Number of incorrect words: " + str(incorrectWords)]

def writeResults(fileName, inputPath, outputPath, result):
    newName = fileName.replace(".txt", "_f18903ls.txt")
    os.chdir(outputPath)
    file = open(newName, "w")
    for line in result:
        file.write(line + "\n")
    file.close()
    os.chdir(inputPath)

#main
w, s, d = getArguments()

#calculate number of files in dir and adds to fileList and creates relative paths
fileList = []
pathOfCurrentFile = os.path.dirname(os.path.abspath("spellcheck_f18903ls.py"))
wordPath = os.path.join(pathOfCurrentFile, w)
sourcePath = os.path.join(pathOfCurrentFile, s)
destinationPath = os.path.join(pathOfCurrentFile, d)
for file in os.listdir(os.path.join(sourcePath)):
    fileList.append(file)

words = readFile(wordPath)

os.chdir(sourcePath)
for file in fileList:
    text = readFile(file)[0].strip()
    ft, numbersRemoved, puncuationRemoved, uppercaseLowered = format(text)
    wordCount, correctWords, incorrectWords = wordAnalysis(words, ft)
    output = formatResults(uppercaseLowered, puncuationRemoved, numbersRemoved, wordCount, correctWords, incorrectWords)
    writeResults(file, sourcePath, destinationPath, output)
