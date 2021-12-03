import argparse, os

parser = argparse.ArgumentParser(description='SpellCheck Program')
parser.add_argument('words', help='English words file path')
parser.add_argument('input', help='Input file path')
parser.add_argument('output', help='Output file path')
args = parser.parse_args()

wordsFile = open(os.path.join(args.words, 'EnglishWords.txt'))
rawWordList = wordsFile.readlines()
strippedWordList = [rawWordList[i].strip() for i in range(len(rawWordList))]
wordsFile.close()

for file in os.listdir(str(args.input)):

	if file.endswith(".txt"):
		inputFile = open(os.path.join(args.input, file))
	else:
		continue

	inputText = ''
	inputList = inputFile.readlines()
	inputFile.close()
	for line in inputList:
		inputText += line

	upperCaseChanged = 0
	punctuationRemoved = 0
	numbersRemoved = 0

	formattedText = ''

	for i in range(len(inputText)):
		currentCharacter = inputText[i]
		if currentCharacter.isalpha() or currentCharacter == ' ':
			if currentCharacter.isupper():
				currentCharacter = currentCharacter.lower()
				upperCaseChanged += 1
			formattedText += currentCharacter
		elif currentCharacter.isdigit():
			numbersRemoved += 1
		elif currentCharacter != '\n':
			if currentCharacter == '.':
				try:
					if inputText[i+1] == '.' and inputText[i+2] == '.':
						punctuationRemoved -= 2  # remove 2 from the count to account for the ... counting as one punctuation mark
				except IndexError:
					pass

			punctuationRemoved += 1

	formattedTextList = formattedText.split(' ')
	try:
		formattedTextList = [word for word in formattedTextList if word != '']
	except ValueError:
		pass

	wordCount = len(formattedTextList)
	correctWords = 0
	incorrectWords = 0
	
	for word in formattedTextList:
		if word in strippedWordList:
			correctWords += 1
		else:
			incorrectWords += 1

	outputFile = open(os.path.join(args.output, file[0:-4] + '_m32784sh.txt'), 'x')
	outputFile.write("m32784sh\n")
	outputFile.write("Formatting ###################\n")
	outputFile.write("Number of upper case words changed: " + str(upperCaseChanged) + "\n")
	outputFile.write("Number of punctuations removed: " + str(punctuationRemoved) + "\n")
	outputFile.write("Number of numbers removed: " + str(numbersRemoved) + "\n")
	outputFile.write("Spellchecking ###################\n")
	outputFile.write("Number of words: " + str(wordCount) + "\n")
	outputFile.write("Number of correct words: " + str(correctWords) + "\n")
	outputFile.write("Number of incorrect words: " + str(incorrectWords))