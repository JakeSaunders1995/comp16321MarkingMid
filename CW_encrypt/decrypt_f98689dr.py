import argparse
import os

#morse code dictionary
morseDict = { '.-':'a', '-...':'b', 
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

#read terminal
cmdline = argparse.ArgumentParser()
cmdline.add_argument("input")
cmdline.add_argument("output")
inp = cmdline.parse_args()
out = cmdline.parse_args()
inputFolderName = str(inp.input)
outputFolderName = str(out.output)
ls = os.listdir(inputFolderName)
loop = 0
for i in ls:
	#read file
	file = inputFolderName+"/"+ls[loop]
	inputFile = open(file,"r")
	inputText = inputFile.read()
	split = inputText.split(":")
	algorithm = split[0]
	cipher = split[1]

	#main
	if algorithm[0] == "H":
		hexvals = cipher.split(" ")
		decrypt = ""
		for i in hexvals:
			binary = bytes.fromhex(i)
			decrypt += binary.decode("ASCII")

	elif algorithm[0] =="C":
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		decrypt = ""
		for letter in cipher:
			if letter == " ":
				decrypt += " "
			else:
				count = 0
				for i in alphabet:
					if i == letter:
						decrypt += alphabet[count-3]
						break
					else:
						count += 1
	elif algorithm[0] == "M":
			morse = cipher.split(" ")
			decrypt = ""
			for code in morse:
				if code == "/":
					decrypt += " "
				else:
					decrypt += morseDict[code]

	#output deciphered text
	temp = ls[loop]
	outputFile = open(outputFolderName+"/"+temp[:-4]+"_f98689dr.txt","w")
	outputFile.write(decrypt)
	outputFile.close()
	loop += 1