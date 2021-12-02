import sys
import os
inFolder = sys.argv[1]
outFolder = sys.argv[2]

os.mkdir(outFolder)

letterList = list(map(chr, range(97, 123)))

#dictionary for morse 
morseDict = { '.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e',
              '..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j',
              '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o',
              '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t',
              '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y', 
              '--..':'z'}

for inFile in os.listdir(inFolder):

	plaintext = ""

	with open(inFolder + "/" + inFile) as file:	#opens the input file
		inFileData = file.read()

	#determines cypher type
	splitFileData = inFileData.split(":")
	cypherText = splitFileData[1]

	#if hex
	if splitFileData[0][0] == "H":
		for letter in cypherText.split():
				plaintext += bytearray.fromhex(letter).decode()

	#if caesar
	elif splitFileData[0][0] == "C":
		for letter in list(cypherText):
			if letter == " " or letter == "\n":
				plaintext += letter
			else:
				indexNo = letterList.index(letter)
				if indexNo < 3:
					if letter == 'c':
						letter = 'z'
					elif letter == 'b':
						letter = 'y'
					elif letter == 'a':
						letter = 'x'
				else:
					indexNo -= 3
					letter = letterList[indexNo]
				plaintext += letter
			
	#if morse
	elif splitFileData[0][0] == "M":
		for letter in cypherText.split():
			if letter == "/":
				plaintext += " "
			else:
				plaintext += morseDict[letter]

	outputLocation = outFolder + "/" + inFile + "_x57595ts.txt"

	with open(outputLocation, "w") as file:	#writes to file
		file.write(plaintext)