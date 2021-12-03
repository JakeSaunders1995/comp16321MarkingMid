import re, sys, os

input_WordList = sys.argv[1]
contentInDir = []
for element in os.listdir(sys.argv[2]):
	contentInDir.append(os.path.join(sys.argv[2],element))
files = list(filter(os.path.isfile, contentInDir))
for eachFile in files:
	file = open(eachFile,"r")
	content = file.read()
	numbers = len(list(filter(None,re.split(r"\D*", content))))
	puncuation = 0
	for eachChar in content:
		if eachChar in ".?,!:;-–()…\"{{}}'[]":
			puncuation += 1
	upperCase = re.split(r"(?![A-Z])\S|\s*", content)
	
	for i in range(0, len(upperCase)):
		if (upperCase[i].islower()):
			upperCase[i]=''
	upperCase = len(list(filter(None, upperCase)))
	file.close()
		
	words = list(filter(None,re.split(r"(?!'+\w)\W|_|[0-9]", content)))
	correctWords = 0
	incorrectWords = 0
	input1_ = open(input_WordList,"r")
	wordList = []
	for line in input1_:
		wordList.append(line.rstrip())

	for i in range(0, len(words)):
		incorrectWords += 1
		for a in range(0, len(wordList)):
			if (words[i].lower() == wordList[a]):
				correctWords += 1
				incorrectWords -=1
	input1_.close()
	output_file = open(os.path.join(sys.argv[3], eachFile[0 -(len(eachFile) - len(sys.argv[2]) - 1):-4] + "_y02478jh.txt"), "w")
	output_file.write("y02478jh"
							+ "\nFormatting ###################"
							+ "\nNumber of upper case words transformed: " + str(upperCase)
							+ "\nNumber of punctuation’s removed: " + str(puncuation)
							+ "\nNumber of numbers removed: " + str(numbers)
							+ "\nSpellchecking ###################"
							+ "\nNumber of words in file: " + str(correctWords + incorrectWords)
							+ "\nNumber of correct words in file: " + str(correctWords)
							+ "\nNumber of incorrect words in file: " + str(incorrectWords))
	output_file.close()







