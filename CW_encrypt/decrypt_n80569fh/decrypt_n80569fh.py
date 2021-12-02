#encryption time

import os
import sys
import re
path = os.getcwd()
try:
	os.chdir(sys.argv[1])
	true_input = sys.argv[1]
	os.chdir(sys.argv[2])
	true_ouput = sys.argv[2]
except:
	arg1 = (sys.argv[1])[2:]
	arg2 = (sys.argv[2])[2:]
	true_input = path + "/" + arg1
	true_ouput = path + "/" + arg2
os.chdir(true_input)
input_folder = os.listdir(true_input)
file_names = []
for file in input_folder:
	if file.endswith(".txt"):
		file_names.append(file)
		with open(file,"r") as f:
			file_content = f.read()
			lowercase_file = file_content.lower()
			print(lowercase_file)
			decrypt = lowercase_file.split(":")
			ciphertext = decrypt[1].strip()
			if "caesar cipher(+3)" in decrypt[0]:
				plaintext = ""
				letters = "xyzabcdefghijklmnopqrstuvwxyzabc"
				ciphertextPos = 0
				while (ciphertextPos < len(ciphertext)):
					ciphertextChar = ciphertext[ciphertextPos]
					alphabetPos = 3
					if ciphertextChar == " ":
						plaintext += " "
					else:
						while ciphertextChar != letters[alphabetPos]:
							alphabetPos += 1
						alphabetPos -= 3
						plaintext += letters[alphabetPos]
					ciphertextPos += 1
				print (plaintext)

			elif "hex" in decrypt[0]:
				ciphertext = ciphertext.strip(" ")
				hexbytes = bytes.fromhex(ciphertext)
				ascii_str = hexbytes.decode("ASCII")
				plaintext = ascii_str.lower()
				print(plaintext)

			elif "morse code" in decrypt[0]:
				mcplaintext = ""
				morselist = ciphertext.split(" ")
				morsePos = 0
				while morsePos < len(morselist):
					morseletter = morselist[morsePos]
					if morseletter == ".-": mcplaintext += "a"
					if morseletter == "-...": mcplaintext += "b"
					if morseletter == "-.-.": mcplaintext += "c"
					if morseletter == "-..": mcplaintext += "d"
					if morseletter == ".": mcplaintext += "e"
					if morseletter == "..-.": mcplaintext += "f"
					if morseletter == "--.": mcplaintext += "g"
					if morseletter == "....": mcplaintext += "h"
					if morseletter == "..": mcplaintext += "i"
					if morseletter == ".---": mcplaintext += "j" 
					if morseletter == "-.-": mcplaintext += "k" 
					if morseletter == ".-..": mcplaintext += "l"
					if morseletter == "--": mcplaintext += "m"
					if morseletter == "-.": mcplaintext += "n"
					if morseletter == "---": mcplaintext += "o"
					if morseletter == ".--.": mcplaintext += "p"
					if morseletter == "--.-": mcplaintext += "q"
					if morseletter == ".-.": mcplaintext += "r"
					if morseletter == "...": mcplaintext += "s"
					if morseletter == "-": mcplaintext += "t"
					if morseletter == "..-": mcplaintext += "u"
					if morseletter == "...-": mcplaintext += "v"
					if morseletter == ".--": mcplaintext += "w"
					if morseletter == "-..-": mcplaintext += "x"
					if morseletter == "-.--": mcplaintext += "y"
					if morseletter == "--..": mcplaintext += "z"
					if morseletter == "-----": mcplaintext += "0"
					if morseletter == ".----": mcplaintext += "1"
					if morseletter == "..---": mcplaintext += "2"
					if morseletter == "...--": mcplaintext += "3"
					if morseletter == "....-": mcplaintext += "4"
					if morseletter == ".....": mcplaintext += "5"
					if morseletter == "-....": mcplaintext += "6"
					if morseletter == "--...": mcplaintext += "7"
					if morseletter == "---..": mcplaintext += "8"
					if morseletter == "----.": mcplaintext += "9"
					if morseletter == "/": mcplaintext += " "
					morsePos += 1
				plaintext = mcplaintext
				print(plaintext)
		os.chdir(true_ouput)
		output_file = file[:-4] + "_n80569fh.txt"
		print (output_file)
		with open(output_file,"w") as o:
			o.write(plaintext)
		print(plaintext)
		os.chdir(true_input)
