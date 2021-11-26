import argparse,sys,os

wordsFile = open(sys.argv[1])
fileContent=wordsFile.read()
wordsFile.close()
inputFolder = sys.argv[2]
outputFolder= sys.argv[3]
if not os.path.exists(outputFolder):
	os.mkdir(outputFolder)
numbers=["0","1","2","3","4","5","6","7","8","9"]
punctuation=[".",",","?","!",":",";","-","(",")","[","]","{","}","'",'"',"@","#"]
uppercaseCount=0
punctuationCount=0
numberCount=0
wordCount=0
correctWordCount=0
inFolderList=os.listdir(inputFolder)

for file in inFolderList:
	if file.endswith('.txt'):
		inputFile=open(inputFolder + '/' + file)
		checkString=inputFile.read()
		inputFile.close()
		formattedString=""
		for i in range(len(checkString)):
			if checkString[i] in numbers:
				numberCount+=1
			elif checkString[i] in punctuation:
				punctuationCount+=1
			elif checkString[i].isupper():
				uppercaseCount+=1
				formattedString+=checkString[i].lower()
			else:
				formattedString+=checkString[i]
		splitString=formattedString.split()
		wordCount=len(splitString)
		fileWords=fileContent.split()
		for word in splitString:
			if word in fileWords:
				correctWordCount+=1

		incorrectWordCount=wordCount-correctWordCount
		newFile=file[:-4]
		outputFile=open(outputFolder + '/' + newFile + "_h01895cg.txt","w")
		outputFile.write("h01895cg\n")
		outputFile.write("Formatting ###################\n")
		outputFile.write("Number of upper case words transformed: " + str(uppercaseCount) + "\n")
		outputFile.write("Number of punctuation’s removed: " + str(punctuationCount) + "\n")
		outputFile.write("Number of numbers removed: " + str(numberCount) + "\n")
		outputFile.write("Spellchecking ###################\n")
		outputFile.write("Number of words in file: " + str(wordCount) +"\n")
		outputFile.write("Number of correct words in file: " + str(correctWordCount) + "\n")
		outputFile.write("Number of incorrect words in file: " + str(incorrectWordCount))

		numberCount=0
		punctuationCount=0
		wordCount=0
		correctWordCount=0
		uppercaseCount=0



