import sys
import os


def morse_func(cipher, plain):
	morse_code = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",
				".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9", "-----": "0",
				".-.-.-": ".", "--..--": ",", "..--..": "?", "-.-.--": "!", "---...": ":", ".----.": "'", ".-..-.": "\"", "-....-": "-", "-.--.": "(", "-.--.-": ")", ".-...": "&", ".--.-.": "@", "-...-": "=", "------..-.-----": "%", ".-.-.": "+", "-..-.": "/"}
	x = 0
	letter = ""
	while x < len(cipher):
		if cipher[x] == "/":
			plain += " "
			x += 2
		elif cipher[x] == " ":
			plain += morse_code[letter]
			letter = ""
			x += 1
		elif x == len(cipher)-1:
			letter += cipher[x]
			plain += morse_code[letter]
			x += 1
		else:
			letter += cipher[x]
			x += 1
	return plain	

def caesar_func(cipher, plain):
	cipher = cipher.lower()
	for x in cipher:
		if ord(x) < 97 or ord(x) >122:
			plain += x
		else:
			letter = chr(97 + ((ord(x)-100) % 26)) # -97 - 3
			plain += letter
	return plain

def hex_func(cipher, plain):
	cipher = cipher.lower()
	hex_code = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
	for x in range(0, len(cipher), 3):
		letter = cipher[x:x+2]
		if letter[0] in hex_code:
			denary = hex_code[letter[0]]*16
		else:
			denary = int(letter[0])*16
		if letter[1] in hex_code:
			denary += hex_code[letter[1]]
		else:
			denary += int(letter[1])
		plain += chr(denary)
	return plain


in_directory = sys.argv[1]
files = os.listdir(in_directory)
for file in files:
	input_path = os.path.join(in_directory, file)
	input_file = open(input_path)
	string = input_file.read()
	input_file.close()

	mode = string[0].upper() # M - morse, C - caesar, H - hex
	i = string.index(":")
	ciphertext = string[i+1::]
	plaintext = ""

	if mode == "M":
		plaintext = morse_func(ciphertext, plaintext)
	elif mode == "C":
		plaintext = caesar_func(ciphertext, plaintext)
	else:
		plaintext = hex_func(ciphertext, plaintext)

	plaintext = plaintext.lower()

	out_directory = sys.argv[2]
	index = file.find(".txt")
	output_path = os.path.join(out_directory, file[:index] + "_b63095jv" + file[index:])
	output_file = open(output_path, "w")
	output_file.write(plaintext)
	output_file.close()
