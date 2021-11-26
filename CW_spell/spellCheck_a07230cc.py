import argparse
import os

##start funct

def spellCheck(fileToRead, fileSave):

	englishWordsFile = open(File.engWordFilePath, "r")
	englishWords = (englishWordsFile.read()).split()
	englishWordsFile.close()

	fileText = fileToRead.read()
	fileToRead.close()

	listOfPunctuation = ['.', '?', '!', ',', ':', ';', '—', '‐', '(', ')', '[', ']', '{', '}', '"', '…', "'"]

	fileTextList = []

	upperCaseTransformed = 0
	punctuationRemoved = 0
	numbersRemoved = 0

	for i in fileText:
		fileTextList.append(i)

	for t in fileText:
		if t.isdigit() == True:
			numbersRemoved = numbersRemoved + 1
			fileTextList.remove(t)
		elif t in listOfPunctuation:
			punctuationRemoved = punctuationRemoved + 1
			fileTextList.remove(t)
		elif ord(t) < 97 and ord(t) > 65:
			 for n in range(len(fileTextList)):
			 	if fileTextList[n] == t:
			 		fileTextList[n] = chr(ord(t) + 32)
			 upperCaseTransformed = upperCaseTransformed + 1

	cleanText = ""

	for i in fileTextList:
		cleanText += i

	cleanTextWords = cleanText.split(" ")
	noOfBlanks = cleanTextWords.count('')
	for i in range(noOfBlanks):
		cleanTextWords.remove('')
	wordsInFile = len(cleanTextWords)

	cleanText = ""
	correctWords = 0
	incorrectWords = 0

	for w in cleanTextWords:
		if w in englishWords:
			correctWords = correctWords + 1
			cleanText += w + " "
		else:
			incorrectWords = incorrectWords + 1

	print(cleanText)

	#print(str(upperCaseTransformed))
	#print(str(punctuationRemoved))
	#print(str(numbersRemoved))
	#print(str(wordsInFile))
	#print(str(correctWords))
	#print(str(incorrectWords))

	fileToSave = open(fileSave, "w")

	fileToSave.write("Formatting ###################\n")
	fileToSave.write("Number of upper case words transformed: " + str(upperCaseTransformed) + "\n")
	fileToSave.write("Number of punctuation's removed: " + str(punctuationRemoved) + "\n")
	fileToSave.write("Number of numbers removed: " + str(numbersRemoved) + "\n")
	fileToSave.write("Spellchecking ###################\n")
	fileToSave.write("Number of words in file: " + str(wordsInFile) + "\n")
	fileToSave.write("Number of correct words in file: " + str(correctWords) + "\n")
	fileToSave.write("Number of incorrect words in file: " + str(incorrectWords) + "\n")
	fileToSave.close()


arg = argparse.ArgumentParser()

arg.add_argument("engWordFilePath")
arg.add_argument("inFolderPath")
arg.add_argument("outFolderPath")

File = arg.parse_args()

direct = os.scandir(File.inFolderPath)

for f in direct:
	folderInput = File.inFolderPath + "/" + f.name
	fileToRead = open(folderInput, "r")
	folderOutput = File.outFolderPath + "/" + f.name
	folderOutput = folderOutput.replace(".txt", "_a07230cc.txt")
	spellCheck(fileToRead, folderOutput)