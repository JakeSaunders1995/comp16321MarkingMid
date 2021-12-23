import os
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("englishwords")
parser.add_argument("inputfolder")
parser.add_argument("outputfolder")
args = parser.parse_args()

def AccessFolder(inputFolder, englishWords, outputFolder):
    for file in os.listdir(inputFolder):
        wordList, symbolCount, numberCount, capitalCount = RemoveNonLetters(os.path.join(inputFolder, file))
        #print(wordList)
        correctWords, incorrectWords, wordCount = spellCheck(wordList, englishWords)
        print("Total words:", wordCount)
        print("Correct words:", correctWords)
        print("Incorrect words:", incorrectWords)
        print("Symbols removed:", symbolCount)
        print("Numbers removed:", numberCount)
        print("Uppercases lowered:", capitalCount)

        filename = os.path.basename(os.path.join(inputFolder, file))
        prefix = filename.split(".txt")
        outputFileName = prefix[0] + "_r94627as.txt"
        WriteFile(outputFolder, outputFileName, wordCount, correctWords, incorrectWords, symbolCount, capitalCount, numberCount)

def RemoveNonLetters(file):
    with open(file, "r") as textToChange:
        text = textToChange.read()
        textToChange.close()
        #print(text)
        char = 0
        #for char in range(len(text)):
        numberCount = 0
        capitalCount = 0
        while char < len(text):
            try:
                int(text[char])
                print(text[char])
                text = text.replace(text[char],"", 1)
                numberCount+=1
            except:
                if text[char] != text[char].lower():
                    text = text.replace(text[char], text[char].lower(), 1)
                    capitalCount += 1
                    #print("I lowered it!!!!!!")
                char+=1
        ellipsis = re.findall(r'(\w+)\.{3,}',text)
        ellipsisCount = len(ellipsis)
        countToSubtract = ellipsisCount*2
        symbols = re.findall(r'[^\w @\n\u2260]', text)
        symbolCount = len(symbols) - countToSubtract

        text = re.sub(r'[^\w ]', '', text)
        return text.split(" "), symbolCount, numberCount, capitalCount

def spellCheck(wordsToCheck, englishWords):
    with open(englishWords, "r") as correctSpelling:
        dictionary = correctSpelling.read()
        dictionary = dictionary.split("\n")
        correctSpelling.close()
    #for every word in words to check
    incorrectWords = 0
    correctWords = 0
    wordCount = 0
    for checkWord in wordsToCheck:
        if checkWord == "":
            continue
        wordCorrect = False
        #check with every word in english words
        for correctWord in dictionary:
            if correctWord == checkWord:
                wordCorrect = True
                break
        if wordCorrect:
            correctWords += 1
        else:
            incorrectWords += 1
        wordCount += 1
    return correctWords, incorrectWords, wordCount

def WriteFile(outputFolder, filename, wordCount, correctWords, incorrectWords, symbolCount, capitalCount, numberCount):
    with open(os.path.join(outputFolder, filename), "w") as outputFile:
        outputFile.writelines(["r94627as\n",
        "Formatting ###################\n",
        "Number of upper case letters changed: "+str(capitalCount)+"\n",
        "Number of punctuations removed: "+str(symbolCount)+"\n",
        "Number of numbers removed: "+str(numberCount)+"\n",
        "Spellchecking ###################\n",
        "Number of words: "+str(wordCount)+"\n",
        "Number of correct words: "+str(correctWords)+"\n",
        "Number of incorrect words: "+str(incorrectWords)])
        outputFile.close()


AccessFolder(args.inputfolder, args.englishwords, args.outputfolder)
