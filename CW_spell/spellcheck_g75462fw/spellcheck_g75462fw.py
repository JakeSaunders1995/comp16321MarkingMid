#!/usr/bin/env python3

'''
COMP16321 Mid Term
Program 3 - Spellchecker
Felix Waller
'''

import os
import re
import argparse

def getOutputFile(inputFileName, outputFolder): 
    return outputFolder + ("" if outputFolder[-1] == "/" else "/") + inputFileName[0 : inputFileName.find(".txt")] + "_g75462fw.txt"

def spellcheck(inputFilePath, inputFileName, englishWords, outputFolder):
    with open(inputFilePath) as file:
        input = file.read()

    capitalsRemoved = len(re.findall(r'[A-Z]', input))
    input = input.lower()

    input, ellipses = re.subn(r'\.\.\.|\. \. \.', '', input)

    input, punctuationRemoved = re.subn(r'[\.\?\!\,\:\;\-\[\]\{\}\(\)\'\"\…\–\—]', '', input)
    
    input, numbersRemoved = re.subn(r'[0-9]', '', input)

    input = input.split()

    with open(englishWords) as file:
        dict = [word.strip() for word in file]

    correctWords = 0

    for word in input:
        if word in dict:
            correctWords += 1

    with open(getOutputFile(inputFileName, outputFolder), "w") as file:
        file.write(f"g75462fw\nFormatting ###################\nNumber of upper case letters changed: {capitalsRemoved}\nNumber of punctuations removed: {punctuationRemoved + ellipses}\nNumber of numbers removed: {numbersRemoved}\nSpellchecking ###################\nNumber of words: {len(input)}\nNumber of correct words: {correctWords}\nNumber of incorrect words: {len(input) - correctWords}\n")

parser = argparse.ArgumentParser()
parser.add_argument("englishWords")
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
args = parser.parse_args()

for entry in os.scandir(args.inputFolder):
    if ".txt" in entry.name:
        spellcheck(entry.path, entry.name, args.englishWords, args.outputFolder)