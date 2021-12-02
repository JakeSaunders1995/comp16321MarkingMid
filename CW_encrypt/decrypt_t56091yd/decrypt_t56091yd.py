import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("inputFolderPath", help = "input file path")
parser.add_argument("outputFolderPath", help = "output file path")
args = parser.parse_args()

inputFolderPath = args.inputFolderPath
outputFolderPath = args.outputFolderPath
inputFiles = os.listdir(inputFolderPath)
z = 0

while z < len(inputFiles):
    inputFile = inputFiles[z]
    inputFilePath = (inputFolderPath + "/" + inputFile)
    f = open(inputFilePath)
    content = f.read()

    a = 0

    while content[a] != ":":
        a += 1

    firstDigit = content[a + 1]
    b = a + 1
    mainPart = content[b:]
    answer = ""

    if ord(firstDigit) > 47 and ord(firstDigit) < 58:
        c = 0
        d = 0
        mainBody = []
        while c < len(mainPart):
            digit = (mainPart[c] + mainPart[c + 1])
            c += 3
            mainBody.append(digit)
        while d < len(mainBody):
            answer += chr(int(mainBody[d], 16))
            d += 1

    elif ord(firstDigit) > 96 and ord(firstDigit) < 123 :
        c = 0
        check = "defghijklmnopqrstuvwxyz"

        while c < len(mainPart):
            if mainPart[c] in check:
                d = mainPart[c]
                e = ord(d) - 3
                answer += chr(e)
            elif mainPart[c] in "a":
                answer += chr(120)
            elif mainPart[c] in "b":
                answer += chr(121)
            elif mainPart[c] in "c":
                answer += chr(122)
            elif mainPart[c] in " ":
                answer += " "
            else:
                break
            c += 1

    elif ord(firstDigit) == 45 or ord(firstDigit) == 46 :
        c = 0
        d = 0
        mainBody = []
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-", "..-","...-",".--","-..-","-.--","--..","-----",".----","..---","...--","....-",".....","-....","--...","---..","----."]
        mainPart += " "
        answer = ""
        
        mainBody = mainPart.split()
        
        while d < len(mainBody):
            e = 0
            while e < len(morseCode):
                if mainBody[d] == morseCode[e]:
                    answer += alphabet[e]
                elif mainBody[d] == "/":
                    answer += " "
                    break
                e += 1
            d += 1


    outputFile = (inputFile[:-4] + "_t56091yd" + inputFile[-4:])
    outputFilePath = (outputFolderPath + "/" + outputFile)
    f = open(outputFilePath, "w")
    f.write(answer.lower())
    z += 1