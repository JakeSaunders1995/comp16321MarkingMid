import string
from sys import * 
from os import listdir
from string import punctuation

englishList = open(argv[1], "r").read().split()

def main(fileText):
    correctWords = 0
    incorrectWords = 0
    punctuationCount = 0
    numberCount = 0
    capitalCount = 0
    wordList = fileText.split(" ")
    newWordList = []
    for word in wordList:
        for letter in word:
            if letter in string.punctuation:
                punctuationCount += 1
                word = word.replace(letter, "")
            elif letter in "1234567890":
                numberCount += 1
                word = word.replace(letter, "")
            elif letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                capitalCount += 1
                word = word.replace(letter, letter.lower())
        newWordList.append(word)    
    for newWord in newWordList:
        if newWord in englishList:
            correctWords += 1
        elif newWord == "":
            pass
        elif newWord == "\n":
            pass
        else:
            incorrectWords += 1
    results = ("y77372db\nFormatting ###################"+
                "\nNumber of upper case letters changed: "+str(capitalCount)+
                "\nNumber of punctuations removed: "+str(punctuationCount)+
                "\nNumber of numbers removed: "+str(numberCount)+
                "\nSpellchecking ###################"+
                "\nNumber of words: "+str((correctWords+incorrectWords))+
                "\nNumber of correct words: "+str(correctWords)+
                "\nNumber of incorrect words: "+str(incorrectWords))
    return results
    

for item in sorted(listdir("./"+argv[2])):
    inputFile = open(argv[2]+"/"+item, "r")
    outputFile = open(argv[3]+"/"+item[:-4]+"_y77372db"+".txt", "w")
    outputFile.write(main(inputFile.read()))
    outputFile.close()
    inputFile.close()