import sys, re, os
englishWords = open(sys.argv[1], "r")
englishWordsRead = englishWords.read()
englishWords.close()

def Formatting (textToFormat):
	numOfNum = 0
	numOfPunc = 0
	numOfUpper = 0
	punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
	for x in punctuation:
		numOfPunc = numOfPunc + textToFormat.count(str(x))
	textToFormat = re.sub(r'[^\w\s]','', textToFormat)
	
	for y in range(10):
		numOfNum = numOfNum + textToFormat.count(str(y))
		textToFormat = re.sub(str(y),'', textToFormat)
	

	for x in textToFormat:
		if ord(x)>64 and ord(x)<91:
			numOfUpper +=1
	textToFormat = textToFormat.lower()

	return numOfNum, numOfUpper, numOfPunc, textToFormat
		

def SpellChecking (textToCheck):
	allWords = textToCheck.split(' ')
	correctWords = 0
	incorrectWords = 0
	wordQuantity = 0
	for x in allWords:
		if x == "" or x == " " or x == "\n":
			continue
		if (re.search(r'\b'+ re.escape(x) + r'\b', englishWordsRead, re.MULTILINE)):
			correctWords+=1
		else:
			incorrectWords+=1
		wordQuantity+=1
		
	return wordQuantity, correctWords, incorrectWords

for file in os.listdir(sys.argv[2]):
	with open(os.path.join(sys.argv[2], file)) as textFile:
		text = textFile.readlines()

	numbers, uppers, punctuation, textAfterFormat = Formatting(text[0])

	numWords, numCorrect, numIncorrect = SpellChecking(textAfterFormat)


	for outputFile in os.listdir(sys.argv[3]):
		correspondFile = os.path.splitext(file)[0] + "_e40896us"
		if(correspondFile == os.path.splitext(outputFile)[0]):
			with open(os.path.join(sys.argv[3], outputFile), 'w') as endStats:
				
				endStats.write("e40896us")
				endStats.write("\n" + "Formatting: ####################################")
				endStats.write("\n" + "Number of upper case words transformed:  "+ str(uppers))
				endStats.write("\n" + "Number of punctuation removed: " + str(punctuation))
				endStats.write("\n" + "Number of numbers removed: " + str(numbers))
				endStats.write("\n" + "SpellChecking: ####################################")
				endStats.write("\n" + "Number of words in file: " + str(numWords))
				endStats.write("\n" + "Number of Correct Words in file: " + str(numCorrect))
				endStats.write("\n" + "Number of Incorrect words in file: " + str(numIncorrect))

