import sys
import os

if (len(sys.argv) != 4):
	print("check the number of arguments\nprogram will exit")
	sys.exit(0)

englishWords = open(sys.argv[1])
englishWords = englishWords.read()

for file in os.listdir(sys.argv[2]):
	file = sys.argv[2] +"/"+ file
#	print(file)
	counter = file[-5]
	fileIn = open(file)
	line = fileIn.read()

	capital = 0
	punctiation = 0
	numbers = 0
	newLine = ""
	for char in line:
		asc = ord(char)
		# capital letters
		if (asc >= 65 and asc <= 90):
			newLine += chr(asc + 32)
			capital += 1
			continue
		elif (asc >= 48 and asc <= 57):
			numbers += 1
			continue
		elif (char == '.' or char == '?' or char == '!' or char == ',' or char == ':' or char == ':' or char == '-' or char == '—' or char == '(' or char == ')' or char == '{' or char == '}' or char == '[' or char == ']' or char == '’' or char == '…' or char == '\"' or char == '\''):
			punctiation += 1
			continue
		newLine += char

	correct = 0
	incorrect = 0
	for word in newLine.split():
			inEnglishWords = False
			for engWord	in englishWords.split():
				if(word == engWord):
					inEnglishWords = True
					correct += 1
					break
			if not inEnglishWords:
				incorrect += 1

	result =  "p93899aa\n"
	result += "Formatting ###################\n"
	result += "Number of upper case letters changed: " + str(capital) + "\n"
	result += "Number of punctuations removed: " + str(punctiation) + "\n"
	result += "Number of numbers removed: " + str(numbers) + "\n"
	result += "Spellchecking ###################\n"
	result += "Number of words: " + str(correct + incorrect) + "\n"
	result += "Number of correct words: " + str(correct) + "\n"
	result += "Number of incorrect words: " + str(incorrect)

	fileOutPath = sys.argv[3] + "/test_file" + str(counter) + "_p93899aa.txt"
	# print(fileOutPath)
	fileOut = open(fileOutPath,'w')
	fileOut.write(result)