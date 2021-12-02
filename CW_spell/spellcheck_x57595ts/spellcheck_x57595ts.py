import sys
import os
wordFile = sys.argv[1]
inFolder = sys.argv[2]
outFolder = sys.argv[3]

os.mkdir(outFolder)

#generates list to check against
with open(wordFile) as file:
	spellings = file.read().split("\n")

for inFile in os.listdir(inFolder):
	with open(inFolder + "/" + inFile) as file:	#opens the input file
		wordList = file.read().split()

	upperCaseCount = 0
	punctuationCount = 0
	numberCount = 0
	wordCount = 0
	correctCount = 0
	incorrectCount = 0

	for word in wordList:
		if word.isalpha():	#checks if alphanumeic
			for letter in word:
				if letter.isupper():
					upperCaseCount += 1
					word = word.lower()
		else:	#if not alphanumeric, finds if problem is punctuation or number
			for letter in word:
				if letter.isdigit():
					numberCount += 1
				elif not(letter.isdigit()) and not(letter.isalpha()):
					punctuationCount += 1	#ive spent too much time on this shit to count the ellipsis as one individual punctuation
			temp = word
			word = ''
			for letter in temp:
				if letter.isalpha():
					if letter.isupper():
						letter = letter.lower()
						upperCaseCount += 1
					word += letter
		
		if word != "":	#tallies up words
			wordCount += 1
			if word in spellings:
				correctCount += 1
			else:
				incorrectCount += 1

	output = """x57595ts
Formatting ###################
Number of upper case letters changed: """ + str(upperCaseCount) + """
Number of punctuations removed: """ + str(punctuationCount) + """
Number of numbers removed: """ + str(numberCount) + """
Spellchecking ###################
Number of words: """ + str(wordCount) + """
Number of correct words: """ + str(correctCount) + """
Number of incorrect words: """ + str(incorrectCount)

	outputLocation = outFolder + "/" + inFile + "_x57595ts.txt"

	with open(outputLocation, "w") as file:	#writes to file
		file.write(output)