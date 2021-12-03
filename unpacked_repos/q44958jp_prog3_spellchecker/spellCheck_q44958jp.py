import argparse, os

def init(): #reads the english words file, gets input and output filepaths
	parser = argparse.ArgumentParser()
	parser.add_argument("englishWords", type=open)
	parser.add_argument("dirIn")
	parser.add_argument("dirOut")

	args = parser.parse_args()
	files = vars(args)

	englishWords = files["englishWords"].readlines()
	#removes '\n' from each line of englishWords
	for i in range(len(englishWords)-1): #last line does not have '\n' char
		word = englishWords[i]
		word = word[:-1]
		englishWords[i] = word

	files["englishWords"].close()
	
	return englishWords, files["dirIn"], files["dirOut"]

def formatText(inputData):
	inp = list(inputData)
	uppercaseCount = 0
	numberCount = 0
	punctuationCount = 0

	for i in range(len(inputData)):
		if 65 <= ord(inputData[i]) <= 90: # if char is uppercase

			inp[i-numberCount-punctuationCount] = chr(ord(inp[i-numberCount-punctuationCount])+32)
			uppercaseCount += 1
		elif 48 <= ord(inputData[i]) <= 57: # if char is a number
			inp.remove(inputData[i])
			numberCount += 1
		elif 33 <= ord(inputData[i]) <= 96: # elif char is some form of punctuation

			inp.remove(inputData[i])
			punctuationCount += 1

	formattedText = ""
	for i in inp:
		formattedText += i

	return formattedText, uppercaseCount, punctuationCount, numberCount


def spellCheck(inputData,englishWords):
	wordCount = 0
	word = ""
	correctWords = 0
	wrongWords = 0

	for i in range(len(inputData)):
		word += inputData[i]
		rongSpeling = True

		if inputData[i] == " " or i+1 == len(inputData):
			if word != " ":
				wordCount += 1
			else:
				rongSpeling = False

			if i +1 != len(inputData):
				word = word[:-1]

			for j in range(len(englishWords)):
				if word == englishWords[j]:
					correctWords += 1
					rongSpeling = False

			if rongSpeling == True:
				wrongWords += 1

			word = ""

	return wordCount, correctWords, wrongWords


eng, dirIn, dirOut = init()

for file in os.listdir(dirIn):

	currentfile = os.path.join(dirIn,file)
	currentfile = open(currentfile, "r")

	inputData = currentfile.read()
	currentfile.close()

	formattedText, upcaseCount, punctCount, numCount  = formatText(inputData)
	wCount, cWords, wWords = spellCheck(formattedText,eng)

	file = os.path.join(dirOut,file.rsplit(".",1)[0])
	fileOut = open(file+"_q44958jp.txt","w")

	fileOut.writelines(["q44958jp\n",
		"Formatting ###################\n",
		"Number of upper case words changed: "+str(upcaseCount)+"\n",
		"Number of punctuations removed: "+str(punctCount)+"\n",
		"Number of numbers removed: "+str(numCount)+"\n",
		"Spellchecking ###################\n",
		"Number of words: "+str(wCount)+"\n",
		"Number of correct words: "+ str(cWords)+"\n",
		"Number of incorrect words: "+str(wWords)+"\n"])

	fileOut.close()
