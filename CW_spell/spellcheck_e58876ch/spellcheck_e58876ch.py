import re
import argparse
import os 

parser = argparse.ArgumentParser()
parser.add_argument("EnglishDict", type = str)
parser.add_argument("inputFolder", type = str)
parser.add_argument("outputFolder", type = str)


args = parser.parse_args()

inputDirectory = args.inputFolder


counterInput = 0

for inputPath in os.listdir(inputDirectory):
	if os.path.isfile(os.path.join(inputDirectory, inputPath)):
		counterInput = counterInput + 1
		
		
counterOutput = 0

outputDirectory = args.outputFolder

for outputPath in os.listdir(inputDirectory):
	if os.path.isfile(os.path.join(outputDirectory, outputPath)):
		counterOutput = counterOutput + 1
		
for nameInput in os.scandir(inputDirectory):
	
	if nameInput.is_file():

		with open(nameInput, "r") as text:
			line = text.readline()


		noPunc = re.sub(r"[^\w\s]", "", line)
		

		noNumbers = re.sub(r"[0-9]+", "", noPunc)

		noCaps = noNumbers.lower()



		words = noCaps.split(" ")
		
		i = 0
		
		plaintext = ""
		
		while i < len(words):
    	
			if words[i] == "":
				plaintext = plaintext
			
			elif words[i] == "\n":
				plaintext =plaintext
    
			elif words[i] != "":
				plaintext = plaintext + " " + words[i]
			i +=1

		
		plaintext = plaintext[1:]
		plaintext = plaintext.split(" ")
		

		characterCount = 0
		CapsChanged = 0

		characterList = list(noNumbers)


		while characterCount < len(characterList):
			if characterList[characterCount] == characterList[characterCount].lower():
				CapsChanged += 0
			elif characterList[characterCount] != characterList[characterCount].lower():
				CapsChanged += 1
			characterCount += 1
		
			
			
				
			

		count = 0

		totalWords = len(plaintext)
		


		dictionary = open(args.EnglishDict, "r")
		lines = dictionary.read()

		dictionaryList = lines.split("\n")
		
		

		dictionaryPosition = 0
	
		correctWords = 0

		incorrectWords = 0

		while count < totalWords:
			plaintextCheck = plaintext[count]
			while plaintextCheck != dictionaryList[dictionaryPosition]:
				dictionaryPosition += 1
				if dictionaryPosition == len(dictionaryList) - 1:
					incorrectWords += 1
					break
			dictionaryPosition = 0
			count += 1
			
	

		dictionary.close()
		
		
		outputDiretory = args.outputFolder
		checker = os.scandir(outputDirectory)
		filename = nameInput.name.split(".")
	
		if counterOutput < counterInput:
			for count in range(counterInput):
				outputFile = filename[0] + "_e58876ch.txt"
				newFile = args.outputFolder + "/" + outputFile
				
			
				newPath = open(newFile, "x") 
				break
		checker = os.scandir(outputDirectory)
		for writtenText in checker:
			write = writtenText.name.split("_")
			concatenation = write[0] + "_" + write[1]
		
			if filename[0] == concatenation:
				finalFile = open(writtenText, "w")
				print(
				"e58876ch"
				"Formatting ###################", "\n"
				"Number of upper case letters changed: ", CapsChanged, "\n"
				"Number of punctuations removed: ", len(line)- len(noPunc), "\n"
				"Number of numbers removed: ", len(noPunc)- len(noNumbers),"\n"
				"Spellchecking ###################","\n"
				"Number of words: ", totalWords, "\n"
				"Number of correct words: ", totalWords - incorrectWords, "\n"
				"Number of incorrect words: ", incorrectWords, "\n",
				file = finalFile
				)
			else:
				continue
				
			
	