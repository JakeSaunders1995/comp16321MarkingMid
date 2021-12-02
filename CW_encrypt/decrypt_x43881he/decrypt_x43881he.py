import sys, os
from pathlib import Path
import ntpath

InFile = sys.argv[1]
OutFile = sys.argv[2]

for in_entry in os.scandir(InFile):
	FileIn = open(in_entry.path, 'r')
	cipher_text = FileIn.readline().strip()
	FileIn.close()

	File2 = Path(in_entry).stem + "_x43881he.txt"
	File2 = os.path.join(OutFile, File2)
	FileOut = open(File2, 'w+')

	if cipher_text.startswith('M'):
		MorseDecryption = {
			'a': '.-',
			'b': '-...',
			'c': '-.-.',
			'd': '-..',
			'e': '.',
			'f': '..-.',
			'g': '--.',
			'h': '....',
			'i': '..',
			'j':'.---',
			'k': '-.-',
			'l': '.-..',
			'm': '--',
			'n': '-.',
			'o': '---',
			'p': '.--.',
			'q': '--.-',
			'r': '.-.',
			's': '...',
			't': '-',
			'u': '..-',
			'v': '...-',
			'w': '.--',
			'x': '-..-',
			'y': '-.--',
			'z': '--..',
			'0': '-----',
			'1': '.----',
			'2': '..---',
			'3': '...--',
			'4': '....-',
			'5': '.....',
			'6': '-....',
			'7': '--...',
			'8': '---..',
			'9': '----.',
			'.': '.-.-.-',
			',': '--..--',
			':': '---...',
			'?': '..--..',
			'-': '-....-',
			'@': '.--.-.',
			'=': '-...-',
			' ': '/'
			}
		alphabet = " "
		decrypt_morse_code = {a:b for b,a in MorseDecryption.items()}
		sentence = cipher_text[11:]
		cipher_text = sentence.split()
		for x in cipher_text:
			text = decrypt_morse_code.get(x)
			alphabet = str(alphabet) + str(text)
			alphabet_in_lower_case = alphabet.lower()
		FileOut.write(alphabet_in_lower_case) 
	

	if cipher_text[0] == 'C':
		word = ""
		index = 18
		while index < len(cipher_text):
			if cipher_text[index] == " ":
				word += " "
				index += 1
			else :
				codeChar = cipher_text[index]
				ASCIIValue = ord(codeChar)
				ASCIIValue = ASCIIValue - 3
				word = word + chr(ASCIIValue)
				index = index + 1
		word_in_lower_case = word.lower()
		FileOut.write(word_in_lower_case)

	if cipher_text[0] == 'H':
		hexa = cipher_text[4:]
		decrypt = bytes.fromhex(hexa)
		decrypthexa = decrypt.decode("ascii")
		lowercase = decrypthexa.lower()
		FileOut.write(str(lowercase))
	
	FileOut.close()