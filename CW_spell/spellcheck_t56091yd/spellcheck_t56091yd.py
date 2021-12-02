import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("englishWordsPath", help = "english words path")
parser.add_argument("inputFolderPath", help = "input file path")
parser.add_argument("outputFolderPath", help = "output file path")
args = parser.parse_args()

englishWordsPath = args.englishWordsPath
inputFolderPath = args.inputFolderPath
outputFolderPath = args.outputFolderPath
inputFiles = os.listdir(inputFolderPath)
z = 0

while z < len(inputFiles):
    inputFile = inputFiles[z]
    inputFilePath = (inputFolderPath + "/" + inputFile)
    

    f = open(englishWordsPath)
    words = f.read()
    wordCheck = words.split()

    f = open(inputFilePath)
    content = f.read()

    a = 0
    capNum = 0
    punNum = 0
    numNum = 0
    corNum = 0
    incorNum = 0
    num = "0123456789"
    pun = "!$%&'()*+,-./:;<=>?[\]^_`{|}~"
    cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while a < len(content):
        if content[a] in num:
            contentList = list(content)
            del contentList[a]
            content = "".join(contentList)
            numNum += 1
        elif content[a] in pun:
            contentList = list(content)
            del contentList[a]
            content = "".join(contentList)
            punNum += 1
        elif content[a] in cap:
            b = ord(content[a])
            c = b + 32
            contentList = list(content)
            contentList[a] = chr(c)
            content = "".join(contentList)
            capNum += 1
        else:
            a += 1

    contentCheck = content.split()
    wordNum = len(contentCheck)
    d = 0
    while d < len(contentCheck):
        e = 0
        while e < len(wordCheck):
            if contentCheck[d] in wordCheck:
                corNum += 1
                break
            else:
                incorNum += 1
                break
            e += 1
        d += 1

    answerLine1 = "t56091yd" + "\n"
    answerLine2 = "Formatting ###################" + "\n"
    answerLine3 = "Number of upper case letters changed: " + str(capNum) + "\n"
    answerLine4 = "Number of punctuations removed: " + str(punNum) + "\n"
    answerLine5 = "Number of numbers removed: " + str(numNum) + "\n"
    answerLine6 = "Spellchecking ###################" + "\n"
    answerLine7 = "Number of words: " + str(wordNum) + "\n"
    answerLine8 = "Number of correct words: " + str(corNum) + "\n"
    answerLine9 = "Number of incorrect words:" + str(incorNum) + "\n"


    outputFile = (inputFile[:-4] + "_t56091yd" + inputFile[-4:])
    outputFilePath = (outputFolderPath + "/" + outputFile)
    answerFile = open(outputFilePath, "w")
    answerFile.write(answerLine1 + answerLine2 + answerLine3 + answerLine4 + answerLine5 + answerLine6 + answerLine7 + answerLine8 + answerLine9)
    z += 1