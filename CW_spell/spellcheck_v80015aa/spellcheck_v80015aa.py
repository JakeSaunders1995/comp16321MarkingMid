#Spell Checker Program 
import os
import sys

#os.chdir(sys.argv[2])
testfiles = os.listdir(sys.argv[2])
englishfile = open(sys.argv[1], "r")
testfolder = os.getcwd()
dictionary = englishfile.read()
dictionary = dictionary.split()
resultsfolder = sys.argv[3]+"/"
Cap = 0
words = 0
correctWord = 0
incorrect = 0
Number_numbers = 0
Number_punctuation = 0
elipceCounter = 0
for file in testfiles:
	os.chdir(sys.argv[2])
	filename = file[:-4] + "_v80015aa.txt"
	finalWord = ""
	inputfile = open(file, "r")
	y = inputfile.read()

	for word in y: #if not word use split()
		if word != word.lower():
			Cap += 1
	x = y.replace("...","")
	if len(y) != len(x):
		if len(y) == len(x) + 3:
			elipceCounter += 1
		elif len(y) == len(x) +6:
			elipceCounter += 2
		elif len(y) == len(x) +9:
			elipceCounter+= 3
		elif len(y) == len(x) +12:
			elipceCounter+= 4
		else:
			elipceCounter = 0

	fixed_punctuation = x.replace(".", "").replace(",", "").replace("/", "").replace("?", "").replace(":", "").replace(";", "").replace("(", "").replace(")", "").replace("-", "").replace("_", "").replace("[", "").replace("]", "").replace("'", "").replace('"', '').replace("{", "").replace('}', '')
	fixed_numbers = fixed_punctuation.replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("0", "")
	Number_punctuation = len(x)-len(fixed_punctuation)+int(elipceCounter)
	Number_numbers =len(fixed_punctuation)-len(fixed_numbers)

	fixedText = fixed_numbers.lower().split()

	for text in fixedText:
		words += 1
		for word in dictionary:
			if word == text:
				correctWord += 1

	incorrect = words - correctWord

	os.chdir(testfolder)
	outputfile = open(resultsfolder+filename, "w")
	outputfile.write ("v80015aa" + "\n")
	outputfile.write ("Formatting ###################" + "\n")
	outputfile.write ("Number of upper case letters changed: " + str(Cap) + "\n")
	outputfile.write ("Number of punctuations removed: " + str(Number_punctuation) + "\n")
	outputfile.write ("Number of numbers removed: " + str(Number_numbers) + "\n")
	outputfile.write ("Spellchecking ###################" + "\n")
	outputfile.write ("Number of words: "+ str(words) +"\n")
	outputfile.write ("Number of correct words: "+ str(correctWord) +"\n")
	outputfile.write ("Number of incorrect words: "+ str(incorrect) +"\n")
	outputfile.close()
	inputfile.close()
	Cap = 0
	correctWord = 0
	words = 0	
	incorrect = 0
	elipceCounter = 0

	#relative file path