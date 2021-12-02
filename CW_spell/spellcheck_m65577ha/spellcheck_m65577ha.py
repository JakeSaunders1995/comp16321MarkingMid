import os, re, argparse


def slice(input):
    return [char for char in input]

parser = argparse.ArgumentParser()
parser.add_argument("library")
parser.add_argument("path")
parser.add_argument("path2")

startDir = os.getcwd()
inputPath = parser.parse_args()
dir_list = os.listdir(inputPath.path)
os.chdir(inputPath.path)

for file in dir_list:
    if file.endswith(".txt"):
        os.chdir(startDir)
        os.chdir(inputPath.path)
        inputFile = open(file)
        input = inputFile.read()
        print(os.linesep + "For the " + file + " file: ")

        slicedInput = slice(input)
        alphabet = [".", "?", "!", ",", ":", ";", "–", "-", "(", ")", 
                        "[", "]", "{", "}", "'", '"']
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        capitalLetters = slice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        currentPosition = 0
        alphabetPosition = 0
        punctuationCounter = 0
        numberCounter = 0
        capitalCounter = 0
        inputLength = len(slicedInput)
        currentLetter = slicedInput[currentPosition]
        while currentPosition != (inputLength):
            currentLetter = slicedInput[currentPosition]
            currentAlphabetLetter = alphabet[alphabetPosition]
            for x in alphabet:
                if (slicedInput[currentPosition] == ".") and ((currentPosition + 2) < inputLength): 
                    if (slicedInput[currentPosition + 1]) == ".":
                        if (slicedInput[currentPosition + 2]) == ".":
                            slicedInput.remove(slicedInput[currentPosition])
                            slicedInput.remove(slicedInput[currentPosition])
                            slicedInput.remove(slicedInput[currentPosition])
                            inputLength = inputLength - 3
                            currentLetter = slicedInput[currentPosition]
                            punctuationCounter = punctuationCounter + 1
                if x == currentLetter:
                    slicedInput.remove(slicedInput[currentPosition])
                    inputLength = inputLength - 1
                    currentPosition = currentPosition - 1
                    currentLetter = slicedInput[currentPosition]
                    punctuationCounter = punctuationCounter + 1
            for x in numbers:
                if x == currentLetter:
                    slicedInput.remove(slicedInput[currentPosition])
                    inputLength = inputLength - 1
                    currentPosition = currentPosition - 1
                    currentLetter = slicedInput[currentPosition]
                    numberCounter = numberCounter + 1
            for x in capitalLetters:
                if x == currentLetter:
                    capitalCounter = capitalCounter + 1
            currentPosition = currentPosition + 1


        unsplicedInput = "".join(slicedInput)
        print(unsplicedInput)
        inputLowercase = unsplicedInput.lower()
        inputWords = re.findall("\w{1,99}", inputLowercase)
        countInputWords = len(inputWords)
        inputWordsLength = len(inputWords)
        os.chdir(startDir)
        englishWordsInput = open(inputPath.library)
        englishList = englishWordsInput.read()
        englishWords = re.findall("\w{1,99}", englishList)
        incorrectWords = [i for i in inputWords if i not in englishWords]
        countIncorrectWords = len(incorrectWords)
        countCorrectWords = len(inputWords) - len(incorrectWords)

        output = ("m65577ha" + os.linesep
        + "Formatting ###################" + os.linesep
        + "Number of upper case letters changed: " + str(capitalCounter) + os.linesep
        + "Number of punctuations removed: " + str(punctuationCounter) + os.linesep
        + "Number of numbers removed: " + str(numberCounter) + os.linesep
        + "Spellchecking ###################" + os.linesep
        + "Number of words: " + str(inputWordsLength) + os.linesep
        + "Number of correct words: "  + str(countCorrectWords) + os.linesep
        + "Number of incorrect words: " + str(countIncorrectWords))
        print(output)

        os.chdir(startDir)
        os.chdir(inputPath.path2)
        filename = file.replace(".txt", "_m65577ha.txt")
        outputFile = open(filename, "w")
        outputFile.write(output)
        inputFile.close()

