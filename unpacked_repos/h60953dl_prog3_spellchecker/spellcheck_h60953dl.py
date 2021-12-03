import sys
import os

for file1 in sorted(os.listdir(sys.argv[2])):
	punctuation = 0
	numbers = 0
	capitals = 0
	numOfwords = 0
	correctWords = 0
	file = open(os.path.join(sys.argv[2], file1),'r') #reads the text files
	readFile = file.read()
	
	spell = open(sys.argv[1], 'r')
	spellFile = []
	textFile =[""]
	counter = 0
	for line in spell:
		line = line.rstrip("\n")
		spellFile.append(line)

	for line in range(len(readFile)):
		if readFile[line] == " ":
			counter += 1
			textFile.append("")
		else:
			textFile[counter] += readFile[line]

	word =0
	while word < len(textFile):
		character = 0
		while character < len(textFile[word]):
			if len(textFile[word]) > 0 or textFile[word]=='...':
				if (ord(textFile[word][character]) !=46 and ((ord(textFile[word][character])<48) or ord(textFile[word][character])>57) and ((ord(textFile[word][character])<65) or ord(textFile[word][character])>90)):
					if ((ord(textFile[word][character])>=33 and ord(textFile[word][character])<=47 and textFile[word][character]!=35) or (ord(textFile[word][character])>=58 and ord(textFile[word][character])<64) or (ord(textFile[word][character])>=91 and ord(textFile[word][character])<=96) or (ord(textFile[word][character])>=123 and ord(textFile[word][character])<=126)):
						textFile[word] = textFile[word].replace(textFile[word][character], '')
						character -= 1
						punctuation +=1
				elif (ord(textFile[word][character]) ==46):
					if (textFile[word]== '...'):
						textFile[word] = textFile[word].replace(textFile[word], '')
						punctuation += 1
						character -= 3
						
					else:
						textFile[word] = textFile[word].replace(textFile[word][character], '')
						character -= 1
						punctuation +=1

				elif (ord(textFile[word][character])>=48 and ord(textFile[word][character])<=57):
					textFile[word] = textFile[word].replace(textFile[word][character], '')
					character -= 1
					numbers += 1	
				elif textFile[word][character].isupper() == True:
					temp=textFile[word][character].lower()
					textFile[word]= textFile[word].replace(textFile[word][character], temp)
					capitals += 1
				character +=1
				if textFile[word] =='':
					textFile.remove(textFile[word])
					word -= 1
		word += 1
	
	lenOfList = 0
	print(textFile)
	while lenOfList < len(textFile):
		if textFile[lenOfList] == '' or textFile[lenOfList] == '\n':
			textFile.remove(textFile[lenOfList])
			lenOfList -= 1
		lenOfList += 1

	for word in textFile:
		for message in range(len(spellFile)-1): #for each word in the spellFile,
			if (word == spellFile[message]):
				correctWords += 1
	
	numOfwords =len(textFile)
	newOutputFile = open(os.path.join(sys.argv[3], file1[:-4] +'_h60953dl.txt'), 'w')
	newOutputFile.write('h60953dl \n')
	newOutputFile.write('Formatting ################### \n')
	newOutputFile.write('Number of upper case letters changed: ' + str(capitals) + '\n')
	newOutputFile.write('Number of punctuations removed: ' + str(punctuation) + '\n')
	newOutputFile.write('Number of numbers removed: ' + str(numbers) + '\n')
	newOutputFile.write('SpellChecking ################### \n')
	newOutputFile.write('Number of words: ' + str(numOfwords) + '\n')
	newOutputFile.write('Number of correct words: ' + str(correctWords) + '\n')
	newOutputFile.write('Number of incorrect words: ' + str(numOfwords-correctWords) + '\n')
	newOutputFile.close()
