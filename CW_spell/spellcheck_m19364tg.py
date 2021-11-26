import os
import argparse
import re

def readArg():
	#Read Argument from Terminal
	parse = argparse.ArgumentParser()
	parse.add_argument("EnglishInput",help = "English.txt File Location")
	parse.add_argument("FileInput", help="Text Input File Path")
	parse.add_argument("FileOutput", help="Text Output File Path")

	ArgReader = parse.parse_args()
	return ArgReader.EnglishInput, ArgReader.FileInput, ArgReader.FileOutput

#Read the files in a directory and places it in a list
def readFile(path):
	previousPath = os.getcwd()
	os.chdir(path)
	files = os.listdir()
	FileNames = []
	pattern = re.compile(r"^.*.txt$")
	for x in files:
		#print(x)
		if ((pattern.search(x)) and (x != "EnglishWords.txt")):
			FileNames.append(x)
			os.chdir(previousPath)
	return FileNames

def calculateFormating(EnglishFileLocation, FileInputLocation, x):
	#Open file at both Input Location
	if (EnglishFileLocation[len(EnglishFileLocation)-16 : len(EnglishFileLocation)] != "EnglishWords.txt"):
		if(EnglishFileLocation[len(EnglishFileLocation)-1 : len(EnglishFileLocation)] == "/"):
			EnglishRead = open(EnglishFileLocation + "EnglishWords.txt", "r")
	else:
		EnglishRead = open(EnglishFileLocation, "r")
	EnglishReadWord = EnglishRead.readline()
	FileToRead = str(str(FileInputLocation) + x)
	FileInputReader = open(FileToRead, "r")
	FileInput = FileInputReader.readline()


	alphabetL = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	alphabetU = ["A", "B", "C", "C", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
	exceptions = [" ", "@", "#", "\n"]
	punctuation = [".", "?", "!", ",", ":", ";", "-", "—", "\u2010", "\u2011", "\u2012", "\u2013", "\u2014", "\u2015", "[", "]", "{", "}", "(", ")", "'", '"']

	words = []
	word = ""
	capitalCount = 0
	punctuationCount = 0
	numberCount = 0
	correctText = 0
	incorrectText = 0

	#Put every word in EnglishWords.txt into a list
	EnglishWord = []
	while (EnglishReadWord != ""):
		EnglishReadWord = EnglishReadWord[0: len(EnglishReadWord) - 1]
		EnglishWord.append(EnglishReadWord)
		EnglishReadWord = EnglishRead.readline()


	while (FileInput != ""):
		FileInput = FileInput + " "
		x = 0
		while (x < len(FileInput)):
			if (FileInput[x] in alphabetL):
				word = word + FileInput[x]
			elif(FileInput[x] in alphabetU):
				word = word + FileInput[x].lower()
				capitalCount = capitalCount + 1
			else:
				if (word != ""):
					words.append(word)
					word = ""
				if(FileInput[x] in numbers):
					numberCount = numberCount + 1
				elif (not(FileInput[x] in exceptions)):
					print(FileInput[x])
					if (FileInput[x] in punctuation):
						punctuationCount = punctuationCount + 1
						if ((FileInput[x] == ".") and (FileInput[x+1] == ".") and (FileInput[x+2] == ".")):
							x = x + 2
						if ((FileInput[x] == "'") and (FileInput[x+1] == "t")):
							correctText = correctText - 1
			x = x + 1
		FileInput = FileInputReader.readline()

	for x in words:
		if (x in EnglishWord):
			correctText = correctText + 1
		else:
			incorrectText = incorrectText + 1
		

	EnglishRead.close()
	FileInputReader.close()
	return(capitalCount, punctuationCount, numberCount, str(int(correctText) + int(incorrectText)),correctText, incorrectText)

#Read Argument from Terminal
EnglishFileLocation, FileInputLocation, FileOutputLocation = readArg()

#Check to see if / is missing at the end of location
if (EnglishFileLocation[len(EnglishFileLocation)-1 : len(EnglishFileLocation)] != "/"):
	if (EnglishFileLocation[len(EnglishFileLocation)-16 : len(EnglishFileLocation)] != "EnglishWords.txt"):
		EnglishFileLocation = EnglishFileLocation + "/"
if (FileInputLocation[len(FileInputLocation)-1 : len(FileInputLocation)] != "/"):
	FileInputLocation = FileInputLocation + "/"
if (FileOutputLocation[len(FileOutputLocation)-1 : len(FileOutputLocation)] != "/"):
	FileOutputLocation = FileOutputLocation + "/"

FileNames = readFile(FileInputLocation)

for x in FileNames:
	print("Results from: " + x)

	#Adding University Username to Output File
	lastLetterLoc = int(len(x)) - 4
	FileWriteName = x [0: lastLetterLoc]
	FileWriteName = FileWriteName + "_m19364tg.txt"
	FileToWrite = str(str(str(FileOutputLocation) + FileWriteName))
	FileOutputWriter = open(FileToWrite, "w")

	capitalCount, punctuationCount, numberCount, totalText,correctText, incorrectText = calculateFormating(EnglishFileLocation, FileInputLocation, x)

	#Write results to result folder and close files
	FileOutputWriter.write("m19364tg\n")
	FileOutputWriter.write("Formatting ###################\n")
	FileOutputWriter.write("Number of upper case words changed: " + str(capitalCount)+ "\n")
	FileOutputWriter.write("Number of punctuations removed: " + str(punctuationCount) + "\n")
	FileOutputWriter.write("Number of numbers removed: " + str(numberCount) + "\n")
	FileOutputWriter.write("Spellchecking ###################\n")
	FileOutputWriter.write("Number of words: " + str(totalText) + "\n")
	FileOutputWriter.write("Number of correct words: " + str(correctText) + "\n")
	FileOutputWriter.write("Number of incorrect words: " + str(incorrectText) + "\n")
	FileOutputWriter.close()