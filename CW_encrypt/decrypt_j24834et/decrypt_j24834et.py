import argparse as pa
import os

def getStartPosition():
    found = False
    tempPointer = 0
    while not found and tempPointer < len(inputLine):
        if inputLine[tempPointer] == ':':
            found = True
            return (tempPointer+1)
        else:
            if tempPointer < len(inputLine):
                tempPointer += 1
            else:
                return None

def hexadecimal():
    global pointer
    readfile = open(outputFileLocation, 'w')
    while pointer < len(inputLine):
        cipher = inputLine[pointer:pointer+2]
        total = 0
        num = [0,0]
        for i in range(2):
            if cipher[i] == 'a':
                num[i] = 10
            elif cipher[i] == 'b':
                num[i] = 11
            elif cipher[i] == 'c':
                num[i] = 12
            elif cipher[i] == 'd':
                num[i] = 13
            elif cipher[i] == 'e':
                num[i] = 14
            elif cipher[i] == 'f':
                num[i] = 15
            else:
                num[i] = cipher[i]
        total = int(num[0])*16 + int(num[1])
        checkUpper = chr(total)
        if checkUpper >= 'a' and checkUpper <= 'z':
            readfile.write(checkUpper)
        elif checkUpper >= 'A' and checkUpper <= 'Z':
            lowerChar = chr(total + 32)
            readfile.write(lowerChar)
        elif checkUpper == ' ':
            readfile.write(' ')
        pointer += 3
    readfile.close()

def caesar():
    global pointer
    text = ''
    readfile = open(outputFileLocation, 'w')
    while pointer < len(inputLine):
        if inputLine[pointer] >=  'a' and inputLine[pointer] <= 'z':
            temp = ord(inputLine[pointer])
            if inputLine[pointer] >= 'a' and inputLine[pointer] <= 'c':
                temp += 26
            new = chr(temp - 3)
            text += new
        elif inputLine[pointer] >=  'A' and inputLine[pointer] <= 'Z':
            temp = ord(inputLine[pointer])
            if inputLine[pointer] >= 'A' and inputLine[pointer] <= 'C':
                temp += 26
            new = chr(temp + 29)
            text += new
        else:
            text += (inputLine[pointer])
        pointer += 1
    for i in range(len(text)):
        if text[i].isalpha() or text[i].isdigit() or text[i] == ' ':
            readfile.write(text[i])
    readfile.close()


key = 'abcdefghijklmnopqrstuvwxyz0123456789.?!(@:=-),`_$;/"'
morseCode = ['.-','-...','-.-.','-..','.','..-.','--.','....',
          '..','.---','-.-','.-..','--','-.','---','.--.',
          '--.-','.-.','...','-', '..-','...-','.--','-..-',
          '-.--','--..','-----','.----','..---','...--',
          '....-','.....','-....','--...','---..','----.','.-.-.-',
          '..--..','-.-.--','-.--.','.--.-.','---...','-...-','-....-','-.--.-','--..--',
          '.----.','..--.-','...-..-','-.-.-.','-..-.','.-..-.']

def morse():
    global pointer
    readfile = open(outputFileLocation, 'w')
    while pointer < len(inputLine):
        if inputLine[pointer] == '/':
            readfile.write(' ')
            pointer += 2
            continue
        charEnd = False
        startPointer = pointer
        while not charEnd and pointer < len(inputLine):
            if inputLine[pointer] != ' ' and inputLine[pointer] != '/':
                pointer += 1
            elif inputLine[pointer] == ' ':
                thisMorseCode = inputLine[startPointer:pointer]
                charEnd = True
            else:
                continue
        for i in range(len(key)):
            if thisMorseCode == morseCode[i]:
                result = key[i]
        pointer += 1
        readfile.write(result)
    readfile.close()

parser = pa.ArgumentParser()
parser.add_argument("inputpath", type=str)
parser.add_argument("outputpath", type=str)
args = parser.parse_args()
InputPath = args.inputpath
OutputPath = args.outputpath

dirs = os.listdir(InputPath)
for file in dirs:
    fileLocation = InputPath + '/' + file
    readfile = open(fileLocation, 'r')
    inputLine = readfile.read()
    readfile.close()
    fileWithoutTxt = file[0:len(file) - 4]
    outputFileLocation = OutputPath + '/' + fileWithoutTxt + '_j24834et.txt'
    pointer = 0
    if inputLine[pointer] == 'H':
        if getStartPosition() != None:
            pointer = getStartPosition()
        else:
            pointer = 4
        hexadecimal()
    elif inputLine[pointer] == 'C':
        if getStartPosition() != None:
            pointer = getStartPosition()
        else:
            pointer = 18
        caesar()
    elif inputLine[pointer] == 'M':
        if getStartPosition() != None:
            pointer = getStartPosition()
        else:
            pointer = 11
        morse()