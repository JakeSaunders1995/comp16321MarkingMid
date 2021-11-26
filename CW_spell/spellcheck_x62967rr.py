import argparse
import re
import os

numWords = 0
numCorrect = 0
numIncorrect = 0
numUpper = 0
numPunc = 0
numNums = 0

def checkWordCorrectness(word):
	global numWords
	global numIncorrect
	global numCorrect
	global englishWordsFilePath
	numWords += 1
	englishWordsFile = open(args["EnglishWordsFile"])
	englishWords = [x.strip() for x in englishWordsFile.readlines()]
	if word not in englishWords:
		numIncorrect += 1
	else:
		numCorrect += 1

def cleanupWord(word):
	# print(word)
	charArray = [x.lower() for x in list(word) if x.isalpha() or x == "@" or x == "#"]
	if not charArray == []:
		word = "".join(charArray)
		checkWordCorrectness(word)

def countCorrections(word):
	global numUpper
	global numPunc
	global numNums
	countDots = 0
	ellipsesMatch = re.match(r'.+\.\.\.', word)
	# print(word)
	if ellipsesMatch != None:
		numPunc += 1
		word = (re.match(r'(.+)\.\.\.', word)).group(1)
		

	for char in word:
		# print(char)
		if char == "…":
			numPunc += 1
		elif char.isupper():
			numUpper += 1
		elif char.isnumeric():
			numNums += 1
		elif not char.isalpha() and not char.isnumeric() and char != "@" and char != "#":
			# try:
			# 	if char == "…":
			# 		numPunc += 1
			# 	elif char != ".":
			# 		numPunc += 1
			# 	elif char == "." and word[index+1] == "." and word[index+2]==".":
			# 		numPunc += 1
			# 	elif word[index-1] == "." and char == "." and word[index+1]==".":
			# 		numPunc += 0
			# 	elif word[index-2] == "." and word[index-1]=="." and char == ".":
			# 		numPunc += 0
			# 	elif char == ".":
			# 		numPunc += 1
			# except:
			# 	pass
			numPunc += 1

def main(filepath):
	global numPunc
	global numNums
	global numUpper
	global numWords
	global numCorrect
	global numIncorrect
	numPunc = 0
	numNums = 0
	numUpper = 0
	numWords = 0
	numCorrect = 0
	numIncorrect = 0

	global outputFilePath
	inputFile = open(filepath)
	contents = inputFile.read()

	contentsArr = contents.split()
	for word in contentsArr:
		if re.match(r'[a-z@#]+$', word) != None:
			checkWordCorrectness(word)
		else:
			countCorrections(word)
			cleanupWord(word)

	inputFile.close()

	outputFile = open(os.path.join(outputFilePath, os.path.basename(filepath[0:-4] + "_x62967rr.txt")), "w")
	outputFile.write("x62967rr\n")
	outputFile.write("Formatting ###################\n")
	outputFile.write("Number of upper case letters changed: " + str(numUpper) + "\n")
	outputFile.write("Number of punctuations removed: " + str(numPunc) + "\n")
	outputFile.write("Number of numbers removed: " + str(numNums) + "\n")
	outputFile.write("Spellchecking ###################" + "\n")
	outputFile.write("Number of words: " + str(numWords) + "\n")
	outputFile.write("Number of correct words: " + str(numCorrect) + "\n")
	outputFile.write("Number of incorrect words: " + str(numIncorrect) + "\n")
	outputFile.close()

parser = argparse.ArgumentParser()
parser.add_argument("EnglishWordsFile")
parser.add_argument("inputFilePath")
parser.add_argument("outputFilePath")
args = vars(parser.parse_args())

outputFilePath = args["outputFilePath"]

for parent, dirnames, filenames in os.walk(args["inputFilePath"]):
    for fn in filenames:
        filepath = os.path.join(parent, fn)
        if (os.path.join(args["inputFilePath"], os.path.basename(filepath)) == filepath) and os.path.basename(filepath)[-4:] == ".txt":
        	main(filepath)
        	# print()