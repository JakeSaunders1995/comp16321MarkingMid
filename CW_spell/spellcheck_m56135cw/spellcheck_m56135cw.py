#SpellChecker_v0
import os
import argparse

#Get input&outpus file path from command line.
parser = argparse.ArgumentParser(description = 'Please enter file path')
parser.add_argument('param1', type = str, help = 'English words file path')
parser.add_argument('param2', type = str, help = 'Input file file path')
parser.add_argument('param3', type = str, help = 'Output file file path')
args = parser.parse_args()

EnglishWords = args.param1
Input_Files = os.listdir(args.param2)
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
punctuation = ['.', ',', '?', '!', ':', ';', '-', '_', '[', ']','{' ,'}', '(', ')', '...', '\'', '"']
def GenerateDictionary():
	with open(args.param1, 'r', encoding='utf-8') as f:
		dic = set(line.rstrip('\n') for line in f)
	return dic

def openFile():
	if not os.path.isdir(file):
		f = open(args.param2+'/'+file, 'r')
		text = f.read()
		listofChar = []
		for i in text:
			listofChar.append(i)
	return listofChar

def CountP():
	count = 0
	position = 0
	for i in listofChar:
		for p in punctuation:
			if i == p:
				count += 1
				listofChar[position] = ""
		position += 1
	return count

def CountN():
	count = 0
	position = 0
	for i in listofChar:
		for p in number:
			if i == p:
				count += 1
				listofChar[position] = ""
		position += 1
	return count

def CountH():
	count = 0
	position = 0
	for i in listofChar:
		for p in alphabet:
			if i == p:
				count += 1
	return count

dic = GenerateDictionary()
a = 0
for file in Input_Files:
	listofChar = openFile()
	P = CountP()
	N = CountN()
	H = CountH()

	instr = "".join(listofChar).lower()
	Wordlist = instr.split()
	wordNumber = len(Wordlist)
	count = [x for x in Wordlist if x in dic]
	correctNumber = len(count)
	IncorrectNumber =  wordNumber - len(count)


	output = open(args.param3 + "/" + (Input_Files[a])[:-4] + "_m56135cw.txt",'a+')
	a += 1
	output.write("m56135cw\n")
	output.write("Formatting ###################\n")
	output.write("Number of upper case letters changed: " + str(H) + "\n")
	output.write("Number of punctuations removed: " + str(P) + "\n")
	output.write("Number of numbers removed: " + str(N) + "\n")
	output.write("Spellchecking ###################\n")
	output.write("Number of words: " + str(wordNumber) + "\n")
	output.write("Number of correct words: " + str(correctNumber) + "\n")
	output.write("Number of incorrect words: " + str(IncorrectNumber) + "\n")
	output.close()

		
 

