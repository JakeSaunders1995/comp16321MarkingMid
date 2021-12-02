import sys
import os

inputFolder = sys.argv[-2]
outputFolder = sys.argv[-1]

if not os.path.isdir(outputFolder):
	os.mkdir(outputFolder)
else:
	pass


def Decryption(inputFile):

	encryptedString = inputFile

	cipherFormat = encryptedString.split(":")[0]
	cipherText = encryptedString.split(":")[1]

	encryptionMethods = ["C", "H", "M"]


	def CaesarDecryption(text):
		decipheredText = ""
		for item in text:
			if item.isalpha():
				asciiItem = ord(item)
				letter = asciiItem - 3
				if letter < ord("a"):
					letter += 26
				engLetter = chr(letter)
				decipheredText += engLetter
			elif item == " ":
				decipheredText+= " "
				decipheredText = decipheredText.lower()
		return decipheredText

	def HexDecryption(text):
		decipheredText = ""
		chars = text.split(" ")
		for char in chars:
			val = int(char,16)
			decipheredText += chr(val)
			decipheredText = decipheredText.lower()
		return decipheredText

	def MorseDecryption(text):
		morseDict 	= { 'a':'.-', 'b':'-...',
	                    'c':'-.-.', 'd':'-..', 'e':'.',
	                    'f':'..-.', 'g':'--.', 'h':'....',
	                    'i':'..', 'j':'.---', 'k':'-.-',
	                    'l':'.-..', 'm':'--', 'n':'-.',
	                    'o':'---', 'p':'.--.', 'q':'--.-',
	                    'r':'.-.', 's':'...', 't':'-',
	                    'u':'..-', 'v':'...-', 'w':'.--',
	                    'x':'-..-', 'y':'-.--', 'z':'--..',
	                    '1':'.----', '2':'..---', '3':'...--',
	                    '4':'....-', '5':'.....', '6':'-....',
	                    '7':'--...', '8':'---..', '9':'----.',
	                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
	                    '?':'..--..', '/':'-..-.', '-':'-....-',
	                    '(':'-.--.', ')':'-.--.-'}
		
		decipheredText = ""
		morseString = text.split("/")
		for word in morseString:
			splitWord = word.split(" ")
			for letter in splitWord:
				for char,morse in morseDict.items():
					if morse == letter:
						decipheredText += char
					else:
						pass
			decipheredText += " "
			decipheredText = decipheredText.lower()
		return decipheredText


	if cipherFormat[0] == encryptionMethods[0]:
		plainText = CaesarDecryption(cipherText)
	elif cipherFormat[0] == encryptionMethods[1]:
		plainText = HexDecryption(cipherText)
	else:
		plainText = MorseDecryption(cipherText)

	return plainText

for testFile in os.listdir(inputFolder):
	with open(os.path.join(inputFolder,testFile), "r") as inputFile:
		inputFile = inputFile.read()
		output = Decryption(inputFile)
		testVal = testFile.rstrip(".txt")
		testFileAndID = testVal + "_s11642lf.txt"
		with open(os.path.join(outputFolder,testFileAndID),"w+") as outputFile:
			outputFile.write(output)
			outputFile.close()