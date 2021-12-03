import argparse, re, os

def defArguments():
	global args
	ap = argparse.ArgumentParser()
	ap.add_argument("EngWords", help = "english words file")
	ap.add_argument("inputFolder", help="input folder")
	ap.add_argument("outputFolder", help="out folder")
	args = ap.parse_args()
def GenerateFileList():
	fileList=[]
	for file in os.listdir(args.inputFolder):
	    if file.endswith(".txt"): 
	         fileList.append(os.path.join(args.inputFolder, file))
	return fileList
def accessFile(f):
	inFile  = open(f)
	txt = inFile.read().strip()
	inFile.close()
	return txt
def generateOutput(f):
	generateOutput.txt= "j14088na\n"
	f = accessFile(f)
	f = format(f)
	f = spellCheck(f)
	return generateOutput.txt
def addText(newText):
	newText += '\n'
	generateOutput.txt += newText
def format(f):
	addText("Formatting ###################")
	caps = 0
	for word in f.split():
		for char in word:
			if ord(char) >= 65 and ord(char) <= 90:
				caps +=1
				break
	f= f.lower()
	addText("Number of upper case words transformed: %s" % caps)
	i=0
	nums=0
	puncs=0
	while i < len(f):
		char = f[i]
		if ord(char) >= 33 and ord(char) <= 96:
			occurances = len(re.findall(re.escape(char), f))
			if ord(char) >= 48 and ord(char) <= 57: nums += occurances
			else: puncs += occurances
			f= re.sub(re.escape(char), "", f)
			i -=1
		i +=1
	f= re.sub(" +", " ", f) #removes extra spaces
	addText("Number of punctuations removed: %s" % puncs)
	addText("Number of numbers removed: %s" % nums)
	return f
def spellCheck(f):
	addText("Spellchecking ###################")
	dictionary = open(args.EngWords)
	wordList= f.split()
	totWords = len(wordList)
	corWords = 0
	for line in dictionary:
		for word in wordList:
			if word == line.strip():
				corWords +=1
	wrgWords = totWords - corWords
	addText("Number of words in file: %s" % totWords)
	addText("Number of correct words in file: %s" % corWords)
	addText("Number of wrong words in file: %s" % wrgWords)
def writeOutput():
	if not os.path.exists(args.outputFolder):
		os.makedirs(args.outputFolder)
	for f in GenerateFileList():
		filename=re.sub((".+/"), "", f)
		filename=re.sub((".txt"), "_j14088na.txt", filename)
		outFile = open(os.path.join(args.outputFolder, filename), "w")
		outFile.write(generateOutput(f))
		outFile.close()


defArguments()
writeOutput()