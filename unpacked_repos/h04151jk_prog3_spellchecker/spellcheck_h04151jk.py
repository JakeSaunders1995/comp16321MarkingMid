import argparse
import os
import string

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("wordList")
arg_parser.add_argument("inFolder")
arg_parser.add_argument("outFolder")
arguments = arg_parser.parse_args()

wordList = arguments.wordList
inFolder = arguments.inFolder
outFolder = arguments.outFolder

#form dictionary
wordFile = open(wordList ,"r")
words = wordFile.readlines()

for i in range(len(words)):
	words[i] = words[i].strip("\n")

wordFile.close()

for root, dirs, files in os.walk(inFolder, topdown=False):
	for name in files:
		fileInName = os.path.join(root, name)

		fileIn = open(fileInName, "r")
		startText = fileIn.read().split(" ")
		fileIn.close()

		numUpper, numPunc, numDigit, numIncWords = 0,0,0,0
		for i in range(len(startText)-1, -1, -1):
			for j in range(len(startText[i])-1, -1, -1):		
			
				#check for uppercase in word
				if startText[i][j] in string.ascii_uppercase:
					numUpper += 1
					startText[i] = startText[i].lower()	
				
				#check for punctuation
				elif startText[i][j] in string.punctuation:
					numPunc += 1
					wordList = list(startText[i])
					del wordList[j]
					startText[i] = "".join(wordList)
					
				#check for digit
				elif startText[i][j] in string.digits:
					numDigit += 1
					wordList = list(startText[i])
					del wordList[j]
					startText[i] = "".join(wordList)
					
			if startText[i] == "":
				del startText[i]

		for i in range(len(startText)-1, -1, -1):
			#check for incorrect words
			if not startText[i] in words:
				numIncWords += 1

		#form output
		output = "h04151jk\nFormatting ###################\nNumber of upper case words changed: " + str(numUpper)
		output += "\nNumber of punctuations removed: " + str(numPunc)
		output += "\nNumber of numbers removed: " + str(numDigit) + "\nSpellchecking ###################"
		output += "\nNumber of words: " + str(len(startText))
		output += "\nNumber of correct words: " + str(len(startText)-numIncWords)
		output += "\nNumber of incorrect words: " + str(numIncWords)

		fileOutName = fileInName[8:-4] + "_h04151jk.txt"
		fileOut = open(outFolder + fileOutName, "w")
		fileOut.write(output)
		fileOut.close()



