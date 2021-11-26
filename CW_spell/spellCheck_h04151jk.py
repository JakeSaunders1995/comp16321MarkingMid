import argparse
import string

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("textIn")
arg_parser.add_argument("textOut")
arguments = arg_parser.parse_args()

fileInName = arguments.textIn
fileOutName = arguments.textOut

#form dictionary
wordFile = open("EnglishWords.txt" ,"r")
words = wordFile.readlines()

for i in range(len(words)):
	words[i] = words[i].strip("\n")

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

fileOut = open(fileOutName, "w")
fileOut.write(output)
fileOut.close()



