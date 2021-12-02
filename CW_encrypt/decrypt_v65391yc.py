import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('inputPath', type=str)
parser.add_argument('outputPath', type=str)
args = parser.parse_args()

fileList = os.listdir(args.inputPath)

morseDict = {
    ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g",
    "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n",
    "---": "o", ".--．": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
    "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",

    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

    "/": " ",
}

caesarList = [
    "z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l",
    "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a", "z", "y", "x",
]

def changeName(inputName):
    nameList = list(inputName)
    nameList.insert(-4, '_v65391yc')
    outputName = ''.join(nameList)
    return outputName

def startChange(input):
    start = 0
    for item in input:
        if item == ':':
            start = start + 1
            break
        else:
            start = start + 1
    input = input[start:]
    return input

def modeCheck(input):
    if input[0] == 'M':
        mode = 'M'
    elif input[0] == 'C':
        mode = 'C'
    elif input[0] == 'H':
        mode = 'H'
    return mode

def morse(input):
    result = ''
    inputList = input.split()
    for item in inputList:
        character = morseDict[item]
        result = result + character
    return result

def caesar(input):
    result = ''
    for item in input:
        if item in caesarList:
            position = caesarList.index(item)
            character = caesarList[position + 3]
            result = result + character
        else:
            result = result + item
    return result

def hex(input):
    result = ''
    inputList = input.split()
    for item in inputList:
        ascii = int(item, 16)
        character = chr(ascii)
        result = result + character
    return result

def fileWrite(input, outputPath):
    print(input)
    newfile = open(outputPath, 'w')
    newfile.write(str(input))
    newfile.close()


for file in fileList:
    inputPath = args.inputPath + '/' + file
    openFile = open(inputPath)
    content = openFile.read()

    outputPath = args.outputPath + '/' + changeName(file)

    if modeCheck(content) == 'M':
        fileWrite(morse(startChange(content)), outputPath)
    elif modeCheck(content) == 'C':
        fileWrite(caesar(startChange(content)), outputPath)
    elif modeCheck(content) == 'H':
        fileWrite(hex(startChange(content)), outputPath)

    openFile.close()
