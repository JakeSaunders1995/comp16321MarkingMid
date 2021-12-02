import argparse, os

parser = argparse.ArgumentParser()

parser.add_argument("wordsFile")
parser.add_argument("inputFolder")
parser.add_argument("outputFolder")
args = parser.parse_args()

wordsFileName = args.wordsFile
inputFolderName = args.inputFolder
outputFolderName = args.outputFolder

filesList = os.listdir(inputFolderName)

for fileName in filesList:
	inputDirectory = inputFolderName + '/' + fileName
	f = open(inputDirectory, "r")
	inputContent = f.read()
	f.close()

	englishWords = open(wordsFileName, "r")
	englishWordsList = []
	for line in englishWords:
		englishWordsList.append(line.strip())


	wordCount = 0
	upperCount = 0
	punctCount = 0
	numCount = 0
	correctCount = 0
	incorrectCount = 0

	username = "r83187jc"

	inputContentList = list(inputContent)
	tempWord = []
	wordArray = []
	for i in range(0, len(inputContentList)):
		if inputContentList[i].isalpha():
			if inputContentList[i].isupper():
				upperCount += 1
			tempWord.append(inputContentList[i].lower())
		elif inputContentList[i].isnumeric():
			numCount += 1
		elif inputContentList[i] == " ":
			tempWordStr = "".join(tempWord)
			if tempWordStr != "":
				wordArray.append(tempWordStr)
				if tempWordStr in englishWordsList:
					correctCount += 1
				else:
					incorrectCount += 1
				tempWord = []
		else:
			punctCount += 1

	tempWordStr = "".join(tempWord)
	wordArray.append("".join(tempWord))
	if tempWordStr != "":
		if tempWordStr in englishWordsList:
			correctCount += 1
		else:
			incorrectCount += 1
	
	wordCount = len(wordArray)

	englishWords.close()

	stringToWrite = "".join((username+"\n",
							"Formatting ###################\n",
							"Number of upper case words changed: " + str(upperCount) + "\n",
							"Number of punctuations removed: " + str(punctCount) + "\n",
							"Number of numbers removed: " + str(numCount) + "\n",
							"Spellchecking ###################\n",
							"Number of words: " + str(wordCount) + "\n",
							"Number of correct words: " + str(correctCount) + "\n",
							"Number of incorrect words: " + str(incorrectCount) + "\n"))


	dotIndex = fileName.find(".")
	outputFileName = fileName[:dotIndex] + "_r83187jc" + fileName[dotIndex:]
	outputDirectory = outputFolderName + '/' + outputFileName
	fOutput = open(outputDirectory, "w")
	fOutput.write(stringToWrite)
	fOutput.close()
