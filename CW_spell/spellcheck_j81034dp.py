# Program 3 - Spellchecker
import os
import sys 
import re



InputFolder = sys.argv[2]
InputFolderList = os.listdir(InputFolder)
InputFolderList.sort()
OutputFolder = sys.argv[3]
OutputFolderList = os.listdir(OutputFolder)

for folder in InputFolderList:
	files = open(os.path.join(InputFolder, folder))
	content = files.read()
	folderstring = folder.replace(".txt","_j81034dp.txt")


	uppercasecounter = 0
	numbercounter = 0
	words = 0
	punctuation = 0
	# The full list of punctuation in the English Language is: the period, question mark, exclamation point, comma, colon, semicolon, dash, hyphen, brackets, braces, parentheses, apostrophe,
    # quotation mark, and ellipsis.
	#exampleofpunctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	exampleofpunctuation = '''.?!,:;—-[]{}()'"'''

	EnlgishDic = sys.argv[1]
	#textFile = sys.argv[2]
	#outputFile = sys.argv[3]
	#with open(textFile, "r") as i:
	#	content = i.read()

	ellipsis = content.count("...")
	ellipsiswithspaces = content.count(". . .")
	ellipsisfromunicode = content.count("…")
	content = content.replace("...","")
	content = content.replace(". . .","")
	content = content.replace("…","")
	punctuation = punctuation + ellipsis + ellipsiswithspaces + ellipsisfromunicode

	#FORMATTING START
	for character in content:
		if character.isupper():
			uppercasecounter += 1
		elif character.isnumeric():
			numbercounter += 1
		elif character == " ":
			words += 1
		else:
			if character in exampleofpunctuation:
				punctuation += 1

	content = re.sub(r'[^\w\s]','', content) # Removes punctuation
	content = re.sub(r'[0-9]','', content) # Removes the numbers
	content = re.sub('\s{2,}',' ', content) # Removes any double spaces

	newcontent = content.lower()
	newcontent = newcontent.split()
	numberofwords = len(newcontent)
	#FORMATTING END



	#FORMATTING ENGLISH DICTIONAIRY START
	with open(EnlgishDic, "r") as i:
		EnlgishDicContent = i.read()

	EnlgishWords = EnlgishDicContent.splitlines()
	# FORMATTING ENGLUSH DICTIONAIRY END


	correctwords= 0
	for x in newcontent:
		for y in EnlgishWords:
			if x == y:
				correctwords += 1


	for folders in OutputFolder:
		outputFile = open(os.path.join(OutputFolder, folderstring), 'w')
		outputFile.writelines("j81034dp" + "\n")
		outputFile.writelines("Formatting ###################" + "\n")
		outputFile.writelines("Number of upper case letters changed: " + str(uppercasecounter)+ "\n")
		outputFile.writelines("Number of punctuations removed: " + str(punctuation)+ "\n")
		outputFile.writelines("Number of numbers removed: " + str(numbercounter)+ "\n")
		outputFile.writelines("Spellchecking ###################"+ "\n")
		outputFile.writelines("Number of words: " + str(numberofwords)+ "\n")
		outputFile.writelines("Number of correct words: " +  str(correctwords)+ "\n")
		outputFile.writelines("Number of incorrect words: " +str(numberofwords - correctwords)+ "\n")
