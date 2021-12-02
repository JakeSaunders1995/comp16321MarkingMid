import sys
import os
import re

removedWords = 0
removedPunctuation = 0
removedNumbers = 0
outputSentences = []
userName = "k47680dm"


def GetCorrectWords():
	correctLines = []
	with open(sys.argv[1]) as f:
		correctLines = f.readlines()

	for i in range(len(correctLines)):
		correctLines[i] = correctLines[i].replace("\n", "")

	return correctLines

def WriteOutput(i, outputs):
	i += 1
	file = open(sys.argv[3] + "/test_file" + str(i) + "_" + userName + ".txt", "w")
	for i in range(len(outputs)):

		file.write(outputs[i] + "\n")

def GetSentencesFromFolder():
	sentences = []

	txtFiles = os.listdir(sys.argv[2])
	txtFiles.sort()

	for i in range(len(txtFiles)):
		file = open(sys.argv[2] + "/" + txtFiles[i])
		sentences.append(file.read())

	return sentences

def RemovePunctuation(sentence, removedPunctuation):
	newSentence = ""
	acceptedPunct = [".", "?", "!", ",", ":", ";", "-", "(", ")", "{", "}", "'", '"', "[", "]"]
	for i in range(len(sentence)):
		if sentence[i] in acceptedPunct:
			removedPunctuation += 1
		else:
			newSentence += sentence[i]


	return newSentence, removedPunctuation

def RemoveNumbers(sentence):
	newSentence = ""
	amountNumbers = 0
	for i in range(len(sentence)):
		if sentence[i] != " ":
			if ord(sentence[i]) > 47 and ord(sentence[i]) < 58:
				amountNumbers += 1
			else:
				newSentence += sentence[i]
		else:
			newSentence += sentence[i]
	return amountNumbers, newSentence

#HERERENRSFLKSANKJAS FJKLASVSFF JSAFOKBJSAKJFKASFVLKASFKASF
def CheckWord(word, correctWords):
	x = correctWords.count(word)

	if x == 0:
		return False
	else:
		return True

def CountUpperCase(sentence):
	upperCaseCount = 0

	for i in range(len(sentence)):
		if sentence[i] != " ":
			if ord(sentence[i]) > 64 and ord(sentence[i]) < 91:
				upperCaseCount += 1

	return upperCaseCount



correctWords = GetCorrectWords()

sentences = GetSentencesFromFolder()

for j in range(len(sentences)):

	outputSentences.append(userName)

	sentence = sentences[j]

	outputSentences.append("Formatting ###################")

	upperCaseCount = CountUpperCase(sentence)
	outputSentences.append("Number of upper case letters changed: " + str(upperCaseCount))

	sentence = sentence.lower()

	removedNumbers, sentence = RemoveNumbers(sentence)

	sentence, removedPunctuation = RemovePunctuation(sentence, removedPunctuation)


	outputSentences.append("Number of punctuations removed: " + str(removedPunctuation))
	outputSentences.append("Number of numbers removed: " + str(removedNumbers))

	sentence = sentence.replace("  ", " ")
	sentence = sentence.replace("  ", " ")

	outputSentences.append("Spellchecking ###################")



	allWords = sentence.split(" ")
	if allWords[len(allWords) - 1] == "\n":
		allWords.pop(len(allWords) - 1)

	correctSentence = []

	for i in range(len(allWords)):
		valid = CheckWord(allWords[i], correctWords)
		if valid:
			correctSentence.append(allWords[i])
		else:
			removedWords += 1

	outputSentences.append("Number of words: " + str(len(allWords)))

	outputSentences.append("Number of correct words: " + str(len(correctSentence)))
	outputSentences.append("Number of incorrect words: " + str(removedWords))

	WriteOutput(j, outputSentences)
	outputSentences.clear()
	removedWords = 0
	removedPunctuation = 0





#Fix amount of words



