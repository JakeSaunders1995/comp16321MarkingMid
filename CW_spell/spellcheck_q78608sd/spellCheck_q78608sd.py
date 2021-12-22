import os
import sys

e = sys.argv[1]
i = sys.argv[2]
o = sys.argv[3]


ifile = open(i, "r")
ofile = open(o, "w")
efile = open(e, "r")

inputfile = (ifile.read())

numCounter = 0

for j in inputfile:
	if j.isdigit():
		inputfile = inputfile.replace (j,"",1)
		numCounter += 1

alphaNum = "ABCDEFGHIJKLMNOPQRSTUVWYXZabcdefghijklmnopqrstuvwxyz "
punCounter = 0
for k in inputfile:
	if k not in alphaNum:
		inputfile = inputfile.replace (k,"",1)
		punCounter += 1

caseCounter = 0		

for l in inputfile:
	if l in alphaNum[0:25]:
		inputfile = inputfile.replace(l,l.lower(),1)
		caseCounter += 1


words = inputfile.split()
numOfWords = len(words)

correctWordCounter = 0
incorrectWordCounter = 0

dictFile = (efile.read())
englishWordFile = dictFile.split()


for n in words:
	if n in englishWordFile:
		correctWordCounter += 1
	else: incorrectWordCounter += 1

ofile.write ("q78608sd")
ofile.write ("\nFormatting ###################")
ofile.write ("\nNumber of upper case words transformed:" + str(caseCounter))
ofile.write ("\nNumber of punctuations removed: " + str(punCounter))
ofile.write ("\nNumber of numbers removed: " + str(numCounter))
ofile.write ("\nSpellchecking ###################")
ofile.write ("\nNumber of words in file: " + str(len(words)))
ofile.write ("\nNumber of correct words in file: " + str(correctWordCounter))
ofile.write ("\nNumber of incorrect words in file: " + str(incorrectWordCounter))