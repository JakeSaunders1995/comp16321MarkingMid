import argparse
from pathlib import Path

#Set up and parse command line arguments
spellcheckParser = argparse.ArgumentParser('Input and output files.')
spellcheckParser.add_argument("englishWordsPath", type=Path)
spellcheckParser.add_argument("inputFolderPath", type=Path)
spellcheckParser.add_argument("outputFolderPath", type=Path)
args = spellcheckParser.parse_args()

#Open and store the contents of EnglishWords.txt
englishWords = []
try:
    with open(args.englishWordsPath, "r+") as inputEnglishWords:
        for line in inputEnglishWords:
            englishWords.append(line.rstrip())
except:
    print("English words dictionary is not valid.")
    quit()

#Iterate through files in input folder
for file in args.inputFolderPath.glob('*'):
    #Read input file
    try:
        with open(file, "r+") as inputFile:
            cleanedText = inputFile.read().rstrip()
    except:
        print("Input file is not valid.")
        continue

    #Remove numbers, compare length before and after to find out how many were removed
    preNumbersLength = len(cleanedText)
    for char in ["0","1","2","3","4","5","6","7","8","9"]:
        cleanedText = cleanedText.replace(char, "")
    numbersRemoved = preNumbersLength - len(cleanedText)

    #Remove punctuation, compare length before and after to find out how many were removed
    prePuncLength = len(cleanedText)
    for char in ["…","...",".","?","!",",",":",";","-","–","—","(",")","[","]","{","}","'","\""]:
        cleanedText = cleanedText.replace(char, "")
    puncRemoved = prePuncLength - len(cleanedText)

    #Count uppercase letters to change, just in case...
    uppercaseLetters = 0
    for char in cleanedText:
        if char in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
            uppercaseLetters += 1

    #Split the number/punctuation-free text up into words
    wordsList = list(filter(None, cleanedText.split(" ")))

    #Iterate through our words, counting how many are correctly and incorrectly spelt, and how many have uppercase characters in
    correctWords = 0
    incorrectWords = 0
    print(wordsList)
    for word in wordsList:
        if word.lower() in englishWords:
            correctWords += 1
        else:
            incorrectWords += 1

    #Write the analysis of the formatting and spelling
    try:
        args.outputFolderPath.mkdir(exist_ok=True)
        with open(args.outputFolderPath / str(file.stem + "_s13506jc.txt"), "w") as outputFile:
            outputFile.write("s13506jc\nFormatting ###################\nNumber of upper case letters changed: " + str(uppercaseLetters) + "\nNumber of punctuations removed: " + str(puncRemoved) + "\nNumber of numbers removed: " + str(numbersRemoved) + "\nSpellchecking ###################\nNumber of words: " + str(len(wordsList)) + "\nNumber of correct words: " + str(correctWords) + "\nNumber of incorrect words: " + str(incorrectWords))
    except:
        print("Output folder path is not valid.")
        quit()
