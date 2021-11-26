import os, sys


def decrypt(string):
	method = string[0]
	encrypted = string[1].split()
	decrypted = ""

	if method[0].upper() == "H":
		for encrypted_char in encrypted:
			decrypted += chr(int(encrypted_char, 16)).lower()
	elif method[0].upper() == "C":
		alphabets = "abcdefghijklmnopqrstuvwxyz"
		for encrypted_word in encrypted:
			for encrypted_char in encrypted_word.lower():
				index = alphabets.find(encrypted_char) - 3
				decrypted += alphabets[index]
			decrypted += " "
		decrypted = decrypted.rstrip()
	elif method[0].upper() == "M":
		char_from_morse = {
			"/": " ",
			".-": "a",
			"-...": "b",
			"-.-.": "c",
			"-..": "d",
			".": "e",
			"..-.": "f",
			"--.": "g",
			"....": "h",
			"..": "i",
			".---": "j",
			"-.-": "k",
			".-..": "l",
			"--": "m",
			"-.": "n",
			"---": "o",
			".--.": "p",
			"--.-": "q",
			".-.": "r",
			"...": "s",
			"-": "t",
			"..-": "u",
			"...-": "v",
			".--": "w",
			"-..-": "x",
			"-.--": "y",
			"--..": "z",
			".----": "1",
			"..---": "2",
			"...--": "3",
			"....-": "4",
			".....": "5",
			"-....": "6",
			"--...": "7",
			"---..": "8",
			"----.": "9",
			"-----": "0"
		}
		for encrypted_char in encrypted:
			decrypted += char_from_morse[encrypted_char]
	else:
		decrypted = "undefined encryption method"

	return decrypted


for filename in os.listdir(sys.argv[1]):
	if filename.endswith(".txt"):
		file = open(f"{sys.argv[1]}/{filename}")
		string = file.readline().split(":")
		file.close()

		output = decrypt(string)
		filename = filename[:-4]
		file = open(f"{sys.argv[2]}/{filename}_n96249ty.txt", "w")
		file.write(output)
		file.close()

