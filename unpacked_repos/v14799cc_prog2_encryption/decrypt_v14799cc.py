import re
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("echo")
parser.add_argument("output")
args = parser.parse_args()
directory_in = args.echo
directory_out = args.output


for file in os.listdir(directory_in):
	x = os.path.join(directory_in, file)
	f = open(x)
	lines = f.read()
	crypto = re.split(':', lines)
	decoded_message = ""
	if crypto[0] == "Hex":
		string = crypto[1]
		temp = bytes.fromhex(string)
		text = temp.decode("ASCII")
		decoded_message = text.lower()


	elif crypto[0] == "Caesar Cipher(+3)":
		string = crypto[1]
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		for letter in string:
			if letter in alphabet:
				index = (alphabet.find(letter) - 3) % len(alphabet)
				decoded_message += alphabet[index]
			else:
				decoded_message += letter
			
				

	elif crypto[0] == "Morse Code":
		string = crypto[1]
		mor_dict = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", 
		"..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k",
		".-..":"l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q",
		".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w",
		"-..-": "x", "-.--": "y", "--..": "z", " ": "\n", "/": " "}
		morse_string = re.split(' |\n', string)
		for i in range(len(morse_string)):
			if morse_string[i] in mor_dict:
				decoded_message += mor_dict[morse_string[i]]
		

	file_name = re.split('.txt', file)
	file_out_name = file_name[0]
	file_out_path = directory_out + "/" + file_out_name + "_" + "v14799cc.txt"
	g = open(file_out_path, "w")
	g.write(decoded_message)


f.close()
g.close()








