import sys
import os
englishWordsL = sys.argv[1]
inDir = sys.argv[2] + "/"
outDir = sys.argv[3] + "/"

enPunct = [".", "?", "!", ",", ":", ";", "-", "(", ")", "[", "]", "{", "}", "'", '"', "…"]

for file in os.listdir(inDir):
	inFile = open(inDir + file, "r")
	text = []
	for line in inFile:
		text.append(line.rstrip("\n"))
	inFile.close()

	numbers = 0
	punct = 0
	uppercase = 0
	correct = 0
	wrong = 0

	for line in range(0, len(text)):
		newLine = ""
		for i in range(0, len(text[line])):
			if text[line][i].isalpha():
				if text[line][i].isupper():
					uppercase += 1
				newLine += text[line][i].lower()
			else:
				if text[line][i].isdigit():
					numbers += 1
				elif text[line][i] == " ":
					newLine += " "
				elif text[line][i] in enPunct:
					punct += 1
				else:
					newLine += text[line][i]

		text[line] = newLine

	englishWords = [line.rstrip("\n") for line in open(englishWordsL, "r")]

	for line in text:
		words = line.split(" ")
		for word in words:
			if word != "":
				if word in englishWords:
					correct += 1
				else: 
					wrong += 1


	outputFileName = file[:-4] + "_r88993ia" + file[-4:]
	outFile = open(outDir + outputFileName, "w")

	toWrite = ["r88993ia",
	"Formatting ###################",
	"Number of upper case letters changed: "+str(uppercase),
	"Number of punctuations removed: "+str(punct),
	"Number of numbers removed: "+str(numbers),
	"Spellchecking ###################",
	"Number of words: "+str(correct+wrong),
	"Number of correct words: "+str(correct),
	"Number of incorrect words: "+str(wrong)]

	for element in toWrite:
		outFile.write(element+"\n")

	outFile.close()