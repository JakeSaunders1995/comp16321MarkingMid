import re
import sys
import os

inputPath = sys.argv[1]  
outputPath = sys.argv[2]
print(inputPath)
print(outputPath)

inputFiles = os.listdir(inputPath)


with open ("EnglishWords.txt", "r") as readWords:
	dictionaryWords = readWords.readlines()
	dictionaryWords = [line.rstrip() for line in dictionaryWords]

	

readWords.close()

count1 = 0
for files in inputFiles:
	os.chdir(inputPath)

	with open (inputFiles[count1], "r") as readFile:
		sentence = readFile.readlines()

	readFile.close()
	
	for words in sentence:
		sentence = words.strip()
	



	noofNumbersRemoved = len(re.findall("[0-9]", sentence))
	

	noofPunctuationRemoved = len(re.findall("[\!\(\)\-\[\]\{\}\;\:\'\"\,\<\>\.\/\?\$\%\^\&\*\_\~]", sentence))
	

	sentence = sentence.split()



	

	incorrectSpelling = {}



	count = 0
	for word in sentence:

		if (word not in dictionaryWords):
			incorrectSpelling[count] = word
			
		count += 1	

	


	wordIndex = list(incorrectSpelling.keys())
	
	incorrectWords = list(incorrectSpelling.values())
	

	capitalLetters = 0
	count = 0


	for word in incorrectWords:
		incorrectWords[count] = re.sub("[0-9]", "", word)
		incorrectWords[count] = re.sub("[\!\(\)\-\[\]\{\}\;\:\'\"\,\<\>\.\/\?\$\%\^\&\*\_\~]", "", incorrectWords[count])
		incorrectWords[count] = incorrectWords[count].lower()
		for char in word:
			if(char.isupper()):
				capitalLetters += 1

		count += 1
		
	

	correctWords = incorrectWords

	

	count = 0
	for word in incorrectWords:
		index = int(wordIndex[count])
		
		sentence[index] = correctWords[count]
		
		count += 1

	sentence = [elem for elem in sentence if elem.strip()]
	

	NoofIncorrectWords = 0

	for word in sentence:
		if word not in dictionaryWords:
			NoofIncorrectWords += 1


	

	spellcheckedSentence = " ".join(sentence)

	

	noofWords = len(spellcheckedSentence.split())
	
	noofCorrectWords = noofWords - NoofIncorrectWords
	

	os.chdir("..")
	os.chdir(outputPath)

	x = re.split(".txt", inputFiles[count1], 1)
	print(x[0])
	fileWriter = open(x[0] + "_j11865sr.txt", "w")
	fileWriter.write("j11865sr")
	fileWriter.write("\nFormatting ###################")
	fileWriter.write("\nNumber of upper case letters changed: " + str(capitalLetters))
	fileWriter.write("\nNumber of punctuation removed: " + str(noofPunctuationRemoved))
	fileWriter.write("\nNumber of numbers removed: " + str(noofNumbersRemoved))
	fileWriter.write("\nSpellchecking ###################")
	fileWriter.write("\nNumber of words: " + str(noofWords))
	fileWriter.write("\nNumber of correct words: " + str(noofCorrectWords))
	fileWriter.write("\nNumber of incorrect words: " + str(NoofIncorrectWords))

	fileWriter.close

	os.chdir("..")
	count1 += 1

