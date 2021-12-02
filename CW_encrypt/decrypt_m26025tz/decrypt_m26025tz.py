import sys
import os

input_folder = sys.argv[1]
output_folder = sys.argv[2]
input_files = os.listdir(input_folder)
for input_file in input_files:
	position = input_folder +"//" + input_file
	with open(position) as f:
		contents = f.read()
	x = len(contents)
	if contents[0] == 'H':
		output = (bytes.fromhex(contents[4:x+1]).decode('utf-8'))

	elif contents[0] == 'C':
		plaintext = contents[18:x+1].lower()
		cipherText = ""
		alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
		plaintextPosition = 0
		while plaintextPosition<len(plaintext):
			plaintextChar = plaintext[plaintextPosition]
			alphabetposition = 3
			if plaintext[plaintextPosition] == " ":
				cipherText = cipherText + " "
				plaintextPosition += 1
				continue
			elif plaintext[plaintextPosition] not in alphabet and  " ":
				plaintextPosition += 1
				continue
			while plaintextChar != alphabet[alphabetposition]:
				alphabetposition += 1
			alphabetposition -= 3
			cipherText = cipherText + alphabet[alphabetposition]
			plaintextPosition += 1
		output = (cipherText)



	elif contents[0] == 'M':
		a = contents[11:x+1]
		s = a.split(" ")
		dict = {'.-'  : 'a',
		  '-...': 'b',
		  '-.-.': 'c',
		  '-..' : 'd',
		  '.'   : 'e',
		  '..-.': 'f',
		  '--.' : 'g',
		  '....': 'h',
		  '..'  : 'i',
		  '.---': 'j',
		  '-.-' : 'k',
		  '.-..': 'l',
		  '--'  : 'm',
		  '-.'  : 'n',
		  '---' : 'o', 
		  '.--.': 'p',
		  '--.-': 'q',
		  '.-.' : 'r',
		  '...' : 's',
		  '-'   : 't',
		  '..-' : 'u',
		  '...-': 'v',
		  '.--' : 'w',
		  '-..-': 'x',
		  '-.--': 'y',
		  '--..': 'z',
		  '-.--.-': '()',
		  '/': ' '
		     }
		output = ""
		for item in s:
			output =  output + (dict[item])
	output_file = output_folder + "//" + input_file[:-4] +"_m26025tz.txt"
	with open(output_file, "w") as f:
		f.write(output.lower())