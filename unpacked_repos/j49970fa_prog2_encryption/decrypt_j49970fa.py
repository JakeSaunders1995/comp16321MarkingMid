import os
import sys 

morseDict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 
			'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 
			'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '1':'.----', '2':'.----', '3':'.----', 
			'4':'.----', '5':'.----', '6':'.----', '7':'.----', '8':'.----', '9':'.----', '0':'.----', 
			'&':'.-...', '\'':'.----.', ')':'-.--.-', '(':'-.--.', ':':'---...', ',':'--..--', '=':'-...-', '!':'-.-.--',
			 '.':'.-.-.-', '-':'-....-', ';':'-.-.-.', '"':'.-..-.', '?':'..--..', '/':'-..-.'
}

# Output File function
def outputFile(content):
	outputFile = open(os.path.join(sys.argv[2], "".join(files.split(".")[0]) + '_j49970fa.txt'), "w")
	outputFile.write(content)
	outputFile.close()

# Real program starts from here
for files in os.listdir(sys.argv[1]):
	file = open(os.path.join(sys.argv[1],files))
	f = file.read()
	splitF = f.split(":")

	# Hexadecimal
	if splitF[0].startswith("H"):
		outputFile(bytearray.fromhex(splitF[-1]).decode().lower())

	# Caesar +3
	elif splitF[0].startswith("C"):
		plain_text = ''
		cipher = splitF[-1].lower().split(" ")
		for encrypted in cipher:
			decrypted = ''
			alphabet = "abcdefghijklmnopqrstuvwxyz"
			
			for letter in encrypted:
				if letter in alphabet:
					position = alphabet.find(letter) - 3
					if position < 0:
						position += 26
					decrypted = decrypted + alphabet[position]

			if plain_text == '':
				plain_text = decrypted
			else:
				plain_text = plain_text + ' ' + decrypted

		outputFile(plain_text)

	# Morse code
	elif splitF[0].startswith("M"):
		morseLetter = splitF[-1].split("/")
		plain_text = ''
		for letter in morseLetter:
			morseChar = letter.split(" ")
			decrypted = ''
			for char in morseChar:
				for key in morseDict:
					if char == morseDict[key]:
						decrypted = decrypted + key

			if plain_text == '':
				plain_text = decrypted
			else:
				plain_text = plain_text + ' ' + decrypted

		outputFile(plain_text)

	file.close()
