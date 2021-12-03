import sys
import os

englishWords = sys.argv[1]
dirIn		 = sys.argv[2]
dirOut		 = sys.argv[3]

wordFile = open(englishWords)
eDict = wordFile.readlines()
convertedEDict = []
for element in eDict:
	convertedEDict.append(element.strip())
	

punctList = [".", ",", "?", "!", "\'", '"', "/", "[", "]", "(", " )", ":", ";", "-", "{", "}", "..."]
numList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
specCharList = ["@", "#", "=", "~", "_", "<", ">", "|", "`", "£", "$", "%", "^", "&", "*", "+"]				


for filename in os.listdir(dirIn):
	f = os.path.join(dirIn, filename)
	if os.path.isfile(f):
		file_in = open(f)
		text	= file_in.read()
		textSep = text.split()
		charachterSel = 0
		numbersRemovedCounter = 0
		punctuationRemovedCounter = 0
		caseCount = 0
		correctCounter = 0
		incorrectCounter = 0
		newWord = ""

		for i in range(0, len(textSep)):
			word = textSep[i]
			for n in range(0, len(word)):
				charachterSel = word[n]
				if charachterSel.isupper() == True:
					caseCount += 1  
					newWord = newWord + charachterSel.lower() 
				elif charachterSel in numList:
					numbersRemoved = charachterSel.translate({ord(w): None for w in word})
					numbersRemovedCounter += 1
				elif charachterSel in punctList:
					punctuationRemoved = charachterSel.translate({ord(q): None for q in word})
					punctuationRemovedCounter += 1 
				elif charachterSel in specCharList:
					specialCharRemoved = charachterSel.translate({ord(j): None for j in word})
				else:
					newWord = newWord + charachterSel 

			newWord = newWord + " "

		textList = newWord.split()
		wordCount = len(textList)
		x = 0

		for m in range(0, len(textList)):
			wordUnderReview = textList[m]

			if wordUnderReview in convertedEDict:
				correctCounter += 1
			else:
				incorrectCounter += 1
		
		outFileName = filename[:-4] + "_p91607ma.txt"
		pathToFile = os.path.join(dirOut, outFileName)
		outFile = open(pathToFile, "a")
		outFile.write("p91607ma \n")
		outFile.write("Formatting ################################# \n")
		outFile.write("Number of upper case words transformed: " + str(caseCount) + "\n")
		outFile.write("Number of Punctuation's removed: " + str(punctuationRemovedCounter) + "\n")
		outFile.write("Number of numbers removed: " + str(numbersRemovedCounter) + "\n")
		outFile.write("SpellChecking ###############################" + "\n")
		outFile.write("Number of words in file: " + str(wordCount) + "\n")
		outFile.write("Number of Correct words in file: " + str(correctCounter) + "\n")
		outFile.write("Number of incorrect words in file: " + str(incorrectCounter) + "\n")
				
				

