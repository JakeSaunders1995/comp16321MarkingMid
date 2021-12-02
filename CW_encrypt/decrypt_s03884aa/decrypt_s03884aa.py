import os
import sys
inputpath = sys.argv[1]
outputpath = sys.argv[2]
ipathfile = open(inputpath,"r")
opathfile = open(outputpath, "w")
inputfile = (ipathfile.read())


for i in range (len(inputfile)):
	if inputfile[i] == ":":
		storei = i
cipherText=inputfile[storei+1:]
plaintext = ''
if inputfile[0]== "C":
	cipherTextPosition = 0
	while(cipherTextPosition < len(cipherText)):
		cipherTextChar = cipherText[cipherTextPosition]
		ASCIIValue= ord(cipherTextChar)
		ASCIIValue= ASCIIValue - 3
		CharValue = chr(ASCIIValue)
		plaintext = plaintext +str(CharValue)
		cipherTextPosition = cipherTextPosition +1 
	opathfile.write(plaintext)

if inputfile[0]=="M":
	morse_dict = { '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '....':'h', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '}
	cipherText = cipherText.split()
	for element in range (0, len(cipherText)):
		opathfile.write(morse_dict.get(cipherText[element]))

if inputfile[0]=='H': 
	text= bytes.fromhex(cipherText)
	ascii_string = text.decode("ASCII")
	opathfile.write(ascii_string)


