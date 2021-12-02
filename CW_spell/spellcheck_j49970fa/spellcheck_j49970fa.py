import os
import sys 
import re
import string

# English word file 
englishFile = open(sys.argv[1])
englishWords = englishFile.read()

# Real code starts from here
for files in os.listdir(sys.argv[2]):

	file = open(os.path.join(sys.argv[2],files))
	f = file.read()

	# Formatting
	numberRemoved = 0
	puncRemoved = 0
	toLowerCase = 0

	for word in f.split():
		for letter in word:
			for i in string.punctuation or i == "…":
				if letter == i:
					puncRemoved += 1
			if letter.isdigit():
				numberRemoved += 1
			if letter.isupper():
				toLowerCase += 1

	words = re.sub(r'\d', '', f).lower()					# remove digits/numbers and transform all chars to lowercase
	words = re.sub(r'[^\w\s]', '', words).split()			# remove everything except words and spaces and split into a list

	# Spellchecking
	incorrrectWords = 0
	wordAmount = len(words)

	for word in words:
		if word not in englishWords:
			incorrrectWords += 1

	englishFile.close()
	file.close()

	# Output Files
	outputFile = open(os.path.join(sys.argv[3], "".join(files.split(".")[0]) + '_j49970fa.txt'), "w")
	outputFile.write("j49970fa" + "\n" +
				    "Formatting ###################" + "\n"
				    "Number of upper case words transformed: " + str(toLowerCase) + "\n"
				    "Number of punctuations removed: " + str(puncRemoved) + "\n"
				    "Number of numbers removed: " + str(numberRemoved) + "\n"
				    "Spellchecking ###################" + "\n"
				    "Number of words in file: " + str(wordAmount) + "\n"
				    "Number of correct words in file: "+ str(wordAmount - incorrrectWords) + "\n"
				    "Number of incorrect words in file: " + str(incorrrectWords)
				    )
	outputFile.close()



