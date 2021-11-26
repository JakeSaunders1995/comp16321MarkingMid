import sys
import os


englishWords = sys.argv[1]
inFolder = sys.argv[2]
outFolder = sys.argv[3]  

for inFile in os.scandir(inFolder):

	fileName = inFile.name

	with open (inFile) as file:

		badText = file.readline()

		countNumbers = 0
		countPun = 0
		countUp = 0
		correctW = 0
		incorrectW = 0

		for i in badText:

			if i.isnumeric():

				countNumbers += 1
				badText = badText.replace(i,"")

			elif (i.isalnum() == False and i != " "):

				countPun += 1
				badText = badText.replace(i,"")

			elif i.isupper():

				countUp += 1
				loweri = i.lower()
				badText = badText.replace(i,loweri)

			else:
				pass

		wordList = badText.split()
		countWords = len(wordList)

		

		with open (englishWords) as d:

			dicOld = d.readlines()
			dic = []

			for element in dicOld:

				dic.append(element.strip())

			for b in wordList:

				if (b in dic):

					correctW += 1

				else:

					incorrectW += 1

		username = "g33966si\n"
		formatting = "Formatting ###################\n"
		upperremoved = "Number of upper case words changed: " + str(countUp) + "\n"
		punremoved = "Number of punctuations removed: " + str(countPun) + "\n"
		numremoved = "Number of numbers removed: " + str(countNumbers) + "\n"
		spellchecking = "Spellchecking ###################\n"
		numWords = "Number of words: " + str(countWords) + "\n"
		numCorrect = "Number of correct words: " + str(correctW) + "\n"
		numIncorrect = "Number of incorrect words: " + str(incorrectW)

		everything = username + formatting + upperremoved + punremoved + numremoved + spellchecking + numWords + numCorrect + numIncorrect


		outFile = fileName.replace(".txt", "_g33966si.txt")
		completeName = os.path.join(outFolder, outFile)
		fileX = open(completeName, "w")
		fileX.write(everything)
		fileX.close()











		

