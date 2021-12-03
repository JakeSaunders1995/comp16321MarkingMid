import sys
import os
import shutil
import string

dictionary = sys.argv[1]
input_Folder = sys.argv[2]
output_Folder = sys.argv[3]
allwords = open(dictionary)
allwords_string = [line.rstrip("\n") for line in allwords]
filelist = os.listdir(input_Folder)
for filename in filelist:
	def spellcheck():
		unCheckedtxt = open(input_Folder + "/" + filename)
		unCheckedtxt_string = unCheckedtxt.read()
		unCheckedtxt.close()
		num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
		spellcheck.numOfUp = 0
		spellcheck.numOfPunc = 0
		spellcheck.numOfNum = 0
		spellcheck.numOfWords = 0
		spellcheck.numOfCwords = 0
		spellcheck.numOfIncwords = 0
		punctuations = string.punctuation
		punctuations = punctuations.replace("@", "")
		punctuations = punctuations.replace("#", "")
		for i in range(len(unCheckedtxt_string)):
			if unCheckedtxt_string[i] in punctuations:
				spellcheck.numOfPunc += 1
			elif unCheckedtxt_string[i].isupper():
				spellcheck.numOfUp += 1
			elif unCheckedtxt_string[i] in num:
				spellcheck.numOfNum += 1
		ellipsis = "..."
		count = unCheckedtxt_string.count(ellipsis)
		spellcheck.numOfPunc -= count * 2
		for char in unCheckedtxt_string:
			if char in punctuations:
				unCheckedtxt_string = unCheckedtxt_string.replace(char, "")
			elif char in num:
				unCheckedtxt_string = unCheckedtxt_string.replace(char, "")
		unCheckedtxt_string = unCheckedtxt_string.lower()
		wordList = unCheckedtxt_string.split()
		for word in wordList:
			if word in allwords_string:
				spellcheck.numOfCwords += 1
			else:
				spellcheck.numOfIncwords += 1
		spellcheck.numOfWords += len(wordList)
	spellcheck()
	checkedReport = open(output_Folder + "/" + filename[0:len(filename) - 4] + "_s93700yl.txt", "w")
	checkedReport.write("s93700yl")
	checkedReport.write("\nFormatting ###################")
	checkedReport.write("\nNumber of upper case words changed: " + str(spellcheck.numOfUp))
	checkedReport.write("\nNumber of punctuations removed: " + str(spellcheck.numOfPunc))
	checkedReport.write("\nNumber of numbers removed: " + str(spellcheck.numOfNum))
	checkedReport.write("\nSpellchecking ###################")
	checkedReport.write("\nNumber of words: " + str(spellcheck.numOfWords))
	checkedReport.write("\nNumber of correct words: " + str(spellcheck.numOfCwords))
	checkedReport.write("\nNumber of incorrect words: " + str(spellcheck.numOfIncwords))
	checkedReport.close()




		


