import os
import sys

i = sys.argv[1]
o = sys.argv[2]

ifile = open(i, "r")
ofile = open(o, "w")
inputfile = (ifile.read())


jIndex = 0
for j in range (len(inputfile)):
	if inputfile[j] == ":":
		jIndex = j
ciphertext= inputfile[jIndex + 1:]

#Caesarcipher

plainText = ""
if inputfile[0] == "C":
	ciphertextPosition = 0
	while (ciphertextPosition < len(ciphertext)):
		ciphertextChar = ciphertext[ciphertextPosition]
		if ciphertextChar == ' ':
	  		plainText = plainText + " "
	  		ciphertextPosition = ciphertextPosition + 1
	  		continue
		ASCIIValue = ord(ciphertextChar)
		ASCIIValue = ASCIIValue - 3
		plainText = plainText + chr(ASCIIValue)
		ciphertextPosition = ciphertextPosition + 1
	ofile.write(plainText)


#Morsecipher

character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
morseCode = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']



if inputfile[0] == "M":
	ciphertext += " "
	letter = ""
	text = ""
	for c in range (len(ciphertext)):
		if ciphertext[c] == " ":
			for a in range(len(morseCode)):
				if letter == morseCode[a]:
					text = text + character[a]
					break
			letter = ""
			continue
		if ciphertext[c] == "/":
			text = text + " "
		letter = letter + ciphertext[c]
	ofile.write(text)



#Hexacipher

if inputfile[0] == "H":
	string = bytes.fromhex(ciphertext)
	string = string.decode("utf-8")
	ofile.write(string)

