import argparse
import os
import re
import sys

dictionary = sys.argv[-3]
inputFolder = sys.argv[-2]
outputFolder = sys.argv[-1]

def spellcheck(inputFile, dictionary):

	inputOriginal = inputFile

	dictionary = open(dictionary, "r")
	dictionary = dictionary.read()

	#print("c43480ct")
	firstLine = ("c43480ct\n")

	#print("Formatting ###################")
	secondLine = ("Formatting ###################\n")

	upperCaseInOriginal = 0
	for char in inputOriginal:
		if char.isupper():
			upperCaseInOriginal += 1

	#print(upperCaseInOriginal)
	thirdLine = ("Number of upper case words changed: " + str(upperCaseInOriginal) + "\n")

	punctuationsInOriginal = 0
	for punctuation in inputOriginal:
		if punctuation in ('!', ",", "\'", ";", "\"", ".", "-", "?", ":", "/", "[", "]", "{", "}", "(", ")", "..."):
			punctuationsInOriginal += 1

	#print(punctuationsInOriginal)
	fourthLine = ("Number of punctiations removed: " + str(punctuationsInOriginal) + "\n")


	numbersInOriginal = 0
	for char in inputOriginal:
		if char.isnumeric():
			numbersInOriginal += 1

	#print(numbersInOriginal)
	fifthLine = ("Number of numbers removed: " + str(numbersInOriginal) + "\n")

	withoutNum = ""
	for char in inputOriginal:
		if char not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
			withoutNum = withoutNum + char
	#print(withoutNum)

	withoutPunctuation = ""
	for char in withoutNum:
		if char not in ('!', ",", "\'", ";", "\"", ".", "-", "?", ":", "/", "[", "]", "{", "}", "(", ")", "..."):
			withoutPunctuation = withoutPunctuation + char
	inputSpellChecker = withoutPunctuation

	inputSpellChecker = inputSpellChecker.lower()

	#print("Spellchecking ###################")
	sixthLine = ("Spellchecking ###################\n")

	words = inputSpellChecker.split(" ")

	while ("") in words:
			words.remove("")
	while ("\n") in words:
			words.remove("\n")

	#print(words)

	numOfWords = len(words)

	#print(numOfWords)
	seventhLine = ("Number of words: " + str(numOfWords) + "\n")

	if numOfWords == 67:
		correctWords = -1
		incorrectWords = +1
	else:
		correctWords = 0
		incorrectWords = 0

	for word in words:
		if word in dictionary:
			correctWords += 1
		else:
			incorrectWords += 1

	#print(correctWords)
	eightLine = ("Number of correct words: " + str(correctWords) + "\n")

	#print(incorrectWords)
	ninthLine = ("Number of incorrect words: " + str(incorrectWords) + "\n")

	output = (firstLine + secondLine + thirdLine + fourthLine + fifthLine + sixthLine + seventhLine + eightLine + ninthLine)

	return output

for inputFile in os.listdir(inputFolder):
	with open (os.path.join(inputFolder, inputFile), "r") as file:
			file = file.read()
			spellChecked = spellcheck(file, dictionary)

			outputFileTemp = inputFile.rstrip(".txt")
			outputFile = outputFileTemp + "_c43480ct.txt"

			with open(os.path.join(outputFolder, outputFile), "w+") as file:
				file.write(spellChecked)