import argparse
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument("englishWords")
parser.add_argument("inputDirectory")
parser.add_argument("outputDirectory")
parsed_args = parser.parse_args(sys.argv[1:])

alphabet = 'abcdefghijklmnopqrstuvwxyz'
wordList = [i.strip() for i in open(parsed_args.englishWords, 'r').readlines()]


def spellCheck(strInp):
    uppercase, punctuation, numbers, correctWords, incorrectWords = 0, 0, 0, 0, 0
    newStr = ""
    for character in strInp:
        if character.isdigit():
            numbers += 1
        elif character in alphabet.upper():
            uppercase += 1
            newStr += character.lower()
        elif character in alphabet or character == ' ':
            newStr += character
        else:
            punctuation += 1
    for word in newStr.split():
        if word in wordList:
            correctWords += 1
        else:
            incorrectWords += 1
    return {"uppercase": uppercase, "punctuation": punctuation, "numbers": numbers, "correctWords": correctWords,
            "incorrectWords": incorrectWords}


def getFiles(dirPath):
    return next(os.walk(dirPath))[2]


files = getFiles(parsed_args.inputDirectory)
for file in files:
    inp = open(f"{parsed_args.inputDirectory}\{file}", 'r')
    out = open(f"{parsed_args.outputDirectory}\{file.replace('.txt', '')}_k63434dr.txt", 'w+')
    results = spellCheck(inp.read())
    out.write(f"k63434dr \nFormatting ################### \nNumber of upper case "
              f"words changed: {results['uppercase']} \nNumber of punctuations removed: {results['punctuation']} \n"
              f"Number of numbers removed: {results['numbers']} \nSpellchecking ################### \nNumber of words: {results['correctWords'] + results['incorrectWords']} \nNumber of correct "
              f"words: {results['correctWords']} \nNumber of incorrect words: {results['incorrectWords']}")
    out.close()
