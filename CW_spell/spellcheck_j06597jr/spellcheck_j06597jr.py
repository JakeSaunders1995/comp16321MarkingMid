import re, os, argparse

def readfile(path):

	with open(path, "r", encoding="utf-8-sig") as f:

		sentence = f.read()

		sentence = sentence.strip()

		f.close()

	return sentence


def readEnglishWords(path):

	with open(path, "r", encoding="utf-8-sig") as f:

		for x in f:

			englishWordsList.append(x.strip())

		f.close()

	return englishWordsList



def writefile(path):

	with open(path, "w", encoding="utf-8-sig") as f:

		result = f.writelines(["[user_name]", "\nFormatting ###################", "\nNumber of upper case letters changed: "+str(upper),

								"\nNumber of punctuations removed: "+str(punc), "\nNumber of numbers removed: "+str(num),

								"\nSpellchecking ###################", "\nNumber of words: "+str(numberOfWords),"\nNumber of correct words: "+str(correct),

								"\nNumber of incorrect words: "+str(numberOfWords - correct)])

		f.close()

	return result



alphabet = "abcdefghijklmnopqrstuvwxyz"

upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers = "1234567890"

punctuations = [".","?","!",",",":",";","/","-","(",")","{","}","[","]","'",'"',"..."]



parser = argparse.ArgumentParser(description="input and output files for encryption")

parser.add_argument("englishWords", type=str, help="english words list")

parser.add_argument("input", type=str, help="input file")

parser.add_argument("output", type=str, help="output file")

args = parser.parse_args()

inputFolder = args.input

outputFolder = args.output

inputFiles = os.listdir(inputFolder)

inputPath = os.listdir(inputFolder)

os.chdir(inputFolder)



for y in range(0,len(inputFiles)):

	inputFiles[y] = inputFiles[y][:-4]



count = 0

for z in range(0,len(inputPath)):

	os.chdir(inputFolder)

	inputPath[z] = inputFolder+"/"+inputPath[z]

	sentence = readfile(inputPath[z])


	upper = 0

	punc = 0

	num = 0

	numberOfWords = 0

	correct = 0

	value = False

	newWordList = []

	englishWordsList = []


	wordList = sentence.split(" ")

	for x in wordList:

		if re.search('\...', x):

				punc += 1

				x = x.strip('\...')

		newWord = x

		for i in x:

			if i in upperCase:

				upper += 1

				for y in range(0,25):

					if i == upperCase[y]:

						newWord = newWord.replace(i, alphabet[y])

			elif i in numbers:

				num += 1

				newWord = newWord.replace(i, "")

			elif i in punctuations:

				punc += 1

				newWord = newWord.replace(i, "")

		if newWord != "":

			newWordList.append(newWord)

	englishWordsList = readEnglishWords(args.englishWords)

	numberOfWords = len(newWordList)



	for x in newWordList:

		for i in englishWordsList:

			if x == i:

				value = True

				correct += 1



	os.chdir(outputFolder)

	outputPath = outputFolder +"/" + inputFiles[count]+"_j06597jr.txt"

	count += 1

	result = writefile(outputPath)