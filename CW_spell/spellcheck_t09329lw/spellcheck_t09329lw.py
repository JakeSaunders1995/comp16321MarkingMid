import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("txtFile")
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")

parsedArgs = parser.parse_args()

files = os.listdir(parsedArgs.inputFolder)

for x in files:
    if "txt" not in x:
        files.remove(x)

for i in files:

    numbers = "0123456789"
    punctuation = ".?!#€£$%^&*()_+{}|:?><~™‹‹-=[];'/.,\""
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    space = " "

    filepath = (str(parsedArgs.inputFolder) + "/" + i)
    file  = open(str(filepath))
    text = file.readline()

    wordFile = str(parsedArgs.txtFile)
    englishWords = open(wordFile)

    def elipsis(input):
        elipsisCount = 0
        for x in range(0, len(text)):
            if x+2 < len(text):
                if text[x] == ".":
                    if text[x+1] == "." and text[x+2] == ".":
                        elipsisCount +=1
        return elipsisCount

    elipsisCount = elipsis(text)

    def number(input, list):
        stripped = ""
        count = 0
        for char in input:
            if char not in list:
                stripped = stripped + char
            else:
                count += 1
        return stripped, count

    numberOutput = number(text, numbers)
    punctuationOutput = number(numberOutput[0], punctuation)
    capitalsOutput = number(punctuationOutput[0], capitals)

    punctiationTotal = punctuationOutput[1]
    punctiationTotal = punctiationTotal - (elipsisCount * 2)


    final = punctuationOutput[0].lower()

    words = final.split(" ")
    words2 = []
    for x in words:
        if x != "":
            words2.append(x)

    wordList = []
    for x in englishWords:
        if x != " ":
            wordList.append(x)

    def spellCheck():
        correct = 0
        incorrect = 0
        found = False
        for x in range(0, len(words2)):
            for y in range (0, len(wordList)):
                if (str(words2[x])+"\n") == wordList[y]:
                    found = True
                    correct += 1
        return correct

    result = spellCheck()

    file.close()
    englishWords.close()

    filename = i.split(".")

    outputFile = open((str(parsedArgs.outputFolder) + "/" + filename[0] + "_t09329lw.txt"), "x")
    outputFile.write("t09329lw")
    outputFile.write("\nFormatting ###################")
    outputFile.write("\nNumber of upper case letters changed: " + str(capitalsOutput[1]))
    outputFile.write("\nNumber of punctuations removed: " + str(punctiationTotal))
    outputFile.write("\nNumber of numbers removed:: " + str(numberOutput[1]))
    outputFile.write("\nSpellchecking ###################")
    outputFile.write("\nNumber of words: " + str(len(words2)))
    outputFile.write("\nNumber of correct words: " + str(result))
    outputFile.write("\nNumber of incorrect words: " + str(len(words2)-result))

    outputFile.close()