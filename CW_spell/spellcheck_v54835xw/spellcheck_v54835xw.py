import argparse
import os

def SpellCheck(pathIn, pathOut, fileName, EnglishWord):
    lowerLetterList = "abcdefghijklmnopqrstuvwxyz"
    upperLetterList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numberList = "1234567890"
    numOfNum = 0
    numOfUpper = 0
    numOfPunctuation = 0
    numOfCorrect = 0
    numOfWorng = 0
    OpenInputFile = open(pathIn, "r")
    Info = OpenInputFile.read()

    for i in range(len(Info)):
        if Info[i] in numberList:
            Info = Info.replace(Info[i], "?", 1)
            numOfNum += 1
        elif Info[i] in upperLetterList:
            position = upperLetterList.find(Info[i])
            Info = Info.replace(Info[i], lowerLetterList[position], 1)
            numOfUpper += 1
        elif Info[i] == " ":
            continue
        elif Info[i] not in lowerLetterList:
            if Info[i] == "@" or "#":
                Info = Info.replace(Info[i], "?", 1)
            else:
                Info = Info.replace(Info[i], "?", 1)
                numOfPunctuation += 1

    wordList = Info.replace("?", "").split(" ")

    a = 0
    for i in range(len(wordList)):
        if wordList[a] == "":
            wordList.pop(a)
        else:
            a += 1

    OpenInputFile.close()

    numOfWord = len(wordList)

    OpenEnglishWord = open(EnglishWord, "r")
    EnglishWordList = OpenEnglishWord.read().splitlines()

    for i in range(len(wordList)):
        if wordList[i] in EnglishWordList:
            numOfCorrect += 1
        else:
            numOfWorng += 1

    fileOutput = open(pathOut + "/" + fileName + "_v54835xw" + ".txt", "a")
    fileOutput.write("Formatting ###################")
    fileOutput.write("\nNumber of upper case words transformed:" + str(numOfUpper))
    fileOutput.write("\nNumber of punctuation’s removed:" + str(numOfPunctuation))
    fileOutput.write("\nNumber of numbers removed:" + str(numOfNum))
    fileOutput.write("\nSpellchecking ###################")
    fileOutput.write("\nNumber of words in file:" + str(numOfWord))
    fileOutput.write("\nNumber of correct words in file:" + str(numOfCorrect))
    fileOutput.write("\nNumber of incorrect words in file:" + str(numOfWorng))
    fileOutput.close()

def OpenFolder(EnglishWord, pathIn, pathOut):
    path = os.path.abspath(pathIn)
    outputPathFolder = os.path.abspath(pathOut)
    fileList = os.listdir(path)
    for i in range(len(fileList)):
        SpellCheck(path + "/" + fileList[i], outputPathFolder, fileList[i], EnglishWord)

parser = argparse.ArgumentParser(description="Decrypt")
parser.add_argument("EnglishWord", type=str)
parser.add_argument("pathIn", type=str)
parser.add_argument("pathOut", type=str)
args = parser.parse_args()

OpenFolder(args.EnglishWord, args.pathIn, args.pathOut)