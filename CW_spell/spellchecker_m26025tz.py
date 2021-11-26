import sys
import os

EnglishWords_file =sys.argv[1]
input_folder = sys.argv[2]
output_folder = sys.argv[3]
input_files = os.listdir(input_folder)

for input_file in input_files:
	position = input_folder +"//" + input_file

	nofwords = 0
	nofcwords = 0
	nofncwords = 0
	word = ""
	nofpunctions = 0
	nofnumbers = 0
	nofUpletters = 0
	with open(position) as f:
		contents = f.read()
	with open(EnglishWords_file) as e:
		EnglishWords = e.read()
	EnglishWords = EnglishWords.split("\n")		
	punctuation = ['.', ',', '?', '!', ':', ';', '-', '_', '[', ']','{' ,'}', '(', ')', '...', '\'', '"']
	nummbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	UpLetters = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	LowerLetters = [" ", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	for i in contents:
		if i in UpLetters:
			nofUpletters += 1
		elif i in nummbers:
			nofnumbers += 1
		elif i in punctuation:
			nofpunctions += 1
	contents = contents.lower()
	newcontents = ""
	for i in contents:
		if i in LowerLetters:
			newcontents += i
	newcontents += " "
	for i in newcontents:
		word += i
		if i == " ":
			word = word.replace(" ", "")
			if len(word) <= 1 and word not in LowerLetters:
				continue
			nofwords += 1
			if word in EnglishWords: nofcwords += 1
			else: nofncwords +=1
			word =""

	output = str(("m26025tz" + "\nFormatting ###################" + "\nNumber of upper case letters changed: " + str(nofUpletters) + "\nNumber of punctuations removed: " + str(nofpunctions) + "\nNumber of numbers removed: " + str(nofnumbers) + "\nSpellchecking ###################" + "\nNumber of words: " + str(nofwords) + "\nNumber of correct words: " + str(nofcwords) + "\nNumber of incorrect words: " + str(nofncwords) ))
	output_file = output_folder + "//" + input_file[:-4] +"_m26025tz.txt"
	with open(output_file, "w") as f:
		f.write(output)