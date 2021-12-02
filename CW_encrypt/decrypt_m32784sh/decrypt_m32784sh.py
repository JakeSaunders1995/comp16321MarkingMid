import argparse, os

parser = argparse.ArgumentParser(description='Decypher Program')
parser.add_argument('input', help='Input file path')
parser.add_argument('output', help='Output file path')
args = parser.parse_args()

for file in os.listdir(str(args.input)):

	if file.endswith(".txt"):
		inputFile = open(os.path.join(args.input, file))
	else:
		continue

	inputString = inputFile.readline().rstrip('\n')
	method = inputString.split(':')[0]
	code = inputString.split(':')[1]

	if method == 'Hex':
		decryptedCode = bytearray.fromhex(code).decode()
	elif method == 'Caesar Cipher(+3)':
		decryptedCode = ''
		for i in range(len(code)):
			if code[i].isalpha():
				oldValue = ord(code[i])
				newValue = oldValue - 3
				if newValue < 65:
					newValue = 123 - (65 - newValue)
				elif 90 < newValue < 97:
					newValue = 91 - (97 - newValue)
				decryptedCode += chr(newValue)
			else:
				decryptedCode += code[i]


	else:
		morseDict = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E', '..-.':'F','--.':'G','....':'H',
		'..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
		'...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z','-----':'0','.----':'1',
		'..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9','.-.-.-':'.',
		'..-..':'?','-.-.--':'!','--..--':',', '---...':':', '-.-.-.':';','-....-':'-', '-.--.':'(', '-.--.-':')',
		'.----.':"'", '.-..-.':'"'}
		splitCodeList = code.split(' ')
		decryptedCode = ''
		for chracter in splitCodeList:
			if chracter == '/':
				decryptedCode += ' '
			elif chracter != '':
				decryptedCode += morseDict[chracter]


	decryptedCode = decryptedCode.lower()

	outputFile = open(os.path.join(args.output, file[0:-4] + '_m32784sh.txt'), 'x')
	outputFile.write(decryptedCode)