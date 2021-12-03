import sys
import os


folderInput = sys.argv[1]
folderOutput = sys.argv[2]





for folder in os.listdir(folderInput):
	files = os.path.join(folderInput, folder)
	if os.path.isfile(files):

		fileRead = open(files, 'r')

		fileName = os.path.basename(files)

		shortfileName = os.path.splitext(fileName)[0]

	
	
		
	
	if os.path.isdir(folderOutput):
		dirName = os.path.join(folderOutput, shortfileName + '_m83653ns.txt')
		fileNew = open(dirName, 'a+')
		data = fileRead.read()
		splitData = data.split(':', 1)
		message = splitData[1]
		sep = message.split()
		
		
			
		
		if "Hex" in data:
			for convertHex in sep:
				str1 = bytes.fromhex(convertHex)
				str1 = str1.decode('ascii')
				str1 = str1.lower()
				fileNew.write(str1)
			

		elif "Caesar" in data:
			for convertCC in message:
				cipherText = convertCC
				cipherTextPos = 0
				while cipherTextPos < len(cipherText):
					ciphertextChar = cipherText[cipherTextPos]
					ASCIIvalue = ord(ciphertextChar)
					if ASCIIvalue == 32:
						fileNew.write(" ")
						cipherTextPos += 1		
					elif ASCIIvalue == 99:
						ASCIIvalue = 122
						plainText = chr(ASCIIvalue)
						fileNew.write(plainText)
						cipherTextPos += 1
					elif ASCIIvalue == 98:
						ASCIIvalue = 121
						plainText = chr(ASCIIvalue)
						fileNew.write(plainText)
						cipherTextPos += 1
					elif ASCIIvalue == 97:
						ASCIIvalue = 120
						plainText = chr(ASCIIvalue)
						fileNew.write(plainText)
						cipherTextPos += 1
					else:
						ASCIIvalue -= 3
						plainText = chr(ASCIIvalue)
						fileNew.write(plainText)
						cipherTextPos += 1


		elif "Morse" in data:
			morseCode_Dict = { 
				'.-':'a', '-...':'b',
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
				'-.--.':'(', '-.--.-':')'
			}
			for convertMC in sep:
				if convertMC == '/':
					fileNew.write(" ")
				else:
					convertMC = morseCode_Dict[convertMC]
					fileNew.write(convertMC)	

	else:
		os.mkdir(folderOutput)


				
	
	
