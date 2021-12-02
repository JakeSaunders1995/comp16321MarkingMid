import sys
import os
import re


for textFile in os.listdir(sys.argv[2]):
	filename = (sys.argv[2]+"/"+textFile)
	file = open(filename, "r")

	oneLine = ""
	firstLine = True
	for line in file:
		exampleInput = line.strip()
		newlineRemoved = re.sub("\n", " ", exampleInput)
		if not firstLine:
			oneLine += " "
		firstLine = False
		oneLine += newlineRemoved

	formatted = ""
	numbersRemoved = 0
	punctuationsRemoved = 0
	uppercaseRemoved = 0


	for i in range(len(oneLine)):
		if oneLine[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			numbersRemoved += 1
		elif oneLine[i] in [".", "?", "!", ",", ":", ";", "-", "–", "—", "[", "]", "{", "}", "(", ")", "'", '"', "…"]:
			punctuationsRemoved += 1
		elif oneLine[i].isupper():
			uppercaseRemoved += 1
			formatted += oneLine[i].lower()
		elif oneLine[i] == " ":
			if formatted[-1:] == " ":
				pass
			else:
				formatted += " "
		elif oneLine[i] == "\n":
			pass
		else:
			formatted += oneLine[i]
	
	formatted = formatted.strip()
	# wordCount = 1
	# for i in range(len(formatted)):
	# 	if formatted[i] == " ":
	# 		wordCount += 1

	correctWords = 0
	incorrectWords = 0
	currentWord = ""
	englishWords = open(sys.argv[1], "r")

	englishDictionary = []
	for line in englishWords:
		englishDictionary.append(line.strip())

	for i in range(len(formatted)):
		if formatted[i] != " ":
			currentWord += formatted[i]
		elif formatted[i] == " ":
			if currentWord in englishDictionary:
				correctWords += 1
			else:
				incorrectWords += 1
			currentWord = ""
		if (i + 1) == len(formatted):
			if currentWord in englishDictionary:
				correctWords += 1
			else:
				incorrectWords += 1
			currentWord = ""

	wordCount = correctWords + incorrectWords




	finalOutput = ("p35799ap\nFormatting ###################\nNumber of upper case letters changed: "+str(uppercaseRemoved)+"\nNumber of punctuations removed: "+str(punctuationsRemoved)+"\nNumber of numbers removed: "+str(numbersRemoved)+"\nSpellchecking ###################\nNumber of words: "+str(wordCount)+"\nNumber of correct words: "+str(correctWords)+"\nNumber of incorrect words: "+str(incorrectWords))
	outputFile = textFile[:-4]
	outputFile += "_p35799ap.txt"
	outputFile = (sys.argv[3]+"/"+outputFile)
	writeFile = open(outputFile, "w")
	writeFile.write(finalOutput)