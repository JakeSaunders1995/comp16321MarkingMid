def spellCheck(txtFile, wordFile):
	with open(txtFile, 'r') as textFile:
		textStr = textFile.read()
		textFile.close()

	#remove numbers, punctuation and uppercase characters
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	nums = '1234567890'
	simpleStr = ''
	numCount = 0
	puncCount = 0
	upperCount = 0

	for i in textStr:
		if i in alphabet or i == ' ':
			simpleStr = simpleStr + i
		else:
			if i in nums:
				numCount += 1
			elif i == '\n':
				simpleStr = simpleStr + ' '
			elif i.lower() in alphabet:
				upperCount += 1
				simpleStr = simpleStr + i.lower()
			else:
				puncCount += 1
				#ensure ellipsis is only counted as 1 punctuation
				if textStr[(textStr.index(i))-1] == '.' and textStr[(textStr.index(i))-1] == '.':
					puncCount -= 2

	#sepearate string into words
	words = []
	currentWord = ''
	for i in simpleStr:
		if i != ' ':
			currentWord = currentWord + i
		else:
			if currentWord != '':
				words.append(currentWord)
			currentWord = ''
	if currentWord != '':
		words.append(currentWord)

	#open english word file and make array of all words
	with open(wordFile, 'r') as wordsFile:
	    engWords = [line.strip() for line in wordsFile]

	misspelt = 0
	test = []
	for i in words:
		if i not in engWords:
			misspelt += 1
			test.append(i)

	#concatonate info into output string
	output = '''z90677pp
Formatting ###################
Number of upper case words changed: ''' + str(upperCount) + '''
Number of punctuations removed: ''' + str(puncCount) + '''
Number of numbers removed: ''' + str(numCount) + '''
Spellchecking ###################
Number of words: ''' + str(len(words)) + '''
Number of correct words: ''' + str((len(words))-misspelt) + '''
Number of incorrect words: ''' + str(misspelt)

	return(output)

#main program
import os, sys, shutil
engWords = sys.argv[1]
inFolder = sys.argv[2]
outFolder = sys.argv[3]
#seperate input folder into list of .txt files
with os.scandir(inFolder) as files:
    for file in files:
    	length = len(file.name)
    	#for each .txt file run function to find scores
    	if file.name[(length-3) : (length)] == 'txt':
    	 	output = spellCheck(file, engWords)
    	 	#write scores to a new file
    	 	newFile = file.name[0 : (length-4)] + '_z90677pp.txt'
    	 	with open(newFile, 'w') as f:
    	 		f.write(output)
    	 		f.close()
    	 	#move file to output folder
    	 	shutil.move(newFile, outFolder)