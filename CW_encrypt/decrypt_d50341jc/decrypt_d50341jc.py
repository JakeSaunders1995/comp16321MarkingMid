import os, argparse


def getUserInput():
	parser = argparse.ArgumentParser()
	parser.add_argument('input_folder', type=str)
	parser.add_argument('output_folder', type=str)
	args = parser.parse_args()

	if not os.path.exists(args.output_folder):
	    os.makedirs(args.output_folder)

	return args.input_folder, args.output_folder


def decryptHex(txt):
	out = ""
	for val in txt.split(" "):
		n = int(val, 16)
		out += chr(n)

	return out.lower()


def decryptCaesar(txt):
	out = ""
	alph = "abcdefghijklmnopqrstuvwxyz"
	for char in txt:
		if char in alph:
			i = alph.index(char)
			out += alph[i-3]
		else:
			out += char

	return out.lower()


def decryptMorse(txt):
	out = ""
	morse_dict = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9", "-----": "0", ".-.-.-": ".", "--..--": ",", "..--..": "?", ".----.": "'", "-.-.--": "!", "-..-.": "/", "-.--.": "(", "-.--.-": ")", ".-...": "&", "---...": ":", "-.-.-.": ";", "-...-": "=", ".-.-.": "+", "-....-": "-", "..--.-": "_", ".-..-.": '"', "...-..-": "$", ".--.-.": "@"}
	for word in txt.split(" / "):
		for char in word.split(" "):
			if char in morse_dict:
				out += morse_dict[char]
		out += " "

	return out.strip().lower()


input_folder, output_folder = getUserInput()
filenames = os.listdir(input_folder)
for file in filenames:
	try:
		if not file.endswith(".txt"):
			continue
		with open(input_folder + "/" + file, "r") as f:
			input_li = f.read().split(":")
			alg = input_li[0]
			txt = (":".join(input_li[1:])).lower()

		if alg == "Hex":
			out = decryptHex(txt)
		elif alg == "Caesar Cipher(+3)":
			out = decryptCaesar(txt)
		elif alg == "Morse Code":
			out = decryptMorse(txt)
	except Exception as e:
		out = ""
		print(repr(e))

	output_location = output_folder + "/" + file[:-4] + "_d50341jc.txt"
	with open(output_location, "w") as f:
		f.write(out)
