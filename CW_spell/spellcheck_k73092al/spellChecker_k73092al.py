import re

def readDictionaryFile(dictionaryFilename):
	dictionaryWords = []
	inputFile = open(dictionaryFilename, "r")
	for line in inputFile:
		word = line.strip()
		dictionaryWords.append(word)
	inputFile.close
	return dictionaryWords

def readTextFile(textFilename):
	words = []
	inputFile = open(textFilename, "r")
	for line in inputFile:
		wordsOnLine = line.strip().split()
		for word in wordsOnLine:
			words.append(word.strip(".,!:;?0123456789").lower())
	inputFile.close()
	return words


def findErrors(dictionaryWords, textWords):
	misspelledWords = []
	for word in textWords:
		if word not in dictionaryWords:
			misspelledWords.append(word)
	return misspelledWords

def printErrors(errorList):
	print("Number of incorrect words: ")
	incorrectWords = []
	for word in errorList:
		if word != "":
			incorrectWords.append(word.strip()) 
	print(len(incorrectWords))


def printWords(textList):
	print("Number of words: ")
	correctWords = []
	for word in textList:
		if word != "":
			correctWords.append(word.strip())
	print(len(correctWords))

def printCorrectWords(correctWordsList):
	print("Number of correct words: ", correctWordsList)


def main():
	dictionaryFile = input("Please enter the dictionary file: ")
	textFile = input("Please enter the text file: ")
	dictionaryList = readDictionaryFile(dictionaryFile)
	textList = readTextFile(textFile)
	errorList = findErrors(dictionaryList, textList)
	correctWordsList = (len(textList))-(len(errorList))
	print("k73092al")
	print("Spell Checking###############")
	printWords(textList)
	printCorrectWords(correctWordsList)
	printErrors(errorList)

main()
