import re, sys, os 
from pathlib import Path
import ntpath
inputfile = sys.argv[2] 
outputfile = sys.argv[3]  

for in_entry in os.scandir(inputfile):
	file1 = open(in_entry.path, 'r')
	Error = file1.readline().strip()
	file1.close()
	file2name = Path(in_entry).stem + "_n79777aa.txt"
	file2name = os.path.join(outputfile, file2name)
	outputfilefinal = open(file2name, 'w+')

	numbers = ["0","1","2","3","4","5","6","7","8","9"]
	punctuation = '''~!$%^&*()"",.?/-_}{[];:`<>…'''
	upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	i = 0
	n = 0
	p = 0
	m = 0
	u = 0
	w = 0
	correct = 0
	incorrect = 0

	while i < len(Error):
		if Error[i] in numbers:
			n = n + 1
		i = i + 1
		
	ErrorNum = re.sub(r'[0-9]', '', Error)

	ErrorPunc = ""
	for x in ErrorNum:
		if x not in punctuation:
			ErrorPunc = ErrorPunc + x
		else:
			p = p + 1

	while m < len(ErrorPunc):
		if ErrorPunc[m] in upper:
			u = u + 1
		m = m + 1

	ErrorLower = ErrorPunc.lower()

	ErrorList = ErrorLower.split()

	l = len(ErrorList)

	words = open("./EnglishWords.txt")
	correctfile = words.read()
	correctfile = correctfile.split()
	words.close()

	for line in correctfile:
		while w < len(ErrorList):
			if ErrorList[w] in correctfile:
				correct = correct + 1
			else:
				incorrect = incorrect + 1
			w = w + 1
	        
	username = "n79777aa \n"
	Format = "Formatting ###################\n"
	UpperCase = "Number of upper case words transformed: " + str(u) + "\n"
	Punct = "Number of punctuation’s removed: " + str(p) + "\n"
	Num = "Number of numbers removed: " + str(n) + "\n"
	Spellcheck = "Spellchecking ###################" + "\n"
	WordsinFile = "Number of words in file: " + str(l) + "\n"
	CorrectWord = "Number of correct words in file: " + str(correct) + "\n"
	IncorrectWord = "Number of incorrect words in file: " + str(incorrect)

	file2name = Path(in_entry).stem + "_n79777aa.txt"
	file2name = os.path.join(outputfile, file2name)
	outputfilefinal = open(file2name, 'w+')
	outputfilefinal.write(str(username))
	outputfilefinal.write(str(Format))
	outputfilefinal.write(str(UpperCase))
	outputfilefinal.write(str(Punct))
	outputfilefinal.write(str(Num))
	outputfilefinal.write(str(Spellcheck))
	outputfilefinal.write(str(WordsinFile))
	outputfilefinal.write(str(CorrectWord))
	outputfilefinal.write(str(IncorrectWord))
	outputfilefinal.close()