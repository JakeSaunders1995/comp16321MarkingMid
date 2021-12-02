# Spellchecker Program

import argparse
import os
from argparse import ArgumentParser

parser = argparse.ArgumentParser()
parser.add_argument('english', type = str, help = 'English dictionary')
parser.add_argument('inputs', type = str, help = 'Input folder')
parser.add_argument('outputs', type = str, help = 'Output folder')
args = parser.parse_args()

for files in os.listdir(args.inputs):
	if files.endswith(".txt"):
		inputfile = (os.path.join(args.inputs, files))
		files = files[:-4] + "_y47496ms.txt"
		outputfile = (os.path.join(args.outputs, files))

		# Open the files to read

		file = open(inputfile, 'rt')
		input1 = file.read()

		# input1 = input("Copy text here: ")
		realinput = ""
		inputlength = len(input1)

		# Remove numbers, punctuation

		position = 0
		numbercount = 0
		punctuationcount = 0
		numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
		punctuation = [".", "?", "!", ",", ":", ";", "-", "–", "—", "--", "(", ")", "[", "]", "{", "}", '"', "'", "…"]

		while inputlength > position:
			inputchar = input1[position]
			if inputchar in numbers:
				realinput += ""
				numbercount += 1
				position += 1
			elif inputchar in punctuation:
				realinput += ""
				punctuationcount += 1
				position += 1
			else:
				realinput += inputchar
				position += 1

		# Make all lower case

		intermediateinput = realinput.split(" ")

		middleinput = []
		for string in intermediateinput:
			if (string != ""):
				middleinput.append(string)

		mediuminput = []
		for string in middleinput:
			if (string != "\n"):
				mediuminput.append(string)

		wordposition = 0
		uppercount = 0
			
		for i in mediuminput:
			currentinput = mediuminput[wordposition]
			for x in currentinput:
				if x.islower() == False:
					uppercount += 1
			wordposition += 1

		# Remove blank strings

		finalinput = []
		for string in mediuminput:
			if (string != ""):
				endstring = string.lower()
				finalinput.append(endstring)

		wordcount = len(finalinput)

		# Compare to dictionary file

		correctwordcount = 0
		incorrectwordcount = 0
		countposition = 0

		for i in range(0, len(finalinput)):
			file = open(args.english, "rt")
			isittrue = False
			for line in file:
				line = line.rstrip()
				wordchar = finalinput[i]
				if wordchar in line:
					if len(wordchar) == len(line):
						isittrue = True
				countposition += 1
			if isittrue == True:
				correctwordcount += 1
			else:
				incorrectwordcount += 1

		output = open(outputfile, 'wt')
		output.write( "y47496ms" +
			"\nFormatting ###################" +
			"\nNumber of upper case words transformed: " + str(uppercount) +
			"\nNumber of punctuation's removed: " + str(punctuationcount) +
			"\nNumber of numbers removed: " + str(numbercount) +
			"\nSpellchecking ###################" +
			"\nNumber of words in file: " + str(wordcount) +
			"\nNumber of correct words in file: " + str(correctwordcount) +
			"\nNumber of incorrect words in file: " + str(incorrectwordcount)
			)
		output.close()
