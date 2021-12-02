import sys
import os
inputFolder = sys.argv[1]
outputFolder = sys.argv[2]




#decryption functions

def decryptCeasar(textInput):
	result = ""
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for x in range(len(textInput)):
		if textInput[x] == " ":
			result = result + " "
			continue
		for y in range (len(alphabet)):
			if textInput[x] == alphabet[y]:
				result = result + alphabet[y-3]
	return result.lower()


def decryptHex(textInput):
	result = ""
	textList = textInput.split(" ")
	for item in textList:
		asciiNum = int(item, 16)
		result = result + chr(asciiNum)
	return result.lower()

def decryptMorse(textInput):
	result = ""
	chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9'," "]
	morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.','/']
	morseDict = dict(zip(chars, morse))
	entries = textInput.split(" ")
	for char in entries:
		for key, value in morseDict.items():
			if char == value:
				result = result + key
	return result.lower()



#main

for inputFile in os.listdir(inputFolder):

	with open(inputFolder + "/" + inputFile, 'r') as i:
		inptxt = i.readlines()[0]
		cipherType = inptxt.split(":")[0]
		encrypted = inptxt.split(":")[1]
		

		if cipherType == "Caesar Cipher(+3)":
			plainText = decryptCeasar(encrypted)
		elif cipherType == "Hex":
			plainText = decryptHex(encrypted)
		elif cipherType == "Morse Code":
			plainText = decryptMorse(encrypted)
		
	with open(outputFolder + "/" + inputFile[:-4] + "_s78014sh.txt", 'w+') as o:
			o.write(plainText)



		