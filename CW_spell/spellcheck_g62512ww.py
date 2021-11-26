import sys
import os
num = "0123456789"
punc = ".?!,:;-/()[]}{'"+'"'
numArgs = len(sys.argv)
if numArgs == 4:
	englishWordsFile = sys.argv[1]
	inputFile = sys.argv[2]
	outputFile = sys.argv[3]
	if os.path.isdir(inputFile):
		if not os.listdir(inputFile):
			print("Input directory is empty")
		else:
			allFiles = os.listdir(inputFile)
			for file in allFiles:
				fileName = file[:-4]
				upperCaseRemoveCount = 0
				puncRemoveCount = 0
				numRemoveCount = 0
				totalWords = 0
				totalWordsCorrect = 0
				totalWordsIncorrect = 0
				with open(inputFile + '/' + file) as f:
					fileData = f.read()					
				fileDataNoPunc = ""	
				ellipsisCheck = ""	
				if (fileData[-1] == "."):
					puncRemoveCount += 1
				for char in fileData:
					if char in num:
						numRemoveCount += 1
						if (ellipsisCheck == "."):
							puncRemoveCount += 1
							ellipsisCheck = ""
					elif char in punc:
						if (char == "."):
							ellipsisCheck += char
							if (ellipsisCheck == "..."):
								puncRemoveCount += 1
								ellipsisCheck = ""
						else:
							if (ellipsisCheck == "."):
								puncRemoveCount += 1
								ellipsisCheck = ""
							puncRemoveCount += 1
					else:
						if (ellipsisCheck == "."):
							puncRemoveCount += 1
							ellipsisCheck = ""
						if (char.isupper() == True):
							upperCaseRemoveCount += 1
						fileDataNoPunc += char
				fileDataNoPunc = fileDataNoPunc.lower()
				wordsToCheck = fileDataNoPunc.split()
				with open(englishWordsFile, "r") as f:
					spellCheck = f.readlines()
				for words in wordsToCheck:
					words += "\n"
					if words in spellCheck:
						totalWordsCorrect += 1
					else:
						totalWordsIncorrect += 1
					totalWords += 1
				outputFileName = outputFile + "/" + fileName + "_g62512ww.txt"
				with open(outputFileName, "x") as f:
					f.write("g62512ww\n")
					f.write("Formatting ###############################\n")
					f.write("Number of upper case letters changed: ")
					f.write(str(upperCaseRemoveCount))
					f.write("\nNumber of punctuations removed:")
					f.write(str(puncRemoveCount))
					f.write("\nNumber of numbers removed: ")
					f.write(str(numRemoveCount))
					f.write("\nSpellchecking ####################################")
					f.write("\nNumber of words: ")
					f.write(str(totalWords))
					f.write("\nNumber of correct words: ")
					f.write(str(totalWordsCorrect))
					f.write("\nNumber of incorrect words: ")
					f.write(str(totalWordsIncorrect))
	else:
		print("Input directory does not exist")