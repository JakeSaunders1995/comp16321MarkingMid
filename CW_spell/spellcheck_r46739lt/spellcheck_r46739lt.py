import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("words")
parser.add_argument("pathIn")
parser.add_argument("pathOut")
inputpaths = parser.parse_args()
filelist = os.listdir(inputpaths.pathIn)
numbers = ["0","1","2","3","4","5","6","7","8","9"]
punc = ["@","#","!",".","?",",",":",";","-","(",")","[","]","{","}","'","...",'"']
UpperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for x in range(len(filelist)):
	filename = filelist[x]
	input_file = open(inputpaths.pathIn+"/"+filename,"r")
	contents = input_file.readline()
	input_file.close()
	#formatting
	numberCount = 0
	punctuationCount = 0
	upperCount = 0
	wordCount = 0
	CorrectCount = 0
	wordList = contents.split()
	ListOfWords = []
	for i in range(len(wordList)):
		word = wordList[i]
		new_word = ""
		for j in range(len(word)):
			if word[j] in numbers:
				numberCount += 1
			elif word[j] in punc:
				punctuationCount += 1
			else:
				if word[j] in UpperCase:
					upperCount += 1
				new_word += word[j]
		new_word = new_word.lower()
		if new_word != "":
			ListOfWords.append(new_word)
		englishWords = open(inputpaths.words, "r")
		for line in englishWords:
			if line.strip() == new_word:
				CorrectCount += 1
				continue
		englishWords.close()
	wordCount = len(ListOfWords)
	name = filename[0:-4]
	outputfilePath = os.path.join(inputpaths.pathOut,name+"_r46739lt.txt")
	file = open(outputfilePath,"w")
	file.write("r46739lt\nFormatting ###################")
	file.write("\nNumber of upper case letters changed: "+str(upperCount))
	file.write("\nNumber of punctuations removed: "+str(punctuationCount))
	file.write("\nNumber of numbers removed: "+str(numberCount))
	file.write("\nSpellchecking ###################")
	file.write("\nNumber of words: "+str(wordCount))
	file.write("\nNumber of correct words: "+str(CorrectCount))
	file.write("\nNumber of incorrect words: "+str(wordCount-CorrectCount))
	file.close()