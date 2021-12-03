import sys
import os

def hex(file):
	for character in range(len(file)):
		if file[character] == ':':
			substringText = file[character+1:len(file)]
	decipherText = bytearray.fromhex(substringText).decode().lower()
	return(decipherText)

def caesar(file):
	alphabet = 'abcdefghijklmnopqrstuvwxyzabc'
	plainText = ""
	for character in range(len(file)):
		if file[character] == ':':
			substringText = file[character+1: len(file)] #adds everything in file from the colon to the end into the substring	
	for character in range(len(substringText)):
		for letter in range(len(alphabet)-3):
			if alphabet[letter] == substringText[character]:
				plainText += alphabet[letter-3]
		if substringText[character] == " ":
			plainText += " "
	return(plainText)

def morse(file):
	morseCode = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '/']
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
	plainText = ""
	morseInFile = ""
	morseList =[]
	firstCharacterIndex = 0
	numOfSpaces = 0
	for character in range(len(file)):
		if file[character] == ':':
			substringText = file[character+1: len(file)]#store everything from the colon into the substring
	
	for character in range(len(substringText)):
		
		if substringText[character] == " " and numOfSpaces != 0:
			i = firstCharacterIndex
			while substringText[i] != " " and i <= len(substringText):
				morseInFile += substringText[i]
				i += 1
				if substringText[i] != " " and i == len(substringText):
					morseInFile += substringText[i]
				elif substringText[i] == " " and i == len(substringText):
					morseInFile += substringText[i]
			morseList.append(morseInFile)
			morseInFile = ""
			numOfSpaces += 1
			firstCharacterIndex = character + 1

		elif substringText[character] == " " and numOfSpaces == 0:
			i = 0
			while substringText[i] != " " and i<len(substringText)-1:
				morseInFile += substringText[i]
				i += 1
			morseList.append(morseInFile)
			morseInFile = ""
			numOfSpaces += 1
			firstCharacterIndex = character + 1

		elif len(substringText)-1 == character:
			morseInFile += substringText[character]
			morseList.append(morseInFile)

	for character in range(0, len(morseList)):
		for morse in range(0, len(morseCode)):
			if(morseList[character]==morseCode[morse]):
				plainText += alphabet[morse]
	return(plainText)

for file1 in sorted(os.listdir(sys.argv[1])): #goes through the files in the directory in order
	file = open(os.path.join(sys.argv[1], file1),'r') #Example_inputs/test_file1.txt 
	readFile = file.read()
	if readFile[0] == "H":
		decrypt = hex(readFile)
	if readFile[0] == "C":
		decrypt = caesar(readFile)
	if readFile[0] == "M":
		decrypt = morse(readFile)
	decryptedFile = open(os.path.join(sys.argv[2], file1[:-4] +'_h60953dl.txt'), 'w')
	decryptedFile.write(decrypt)
	decryptedFile.close()