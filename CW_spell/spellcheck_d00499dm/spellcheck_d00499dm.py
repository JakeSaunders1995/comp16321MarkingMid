import string
import os
import sys

dictionary = sys.argv[1]
inputfile = sys.argv[2]
outputfile = sys.argv[3]

dictionaryWords = []
inputFile = open(dictionary, "r")
for line in inputFile:
	word = line.strip()
	dictionaryWords.append(word)
inputFile.close()


file = open(inputfile,'r')
words = []
inputFile = open(file, "r")
for line in inputFile: 
	count = len([elem for elem in line if elem.isupper()])
	numbers = len([elem for elem in line if elem.isdigit()])
	line = ''.join([i for i in line if not i.isdigit()])
	punct=0
	punctuations = string.punctuation
	for i in line:
		if i in punctuations:
			punct+=1
	wordsOnLine =line.strip().split()
	for word in wordsOnLine:
		words.append(word.strip(".,!\";:/?][").lower())
inputFile.close()

misspelledWords = []
words = [x for x in words if x]
for word in words:
	if word not in dictionaryWords:
		misspelledWords.append(word)

print("Formatting##################")
print("Number of upper case words transformed: " + str(count))
print("Number of numbers removed: "+ str(numbers))
print("Number of punctuations removed: "+ str(punct))
print("Spellchecking###############")
print("Number of words in file: " + str(len(words)))
correctWords = len(words)-len(misspelledWords)
print("Number of correct words in file: "+str(correctWords))
print("Number of incorrect words in file: " + str(len(misspelledWords)))
for word in misspelledWords:	#errorList contains incorrect words
	print(word)



file = open(outputfile,'w')
file.write("d00499dm" )
file.write('\n' "Formatting##################" )
file.write('\n'"Number of upper case words transformed: " + str(count) )
file.write('\n'"Number of numbers removed: "+ str(numbers))
file.write('\n'"Number of punctuations removed: "+ str(punct))
file.write('\n'"Spellchecking###############")
file.write('\n'"Number of words in file: " + str(len(words)))
file.write('\n'"Number of correct words in file: "+str(correctWords))
file.write('\n'"Number of incorrect words in file: " + str(len(misspelledWords)))

	# else:
	# 	continue
# def readTextFile(textFilename):
# 	global words
# 	words = []
# 	inputFile = open(textFilename, "r")
# 	for line in inputFile: 
# 		count = len([elem for elem in line if elem.isupper()])
# 		print("Number of upper case words transformed: " + str(count))
# 		numbers = len([elem for elem in line if elem.isdigit()])
# 		print("Number of numbers removed: "+ str(numbers))
# 		line = ''.join([i for i in line if not i.isdigit()])
# 		punct=0
# 		punctuations = string.punctuation
# 		for i in line:
# 			if i in punctuations:
# 				punct+=1
# 		print("Number of punctuations removed: "+ str(punct))
# 		wordsOnLine =line.strip().split()
# 		for word in wordsOnLine:
# 			words.append(word.strip(".,!\";:/?").lower())
# 	inputFile.close()
# 	return words


# def findErrors(dictionaryWords, textWords):
# 	misspelledWords = []
# 	textWords = [x for x in textWords if x]
# 	for word in textWords:
# 		if word not in dictionaryWords:
# 			misspelledWords.append(word)
# 	return misspelledWords

# def printResults(errorList):
# 	print("Spellchecking###############")
# 	print("Number of words in file: " + str(len(words)))
# 	correctWords = len(words)-len(errorList)
# 	print("Number of correct words in file: "+str(correctWords))
# 	print("Number of incorrect words in file: " + str(len(errorList)))
# 	for word in errorList:	#errorList contains incorrect words
# 		print(word)

# def main():
# 	dictionaryFile = input("Please enter the dictionary file: ")
# 	textFile = input("Please enter the text file: ")
# 	dictionaryList = readDictionaryFile(dictionaryFile)
# 	textList = readTextFile(textFile)
# 	errorList = findErrors(dictionaryList, textList)
# 	printResults(errorList)
	

# main()

