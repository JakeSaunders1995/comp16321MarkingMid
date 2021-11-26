from sys import *
from os import listdir

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
morseDict = {".-" : "a", "-..." : "b", "-.-." : "c", "-.." : "d", "." : "e",
"..-." : "f", "--." : "g", "...." : "h", ".." : "i", ".---" : "j", "-.-" : "k",
".-.." : "l", "--" : "m", "-." : "n", "---" : "o", ".--." : "p", "--.-" : "q",
".-." : "r", "..." : "s", "-" : "t", "..-" : "u", "...-" : "v", ".--" : "w",
"-..-" : "x", "-.--" : "y", "--.." : "z", ".----" : "1", "..---" : "2", 
"...--" : "3", "....-" : "4", "....." : "5", "-...." : "6", "--..." : "7",
"---.." : "8", "----." : "9", "-----" : "0", "/" : " "}

def convertHex(hexList):
    convertedString = ""
    for hex in hexList:
        convertedString += bytes.fromhex(hex).decode("ASCII")
    return convertedString.lower()

def convertCaesar(caesarList):
    convertedString = ""
    for caesarWord in caesarList:
        for letter in caesarWord:
            convertedString += alphabet[alphabet.find(letter)-3]
        convertedString += " "
    return convertedString.lower()

def convertMorse(morseList):
    convertedString = ""
    for morse in morseList:
        convertedString += morseDict.get(morse)
    return convertedString

for item in sorted(listdir("./"+argv[1])):
    inputFile = open(argv[1]+"/"+item, "r")
    outputFile = open(argv[2]+"/"+item[:-4]+"_y77372db"+".txt", "w")
    fileText = inputFile.read()
    if fileText[0] == "H":
        outputFile.write(convertHex(fileText[4:].split(" ")))
        outputFile.close()
        inputFile.close()
    elif fileText[0] == "C":
        outputFile.write(convertCaesar(fileText.strip()[18:].split(" ")))
        outputFile.close()
        inputFile.close()
    elif fileText[0] == "M":
        outputFile.write(convertMorse(fileText[11:].split(" ")))
        outputFile.close()
        inputFile.close()
  