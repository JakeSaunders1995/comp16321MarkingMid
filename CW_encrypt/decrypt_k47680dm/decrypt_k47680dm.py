import sys
import os

cipherText = ""
plainText = ""

def GetCiphersFromFiles():
	ciphers = []

	txtFiles = os.listdir(sys.argv[1])
	txtFiles.sort()

	for i in range(len(txtFiles)):
		file = open(sys.argv[1] + "/" + txtFiles[i])
		ciphers.append(file.read())

	return ciphers

def GetType():
	typeName = cipherText.split(':')
	if typeName[0] == "Morse Code":
		return 0
	elif typeName[0] == "Caesar Cipher(+3)":
		return 1
	elif typeName[0] == "Hex":
		return 2

def DecodeMorse(actual):

	morseCodes = ['.-',
            	'-...',
            	'-.-.',
            	'-..',
            	'.',
            	'..-.',
            	'--.',
            	'....',
            	'..',
            	'.---',
            	'-.-',
	            '.-..',
	            '--',
	            '-.',
	            '---',
	            '.--.',
	            '--.-',
	            '.-.',
	            '...',
	            '-',
	            '..-',
	            '...-',
	            '.--',
	            '-..-',
	            '-.--',
	            '--..']

    

	plain = ""
	letters = actual.split(" ")

	for i in range(len(letters)):
		if letters[i] == "/":
			plain += " "
		else:
			index = morseCodes.index(letters[i])
			val = 97 + index
			plain += chr(val)


	return plain


def DecodeCaesar(actual):
	plain = ""

	for i in range(len(actual) - 1):
		if actual[i] == " ":
			plain += " "

		else:
			val = ord(actual[i])
			val -= 3

			if val == 96:
				val = 122
			elif val == 95:
				val = 121
			elif val == 94:
				val = 120
			plain += chr(val)

	return plain



def DecodeHex(actual):
	letters = actual.split(" ")
	plain = ""

	for i in range(len(letters)):
		number = int(letters[i], 16)
		plain += chr(number)

	plain = plain.lower()


	return plain

def ReturnPlainText(i, plainText):
	i+=1
	file = open(sys.argv[2] + "/" + "test_file" + str(i) + "_k47680dm.txt", "w")
	file.write(plainText)
	file.close()


cipherTexts = GetCiphersFromFiles()

for j in range(len(cipherTexts)):

	cipherText = cipherTexts[j]

	typeCipher = GetType()

	actualCipher = cipherText.split(":")[1]

	if typeCipher == 0:
		plainText = DecodeMorse(actualCipher)
	elif typeCipher == 1:
		plainText = DecodeCaesar(actualCipher)
	elif typeCipher == 2:
		plainText = DecodeHex(actualCipher)

	ReturnPlainText(j, plainText)