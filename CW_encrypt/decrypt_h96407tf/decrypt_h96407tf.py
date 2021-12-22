import os
import argparse

arg_parser = argparse.ArgumentParser(description="Decryption program")
arg_parser.add_argument('input_folder')
arg_parser.add_argument('output_folder')
args = arg_parser.parse_args()

if not os.path.exists(args.output_folder):
	os.makedirs(args.output_folder)

morse_code = {
	".-":  'A',
	"-...":'B',
	"-.-.":'C',
	"-..": 'D',
	".":   'E',
	"..-.":'F',
	"--.": 'G',
	"....":'H',
	"..":  'I',
	".---":'J',
	"-.-": 'K',
	".-..":'L',
	"--":  'M',
	"-.":  'N',
	"---": 'O',
	".--.":'P',
	"--.-":'Q',
	".-.": 'R',
	"...": 'S',
	"-":   'T',
	"..-": 'U',
	"...-":'V',
	".--": 'W',
	"-..-":'X',
	"-.--":'Y',
	"--..":'Z',
	".----": "1",
	"..---": "2",
	"...--": "3",
	"....-": "4",
	".....": "5",
	"-....": "6",
	"--...": "7",
	"---..": "8",
	"----.": "9",
	"-----": "0",
	"..--..": "?",
	"-.-.--": "!",
	".-.-.-": ".",
	"--..--": ",",
	"-.-.-.": ";",
	"---...": ":",
	".-.-.": "+",
	"-....-": "-",
	"-..-.": "/",
	"-...-": "=",
	".----.": "`",
	".-..-.": "\"",
	"-.--.": "(",
	"-.--.-": ")",
	".-...": "&",
	"..--.-": "_"
}


for file_name in os.listdir(args.input_folder):
	with open(args.input_folder + "/" + file_name, "r") as file:
		contents = file.read().split(':')
		algo = contents[0]
		ciphertext = contents[1]

	decrypted_text = ""

	if algo == "Hex":
		bytes = bytes.fromhex(ciphertext)
		decrypted_text = bytes.decode("ASCII")
	elif algo == "Caesar Cipher(+3)":
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		for char in ciphertext:
			if char not in alphabet: decrypted_text += char
			else: decrypted_text += alphabet[alphabet.find(char)-3]
	elif algo == "Morse Code":
		words = ciphertext.split('/')
		for word in words:
			letters = word.split(' ')
			for letter in letters:
				if letter in morse_code.keys():
					decrypted_text += morse_code[letter]
			decrypted_text += " "
		decrypted_text = decrypted_text[:len(decrypted_text)-1]

	output_file = file_name.split('.')[0] + "_h96407tf.txt"
	with open(args.output_folder + "/" + output_file, "w") as file:
		file.write(decrypted_text.lower())