import sys, os

cwd 		= os.getcwd()
inputDir 	= sys.argv[2]
outputDir 	= sys.argv[3]

def finalOutput(upperCount, punctCount, numCount, correctCount, incorrectCount):
	output = [
		'b95211hc\n',
		'Formatting ###################\n',
		'Number of upper case words changed: ' + str(upperCount) + '\n',
		'Number of punctuations removed: ' + str(punctCount) + '\n',
		'Number of numbers removed: ' + str(numCount) + '\n',
		'Spellchecking ###################\n',
		'Number of words: ' + str(correctCount + incorrectCount) + '\n',
		'Number of correct words: ' + str(correctCount) + '\n',
		'Number of incorrect word: ' + str(incorrectCount)
		]
	return output

os.chdir(inputDir)

outputList = []

for file in os.listdir():
	inFile 		= open(file, 'r')
	line 		= (inFile.read()).split()
	inFile.close()

	dictFile 	= open(sys.argv[1], 'r')
	words 		= []
	for a in dictFile:
		words.append(a.replace('\n', ''))
	dictFile.close()

	numbers 		= [	'0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	upperAlpha 		= [	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
						'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
						'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
						'Y', 'Z']

	upperCount 		= 0
	punctCount 		= 0
	numCount 		= 0
	correctCount 	= 0
	incorrectCount 	= 0

	newLine 		= ''

	for word in line:
		for letter in word:
			if letter in numbers:		#checks if character is a number
				numCount += 1
				word = word.replace(letter, '', 1)

			elif letter in upperAlpha:	#checks if character uppercase
				upperCount += 1

			elif letter.upper() not in upperAlpha:	#checks if character in alphabet
				punctCount += 1
				word = word.replace(letter, '', 1)

		word = word.lower()
		newLine += word
		newLine += ' '

	newLine = newLine.split()

	for word in newLine:
		if word in words:
			correctCount += 1
		elif word not in words:
			incorrectCount += 1

	outputList.append([
		(file.split('.'))[0],	#0
		upperCount,				#1
		punctCount,				#2
		numCount,				#3
		correctCount,			#4
		incorrectCount,])		#5

os.chdir(cwd)
os.mkdir(outputDir)
os.chdir(outputDir)

for element in outputList:
	outputFile = open(element[0] + '_b95211hc.txt', 'w')
	for output in finalOutput(element[1], element[2], element[3], element[4], element[5]):
		outputFile.write(output)
	outputFile.close()
