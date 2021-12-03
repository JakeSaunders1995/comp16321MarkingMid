import os
import sys

#Declaring variables

englishWords = sys.argv[1]
folderIn = sys.argv[2]
folderOut = sys.argv[3]
file_number = 0
textIn = []
ENGLISH_WORDS = []

current_file = 0
transformed = 0
punctuation = 0
numbers = 0 
words = 0
correctWords = 0
incorrectWords = 0

letters = ""

#Inputting the folder with files

for file in sorted(os.listdir(folderIn)):
	file_number += 1
	with open(os.path.join(folderIn, file), 'r') as f:
		allWords = f.read().rstrip()
		textIn.append(allWords)

with open(englishWords, 'r') as j:
	for line in j:
		ENGLISH_WORDS.append(line.rstrip())

#Checking for punctuation, numbers, transformed letters

for x in textIn:
	letters = ""
	current_file += 1
	transformed = 0
	punctuation = 0
	numbers = 0 
	words = 0
	correctWords = 0
	incorrectWords = 0
	for letter in x:
		if letter == " ":
			letters += " "
		elif 97 <= ord(letter) <= 122:
			letters += letter
		elif 65 <= ord(letter) <= 90:
			letters += letter.lower()
			transformed += 1
		elif 48 <= ord(letter) <= 57:
			numbers += 1
		elif ord(letter) == 35 or ord(letter) == 64:
			letters += letter
		else:
			punctuation += 1

	#Checking for words, correct words and incorrect words and a fix

	tempstring = ""		
	for i in range(len(letters)):
		if letters[i] == " " and i != len(letters) - 1:
			if letters[i+1] != " ":
				tempstring += letters[i]
		elif letters[i] != " ":
			tempstring += letters[i]

	temparray = tempstring.split(" ")

	for i in temparray:
		for x in ENGLISH_WORDS:
			if i == x:
				correctWords += 1
				
	#Outputting final data

	output_name = "test_file" + str(current_file) + "_b16225mz"
	output = open(folderOut+"/"+output_name+".txt", "w")
	output.write("b16225mz" + "\n")
	output.write("Formatting ###################" + "\n")
	output.write("Number of upper case letters changed: " + str(transformed) + "\n")
	output.write("Number of punctuations removed: " + str(punctuation) + "\n")
	output.write("Number of numbers removed: " + str(numbers) + "\n")
	output.write("Spellchecking ###################" + "\n")
	output.write("Number of words: " + str(len(temparray)) + "\n")
	output.write("Number of correct words: " + str(correctWords) + "\n")
	output.write("Number of incorrect words: " + str(len(temparray) - correctWords) + "\n")









