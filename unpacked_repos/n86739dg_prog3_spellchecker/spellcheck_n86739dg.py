import os, sys, argparse


# handle input arguments
if len(sys.argv) == 4:

	dictionaryEnglishWords = sys.argv[1]
	inputDirectory = sys.argv[2]
	outputDirectory = sys.argv[3]

    #print(inputDirectory)
	for currentFileName in os.listdir(inputDirectory):
		#print(currentFileName)		
        
		with open(inputDirectory + "/" + currentFileName, 'r') as f:
            
            # step 1 - READ CURRENT FILE
			currentFileContents = f.read()
			print(currentFileContents)
			f.close()

            # step 2 - DO LOGIC
			text = currentFileContents 
			#MORE VARIABLES
				#formatting
			upperCaseTrans = 0
			puncRemoved = 0
			numRemoved = 0
				#spellchecking
			correctWords = 0
			incorrectWords = 0

			#OTHER VARIABLES

			punc = """!\()-,[]{};:'"<>./?$%^&*_~"""
			result = "" #WE ARE GOING TO BE ACCUMULATING CHARACTERS TO THIS VARIABLE

			#LET'S BEGIN CHECKING EACH CHARACTER OF TEXT...

			i = 0

			while i < len(text):

				#FORMATTING

				if (97 <= ord(text[i]) <= 122):
					result += text[i]
				if (65 <= ord(text[i]) <= 90): #FOR UPPERCASE 
					result += chr(ord(text[i]) + 32) #TRANSFORM TO LOWER CASE THROUGH ASCII 
					upperCaseTrans += 1
				if text[i] in punc: #REMOVING PUNCTUATION
					result += text[i].replace(text[i], "")
					puncRemoved += 1
				if text[i].isdigit() == True: #REMOVING DIGIT CHARACTERS (NUMBERS)
					result += ""
					numRemoved += 1				 				
				if text[i] == ' ':
					result += ' ' #ADD SPACE WHEN SPACE IS REACHED
				i += 1


			#print(result) #THIS IS THE TEXT WITHOUT NUMBERS, PUNCTUATION AND UPPERCASE CONVERTED TO LOWERCASE 

			#SPELLCHECKING

			listOfResult = result.split() #CREATING LIST OF WORDS OF INPUT GIVEN CORRECTED
			numOfWords = len(listOfResult)

			with open(dictionaryEnglishWords, 'r') as g:
				dicEnglishWords = g.read()
				g.close()
			dicEnglishWords = dicEnglishWords.split() #CREATES LIST OF ENGLISH WORDS

			for i in listOfResult:
				if i in dicEnglishWords:  #COMPARING BOTH LISTS, IF IT IS NOT EQUAL, THEN IT WOULD BE AN INCORRECT WORD
					correctWords += 1
					#print("correct")
				else:
					incorrectWords += 1
					#print("incorrect")



			#PRINTING

			#FORMATTING
			print("n86739dg")
			print("Formatting ###################")
			print("Number of upper case letters changed: " + str(upperCaseTrans))
			print("Number of punctuations removed: " + str(puncRemoved))
			print("Number of numbers removed: " + str(numRemoved))
			#SPELLCHECKING
			print("Spellchecking ###################")
			print("Number of words: " + str(numOfWords))
			print("Number of correct words: " + str(correctWords))
			print("Number of incorrect words: " + str(incorrectWords))

            # step 3 - CREATING OUTPUT FILEPATH AND FILENAME
			fileSplitArray = os.path.splitext(currentFileName)
			currentOutputFileName = outputDirectory + "/" + fileSplitArray[0] + "_n86729dg" + fileSplitArray[1]
			#print(currentOutputFileName)

            # step 4 - WRITE CONTENTS ON OUTPUT FILE
			currentFileWriter = open(currentOutputFileName, "w")
			currentFileWriter.write("n86739dg\n" + "Formatting ###################\n" + "Number of upper case letters changed: " 
		+ str(upperCaseTrans) + "\nNumber of punctuations removed: " + str(puncRemoved) + 
		"\nNumber of numbers removed: " + str(numRemoved) + "\nSpellchecking ###################" 
		+ "\nNumber of words: " + str(numOfWords) + "\nNumber of correct words: " + str(correctWords)
		+ "\nNumber of incorrect words: " + str(incorrectWords))
			currentFileWriter.close()
else:
	print("Invalid parameters error. Expected: python3 spellcheck_n86739dg.py ./EnglishWords.txt ./[input folder] ./[output folder]")


