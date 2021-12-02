import argparse, os

def read_and_split(input_file, realWords):
	newfile = open(input_file, "r")
	theString = newfile.read()
	theList = list(theString)
	theList = transform_uppercase(theList)
	theList = transform_punctuation(theList)
	theList = transform_numbers(theList)
	spelling(theList, realWords)

def transform_uppercase(theList):
	global uppercase_transformed
	UpperAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	for i in range(len(theList)):
		if theList[i] in UpperAlphabet:
			uppercase_transformed += 1
			theList[i] = theList[i].lower()
	return theList

def transform_punctuation(theList):
	global punctuation_transformed
	toRemove = []
	AlphabetAndNumbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
	for i in range(len(theList)):
		if theList[i] not in AlphabetAndNumbers:
			punctuation_transformed += 1
			toRemove.append(i)
	toRemove.sort()
	toRemove = toRemove[::-1]
	for item in toRemove:
		theList.pop(item)
	return theList

def transform_numbers(theList):
	global numbers_transformed
	toRemove = []
	numbers = ['0', '1' , '2' ,'3', '4' ,'5', '6', '7' ,'8' , '9']
	for i in range(len(theList)):
		if theList[i] in numbers:
			numbers_transformed += 1
			toRemove.append(i)
	toRemove.sort()
	toRemove = toRemove[::-1]
	for item in toRemove:
		theList.pop(item)
	return theList

def spelling(theList, realWords):
	global wordCount
	global badWordCount
	global goodWordCount
	theFile = open(realWords, "r")
	listOfRealWords = (theFile.read()).split()
	theString = "".join(theList)
	newList = theString.split()
	for word in newList:
		wordCount += 1
		if word not in listOfRealWords:
			badWordCount += 1
	goodWordCount = wordCount - badWordCount

def output_results(numbers, output_path, input_name):
	textToWrite = []
	textToWrite.append("a24872zh")
	textToWrite.append("Formatting ###################")
	textToWrite.append("Number of upper case letters changed: " + str(numbers[0]))
	textToWrite.append("Number of punctuations removed: " + str(numbers[1]))
	textToWrite.append("Number of numbers removed: " + str(numbers[2]))
	textToWrite.append("Spellchecking ###################")
	textToWrite.append("Number of words: " + str(numbers[3]))
	textToWrite.append("Number of correct words: " + str(numbers[4]))
	textToWrite.append("Number of incorrect words: " + str(numbers[5]))
	nameOfOutput = input_name[:-4]
	nameOfOutput += "_a24872zh.txt"
	output_to = open(output_path + "/" + nameOfOutput, "w")
	for line in textToWrite:
		output_to.write(line)
		output_to.write("\n")
	output_to.close()

parser = argparse.ArgumentParser()
parser.add_argument('english_words')
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

input_path = args.input_file
output_path = args.output_file
listOfTextFiles = os.listdir(input_path)

for i in range(len(listOfTextFiles)):
	item = listOfTextFiles[i]
	uppercase_transformed = 0
	punctuation_transformed = 0
	numbers_transformed = 0
	wordCount = 0
	goodWordCount = 0
	badWordCount = 0
	read_and_split(input_path + "/" + item, args.english_words)
	numbers = [uppercase_transformed, punctuation_transformed, numbers_transformed, wordCount, goodWordCount, badWordCount]
	output_results(numbers, output_path, item)






