import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("englishPath")
parser.add_argument("inputPath")
parser.add_argument("outputPath")
args = parser.parse_args()

inputFolder = str(args.inputPath)
listFiles = os.listdir(inputFolder)

for x in listFiles:
    if ".txt" not in x:
        listFiles.remove(x)

noOfFiles = len(listFiles)

for y in range(noOfFiles):
    inputFile = open(inputFolder+"/"+listFiles[y])
    string = inputFile.read()

    lowerString = string.lower()
    formattedString = ""
    lengthOfString = len(lowerString)

    alphabet = "abcdefghijklmnopqrstuvwxyz "
    capAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    punctuation = ".!?,;:-–[]{}()'@£$%^&*€#<>|/`~≤≥\""

    numOfCaps = 0
    numOfNums = 0
    numOfPuncs = 0

    # count how many caps, nums and punc in string and produces a formatted string
    for i in range(lengthOfString):
        if (lowerString[i] in alphabet):
            formattedString = formattedString + lowerString[i]
        if (string[i] in capAlphabet):
            numOfCaps = numOfCaps + 1
        if (string[i] in numbers):
            numOfNums = numOfNums + 1
        if (string[i] in punctuation):
            if(i + 2 < lengthOfString):
                isEllipsis = string[i]+string[i+1]+string[i+2]
                print(isEllipsis)
                if (isEllipsis == "..."):
                    numOfPuncs = numOfPuncs - 2
            numOfPuncs = numOfPuncs + 1

    words = formattedString.split(" ")

    englishFile = open(str(args.englishPath))
    readData = englishFile.readlines()

    found = 0
    notfound = 0
    numberOfWords = len(words)
    emptyWords = 0

    # gets rid of empty words i.e ''
    for x in range(numberOfWords):
        word = words[x]
        if (emptyWords + x + 1) > numberOfWords - 1:
            break
        if words[x] == '':
            del words[x]
            emptyWords = emptyWords + 1

    # spellcheck
    for x in words:
        if (x + "\n") in readData:
            found = found + 1
        else:
            notfound = notfound + 1

    fileName = ""
    name = str(listFiles[y])

    for i in name:
        if i == ".":
            break
        else:
            fileName = fileName + i

    # output file
    outputfile = open((str(args.outputPath)+"/"+fileName+"_x48913aw.txt"), "x")
    outputfile.write("x48913aw")
    outputfile.write("\nFormatting ###################")
    outputfile.write("\nNumber of upper case words transformed: " + str(numOfCaps))
    outputfile.write("\nNumber of punctuation’s removed: " + str(numOfPuncs))
    outputfile.write("\nNumber of numbers removed: " + str(numOfNums))
    outputfile.write("\nSpellchecking ###################")
    outputfile.write("\nNumber of words in file: " + str(numberOfWords - emptyWords))
    outputfile.write("\nNumber of correct words in file: " + str(found))
    outputfile.write("\nNumber of incorrect words in file: " + str(notfound))
