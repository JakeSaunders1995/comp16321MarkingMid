import argparse
import os
input_files = []
output_files = []
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
object = os.scandir(path = args.input)
h = 0
for h in object :
	if h.is_file():
		input_files.append(h.name)
alphabet = "abcdefghijklmnopqrstuvwxyz"
morse_code = [["a", ".-"], ["b", "-..."], ["c", "-.-."], ["d", "-.."], ["e", "."], ["f", "..-."], ["g", "--."], ["h", "...."], ["i", ".."], ["j", ".---"], ["k", "-.-"], ["l", ".-.."], ["m", "--"], ["n", "-."], ["o", "---"], ["p", ".--."], ["q", "--.-"], ["r", ".-."], ["s", "..."], ["t", "-"], ["u", "..-"], ["v", "...-"], ["w", ".--"], ["x", "-..-"], ["y", "-.--"], ["z", "--.."], ["0", "-----"], ["1", ".----"], ["2", "..---"], ["3", "...--"], ["4", "....-"], ["5", "....."], ["6", "-...."], ["7", "--..."], ["8", "---.."], ["9", "----."], [" ", "/"]]
username = "p06411ua"
k = 0
for k in range (0, len(input_files)):
	text = ""
	cipher_text_file = open (args.input + input_files[k], "r")
	cipher_text = cipher_text_file.read()
	i = 0
	algorithm = ""
	while cipher_text[i] != ":":
		algorithm += cipher_text[i]
		i += 1
	j = 0
	cipher = ""
	for j in range (i+1, len(cipher_text)):
		cipher += cipher_text[j]
	if algorithm == "Morse Code":
		i = 0
		temp = ""
		for i in range (0, len(cipher)):
			if cipher[i] == "." or cipher[i] == "-" or cipher[i] == "/":
				temp += cipher[i]
			else:
				j = 0
				for j in range (0, 37):
					if temp == morse_code[j][1]:
						text += morse_code[j][0]
						temp = ""
		j = 0
		for j in range (0, 37):
			if temp == morse_code[j][1]:
				text += morse_code[j][0]
				temp = ""
	elif algorithm == "Hex":
		text = bytearray.fromhex(cipher).decode().lower()
	elif algorithm == "Caesar Cipher(+3)":
		i = 0
		for i in range (0, len(cipher)-1):
			j = 0
			for j in range (0, 25):
				if cipher[i] == alphabet[j]:
					if (j-3) >= 0:
						text += alphabet[j-3]
					else:
						text += alphabet[26+(j-3)]
			if len(text) < (i+1):
				text += cipher[i]
		j = 0
		for j in range (0, 25):
			if cipher[i+1] == alphabet[j]:
				if (j-3) >= 0:
					text += alphabet[j-3]
				else:
					text += alphabet[26+(j-3)]
		if len(text) < (i+1):
			text += cipher[i]
	else:
		print("Algorithm couldn't be found")
	print (text)
	l = 0
	temp = ""
	while input_files[k][l] != ".":
		temp += input_files[k][l]
		l += 1
	english_text_file = open (args.output + temp + "_" + username +".txt", "w")
	english_text_file.write(text)
	
	
	
	
	
