import argparse
import os
import re

parser = argparse.ArgumentParser() 	# initialing parser
parser.add_argument('EnglishWords')
parser.add_argument('inputFolder') 	# inputting input folder from command line
parser.add_argument('outputFolder') 
folders = parser.parse_args() 		# passing the parameters

EnglishWordsPath = folders.EnglishWords
inputpath = folders.inputFolder
outputpath = folders.outputFolder	
inputDir = os.listdir(inputpath) # stores the list of files in the input folder to inputDir
outputDir = os.listdir(outputpath)

EnglishWordsFile = open(EnglishWordsPath)
EnglishWordsList = EnglishWordsFile.read()
EnglishWords = EnglishWordsList.split()
EnglishWordsFile.close()

num = ["0","1","2","3","4","5","6","7","8","9"]
punctuations = ["...",".","?","!",",",":",";","—","-","(",")","{","}","[","]","<",">",'"',"'"]

for inputfilename in inputDir:
	uppercount = 0
	numcount = 0
	puncount = 0
	correctWords = 0
	incorrectWords = 0
	inputtext = os.path.join(inputpath,inputfilename) # creating the path of the input file
	if os.path.isfile(inputtext) and inputfilename.endswith(".txt"):
		with open(inputtext) as inputfile:
			line = inputfile.read()
			numlist = re.findall("[0-9]", line)
			numcount = len(numlist)
			for x in num:
				line = line.replace(x,"")
			for y in punctuations:
				puncount += line.count(y)
				line = line.replace(y,"")
			for i in range(len(line)):
				char = line[i]
				if char.isupper():
					uppercount += 1
			line = line.lower()
			words = line.split()
			for word in words:
				if word in EnglishWords:
					correctWords += 1
				else:
					incorrectWords +=1

		outputfilename = inputfilename.replace('.txt', "") + "_p75341vk.txt" # creating the output file name from the input file name
		outputtext = os.path.join(outputpath,outputfilename) # creating the path of the output file

		if (outputfilename not in outputDir): # to check if the file is present or not
			outputfile = open(outputtext, "x") # create file, if not present
		else:
			outputfile = open(outputtext, "w") # write to existing file, if present
		outputfile.write("p75341vk\n")
		outputfile.write("Formatting ###################\n")
		outputfile.write("Number of upper case letters changed: " + str(uppercount) + "\n")
		outputfile.write("Number of punctuations removed: " + str(puncount) + "\n")
		outputfile.write("Number of numbers removed: " + str(numcount) + "\n")
		outputfile.write("Spellchecking ###################\n")
		outputfile.write("Number of words: " + str(len(words)) + "\n")
		outputfile.write("Number of correct words: " + str(correctWords) + "\n")
		outputfile.write("Number of incorrect words: " + str(incorrectWords))
		outputfile.close()
		inputfile.close()	