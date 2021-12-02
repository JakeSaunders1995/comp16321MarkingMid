import sys
import os.path
import os
filenumber = ""
inputpath = sys.argv[2]
filelist = os.listdir(inputpath)
for file in filelist:
	f = open(inputpath+"/"+file)
	text = f.read()
	text_length = len(text)
	inputfile2 = sys.argv[1]
	EnglishWordFile = open(inputfile2)
	EnlgishWords = []
	for line in EnglishWordFile:
		line = line.rstrip()
		EnlgishWords.append(line)


	#Remove Punctuation
	punctuations = str()
	punctuation_count = 0
	for x in range(33,48):
		punctuations += str(chr(x))
	for x in range(58,65):
		punctuations += str(chr(x))
	for x in range(91,97):
		punctuations += str(chr(x))
	for x in range(123,134):
		punctuations += str(chr(x))
	for punctuation in punctuations:
		punctuation_count += text.count(punctuation)
		text = text.replace(punctuation,"")

	#Remove numbers
	numbers = str()
	number_count = 0
	for x in range(48,58):
		numbers += str(chr(x))
	for number in numbers:
		number_count += text.count(number)
		text = text.replace(number,"")

	#Replace upper case letter
	UpperCaseLetters = str()
	UpperCaseLetter_count = 0
	for x in range(65,91):
		UpperCaseLetters += str(chr(x))
	for UpperCaseLetter in UpperCaseLetters:
		UpperCaseLetter_count += text.count(UpperCaseLetter)
		UpperCaseLetterASCII = ord(UpperCaseLetter)
		LowerCaseLetterASCII = 32 + UpperCaseLetterASCII
		text = text.replace(UpperCaseLetter,chr(LowerCaseLetterASCII))

	#SpellCheck
	Correct_WordCount = 0
	Words_in_Text = text.split(" ")
	Words_in_Text =[x for x in Words_in_Text if x != "" and x !="\n"]
	Total_WordCount = len(Words_in_Text)
	for x in Words_in_Text:
		if x in EnlgishWords:
			Correct_WordCount += 1
	Incorrect_WordCount = Total_WordCount - Correct_WordCount


	outputpath = sys.argv[-1]
	outputfile = file.split(".")
	output = open(outputpath+outputfile[0]+"_p70810yk.txt","x")
	output.write("p70810yk\nFormatting ###################\nNumber of upper case letters changed: "+ str(UpperCaseLetter_count)+"\nNumber of punctuations removed: "+ str(punctuation_count)+"\nNumber of numbers removed: "+ str(number_count) +"\nSpellchecking ###################\nNumber of words: "+ str(Total_WordCount)+"\nNumber of correct words: "+ str(Correct_WordCount)+"\nNumber of incorrect words: " + str(Incorrect_WordCount))
	filenumber = ""