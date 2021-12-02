import argparse
import os
import re

parser = argparse.ArgumentParser()

parser.add_argument("dir", nargs = "+")
args = parser.parse_args()

listOfFile = os.listdir(args.dir[0])


for x in range (0,len(listOfFile)):
	inputFile = args.dir[0] + "/" + listOfFile[x]
	plaintext = ''
	Ciphertext = open(inputFile,"r")
	algorithm = Ciphertext.read(1)
	Ciphertext = Ciphertext.read()

	if algorithm == "H":
		Ciphertext = Ciphertext[3:len(Ciphertext)]
		Ciphertext = Ciphertext.replace(" ","")
		Ciphertext = bytearray.fromhex(Ciphertext)
		plaintext = Ciphertext.decode()
		plaintext = plaintext.lower()

	if algorithm == "C":
		Ciphertext = Ciphertext[17:len(Ciphertext)]

		alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
		cipherTextPosition = 0

		for cipherTextChar in Ciphertext:
		    for alphabetPosition in range(3,len(alphabet)):
		    	if cipherTextChar == alphabet[alphabetPosition]:
		    		plaintext += alphabet[alphabetPosition-3]
		    		break
		    	elif cipherTextChar == " ":
		    		plaintext = plaintext + " "
		    		plaintext = re.sub(" +"," ",plaintext)



	if algorithm == "M":
		Ciphertext = Ciphertext[10:len(Ciphertext)]
		dic = {'..-.': 'f', '-..-': 'x',
	     '.--.': 'p', '-': 't', '..---': '2',
	     '....-': '4', '-----': '0', '--...': '7',
	     '...-': 'v', '-.-.': 'c', '.': 'e', '.---': 'j',
	     '---': 'o', '-.-': 'k', '----.': '9', '..': 'i',
	     '.-..': 'l', '.....': '5', '...--': '3', '-.--': 'y',
	     '-....': '6', '.--': 'w', '....': 'h', '-.': 'n', '.-.': 'r',
	     '-...': 'b', '---..': '8', '--..': 'z', '-..': 'd', '--.-': 'q',
	     '--.': 'g', '--': 'm', '..-': 'u', '.-': 'a', '...': 's', '.----': '1', '/': " ",
	     '._._._': '.', '__..__': ',', '..__..': "?", '_._._.': ";"
	     , '___...': ":", '_...._': "-", '_.._.': "/",
	     '.----.': "'", '._.._.': '"', '_.__._': ")", '_.__.': "(", '-.-.--': "!"}

		code = ""
		Ciphertext = Ciphertext + " "

		for i in Ciphertext:
			if i == " ":
				plaintext = plaintext + dic[code]
				code = ""
			else:
				code = code + i


	c = args.dir[1] + "/" + listOfFile[x]
	d = c.replace(".txt", "_p17128xt.txt")
	f = open(d,'w')
	f.write(plaintext)
	f.close