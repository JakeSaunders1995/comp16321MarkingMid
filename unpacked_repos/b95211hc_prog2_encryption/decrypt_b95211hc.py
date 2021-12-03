import sys, os

cwd 		= os.getcwd()
inputDir 	= sys.argv[1]
outputDir   = sys.argv[2]

os.chdir(inputDir)

morseCode = [	'.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
				'..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
				'--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
				'-.--', '--..', '/']


def decode(cipher, text):
	plainText = ''
	if cipher == 'Hex':
		for element in text:
			element = int(element, 16)
			newLetter  = chr(element)
			plainText += newLetter

	elif cipher == 'Caesar Cipher(+3)':
		for element in text:
			for letter in element:
				newPos = ord(letter) - 3
				if 94 <= newPos < 97:
					newPos += 26
				elif 30 <= newPos < 33:
					newPos += 32
				newLetter = chr(newPos)
				plainText += newLetter
			plainText += ' '
	
	elif cipher == 'Morse Code':
		for element in text:
			pos = morseCode.index(element)
			letter = chr(pos + 97)
			if pos == 26:
				plainText += ' '
			else:
			    plainText += letter
	return plainText

outputList = []

for file in os.listdir():
	inFile = open(file, 'r')
	line = (inFile.read()).split(':')

	cipher = line[0]
	cipherText = (line[1].lower()).split()

	plainText = decode(cipher, cipherText) 

	outputList.append([(file.split('.'))[0], plainText])

os.chdir(cwd)
os.mkdir(outputDir)
os.chdir(outputDir)

for element in outputList:
	newFile = open(element[0] + '_b95211hc.txt', 'w')
	newFile.write(element[1])
	newFile.close()

	

