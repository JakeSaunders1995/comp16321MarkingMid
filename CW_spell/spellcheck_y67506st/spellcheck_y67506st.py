import argparse
import os

# argparse
parser = argparse.ArgumentParser(description="Spellchecker")
parser.add_argument('dictionary', help='Input English Word file')
parser.add_argument('CheckerIndir', type=str, help='Input dir for checker')
parser.add_argument('CheckerOutdir', type=str, help='Output dir for checker')

args, unknown = parser.parse_known_args()

path = os.path.abspath(args.CheckerIndir)
englistPath = os.path.abspath(args.dictionary)
outputPath = os.path.abspath(args.CheckerOutdir)

initialPunc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# read file and remove punctuation

for filename in os.listdir(path):
	if filename.endswith(".txt"):
		inputFile = open(os.path.join(path, filename), 'r')
		y = inputFile.read()
		removedPunc = []
		for line in y:
			wordsOnline = line.strip().split()	
			for word in wordsOnline:
				if word in initialPunc:
					y = y.replace(word, "")
					removedPunc.append(word)
		# print(y)

		# read dictionary file strip space
		dictionaryWords = []
		dictionaryFile = open(englistPath, 'r')
		for line in dictionaryFile:
			word = line.strip()
			dictionaryWords.append(word)
		dictionaryFile.close()
		# print(dictionaryWords)

		# dictionaryStr = ','.join([str(elem) for elem in dictionaryWords])
		# print(dictionaryStr)

		# remove number in text
		removedNum = ''.join((item for item in y if item.isdigit()))
		textOnlyfile = ''.join((item for item in y if not item.isdigit()))
		# print(textOnlyfile)

		# convert upper to Lower case
		upperCase = sum(1 for elem in textOnlyfile if elem.isupper())
		formattedFile = textOnlyfile.lower().split()
		# print(formattedFile)

		# compare text to dictionary
		incorrect = []
		for i in formattedFile:
			if i not in dictionaryWords:
				incorrect.append(i)
		# print(incorrect)

		x = filename.replace(".txt","_y67506st.txt")
		outputFolder = os.path.join(outputPath, x)

		f = open(outputFolder, "w")
		f.write(
		"y67506st\nFormatting ###################\nNumber of upper case words transformed: " + str(upperCase)+"\nNumber of punctuation’s removed: " + str(len(removedPunc))+"\nNumber of numbers removed: " + str(len(removedNum))+"\nSpellchecking ###################\nNumber of words in file: " + str(len(formattedFile))+"\nNumber of correct words in file: " + str(len(formattedFile) - len(incorrect))+"\nNumber of incorrect words in file: " + str(len(incorrect))+"\n")
		f.close()

