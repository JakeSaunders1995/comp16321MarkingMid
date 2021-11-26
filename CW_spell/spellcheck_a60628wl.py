import re
import sys

EnglishWords = sys.argv[1]
InputFolder = sys.argv[2] + "/test_file3.txt"
OutputFolder = sys.argv[3] + "/Spellckeckoutput.txt"


readFile = open(InputFolder, "r")

fileTextRaw = readFile.readlines()
fileText = ""
for a in fileTextRaw:
	fileText = fileText + a
pass

EnglishWords = open("EnglishWords.txt", "r")

EnglishWordsRaw = EnglishWords.readlines()
EnglishWordsString = ""
for b in EnglishWordsRaw:
	EnglishWordsString = EnglishWordsString + b
pass

EnglishWordsList = EnglishWordsString.split()


removed = re.sub(r"[0-9]+", "", fileText)

punctuation = "!()-[]{};:',<>./?@#$%^&*_~"
for c in removed:
	if c in punctuation:
		punctLength = len(c)
		removed = removed.replace(c, "")

lowercase = removed.lower()

wordsList = lowercase.split()

correct = set(EnglishWordsList) & set(wordsList)

NumCapitals = len(re.findall(r"[A-Z]",fileText))

NumNumb = sum(d.isdigit() for d in fileText)

NumWordsList = len(wordsList)

NumCorrect = len(correct)

NumIncorrect = NumWordsList - NumCorrect

SpellCheckFile = open(OutputFolder, "w")
SpellCheckFile.write("a60628wl" + "\nFormatting ###################" + "\nNumber of upper case letters changed: " + str(NumCapitals) + "\nNumber of punctuations removed: " + str(punctLength) + "\nNumber of numbers removed: " + str(NumNumb) + "\nSpellchecking ###################" + "\nNumber of words: " + str(NumWordsList) + "\nNumber of correct words: " + str(NumCorrect) + "\nNumber of incorrect words: " + str(NumIncorrect))
SpellCheckFile.close()