import sys
import string

fileName = sys.argv[0]
username = fileName[-11:-3]
englishWordsFilePath = sys.argv[1]
inputFilePath = sys.argv[2]
outputFilePath = sys.argv[3]

with open(inputFilePath, 'r') as f:
    inputFileData = f.read()

dataList = list(inputFileData)

alphaString = ""

upperCounter = 0
numberCounter = 0
punctuationCounter = 0

for i in range(0, len(dataList)):
    if dataList[i] in string.punctuation:
        punctuationCounter += 1
    elif (dataList[i].isalpha() and dataList[i].upper() == dataList[i] and dataList[i] != " "):
        upperCounter += 1
        alphaString += dataList[i].lower()
    elif dataList[i] in string.digits:
        numberCounter += 1
    else:
        alphaString += dataList[i]

listOfWords = alphaString.split(" ")
for word in listOfWords:
    if word == "":
        listOfWords.remove(word)

alphaString = ""

for word in listOfWords:
    alphaString += word + " "

numberOfWords = len(listOfWords)

with open(englishWordsFilePath, 'r') as f:
    englishWordsListTemp = f.readlines()

englishWordsList = []
correctWords = 0
incorrectWords = 0


for word in englishWordsListTemp:
    englishWordsList.append(word.strip("\n"))

for word in listOfWords:
    if word in englishWordsList:
        correctWords += 1
    else:
        incorrectWords += 1

outputString = username + "\n"
outputString += "Formatting ##################\n"
outputString += "Number of upper case letters changed: " + str(upperCounter) + "\n"
outputString += "Number of punctuations removed: " + str(punctuationCounter) + "\n"
outputString += "Number of numbers removed: " + str(numberCounter) + "\n"
outputString += "Spellchecking ##################\n"
outputString += "Number of words: " + str(numberOfWords) + "\n"
outputString += "Number of correct words: " + str(correctWords) + "\n"
outputString += "Number of incorrect words: " + str(incorrectWords)

with open(outputFilePath, "w") as f:
    f.write(outputString)

