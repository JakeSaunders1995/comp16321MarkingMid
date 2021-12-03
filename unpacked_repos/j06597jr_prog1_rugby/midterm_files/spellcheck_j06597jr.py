import re
import argparse

def readfile(path):
	with open(path, "r", encoding="utf-8-sig") as f:
		sentence = f.read()
		sentence = sentence.strip()
		f.close()
	return sentence

def readEnglishWords(path):
	with open(path, "r", encoding="utf-8-sig") as f:
		for x in f:
			englishWords = f.read()
		f.close()
	return englishWords

parser = argparse.ArgumentParser(description="input and output files for encryption")
parser.add_argument("englishWords", type=str, help="english words list")
parser.add_argument("input", type=str, help="input file")
parser.add_argument("output", type=str, help="output file")
args = parser.parse_args()
sentence = readfile(args.input)
englishWords = readEnglishWords(args.englishWords)

alphabet = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
punctuations = ",./?><()`¬!'@$%^&*()_-+=[]{}#~;:"
upper = 0
punc = 0
num = 0
numberOfWords = 0
newWordList = []
correct = 0

wordList = sentence.split(" ")
for x in wordList:
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
print(newWordList)
for x in newWordList:
	if x in englishWords:
		correct += 1
	else:
		print(x)

numberOfWords = len(newWordList)

def writefile(path):
	with open(path, "w", encoding="utf-8-sig") as f:
		result = f.writelines(["[user_name]", "\nFormatting ###################", "\nNumber of upper case letters changed: "+str(upper),
								"\nNumber of punctuations removed: "+str(punc), "\nNumber of numbers removed: "+str(num),
								"\nSpellchecking ###################", "\nNumber of words: "+str(numberOfWords),"\nNumber of correct words: "+str(correct),
								"\nNumber of incorrect words: "+str(numberOfWords - correct)])
		f.close()
	return result

result = writefile(args.output)



