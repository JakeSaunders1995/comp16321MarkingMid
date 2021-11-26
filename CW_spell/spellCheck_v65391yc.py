import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('englishWords', type=str)
parser.add_argument('inputPath', type=str)
parser.add_argument('outputPath', type=str)
args = parser.parse_args()

fileList = os.listdir(args.inputPath)

def changeName(inputName):
    nameList = list(inputName)
    nameList.insert(-4, '_v65391yc')
    outputName = ''.join(nameList)
    return outputName

def ascii(input):
    result = ord(input)
    return result

def spellChecker(input):
    result = ''
    transformed = 0
    punctuation = 0
    number = 0
    for item in input:
        if 65 <= ascii(item) <= 90:
            character = chr(ascii(item) + 32)
            result = result + character
            transformed = transformed + 1
        elif 97 <= ascii(item) <= 122:
            result = result + item
        elif 48 <= ascii(item) <= 57:
            number = number + 1
        elif 33 <= ascii(item) <=47 or 58 <= ascii(item) <= 64 or 91 <= ascii(item) <= 96 or 123 <= ascii(item) <= 126:
            punctuation = punctuation + 1
        elif ascii(item) == 32:
            result = result + ' '

    transformedWrite = 'Number of upper case words transformed: ' + str(transformed) + '\n'
    punctuationWrite = 'Number of punctuation\'s removed: ' + str(punctuation) + '\n'
    numberWrite = 'Number of numbers removed: ' + str(number) + '\n'

    newfile = open(outputPath, 'w')
    newfile.write('v65391yc\n')
    newfile.write('Formatting ###################\n')
    newfile.write(str(transformedWrite))
    newfile.write(str(punctuationWrite))
    newfile.write(str(numberWrite))
    newfile.close()
    return result

with open(args.englishWords) as englishFile:
    englishWords = []
    for line in englishFile:
        englishWords.append(line.strip('\n'))

    for file in fileList:
        inputPath = args.inputPath + '/' + file
        openFile = open(inputPath)
        content = openFile.read()

        outputPath = args.outputPath + '/' + changeName(file)

        checkList = spellChecker(content).split()
        countWord = 0
        rightWord = 0
        wrongWord = 0

        for item in checkList:
            countWord = countWord + 1
            for word in englishWords:
                if item == word:
                    rightWord = rightWord + 1

            wrongWord = countWord - rightWord

        countWrite = 'Number of words in file: ' + str(countWord) + '\n'
        rightWrite = 'Number of correct words in file: ' + str(rightWord) + '\n'
        wrongWrite = 'Number of incorrect words in file: ' + str(wrongWord) + '\n'

        againfile = open(outputPath, 'a')
        againfile.write('Spellchecking ###################\n')
        againfile.write(str(countWrite))
        againfile.write(str(rightWrite))
        againfile.write(str(wrongWrite))
        againfile.close()

        openFile.close()
