import os
import sys
directory = sys.argv[1]
outputDirectory = sys.argv[2]
for filename in os.listdir(directory):
	filepath = directory + "/" + filename
	text_file = open(filepath, "r")
	encryption = text_file.read()

	plainText = ""
	identifier = []
	decryption = []
	identifier.append(encryption)

	if identifier[0][0] == "c" or identifier[0][0] == "C":
		cipherText = '' .join([str(item) for item in identifier])
		cipherText.split(':')
		cipherText = cipherText.split(':')[1]
		plainText = ""
		ciphertextPosition = 0
		while ciphertextPosition < len(cipherText):
			ciphertextChar = cipherText[ciphertextPosition]
			ASCIIValue = ord(ciphertextChar)
			if ASCIIValue == 65 or ASCIIValue == 66 or ASCIIValue == 67:
				ASCIIValue =  ASCIIValue + 55
				plainText = plainText + chr(ASCIIValue)
			elif ASCIIValue == 97 or ASCIIValue == 98 or ASCIIValue == 99:
				ASCIIValue =  ASCIIValue - 9
				plainText = plainText + chr(ASCIIValue)
			elif ASCIIValue <= 122 and ASCIIValue >= 100:
				ASCIIValue = ASCIIValue - 3
				plainText = plainText + chr(ASCIIValue)
			else:
				plainText = plainText + chr(ASCIIValue)
			ciphertextPosition += 1
		outputFile = outputDirectory + "/" + filename[0:-4] + "_" + "f37609ak" + ".txt"
		f = open(outputFile, "w")
		f.write(plainText.lower())
		f.close

	if identifier[0][0] == "h" or identifier[0][0] == "H":
		cipherText = '' .join([str(item) for item in identifier])
		cipherText.split(':')
		cipherText = cipherText.split(':')[1]
		sentence = cipherText.replace(" ","")
		plainText = ""
		for i in range (0, len(sentence), 2):
			extract = sentence[i : i+2]
			ch = chr(int(extract, 16))
			plainText += ch 
		outputFile = outputDirectory + "/" + filename[0:-4] + "_" + "f37609ak" + ".txt"
		f = open(outputFile, "w")
		f.write(plainText.lower())
		f.close

	if identifier[0][0] == "m" or identifier[0][0] == "M":
		outputFile = outputDirectory + "/" + filename[0:-4] + "_" + "f37609ak" + ".txt"
		morseCode = { '/': ' ', '.-':'a', '-...':'b','-.-.':'c', '-..':'d', '.':'e','..-.':'f', '--.':'g', '....':'h','..':'i', '.---':'j', '-.-':'k','.-..':'l', '--':'m', '-.':'n','---':'o', '.--.':'p', '--.-':'q','.-.':'r', '...':'s', '-':'t','..-':'u', '...-':'v', '.--':'w','-..-':'x', '-.--':'y', '--..':'z','.----':'1', '..---':'2', '...--':'3','....-':'4', '.....':'5', '-....':'6','--...':'7', '---..':'8', '----.':'9','-----':'0', '--..-- ':',', '.-.-.-':'.','..--..':'?', '-..-.':'/', '-....-':'-','-.--.':'(', '-.--.-':')'}
		decryption = '' .join([str(item) for item in identifier])
		decryption.split(':')
		decryption = decryption.split(':')[1]
		decryption += ' '
		words = ''
		plainText = " "
		for i in decryption:
			if i != ' ':
				words += i
			else:
				plainText += morseCode[words] 
				words = ''
		outputFile = outputDirectory + "/" + filename[0:-4] + "_" + "f37609ak" + ".txt"
		f = open(outputFile, "w")
		f.write(plainText.lstrip())
		f.close

	text_file.close()


	



	






