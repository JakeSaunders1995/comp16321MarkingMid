import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("englishWords")
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
englishWordsFile = args.englishWords
inputFolder = args.input
outputFolder = args.output
fileList = os.listdir(inputFolder)
numberFiles = len(fileList)

fileIn = open(englishWordsFile, "r")
dict = fileIn.read()
fileIn.close()

for a in range(numberFiles):

	upper = 0
	punc = 0
	num = 0
	numWords = 0
	correct = 0
	incorrect = 0

	fileIn = open(inputFolder + "/" + fileList[a], "r")
	text = fileIn.readline().strip(" ")
	fileIn.close()

	for x in range(0, len(text)):
		if (text[x].isdigit()):
			num+=1
	text = ''.join(filter(lambda i: not i.isdigit(),text))

	punctuation = '''.?!,:;-[]{}()'""...'''
	for x in text:
		if x in punctuation:
			text = text.replace(x, "")
			punc += 1

	count = 0
	while count < len(text):
		if (text[count].isupper()):
			upper +=1
		count+=1
	
	text = text.lower()
	textList = text.split()
	dictList = dict.split()
	numWords = len(textList)

	for x in range(0, len(textList)):
		spelt = False
		for i in range (0, len(dictList)):
			if (textList[x] == dictList[i]):
				correct +=1
				spelt = True
		if(spelt == False):
			incorrect+=1


	outText = "x63917cd\nFormatting ###################\n"
	outText =outText+"Number of upper case letters changed: "+str(upper)+"\n"
	outText =outText+"Number of punctuations removed: "+ str(punc)+"\n"
	outText = outText+"Number of numbers removed: "+str(num)+"\n"
	outText =outText+"Spellchecking ###################\n"
	outText =outText+"Number of words: "+str(numWords)+"\n"
	outText =outText+"Number of correct words: "+ str(correct)+"\n"
	outText =outText+"Number of incorrect words: "+str(incorrect)

	outputFolder +="/"
	fileName = fileList[a].replace(".txt", "") + "_x63917cd.txt"
	outputName = os.path.join(outputFolder, fileName)
	fileOut = open(outputName, "w")
	fileOut.write (outText)
	fileOut.close()