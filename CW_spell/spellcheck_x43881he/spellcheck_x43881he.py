import sys, os
from pathlib import Path
import ntpath
import re

list1=[]
InFile = sys.argv[2]
OutFile = sys.argv[3]

for in_entry in os.scandir(InFile):
	FileIn = open(in_entry.path, "r")
	result = FileIn.readline().strip()
	FileIn.close()


	l = 0
	f = 0 
	nmbr = ["0","1","2","3","4","5","6","7","8","9"]
	pattern = r'[0-9]'

	while l < len(result):
		if result[l] in nmbr:
			f = f + 1
		l = l + 1

	newresult = re.sub(r'[0-9]','',result)

	punctuations = '''!()-[]}{;:'"<>,./?$%^&*_~'''
	p = 0

	punc_removed = ""
	for x in newresult:
		if x not in punctuations:
			punc_removed = punc_removed + x
		else:
			p = p + 1
	    
	   
	uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	    
	a=0
	y=0

	while a < len(punc_removed):
	    if punc_removed[a] in uppercase:
	    	y = y + 1
	    a = a + 1
	    
	allinlowercase = punc_removed.lower()

	splittext = allinlowercase.split()

	wordcount = len(splittext)
	
	Engfile = open("./EnglishWords.txt")
	Engread = Engfile.read()
	Engread = Engread.split()
	Engfile.close()

	right=0
	wrong=0
	s=0
	    
	for line in splittext:
		if line in Engread:
			right += 1
		else :
			wrong += 1

	

	MyUsername = "x43881he\n" 
	Encryption1 = "Formatting ###################\n"
	Encryption2 = "Number of upper case letters changed: " + str(y) + "\n"
	Encryption3 = "Number of punctuations removed: " + str(p) + "\n"
	Encryption4 = "Number of numbers removed: " + str(f) + "\n"
	Encryption5 = "Spellchecking ###################" + "\n"
	Encryption6 = "Number of words: " + str(wordcount) + "\n"
	Encryption7 = "Number of correct words: " + str(right) + "\n"
	Encryption8 = "Number of incorrect words: " + str(wrong)

	File2 = Path(in_entry).stem + "_x43881he.txt"
	File2 = os.path.join(OutFile, File2)
	FileOut = open(File2, 'w+')
	FileOut.write(str(MyUsername))
	FileOut.write(str(Encryption1))
	FileOut.write(str(Encryption2))
	FileOut.write(str(Encryption3))
	FileOut.write(str(Encryption4))
	FileOut.write(str(Encryption5))
	FileOut.write(str(Encryption6))
	FileOut.write(str(Encryption7))
	FileOut.write(str(Encryption8))
	FileOut.close()
    



