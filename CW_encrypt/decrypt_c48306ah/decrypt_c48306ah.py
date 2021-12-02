import os
import argparse


def get_cipher(text):
	return text.split(":")[0]


def decode_hex(text):
	text = text.split(" ")

	plain = ""

	for letter in text:
		plain += chr(int(letter, 16))

	return plain


def decode_morse(text):
	morse_map = {
		".-": "A",    "-...": "B",  "-.-.": "C",
	    "-..": "D",   ".": "E",     "..-.": "F",
	    "--.": "G",   "....": "H",  "..": "I",  
	    ".---": "J",  "-.-": "K",   ".-..": "L",
	    "--": "M",    "-.": "N",    "---": "O", 
	    ".--.": "P",  "--.-": "Q",  ".-.": "R",
	    "...": "S",   "-": "T",     "..-": "U", 
	    "...-": "V",  ".--": "W",   "-..-": "X",
	    "-.--": "Y",  "--..": "Z",  "-----": "0", 
	    ".----": "1", "..---": "2", "...--": "3",
	    "....-": "4", ".....": "5", "-....": "6", 
	    "--...": "7", "---..": "8", "----.": "9",
		".-.-.-": ".", "--..--": ",", "..--..": "?",
		"-.-.-.": ";", "---...": ":", "-....-": "-",
		"-..-.": "/", ".----.": "'", ".-..-.": '"'
    }

	plain = ""
	text = text.split("/")

	for i in range(len(text)):
		text[i] = text[i].strip().split(" ")

	for word in text:
		for letter in word:
			plain += morse_map[letter]

		plain += " "

	return plain.lower()


def decode_caeser(text, offset):
	text = text.split(" ")

	for i in range(len(text)):
		text[i] = list(text[i])

	for i in range(len(text)):
		for pos in range(len(text[i])):
			ascii_pos = ord(text[i][pos]) + offset

			if ascii_pos < 97:
				difference = 97 - ascii_pos
				ascii_pos = 123 - difference

			elif ascii_pos > 122:
				difference = difference - 122
				ascii_pos = 96 + difference

			text[i][pos] = chr(ascii_pos)

		text[i] = "".join(text[i])

	return " ".join(text)


def main():
	parser = argparse.ArgumentParser()

	parser.add_argument("input")
	parser.add_argument("output")

	args = parser.parse_args()

	for f in os.listdir(args.input):
		file = open(os.path.join(args.input, f))
		text =  file.read().replace("\n", "").lower()
		file.close()

		cipher = get_cipher(text)

		if "hex" == cipher.lower():
			plaintext = decode_hex(text.split(":")[1])
		elif "morse code" == cipher.lower():
			plaintext = decode_morse(text.split(":")[1])
		else:
			plaintext = decode_caeser(text.split(":")[1], -int(cipher[14:16]))

		file = open(os.path.join(args.output, f"{os.path.splitext(f)[0]}_c48306ah.txt"), "w")
		file.write(plaintext.lower())
		file.close()


main()