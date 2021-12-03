def decrypt(txtFile):
	with open(txtFile, 'r') as cipherFile:
		encrypted = cipherFile.read()
		cipherFile.close()

	#split input file into encryption method and ciphertext
	i=0
	method = ''
	cipher = ''

	while encrypted[i] != ':':
		method = method + encrypted[i]
		i += 1

	#ensure ':' is not included in cipher
	i += 1

	while i < len(encrypted):
		cipher = cipher + encrypted[i]
		i += 1

	plaintext = ''

	if method == 'Hex':
		#split encrypted message into hex digtis
		i = 0
		hexNums = []
		while i < len(cipher):
			current = cipher[i] + cipher[i+1]
			hexNums.append(current)
			i += 3
		#convert hex to denary
		hexDigits = '0123456789abcdef'
		for hexNum in hexNums:
			denary = (hexDigits.index(hexNum[0]) * 16) + hexDigits.index(hexNum[1])
			#convert denary to ascii character concatonate to plaintext
			plaintext = plaintext + chr(denary)

	elif method == 'Caesar Cipher(+3)':
		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		#shift each character back three in the alphabet
		for i in cipher:
			if i in alphabet:
				idx = alphabet.index(i)
				plaintext = plaintext + alphabet[idx-3]
			else:
				plaintext = plaintext + i

	elif method == 'Morse Code':
		morseDict = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h',
	                '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p',
	                '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
	                '-.--': 'y', '--..': 'z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
	                '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '--..--': ',', '.-.-.-':'.',
	                '..--..':'?', ".----.":"'", '-.-.-.':';', '---...':':', '-....-':'-', '.-..-.':'"', '-.--.':'(',
	                '-.--.-':')', '-.-.--':'!', '-..-.':'/', '.-...':'&', '-...-':'=', '.-.-.':'+'}
		#seperate into characters
		char = ''
		charList = []
		i = 0
		while i < len(cipher):
			if cipher[i] != ' ':
				char = char + cipher[i]
				if i == len(cipher)-1:
					charList.append(char)
			else:
				charList.append(char)
				char = ''
			i += 1

		#convert characters into plaintext
		for x in charList:
			if x == '/':
				plaintext = plaintext + ' '
			elif x in morseDict.keys():
				plaintext = plaintext + morseDict[x]
			else:
				plaintext = plaintext + x

	return(plaintext)


#main program
import os, sys, shutil
inFolder = sys.argv[1]
outFolder = sys.argv[2]
#seperate input folder into list of .txt files
with os.scandir(inFolder) as files:
    for file in files:
    	length = len(file.name)
    	#for each .txt file run function to find scores
    	if file.name[(length-3) : (length)] == 'txt':
    	 	plaintext = decrypt(file)
    	 	#write scores to a new file
    	 	newFile = file.name[0 : (length-4)] + '_z90677pp.txt'
    	 	with open(newFile, 'w') as f:
    	 		f.write(plaintext)
    	 		f.close()
    	 	#move file to output folder
    	 	shutil.move(newFile, outFolder)