#Program which decrypts strings depending on how it was encoded

import argparse, os


def init(): #reads the input data from file, opens output file
		parser = argparse.ArgumentParser()
		parser.add_argument("dirIn")
		parser.add_argument("dirOut")

		args = parser.parse_args()
		dirs = vars(args)

		return dirs["dirIn"], dirs["dirOut"]

def getEncryptionMethod(string): #Finds out how the text is encrypted and removes the prefix
	if "Hex:" in string:
		encMethod = "Hex"
	elif "Caesar Cipher(+3):" in string:
		encMethod = "Csr"
	elif "Morse Code:" in string:
		encMethod = "Mor"
	else:
		encMethod = "n/a"

	while string[0] != ":":
		string = string[1:]

	string = string[1:]

	return encMethod, string

def decrypt(encType, string): #Decrypts the string
	newString = ""
	if encType == "Hex":
		charHex = ""
		for i in range(len(string)):
			charHex += string[i]
			if string[i] == " ":
				newString += chr(int("0x"+str(charHex),0)) # hexadecimal form
				charHex = ""
		newString += chr(int("0x"+str(charHex),0)) # no space at end of the text
			
	elif encType == "Csr":
		for i in range(len(string)):
			char = string[i]

			if string[i] == " ":
				newString += " "
				i += 2

			if ord(char) - 3 < 61 and char != " ":
				char = chr(ord(char) + 26)
			elif char == " ":
				char = chr(ord(char) + 3)	
			char = chr(ord(char) - 3)
			newString += char

	elif encType == "Mor":
		morse_dict = {
		"a":".-",
		"b":"-...",
		"c":"-.-.",
		"d":"-..",
		"e":".",
		"f":"..-.",
		"g":"--.",
		"h":"....",
		"i":"..",
		"j":".---",
		"k":"-.-",
		"l":".-..",
		"m":"--",
		"n":"-.",
		"o":"---",
		"p":".--.",
		"q":"--.-",
		"r":".-.",
		"s":"...",
		"t":"-",
		"u":"..-",
		"v":"...-",
		"w":".--",
		"x":"-..-",
		"y":"-.--",
		"z":"--..",
		"1":".----",
		"2":"..---",
		"3":"...--",
		"4":"....-",
		"5":".....",
		"6":"-....",
		"7":"--...",
		"8":"---..",
		"9":"----.",
		"0":"-----",
		}

		char = ""
		j = 0
		while j <= len(string):
			char = ""
			while j != len(string) and string[j] != " ":
				char += string[j]

				j += 1

			if char == "/":
				newString += " "
			j += 1

			for key, val in morse_dict.items():
				if char == val:
					newString += key

	return newString

def removeCaps(string):
	string = list(string)
	for i in range(len(string)):
		if 65 <= ord(string[i]) <= 90:
			string[i] = chr(ord(string[i]) + 32)
	string = "".join(string)
	return string


dirIn, dirOut = init()

for file in os.listdir(dirIn):
	currentfile = os.path.join(dirIn,file)

	currentfile = open(currentfile, "r")

	inputData = currentfile.read()
	currentfile.close()

	encMethod, encText = getEncryptionMethod(inputData)
	decText = decrypt(encMethod, encText)
	decText = removeCaps(decText)


	file = os.path.join(dirOut,file.rsplit(".",1)[0])

	fileOut = open(file+"_q44958jp.txt","w")

	fileOut.write(decText)
	fileOut.close()
