import argparse
import os
import re

#Arguments
parser = argparse.ArgumentParser(description = "Input and Output to folders specified")
parser.add_argument("input", type = str, help = "Input folder path")
parser.add_argument("output", type = str, help = "Output folder path")
parser.add_argument("dictionary", type = str, help = "Dictionary file path")
args = parser.parse_args()

#Initial
punc = '''.?!,:;-—()[]}{'"…£$%^&*~¬`|/<>'''

#Functions
def CheckInput():
	exists = os.path.isdir(args.input)
	if exists == False:
		print("The specified input folder does not exist")
		exit()
	else:
		return

def CheckDictionary():
	exists = os.path.exists(args.dictionary)
	if exists == False:
		print("The path you specified for the dictionary does not exist")
		exit()
	else:
		return

def CheckOutput():
	exists = os.path.isdir(args.output)
	if exists == False:
		os.mkdir(args.output)
	else:
		return

def GetDocument():
	opendir = str(args.input) + "/" + str(inputlist[file])
	f = open(opendir)
	document = f.read()
	f.close()
	return document

def Formatting():
	global wordslist, uppercase, punctuation, numbers
	uppercase = 0
	punctuation = 0
	numbers = 0
	wordslist = []
	for x in range(0, len(document)):
		if document[x].isupper() == True:
			uppercase += 1
		if document[x].isnumeric() == True:
			numbers += 1
		if document[x] in punc:
			punctuation += 1
	document1 = re.sub(r"[0-9]", "", document)
	document2 = document1.lower()
	document3 = re.sub(r"\n", " ", document2)
	document4 = re.sub(r"[^a-z ]+", "", document3)
	document5 = re.sub(" +", " ", document4)
	wordslist = []
	letters = ""
	wordslist = document5.split()
	return wordslist, uppercase, punctuation, numbers

def Get_Dict():
	dictionarylist = []
	with open(args.dictionary) as file:
		dictionarylist = file.readlines()
	dictionarylist = [line.rstrip("\n") for line in dictionarylist]
	file.close()
	return dictionarylist

def SpellCheck():
	global correct, incorrect
	correct, incorrect = 0, 0
	for x in range(0, len(wordslist)):
		speltcorrect = True
		for y in range(0, len(dictionary)):
			speltcorrect = False
			if wordslist[x] == dictionary[y]:
				correct += 1
				speltcorrect = True
				break
		if speltcorrect == False:
			incorrect += 1
	return correct, incorrect

def Output():
	opendir = str(args.output) + "/" + str(inputlist[file].rstrip(".txt") + "_y62498rh.txt")
	g = open(opendir, "w")
	g.writelines(["y62498rh\n", "Formatting ###################","\n", "Number of upper case letters changed: ", str(uppercase), "\n", "Number of punctuations removed: ", str(punctuation), "\n", "Number of numbers removed: ", str(numbers), "\n", "Spellchecking ###################", "\n", "Number of words: ", str(correct + incorrect), "\n", "Number of correct words: ", str(correct), "\n", "Number of incorrect words: ", str(incorrect)])
	g.close()

#Main
CheckInput()
CheckOutput()
CheckDictionary()
inputlist = os.listdir(args.input)
for file in range (0, len(inputlist)):
	global document
	document = GetDocument()
	Formatting()
	dictionary = Get_Dict()
	SpellCheck()
	Output()