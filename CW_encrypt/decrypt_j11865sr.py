import re
import sys
import os

inputPath = sys.argv[1]  
outputPath = sys.argv[2]
print(inputPath)
print(outputPath)

inputFiles = os.listdir(inputPath)


encryptionMethod = "unknown"

count = 0
for files in inputFiles:
	os.chdir(inputPath)

	with open (inputFiles[count], "r") as readFile:
		fileReader = readFile.readline()


	

	fileReader = fileReader.strip()

	count2 = 0
	for char in fileReader:
		if (fileReader[count2] == ":"):
			encryptedMsg = fileReader[count2 + 1:]
			encryptedMsg = encryptedMsg.strip()

		count2 += 1	


	

	wordList = re.split("\s", encryptedMsg)
	

	for char in wordList:
		if (re.search("\d[a-f]*", char)):
			encryptionMethod = "Hexadecimal"
		elif (re.search("\D|[a-z]|[A-Z]", char) and "-" not in char):
			encryptionMethod = "Caeser Cipher"	

		elif (re.search("\.|\-|\/", char)):
			encryptionMethod = "Morse Code"
		else:
			encryptionMethod = "unknown"		

	
	
	if(encryptionMethod == "Hexadecimal"):
		decryptedChars = []	
		decryptedSentence = ""
		for hexa in wordList:
			convertToInt =  int(hexa, 16)
			decryptedChars.append(chr(convertToInt))
			decryptedSentence = "".join(decryptedChars)
			
		


	elif(encryptionMethod == "Caeser Cipher"):
		plaintext = ""
		decryptedWords = []
		for words in wordList:
			for char in words:
				ASCIICipherChar = ord(char)
				ASCIIPlainChar = ASCIICipherChar - 3
				plaintext = plaintext + chr(ASCIIPlainChar)
				
			word = plaintext		
			decryptedWords.append(word)		
			plaintext = ""	

		decryptedSentence = " ".join(decryptedWords)	
		


	elif(encryptionMethod == "Morse Code"):
		decryptedWords = []
		morseCodeDictionary = { 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ': '/' }
		               
		for word in wordList:
			for key, value in morseCodeDictionary.items():
				if (word == value):	
					decryptedWords.append(key)
		decryptedSentence = "".join(decryptedWords)			
	    	               
		

	else:
		decryptedSentence = "Unknown encryption method"


	readFile.close()	
	
	os.chdir("..")
	os.chdir(outputPath)

	x = re.split(".txt", inputFiles[count], 1)
	print(x[0])
	fileWriter = open(x[0] + "_j11865sr.txt", "w")
	fileWriter.write(decryptedSentence)
	fileWriter.close

	os.chdir("..")
	count += 1
				

