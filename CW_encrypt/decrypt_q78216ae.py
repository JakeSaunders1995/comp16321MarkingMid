import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('inputfile')
parser.add_argument('outputfile')
args = parser.parse_args()

filepath = args.inputfile
outfilepath = args.outputfile

morseCodeDict = {'.-':'a', '-...':'b',
'-.-.':'c', '-..':'d', '.':'e',
'..-.':'f', '--.':'g', '....':'h',
'..':'i', '.---':'j', '-.-':'k',
'.-..':'l', '--':'m', '-.':'n',
'---':'o', '.--.':'p', '--.-':'q',
'.-.':'r', '...':'s', '-':'t',
'..-':'u', '...-':'v', '.--':'w',
'-..-':'x', '-.--':'y', '--..':'z',
'.----':'1', '..---':'2', '...--':'3',
'....-':'4', '.....':'5', '-....':'6',
'--...':'7', '---..':'8', '----.':'9',
'-----':'0', '--..--':', ', '.-.-.-':'.',
'..--..':'?', '-..-.':'/', '-....-':'-',
'-.--.':'(', '-.--.-':')'}

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for file in os.listdir(filepath):
	with open(filepath + "/" + file) as f:
		inp = f.readlines()

	sepInp = inp[0].split(":",1)
	algorithm = sepInp[0]
	cipherText = sepInp[1]
	plaintext = ""

	if algorithm[0].lower() == "m":
		cipherText = cipherText.split()
		for char in cipherText:
			if char == "/":
				plaintext += " "
			else:
				plaintext += morseCodeDict[char]
	elif algorithm[0].lower() == "c":
		for char in cipherText:
			if char == " ":
				plaintext += " "
			elif char == "\n":
				plaintext += "\n"
			else:
				newLetter = letters[letters.index(char) - 3]
				plaintext = plaintext + newLetter
	else:
		cipherText = cipherText.split()
		for char in cipherText:
			newLetter = int(char, 16)
			plaintext += chr(newLetter)
	print(plaintext)
	newfilepath = outfilepath + "/" + file[:-4] + "_q78216ae.txt"
	file = open(newfilepath,'w')
	file.write(plaintext)
	file.close()
