inputFileName = input("Please enter the name of the file including the extension: ")



englishWordFile = open("englishWords.txt", "r")
englishWordList = []
inputList = []

for i in englishWordFile:
	word = i.strip()
	englishWordList.append(word)
#CREATES A LIST STORING ALL WORDS IN ENGLISHWORDS TEXT FILE 
englishWordFile.close()

inputFile = open(inputFileName, "r")
for item in inputFile:
	inputString = item
	#print(inputString)
	numbers = "0123456789"
	punctuation = ".?!$£%^&*():;',/"
	punctuation = punctuation + '"'
	upperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numberCount = 0
	punctuationCount = 0
	upperCaseCount = 0 


	for i in inputString:
		if i in punctuation:
			inputString = inputString.replace(i,"")
			punctuationCount+=1
		elif i in numbers:
			inputString = inputString.replace(i, "")
			numberCount+=1
		elif i in upperCaseLetters:
			inputString = inputString.lower()
			upperCaseCount+=1


	#print(inputString)
inputFile.close()
#CREATES A VARIABLE STORING THE STRING ENTERED BY THE USER IN THE CORRECT FORMAT
for i in range(0, len(inputString)):
	inputList = inputString.split()
#print(inputList)
#CREATES A LIST OF WORDS IN VARIABLE
incorrectWordsList = []
correctWords = 0 
incorrectWords = 0
NumOfWords = len(inputList)
for word in inputList:
	if word in englishWordList: 
		correctWords+=1
	else:
		incorrectWords+=1
		incorrectWordsList.append(word)


#print(incorrectWordsList)
	


print("Y41988AL")
print("Formatting #################")
print("Number of upper case letters changed: "+ str(upperCaseCount))
print("Number of punctuations removed: "+ str(punctuationCount))
print("Number of numbers removed: "+ str(numberCount))
print("SpellChecking ###############")
print("Number of words: "+str(NumOfWords))
print("Number of correct words: "+ str(correctWords))
print("Number of incorrect words: "+ str(incorrectWords))

#print("################################")
outputFileName = input("Please enter the name of the file you wish to output the data to including the extension: ")
outputFile = open(outputFileName, "w")
outputFile.write("Y41988AL \nFormatting ################# " + "\nNumber of upper case letters changed: "+ str(upperCaseCount) +
	"\nNumber of punctuations removed: "+ str(punctuationCount) + "\nNumber of numbers removed: "+ str(numberCount) + 
	"\nSpellChecking ###############" + "\nNumber of words: "+str(NumOfWords) + "\nNumber of correct words: "+ str(correctWords)+
	"\nNumber of incorrect words: "+ str(incorrectWords) )
outputFile.close()