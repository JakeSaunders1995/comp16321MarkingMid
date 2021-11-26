import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('englishwordstxt', type=str)
parser.add_argument('inputPath', type=str)
parser.add_argument('outputPath', type=str)
args = parser.parse_args()

englishwordstxt = args.englishwordstxt
inputPath = args.inputPath
outputPath = args.outputPath

def spellcheck(inputFilename):
    #Read in input file
    #Separate it into words (split by space)
    with open(inputPath + "/" + inputFilename) as file:
        words = file.read().split()

    upperCounter = 0
    punctCounter = 0
    numCounter = 0

    #Iterate through each word
    for i in range(0, len(words)):
        formattedWord = ""
    #Iterate through each character in word
        for c in words[i]:
    #If character is not alphanumeric (punctuation), increment punctuation counter
            if c.isalnum() == False:
                punctCounter += 1
    #If character is a number, increment number counter
            elif c.isnumeric():
                numCounter += 1
    #If character is uppercase, increment uppercase counter and add lower cased letter to formattedWord
            elif c.isupper():
                upperCounter += 1
                formattedWord += c.lower()
    #Else (if alphanumeric and not a number and lowercase) add character to formattedWord
            else:
                formattedWord += c
    #Replace word with formattedWord
        words[i] = formattedWord

    wordCounter = 0
    correctCounter = 0
    incorrectCounter = 0

    #Read EnglishWords.txt into an array (split by newline)
    with open(englishwordstxt) as file:
        englishWords = file.read().splitlines()
    #Iterate through formatted words from input file
    for word in words:
    #If string not empty
        if word != "":
    #Increment word counter
            wordCounter += 1
    #If word is in english words array, increment correct word counter
            if word in englishWords:
                correctCounter += 1
    #Else, increment incorrect word counter
            else:
                incorrectCounter += 1

    #Output with correct file name
    outputFilename = inputFilename[0:-4] + "_w25478ia.txt"

    output = ["w25478ia",
            "\nFormatting ###################",
            "\nNumber of upper case letters changed: " + str(upperCounter),
            "\nNumber of punctuations removed: " + str(punctCounter),
            "\nNumber of numbers removed: " + str(numCounter),
            "\nSpellchecking ###################",
            "\nNumber of words: " + str(wordCounter),
            "\nNumber of correct words: " + str(correctCounter),
            "\nNumber of incorrect words: " + str(incorrectCounter)]
    with open(outputPath + "/" + outputFilename, "w") as file:
        file.writelines(output)

dirs = os.listdir(inputPath)

for file in dirs:
    if file[-4:] == ".txt":
        spellcheck(file)

