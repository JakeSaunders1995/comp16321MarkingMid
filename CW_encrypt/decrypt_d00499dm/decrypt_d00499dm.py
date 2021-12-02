import sys
import os

input = sys.argv[1]
output = sys.argv[2]
inputfile = os.listdir(input)

for p in inputfile:

	file = open(input + "/" + p,'r')
	inputtext = file.read()
	if inputtext[0] == "C" or "c":
		#decrypting caesar cipher
		plaintext= ""
		ciphertext= inputtext	
		ciphertext= ciphertext.lower().replace(" ","")
		alphabet="abcdefghijklmnopqrstuvwxyzabc"

		ciphertextposition=0

		while ciphertextposition<len(ciphertext):
			ciphertextChar = ciphertext[ciphertextposition]
			alphabetposition=0
			while ciphertextChar != alphabet[alphabetposition]:
				alphabetposition += 1
				continue
			alphabetposition -= 3
			plaintext += alphabet[alphabetposition]		
			ciphertextposition += 1


		print(plaintext)	

		if inputtext[0] == "H" or "h":		#MAKE SURE YOU DO THE PART WHERE YOU HAVE TO SKIP THE FIRST FEW LETTER BECAUSE OF 'MORSE' OR 'HEXA'
			#decrypting hexadecimal
			def convertHex(hexSubString):
				return chr(int(hexSubString, 16))

			hexString = inputtext
			hexString = hexString.replace(" ","")
			outString = ""



			if len(hexString) % 2 == 0:
				for i in range(0,len(hexString), 2):
					subStr = hexString[i] + hexString[i+1]
					outString += convertHex(subStr)

			print(outString)	

		elif inputtext[0] == "M" or "m":
			for x in range(11,len(inputtext)):
				CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
				        'D': '-..',    'E': '.',      'F': '..-.',
				        'G': '--.',    'H': '....',   'I': '..',
				        'J': '.---',   'K': '-.-',    'L': '.-..',
				        'M': '--',     'N': '-.',     'O': '---',
				        'P': '.--.',   'Q': '--.-',   'R': '.-.',
				        'S': '...',    'T': '-',      'U': '..-',
				        'V': '...-',   'W': '.--',    'X': '-..-',
				        'Y': '-.--',   'Z': '--..',

				        '0': '-----',  '1': '.----',  '2': '..---',
				        '3': '...--',  '4': '....-',  '5': '.....',
				        '6': '-....',  '7': '--...',  '8': '---..',
				        '9': '----.',  ' ': '/'
				        }

				CODE_REVERSED = {value:key for key,value in CODE.items()}

				value = inputtext

				code = value.split()

				for element in range(0,len(code)):
					print(CODE_REVERSED.get(code[element]), end='')