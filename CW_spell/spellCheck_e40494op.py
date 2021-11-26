import sys, os, string

inputDirName = sys.argv[2]
outputDirName = sys.argv[3]
inputEnglishWords = sys.argv[1]

files = os.listdir(inputDirName)

for file in files:
	#gets the name of the file minus .txt
	baseFileName = os.path.splitext(file)[0]
	#make a full file path
	fullFileName = inputDirName + "/" + file

	#reads in the .txt file to a string
	uneditedStrings = open(fullFileName, "r")
	uneditedString = uneditedStrings.read()
	uneditedStrings.close()

	#creates an output file
	outputFullFileName = outputDirName + "/" + baseFileName + "_e40494op.txt"
	formatingAndSpellchecking = open(outputFullFileName, "w")
	
	editedString = uneditedString + ""
	deletedNumbers = 0
	deletedPunctuation = 0
	deletedUppercase = 0

	
	for letter in uneditedString:
		#checks to see if letter is number then deletes it
		if letter.isdigit():
			editedString = editedString.replace(str(letter), "")
			deletedNumbers += 1
		#checks to see if letter is uppercase then deletes it
		if ord(letter) >= 65 and ord(letter) <= 90:
				editedString = editedString.replace(str(letter), str(letter.lower()))
				deletedUppercase += 1
		#checks to see if letter is a puncuation then deletes it
	for letter in editedString:
		if letter in string.punctuation:
			editedString = editedString.replace(str(letter), "")
			deletedPunctuation += 1
	
	
	#makes a list of all the words from editedString
	editedStringAsList = editedString.split()
	englishWords = open(inputEnglishWords, "r")
	englishWordList = englishWords.read()
	englishWords.close()
	checkList = englishWordList.split()
	
	total = 0
	correct = 0
	incorect = 0

	for word in editedStringAsList:
		total += 1
		if word in checkList:
			correct += 1
		else:
			incorect += 1


	formatingAndSpellchecking.write("e40494op\nFormatting ###################\nNumber of upper case letters changed: %d\nNumber of punctuations removed: %d\nNumber of numbers removed: %d\nSpellchecking ###################\nNumber of words: %d\nNumber of correct words: %d\nNumber of incorrect words: %d"%(deletedUppercase, deletedPunctuation, deletedNumbers, total, correct, incorect))
	formatingAndSpellchecking.close()