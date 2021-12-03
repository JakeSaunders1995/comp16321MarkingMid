import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input_path")
parser.add_argument("output_path")
args = parser.parse_args()

for file in os.listdir(args.input_path):
	input_destination = args.input_path + "/" + file
	input_file = open(input_destination)
	input = input_file.read()
	input_file.close()

	algorithm_type = ""
	ciphertext = ""

	before_colon = True
	for i in input:
		if i == ":":
			before_colon = False
		elif before_colon == True:
			algorithm_type += i
		elif before_colon == False:
			ciphertext += i


	plaintext = ""
	if algorithm_type == "Caesar Cipher(+3)":
		alphabet = "abcdefghijklmnopqrstuvwxyzabc"
		for i in range(0,len(ciphertext) - 1):
			ciphertextChar = ciphertext[i]
			alphabetPosition = 3
			if ciphertextChar == " ":
				plaintext += " "
			else:
				while ciphertextChar != alphabet[alphabetPosition]:
					alphabetPosition +=1
				alphabetPosition -= 3
				plaintext += alphabet[alphabetPosition]
	elif algorithm_type == "Morse Code":
		morseCodeDict = {
	    '.-' : 'a',
	    '-...' : 'b',
	    '-.-.' : 'c',
	    '-..' : 'd',
	    '.' : 'e',
	    '..-.' : 'f',
	    '--.' : 'g',
	    '....' : 'h',
	    '..' : 'i',
	    '.---' : 'j',
	    '-.-' : 'k',
	    '.-..' : 'l',
	    '--' : 'm', '-.' : 'n',
	    '---' : 'o', '.--.' : 'p', '--.-' : 'q',
	    '.-.' : 'r', '...' : 's', '-' : 't',
	    '..-' : 'u', '...-' : 'v', '.--' : 'w',
	    '-..-' : 'x', '-.--' : 'y', '--..' : 'z',
	    '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' ',
	    '-.-.-.' : ';', '-.-.--' : '!', '---...' : ':', '-.--.' : '(',
	    '-.--.-' : ')', '.----.' : "'"
		}
		current_value = ""
		cipherlist = ciphertext.split()
		for i in cipherlist:
			plaintext += morseCodeDict[i]
	elif algorithm_type == "Hex":
		current_value = ""
		cipherlist = []
		plainlist = []
		cipherlist = ciphertext.split()
		for i in cipherlist:
			plainlist.append(int(i, 16))
		for i in plainlist:
			plaintext += chr(i)

	output_destination = args.output_path + "/" + file[0:-4] + "_u38012ek.txt"
	output_file = open(output_destination, "w")
	output_file.write(plaintext.lower())
	output_file.close()
