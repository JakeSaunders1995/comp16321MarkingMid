import argparse
import os

parserVariable = argparse.ArgumentParser()
parserVariable.add_argument("dictionaryFilePath", type = str)
parserVariable.add_argument("inputFolderPath", type = str)
parserVariable.add_argument("outputFolderPath", type = str)
arguments = parserVariable.parse_args()

files = os.listdir(arguments.inputFolderPath)
files.sort()
for file in files :
	if len(file) >= 4 :
		if file[-4 :] == ".txt" :

			inputFilePath = (arguments.inputFolderPath + "/" + file)
			inputFile = open(inputFilePath)
			inputString = inputFile.read()
			inputFile.close()

			dictionaryFile = open(arguments.dictionaryFilePath)
			lines = dictionaryFile.readlines()
			dictionaryFile.close()

			dictionaryWords = []
			for line in lines :
				dictionaryWords.append(line.strip())

			correctedString = ""
			numbers = 0
			punctuation = 0
			upperCase = 0
			ellipsis_count = 0

			for x in inputString :

				if x == "." :
					ellipsis_count += 1
				else :
					punctuation += ellipsis_count
					ellipsis_count = 0

				if ellipsis_count == 3 :
					punctuation += 1
					ellipsis_count = 0	

				if x.isupper() :
					upperCase += 1
					correctedString += x.lower()
				elif x.islower() or x == " " :
					correctedString += x
				elif x.isnumeric() :
					numbers += 1
				elif x in ["?", "!", ",", ":", ";", "-", "[", "]", "{", "}", "(", ")", "'", '"', "–", "…"] :
					punctuation += 1;

			punctuation += ellipsis_count
					
			wordList = []
			currentWord = ""
			for y in range(len(correctedString)) :
				if correctedString[y].isalpha() :
					currentWord += correctedString[y]
					if y == len(correctedString) - 1 :
						wordList.append(currentWord)
					elif correctedString[y+1] == " " :
						wordList.append(currentWord)
						currentWord = ""


			incorrectWords = 0
			for z in wordList :
				if z not in dictionaryWords :
					incorrectWords += 1

			outputFilePath = arguments.outputFolderPath + "/" + file[0 : len(file) - 4] + "_h00203pb.txt"
			outputFile = open(outputFilePath, "w")
			outputFile.write("h00203pb\nFormatting ###################\nNumber of upper case letters changed: " + str(upperCase) + "\nNumber of punctuations removed: " + str(punctuation) + "\nNumber of numbers removed: " + str(numbers) + 
				"\nSpellchecking ###################\nNumber of words: " + str(len(wordList)) + "\nNumber of correct words: " + str(len(wordList) - incorrectWords) + 
				"\nNumber of incorrect words: " + str(incorrectWords))
			outputFile.close()







		
