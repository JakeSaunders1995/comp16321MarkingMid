import argparse
import string
import os

parser = argparse.ArgumentParser()
parser.add_argument("wordsPath", type=str)
parser.add_argument("inPath", type=str)
parser.add_argument("outPath", type=str)
args = parser.parse_args()

file3 = open(args.wordsPath, "r")
englishWords = file3.read()
englishWords = englishWords.split()

def format(inText):
	nums = 0
	puncs = 0
	transforms = 0
	for i in range(100):
		for i in range(len(inText)):
			if(i>=len(inText)):
				break
			if(inText[i] in string.digits):
				inText = (inText[0:i] + inText[i+1:])
				nums += 1
			elif(inText[i] in ".?!,:;-()[]'—`…" or inText[i] in ('"',"...", ". . .")):
				inText = (inText[0:i] + inText[i+1:])
				puncs += 1
			elif(inText[i] != inText[i].lower()):
				inText = (inText[0:i] + inText[i].lower() + inText[i+1:])
				transforms += 1
	words = inText.split()
	correctWords = 0
	incorrectWords = 0
	numWords = 0
	for i in words:
		numWords += 1
		if i.lower() in englishWords:
			correctWords += 1
		else:
			incorrectWords += 1

	endFile = ("""z83313gg
Formatting ###################
Number of upper case words changed: """ + str(transforms) + """
Number of punctuations removed: """ + str(puncs) + """
Number of numbers removed: """ + str(nums) + """
Spellchecking ###################
Number of words: """ + str(numWords) + """
Number of correct words: """ + str(correctWords) + """
Number of incorrect words: """ + str(incorrectWords))
	return(endFile)

def main():
    files =	os.listdir(args.inPath)
    for i in files:
    	file1 = open(args.inPath + i, "r")
    	inText = file1.read()
    	file1.close()

    	outText = format(inText)
    	fileName = i.split(".")[0] + "_z83313gg.txt"
    	file2 = open(args.outPath + fileName, "w")
    	file2.write(outText)
    	file2.close()

main()

