import os 
import sys
dictionaryPath = sys.argv[1]
directory = sys.argv[2]
outputDirectory = sys.argv[3]
for filename in os.listdir(directory):
	filepath = directory + "/" + filename
	text_file = open(filepath, "r")
	essay = text_file.read()

	upperCase = 0
	punctuationCount = 0
	numberCount = 0
	wordCount = 0
	correctWords = 0
	incorrectWords = 0
	tracker = 0

	dictionary_List = []
	punctuation_List = ["'", ".", "?", "!", ",", ":", ";", "—", "‐", "(", ")", "{", "}", "[", "]", ''', ''', '"', '‘', '’']
	number_List = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

	essay += " "
	edit = ""
	edit2 = ""
	newEssay = ""
	newEssay2 = ""
	newEssay3 = ""

	tracker = essay.count("...")
	tracker += essay.count(". . .")
	while essay.find('...') != -1 or essay.find('. . .') != -1:
		if essay.find('...') != -1:
			essay = essay.replace('...', '')
		elif essay.find('. . .') != -1:
			essay = essay.replace('. . .', '')

	for i in essay:
		if i != ' ':
			edit += i
		else:
			for j in edit:
				if ord(j) >= 65 and ord(j) <= 90:
					upperCase += 1
			newEssay += edit.lower() + " "
			edit = ""


	for i in newEssay:
		if i != ' ':
			edit += i
		else:
			for j in edit:
				if j in number_List:
					edit = edit.replace(j, "")
					numberCount += 1
			newEssay2 += edit + " "
			edit = ""

	for i in newEssay2:
		if i != ' ':
			edit += i
		else:
			for j in edit:
				if j in punctuation_List:
					edit = edit.replace(j, "")
					punctuationCount += 1
			newEssay3 += edit + " "
			edit = ""

	newEssay3 = " ".join(newEssay3.split())
	newEssay3 += " "
	dictionary = open(dictionaryPath, "r")
	for line in dictionary:
		line = line.rstrip()
		dictionary_List.append(line)
	for i in newEssay3:
		if i != ' ':
			edit += i
		else:
			if edit in dictionary_List:
				correctWords += 1
				wordCount += 1
				edit = ""
			else:
				incorrectWords += 1
				wordCount += 1
				edit = ""
	dictionary.close

	punctuationCount += tracker

	outputFile = outputDirectory + "/" + filename[0:-4] + "_" + "f37609ak" + ".txt"
	f = open(outputFile, "w")
	f.write("f37609ak" + '\n')
	f.write("Formatting ###################" + '\n')
	f.write("Number of upper case letters changed: " + str(upperCase) + '\n')
	f.write("Number of punctuations removed: " + str(punctuationCount) + '\n')
	f.write("Number of numbers removed: " + str(numberCount) + '\n')
	f.write("Spellchecking ###################" + '\n')
	f.write("Number of words: " + str(wordCount) + '\n')
	f.write("Number of correct words: " + str(correctWords) + '\n')
	f.write("Number of incorrect words: " + str(incorrectWords) + '\n')
	f.close

	text_file.close()
