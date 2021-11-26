import sys
import os

outputFolder = sys.argv[-1]
inputFolder = sys.argv[-2]
englishFile = sys.argv[-3]


if not os.path.isdir(outputFolder):
	os.mkdir(outputFolder)
else:
	pass


def SpellCheck(inputFile,englishFile):

	textString = inputFile

	wordList = open(englishFile, "r")
	wordList = wordList.read()
	wordList = wordList.strip()
	wordList = wordList.split()



	lowerCount = 0
	punctCount = 0
	numCount = 0
	punctuationAndSymbols = [".","?","!",",",":",";","-","–","—","(",")","{","}","[","]","'",'"',"..."]

	for char in textString:
		if char.isdigit():
			textString = textString.replace(char,"")
			numCount += 1

	for char in textString:
		if char in punctuationAndSymbols:
			textString = textString.replace(char,"")
			punctCount += 1

	for char in textString:
		if char.isupper():
			lower_char = char.lower()
			textString = textString.replace(char,lower_char)
			lowerCount += 1

	textString = " ".join(textString.split())
	textString = textString.split()

	correctWords = 0
	incorrectWords = 0

	for char in textString:
		if char in wordList:
			correctWords += 1
		else:
			incorrectWords += 1

	a = 's11642lf\n'
	b = 'Formatting ###################\n'
	c = 'Number of upper case letters changed: '+str(lowerCount)+'\n'
	d = 'Number of punctuations removed: '+str(punctCount)+'\n'
	e = 'Number of numbers removed: '+str(numCount)+'\n'

	f = 'Spellchecking ###################\n'
	g = 'Number of words: '+str(len(textString))+'\n'
	h = 'Number of correct words: '+str(correctWords)+'\n'
	i = 'Number of incorrect words: '+str(incorrectWords)+'\n'

	return [a,b,c,d,e,f,g,h,i]

for testFile in os.listdir(inputFolder):
	with open(os.path.join(inputFolder,testFile), "r") as inputFile:
		inputFile = inputFile.read()

		output = SpellCheck(inputFile,englishFile)

		testVal = testFile.rstrip(".txt")
		testFileAndID = testVal + "_s11642lf.txt"

		with open(os.path.join(outputFolder,testFileAndID),"w+") as outputFile:
			for item in output:
				outputFile.write(item)