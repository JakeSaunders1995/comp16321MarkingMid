# Decryption program

import argparse
import os
import re


# Parsing directories

parser = argparse.ArgumentParser()
parser.add_argument('inputdir')
parser.add_argument('outputdir')
args = parser.parse_args()


# Alphabet for ceaser cipher

alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"


# Reading input files from input directory

input_directory = args.inputdir
for filename in os.listdir(input_directory):
	if filename.endswith(".txt"):
		f = os.path.join(input_directory, filename)
		readfile = open(f, "r")
		encrypted_code = readfile.readline()
		
		

		# Decryption process


		if "Hex" in encrypted_code:
			# print("This is hex code")
			hex_list = []
			string_list = []			
			# print(encrypted_code)
			space = ""
			encrypted_code_position = 4 
			# while encrypted_code_position < len(encrypted_code):
			n = 3

			for i in range (encrypted_code_position, len(encrypted_code), n):	
				# print(encrypted_code[i:i+n])
				hex_list.append(encrypted_code[i:i+n])
				encrypted_code_position += n
			# print(hex_list)
			

			for hex_piece in hex_list:
				bytes_piece = bytes.fromhex(hex_piece)
				ascii_piece = bytes_piece.decode("ASCII")
				# print(ascii_piece)
				space += ascii_piece
				string_list.append(ascii_piece)
			print(space)


		elif "Caesar Cipher(+3)" in encrypted_code:
			# print("This is ceaser Cipher code with shift (+3)")
			
			plaintext = ""
			encrypted_code_position = 18
			while encrypted_code_position < len(encrypted_code):
				encrypted_code_char = encrypted_code[encrypted_code_position]
				# print(encrypted_code_char)
				alphabet_position = 3
				if encrypted_code_char in alphabet:
					while encrypted_code_char != alphabet[alphabet_position]:
						alphabet_position = alphabet_position + 1
					# print(alphabet[alphabet_position])
					alphabet_position = alphabet_position - 3
					plaintext = plaintext + alphabet[alphabet_position]
					encrypted_code_position = encrypted_code_position + 1				
				else:
					plaintext = plaintext + encrypted_code_char
					encrypted_code_position = encrypted_code_position + 1

			print(plaintext)


		elif "Morse Code" in encrypted_code:
			# print("This is morse code")
			encrypted_code_position = 11
			morse_str_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '?', '!', ',', ':', ';', '-', '(', ')', '[', ']', "'", '"', '...', '{', '}']
			morse_code_alphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.-.-.-', '..--..', '-.-.--', '--..--', '---...', '-.-.-.', '-....-', '-.--.', '-.--.-', '-.--.', '-.--.-', '.---.', '.-..-.'] #need to add "...", "{}"

			morseText = encrypted_code[encrypted_code_position:len(encrypted_code)]
			# print(morseText)
			morseText2 = re.split('/', morseText)
			# print(morseText2)
			finished = ''
			for word in morseText2:
				# print(word)
				for i in range(0,len(word)):
					letter = re.split(' ', word)
				word2 = ''
				for char in letter:
					# print(char)
					for i in range(0,39):			#need to change 39 to 42 when found ... {  }

						if char == morse_code_alphabet[i]:
							word2 += morse_str_alphabet[i]
				finished += word2 + ' '
			print(finished)



			
	# Writing output files to an output directory

	output_directory = args.outputdir
	writefile = open(output_directory + "/" + filename[:-3] + "_j80560hh.txt", "w")
	if "Hex" in encrypted_code:
		writefile.write(str(space))
	elif "Caesar Cipher(+3)" in encrypted_code:
		writefile.write(str(plaintext))
	elif "Morse Code" in encrypted_code:
		writefile.write(str(finished))




	

			# print (len(morse_code_alphabet))
			# print(len(morse_str_alphabet))













			