import argparse, os, re
	
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()

f_input = os.listdir(args.input)

hex_dict = {
	"20": " ", "21": "!", "22": '"', "27": "'", "28": "(", "29": ")", "2c": ",", "2d": "-", "2e": ".", "2f": "/",
	"30": "0", "31": "1", "32": "2", "33": "3", "34": "4", "35": "5", "36": "6", "37": "7", "38": "8", "39": "9", "3a": ":", "3b": ";", "3f": "?",
	"41": "a", "42": "b", "43": "c", "44": "d", "45": "e", "46": "f", "47": "g", "48": "h", "49": "i", "4a": "j", "4b": "k", "4c": "l", "4d": "m", "4e": "n", "4f": "o",
	"50": "p", "51": "q", "52": "r", "53": "s", "54": "t", "55": "u", "56": "v", "57": "w", "58": "x", "59": "y", "5a": "z", "5b": "[", "5d": "]",
	"61": "a", "62": "b", "63": "c", "64": "d", "65": "e", "66": "f", "67": "g", "68": "h", "69": "i", "6a": "j", "6b": "k", "6c": "l", "6d": "m", "6e": "n", "6f": "o",
	"70": "p", "71": "q", "72": "r", "73": "s", "74": "t", "75": "u", "76": "v", "77": "w", "78": "x", "79": "y", "7a": "z", "7b": "{", "7d": "}"
}

morse_dict = {
	".-" : "a", "-..." : "b", "-.-." : "c", "-.." : "d", "." : "e", "..-." : "f", "--." : "g", "...." : "h", ".." : "i", ".---" : "j", "-.-" : "k", ".-.." : "l", "--" : "m", "-." : "n", "---" : "o", ".--." : "p", "--.-" : "q", ".-." : "r", "..." : "s", "-" : "t", "..-" : "u", "...-" : "v", ".--" : "w", "-..-" : "x", "-.--" : "y", "--.." : "z",
	"-----" : "0", ".----" : "1", "..---" : "2", "...--" : "3", "....-" : "4", "....." : "5", "-...." : "6", "--..." : "7", "---.." : "8", "----." : "9",
	".-.-.-" : ".", "--..--" : ",", ".----." : "'", ".-..-." : '"', "-....-" : "-", "..--.." : "?", "-.-.--" : "!", "-..-." : "/", "---..." : ":", "-.--." : "(", "-.--.-" : ")", "/" : " ", " " : ""
}

caesar_dict = {
	"a" : "x",
	"b" : "y",
	"c" : "z",
	"d" : "a",
	"e" : "b",
	"f" : "c",
	"g" : "d",
	"h" : "e",
	"i" : "f",
	"j" : "g",
	"k" : "h",
	"l" : "i",
	"m" : "j",
	"n" : "k",
	"o" : "l",
	"p" : "m",
	"q" : "n",
	"r" : "o",
	"s" : "p",
	"t" : "q",
	"u" : "r",
	"v" : "s",
	"w" : "t",
	"x" : "u",
	"y" : "v",
	"z" : "w",
	" " : " "
}

def hexadecimal(code):

	code = code[4:]

	decrypt = ""

	for i in range(len(code)):

		if code == "": break

		decrypt = decrypt + hex_dict.get(code[0:2])

		code = code[3:]

	return decrypt

def caesarCipher(code):

	decrypt = ""

	for i in range(18, len(code)):

		decrypt = decrypt + caesar_dict.get(code[i])

	return decrypt

def morseCode(code):

	code = code[11:]
	decrypt = ""
	sub_code = ""

	for i in range(len(code)):

		if code[i] == " ":

			decrypt = decrypt + morse_dict.get(sub_code)
			sub_code = ""

		else:
			sub_code = sub_code + code[i]
		
	decrypt = decrypt + morse_dict.get(sub_code)

	return decrypt

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

for i in range(len(f_input)):
	
	with open (args.input + "/" + f_input[i], "r") as file:

		cipher_text = file.readline()

	file.close()

	if "Hex:" in cipher_text:

		og_message = hexadecimal(cipher_text)

	elif "Caesar Cipher(+3):" in cipher_text:

		og_message = caesarCipher(cipher_text)

	elif "Morse Code:" in cipher_text:

		og_message = morseCode(cipher_text)

	else:

		print("You've broken it!")

	f_output = f_input[i][:-4] + "_p23525lg.txt"

	with open (args.output + "/" + f_output, "w") as file:

		file.write(og_message)

	file.close()
