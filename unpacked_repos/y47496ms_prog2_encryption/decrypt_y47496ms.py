# Decryption Program

import argparse
import os
from argparse import ArgumentParser

parser = argparse.ArgumentParser()
parser.add_argument('inputs', type=str, help='Input folder')
parser.add_argument('outputs', type=str, help='Output folder')
args = parser.parse_args()

for files in os.listdir(args.inputs):
	if files.endswith(".txt"):
		inputfile = (os.path.join(args.inputs, files))
		files = files[:-4] + "_y47496ms.txt"
		outputfile = (os.path.join(args.outputs, files))

		# Open the files to read

		file = open(inputfile, 'rt')
		input2 = file.read()

		# Hexadecimal decryption:

		if "Hex" in input2:

			input3 = input2.split(":")
			input4 = input3[1]
			input5 = bytearray.fromhex(input4)
			decimal = input5.decode("ASCII")
			hexa = decimal.lower()
			output = open(outputfile, 'wt')
			output.write(hexa)
			output.close()

		# Caesar Cipher decryption:

		if "Caesar" in input2:

			input6 = input2.split("(+3):")
			preplaintext = input6[1]
			plaintext = preplaintext.lower()
			ciphertext = ""
			plaintextposition = 0
			plaintextlen = len(plaintext)

			while plaintextposition < plaintextlen:
				plaintextchar = plaintext[plaintextposition]
				if plaintextchar == " ":
					ciphertext += " "
					plaintextposition += 1
				else:
					ASCIIValue = ord(plaintextchar)
					ASCIIValue -= 3
					if ASCIIValue < 97:
						ASCIIValue += 26
					elif ASCIIValue > 122:
						ASCIIValue -= 26
					ciphertext += chr(ASCIIValue)
					plaintextposition += 1

					caesartext = ""
					punctuation = [".", "?", "!", ",", ":", ";", "-", "–", "—", "--", "(", ")", "[", "]", "{", "}", '"', "'", "…"]
					for x in ciphertext:
						if x in punctuation:
							caesartext += ""
						else:
							caesartext += x

			else:
				# caesartext = ciphertext.lower()
				output = open(outputfile, 'wt')
				output.write(caesartext)
				output.close()

		# Morse Code decryption:

		if "Morse" in input2:

			morsecodedictionary = {
				'.-': 'a',
				'-...': 'b',
				'-.-.': 'c',
				'-..': 'd',
				'.': 'e',
				'..-.': 'f',
				'--.': 'g',
				'....': 'h',
				'..': 'i',
				'.---': 'j',
				'-.-': 'k',
				'.-..': 'l',
				'--': 'm',
				'-.': 'n',
				'---': 'o',
				'.--.': 'p',
				'--.-': 'q',
				'.-.': 'r',
				'...': 's',
				'-': 't',
				'..-': 'u',
				'...-': 'v',
				'.--': 'w',
				'-..-': 'x',
				'-.--': 'y',
				'--..': 'z',
				'.----': '1',
				'..---': '2',
				'...--': '3',
				'....-': '4',
				'.....': '5',
				'-....': '6',
				'--...': '7',
				'---..': '8',
				'----.': '9',
				'-----': '0',
				'..--..': '?',
				'-.-.--': '!',
				'.-.-.-': '.',
				'--..--': ',',
				'-.-.-.': ';',
				'---...': ':',
				'.-.-.': '+',
				'-....-': '-',
				'-..-.': '/',
				'-..-.': '=',
				'/': ' ',
				'-.--.-': ')',
				'-.--.': '(',
				'.-..-.': '"',
				'.----.': "'",
			}

			input7 = input2.split(":")
			input8 = input7[1]
			morsetext = input8.split(" ")
			decrypted = ""
			morsetextlen = len(morsetext)

			for i in range(0, morsetextlen):
				if morsetext[i] in morsecodedictionary:
					decrypted += morsecodedictionary[morsetext[i]]

			output = open(outputfile, 'wt')
			output.write(decrypted)
			output.close()

