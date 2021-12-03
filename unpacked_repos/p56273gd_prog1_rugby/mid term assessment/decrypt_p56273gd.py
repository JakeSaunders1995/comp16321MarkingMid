import os, argparse
parser = argparse.ArgumentParser()
parser.add_argument("inputFile")
parser.add_argument("outputFolder")
args = parser.parse_args()
input1 = args.inputFile
output = args.outputFolder

inputtedFiles = os.listdir(input1)

# inputtedFile = open(input1, "r")
# inputtedFile = inputtedFile.read()



def determineEncryption(inputtedFile):
	splitString = inputtedFile.split(":")
	encryptionType = ""
	if splitString[0] == "Hex":
		print("Encryption type is Hexadecimal")
		encryptionType = "hex"

	# for some reason it would not compare Caeser Cipher(+3) to split string[0] so i had to use this method for caeser instead
	elif inputtedFile[0] == "C":
		print("Encryption type is caeser cipher")
		encryptionType = "caeser"
	elif splitString[0] == "Morse Code":
		print("Encryption type is morse code")
		encryptionType = "morse"

	return encryptionType

def GetEncryptedText(inputtedFile):
	splitString = inputtedFile.split(":")
	encryptedText = ""
	encryptedText = splitString[1]
	print (encryptedText)
	return encryptedText

def decryptHex(encryptedText):
	decryptedText = ""
	decryptedText = bytes.fromhex(encryptedText).decode("utf-8")
	print(decryptedText)
	return decryptedText

def decryptCaeser(encryptedText):
	decryptedText = ""
	for i in range(len(encryptedText)-1):
		letter = encryptedText[i]
		if letter == " ":
			decryptedText += " "

		elif letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			asciiValue = ord(letter)
			asciiValue = (asciiValue-3-48)%10 + 48
			decryptedText += chr(asciiValue)

		else:
			asciiValue = ord(letter)
			asciiValue = (asciiValue-3-97)%26 + 97
			decryptedText += chr(asciiValue)
	print(decryptedText)
	return decryptedText

def decryptMorse(encryptedText):
	morseDictionary = {'.-': 'a',   '-...': 'b',   '-.-.': 'c',
		   '-..': 'd',      '.': 'e',   '..-.': 'f',
		     '--.': 'g',   '....': 'h',     '..': 'i',
		     '.---': 'j',    '-.-': 'k',   '.-..': 'l',
		    '--': 'm',     '-.': 'n',    '---': 'o', 
		  '.--.': 'p',   '--.-': 'q',    '.-.': 'r',
		   '...': 's',      '-': 't',    '..-': 'u', 
		  '...-': 'v',    '.--': 'w',   '-..-': 'x',
		  '-.--': 'y',   '--..': 'z',  '-----': '0', 
		 '.----': '1',  '..---': '2',  '...--': '3',
		 '....-': '4',  '.....': '5',  '-....': '6', 
		 '--...': '7',  '---..': '8',  '----.': '9'}
	decryptedText = " "
	splitUpText = encryptedText.split(" ")
	for i in splitUpText:
		if i == "/":
			decryptedText += " "
		else:
			decryptedText += morseDictionary[i]
	print(decryptedText)
	return decryptedText

def WriteToFile(decryptedText, output, fileName):
	fileToOutput = os.path.join(output, fileName + "_p56273gd.txt")
	file = open(fileToOutput, "w")
	file.write(decryptedText)



for file in inputtedFiles:
	fileLocation = os.path.join(input1, file)
	cipherText = open(fileLocation, "r")
	cipherText = cipherText.read()

	encryptionType = determineEncryption(cipherText)

	encryptedText = GetEncryptedText(cipherText)
	decryptedText = ""

	if encryptionType == "hex":
		decryptedText = decryptHex(encryptedText)
	elif encryptionType == "caeser":
		decryptedText = decryptCaeser(encryptedText)
	elif encryptionType == "morse":
		decryptedText = decryptMorse(encryptedText)

	fileSplit = file.split(".")
	fileName = fileSplit[0]


	WriteToFile(decryptedText, output, fileName)