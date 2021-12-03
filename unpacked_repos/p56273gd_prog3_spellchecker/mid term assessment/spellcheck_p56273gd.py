import os, argparse
parser = argparse.ArgumentParser()
parser.add_argument("DictTextFile")
parser.add_argument("inputFile")
parser.add_argument("outputFolder")
args = parser.parse_args()
textFile = args.DictTextFile
input1 = args.inputFile
output = args.outputFolder
formattedString = ""
counters = []

def Formatting(file):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	uAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	punct = [".", "?", "!", ",",":", ";", "-", "(", ")", "[", "]", "{", "}", "'", '"']
	ellipsis = "..."
	newString = ""
	upperCounter = 0
	punctCounter = 0
	numCounter = 0 
	ellipsisCounter = 0
	for i in range(0, len(file)):
		if ellipsisCounter > 0:
			ellipsisCounter -= 1
		else:
			if file[i] in alphabet:
				newString += file[i]
			elif file[i] == " ":
				newString += " "
			elif file[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
				numCounter += 1
			elif file[i] in uAlphabet:
				newString += file[i].lower()
				upperCounter += 1
			elif file[i] in punct:
				if file[i] == ".":
					if i != len(file) -1:
						if (file[i+1] == "." and file[i+2] == "."):
							ellipsisCounter = 2
							punctCounter += 1
						else:
							punctCounter += 1
				



	print(newString)
	formattedString = newString
	counters = [upperCounter, punctCounter, numCounter]
	return (newString, counters)


def splitWords(string1):
	listOfWords = string1.split(" ")
	return listOfWords

def SpellCheck(listOfWords):
	words = 0
	correctwords = 0
	incorrectWords = 0
	dictio = open(textFile, "r")
	dictio = dictio.read()
	for word in listOfWords:
		if word != "":
			words += 1
			if word in dictio:
				correctwords += 1
			else:
				incorrectWords +=1 
	return (words, correctwords, incorrectWords)


def WriteToFile(output, filename, counters, spellValues):
	fileLocation = os.path.join(output, filename + "_p56273gd.txt")
	fileToWrite = open(fileLocation, "w")
	fileToWrite.write("p56273gd \n")
	fileToWrite.write("Formatting  ################### \n")
	fileToWrite.write("Number of upper case letters changed: "+ str(counters[0]) + "\n")
	fileToWrite.write("Number of punctuations removed: "+ str(counters[1]) + "\n")
	fileToWrite.write("Number of numbers removed: "+ str(counters[2]) + "\n")
	fileToWrite.write("Spellchecking  ################### \n")
	fileToWrite.write("Number of words: "+ str(spellValues[0]) + "\n")
	fileToWrite.write("Number of correct words: "+ str(spellValues[1]) + "\n")
	fileToWrite.write("Number of incorrect words: "+ str(spellValues[2]) + "\n")

inputtedFiles = os.listdir(input1)
for file in inputtedFiles:

	fileLocation = os.path.join(input1, file)
	openedFile = open(fileLocation, "r")
	openedFile = openedFile.read()


	formatValues = Formatting(openedFile)
	formattedString = formatValues[0]
	counters = formatValues[1]
	filenameSplit = file.split(".")
	filename = filenameSplit[0]

	spellValues = SpellCheck(splitWords(formattedString))
	WriteToFile(output, filename, counters, spellValues)






