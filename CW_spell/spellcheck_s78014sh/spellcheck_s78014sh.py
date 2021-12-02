import sys
import os
textFile = sys.argv[1]
inputFolder = sys.argv[2] #change to two once using text file
outputFolder = sys.argv[3]


def removeWhitespace(words):
	newlist = []
	for word in words:
		tempWord = ""
		for char in word:
			if char == "":
				continue
			else:
				tempWord += char
		newlist.append(tempWord)

	for element in newlist:
		if not element:
			newlist.remove(element)

	return newlist
	

for inputFile in os.listdir(inputFolder):

	with open(inputFolder + "/" + inputFile, 'r') as i:
		inptxt = i.readlines()[0]
		inpWords = inptxt.split(" ")
		
		outputTxt = ""
		numRemoved = 0
		puncRemoved = 0
		upperRemoved = 0
		wordCount = 0
		correctWords = 0
		incorrectWords = 0

		for x in range(len(inpWords)):
			for y in range(len(inpWords[x])):
				currentChar = inpWords[x][y]
				if currentChar in ['0','1','2','3','4','5','6','7','8','9']:
					numRemoved += 1
				elif currentChar.isalnum() == False:
					puncRemoved += 1
				elif currentChar.isupper():
					outputTxt += currentChar.lower()
					upperRemoved += 1
				else:
					outputTxt += currentChar
			outputTxt += "."

		

		formattedWords = removeWhitespace(outputTxt.split("."))

		
		wordCount = len(formattedWords)

		

		with open(textFile, 'r') as o:
			englishDict = []
			lines = o.readlines()
			for element in lines:
				englishDict.append(element.strip())
			
			for word in formattedWords:
				if word in englishDict:
					correctWords += 1
				else:
					incorrectWords += 1



		
		with open(outputFolder + "/" + inputFile[:-4] + "_s78014sh.txt", 'w+') as p:
			p.write("s78014sh\n")
			p.write("Formatting ###################\n")
			p.write("Number of upper case words changed: " + str(upperRemoved) + "\n")
			p.write("Number of punctuations removed: " + str(puncRemoved) + "\n")
			p.write("Number of numbers removed: " + str(numRemoved) + "\n")
			p.write("Spellchecking ###################\n")
			p.write("Number of words: " + str(wordCount) + "\n")
			p.write("Number of correct words: " + str(correctWords) + "\n")
			p.write("Number of incorrect words: " + str(incorrectWords) + "\n")
