import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("englishwordsfilepath")
parser.add_argument("inputfolderpath")
parser.add_argument("outputfolderpath")

args = parser.parse_args()

#creating list to store input file paths
inputfilelist = []
for filename in os.scandir(args.inputfolderpath):
	if filename.path.endswith(".txt") and filename.is_file():
		inputfilelist.append(filename.path)

englishwordsfile = open(args.englishwordsfilepath).readlines()

number = ["0","1","2","3","4","5","6","7","8","9"]
punctuation = [".", "?", "!", ",", ":", ";", "–", "-", "(", ")", "[", "]", "{", "}", "'", '"', "..."]


#iterate through files in input folder
for files in inputfilelist:
	inputfile = open(files)

	punccount = 0
	numbercount = 0
	uppercount = 0
	newtext = ""
	punccharlist = []
	
	# formatting
	for text in inputfile:

		rmpunc = text.split(" ")
		for words in rmpunc:
			puncchar = ""
			for char in words:
				for elements in punctuation:
					if char == elements:
						puncchar += char
			for elements in punctuation:
				if puncchar == elements:
					punccount += 1
				else:
					for char in puncchar:
						if char == elements and not("..." in puncchar):
							punccount += 1

		for char in text:
			if char == "\n":
				char = ""

			for elements in punctuation:
				if char == elements:
					char = ""

			for elements in number:
				if char == elements:
					char = ""
					numbercount += 1

			newtext += char	

	#entering formatted words into list
	wordslist = newtext.split(" ")

	#counting all uppercase words
	for elements in wordslist:
		for char in elements:
			if (ord(char) < 91) and (ord(char) > 64):
				uppercount += 1

	#removing empty list and 'newline' elements
	while ("" in wordslist):
		wordslist.remove("")

	while ("\n" in wordslist):
		wordslist.remove("\n")

	print(wordslist)	

	#tranforming all uppercase characters to lowercase
	wordslist = [element.lower() for element in wordslist]

	#entering english words text into list
	englishwordslist = []
	for lines in englishwordsfile:
		englishwordslist.append(lines.strip())

	# spellchecking
	correctcount = 0
	incorrectcount = 0 
	for words in wordslist:
		if words in englishwordslist:
			correctcount += 1
		else:
			incorrectcount += 1

	numwords = (len(wordslist))


	#creating complete output file path 
	inputfilename = os.path.basename(files)
	outputfilename = inputfilename[0:(len(inputfilename)-4)] + '_u24264cw'
	completefilepath = os.path.join(args.outputfolderpath, outputfilename + ".txt")

	outputf = open(completefilepath, "w")

	outputf.write("u24264cw\n")
	outputf.write("Formatting ###################\n")
	outputf.write("Number of upper case letters changed: {}\n".format(uppercount))
	outputf.write("Number of punctuations removed: {}\n".format(punccount))
	outputf.write("Number of numbers removed: {}\n".format(numbercount))
	outputf.write("Spellchecking ###################\n")
	outputf.write("Number of words: {}\n".format(numwords))
	outputf.write("Number of correct words: {}\n".format(correctcount))
	outputf.write("Number of incorrect words: {}\n".format(incorrectcount))

	outputf.close()

inputfile.close()

