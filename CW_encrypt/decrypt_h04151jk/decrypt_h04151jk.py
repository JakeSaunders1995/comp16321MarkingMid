import argparse
import os

morseAlph = {
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
"-----": "0",
".-.-.": ".",
"--..--": ",",
"..--..": "?",
"/": " "}

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("inFolder")
arg_parser.add_argument("outFolder")
arguments = arg_parser.parse_args()

inFolder = arguments.inFolder
outFolder = arguments.outFolder

for root, dirs, files in os.walk(inFolder, topdown=False):
	for name in files:
		fileInName = os.path.join(root, name)

		fileIn = open(fileInName, "r")

		ciphertext = fileIn.readline().strip("\n")

		fileIn.close()

		#split into parts
		ciphertext = ciphertext.split(":")

		alphabet = list("abcdefghijklmnopqrstuvwxyz")

		output = ""

		#determine which encryption technique used

		if ciphertext[0] == "Morse Code":
			body = ciphertext[1].split(" ")
			
			for i in range(len(body)):
				output += morseAlph[body[i]]
				
		elif ciphertext[0] == "Caesar Cipher(+3)":
			body = ciphertext[1]
			
			for i in range(len(body)):
				if body[i] != " ":
					originalPos = alphabet.index(body[i])
					newPos = originalPos - 3
					output += alphabet[newPos].lower()
					
				else:
					output += " "
					
		elif ciphertext[0] == "Hex":
			body = ciphertext[1].split(" ")
			
			for i in range(len(body)):
				ascii = chr(int(body[i], 16))
				output += ascii.lower()
			
		fileOutName = fileInName[8:-4] + "_h04151jk.txt"
		fileOut = open(outFolder + fileOutName, "w")
		fileOut.write(output)
		fileOut.close()
		
		
		
