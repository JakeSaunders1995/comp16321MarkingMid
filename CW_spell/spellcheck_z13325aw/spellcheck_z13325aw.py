#Final Spell Checker

import argparse, os, re


#Getting Args from the Terminal
parser = argparse.ArgumentParser()
parser.add_argument("english", type = str)
parser.add_argument("input", type = str)
parser.add_argument("output", type = str)
args = parser.parse_args()

# Iterating Through Files
for file in os.listdir(args.input):

	# Check whether file is in text format or not
	if file.endswith(".txt"):
		file_path = f"{args.input}/{file}"

		#Reading File and Saving Words as a List
		with open(file_path, "r") as f:
			inputFile = f.read() #reads in everything

		inputFile = inputFile.split() #splits a string into a list where each word is an item

		#Removing Spaces
		for inputWord in range(len(inputFile)):
			inputFile[inputWord] = inputFile[inputWord].replace(" ", "")

		#Seeing How many Uppercase Letters will be Removed
		inputWord = 0
		uppercase = 0
	
		for inputWord in range(len(inputFile)):
			lower = inputFile[inputWord].lower()
			for character in range(len(lower)):
				if lower[character] != inputFile[inputWord][character]:
					uppercase += 1

		#Actually Removing Uppercase Letters
		inputFile = list(inputWord.lower() for inputWord in inputFile)

		#To See How much Punctuation will be Removed
		inputWord = 0
		punctuation = 0
		noPunctuation = ""

		for inputWord in range(len(inputFile)):
			Ellipses = inputFile[inputWord].count("...")
			punctuation += Ellipses
			noEllipses = inputFile[inputWord].replace("...", "")
			punctuationDictionary = {
			 "." : "",
			 "?" : "",
			 "!" : "",
			 '"' : "",
			 "," : "",
			 ":" : "",
			 ";" : "",
			 "(" : "",
			 ")" : "",
			 "[" : "",
			 "]" : "",
			 "{" : "",
			 "}" : "",
			 "'" : "",
			 "-" : "",
			 "–" : "",
			 "—" : "",
			
			}

			for key in punctuationDictionary:
				for x in range(len(noEllipses)):
					if noEllipses[x].count(key) == 1:
						punctuation += 1

		#To See How many Numbers will be Removed
		inputWord = 0
		numbers = 0

		for inputWord in range(len(inputFile)):
			for num in range(0,10):
				for y in range(len(inputFile[inputWord])):
					if inputFile[inputWord][y].count(str(num)) > 0:
						numbers += 1
		
		#Removing Everything that is Non-Alpha Numeric for Spell-Checking
		inputWord = 0
		inputFile = list(re.sub(r'[^a-z]', "", inputWord) for inputWord in inputFile) 
		while ("" in inputFile):
			inputFile.remove("") #removing empty strings that may have occured.

		#Reading from English Words
		with open("EnglishWords.txt") as e:
			englishFile = e.readlines()
			englishFile = [line.rstrip('\n') for line in open("EnglishWords.txt")]

		#Comparing Words 
		inputWord = 0
		correct = []
		mistake = []

		for inputWord in range(len(inputFile)):
			for englishWord in range(len(englishFile)):
				if (inputFile[inputWord] == englishFile[englishWord]):
					correct.append(inputFile[inputWord]) 
			
			if inputFile[inputWord] not in correct:
				mistake.append(inputFile[inputWord]) 


		#Output Formatting
		username = "z13325aw"
		formatting = "\nFormatting ###################"
		outputUpperCase = "\nNumber of upper case letters changed: " + str(uppercase)
		outputPunctuation = "\nNumber of punctuations removed: " + str(punctuation)
		outputNumbers = "\nNumber of numbers removed: " + str(numbers)
		outputSpellchecking = "\nSpellchecking ###################"
		outputNumberofWords = "\nNumber of words: " + str(len(inputFile))
		outputCorrectWords = "\nNumber of correct words: " + str(len(correct))
		outputIncorrectWords = "\nNumber of incorrect words: " + str(len(mistake))
		#Outputting to File
		onlyName = os.path.splitext(file)[0] #Removes Extension from File Name
		newName = onlyName + "_z13325aw" + ".txt" 
		file_path = f"{args.output}/{newName}"
		with open(file_path, "w") as o:
			o.write(username + formatting + outputUpperCase + outputPunctuation + outputNumbers + outputSpellchecking + outputNumberofWords + outputCorrectWords + outputIncorrectWords)




