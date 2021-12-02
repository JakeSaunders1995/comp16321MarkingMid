import argparse

parser = argparse.ArgumentParser(description = "Descryption")
parser.add_argument('inputpath')
parser.add_argument('onputpath')
path = parser.parse_args()
inputPath = path.inputpath
outputPath = path.onputpath
inputStream = open(inputPath, "r")
inputContent = inputStream.read()

morseDic = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e',
			'..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j',
			'-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o',
			'.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t', 
			'..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y', 
			'--..':'z', '-----':'0', '.----':'1', '..---':'2', '...--':'3', 
			'....-':'4', '.....':'5', '-....':'6', '--...':'7', '---..':'8', 
			'----.':'9', '.-.-.-':'.', '---...':':', '--..--':',', '-.-.-.':';', 
			'..--..':'?', '-...-':'=', '.----.':'\'', '-..-.':'/', '-.-.--':'!', 
			'-....-':'-', '..--.-':'_', '.-..-.':'"', '-.--.':'(', '-.--.-':')', 
			'...-..-':'$', '.-...':'&', '.--.-.':'@', '.-.-.':'+', '/': ' '}

def morseDecrypt(cipherText):
	cipherList = cipherText.split(' ')
	cipherLen = len(cipherList)
	plainText = ''
	for i in cipherList:
		plainText += morseDic[i]
	return plainText

def caesarDecrypt(cipherText):
	plainText = ''
	for i in cipherText:
		if i == ' ':
			plainText += ' '
		else:
			plainText += chr(ord(i) - 3) 
	return plainText

def hexDecrypt(cipherText):
	cipherList = cipherText.split(' ')
	cipherLen = len(cipherList)
	plainText = ''
	for i in cipherList:
		plainText += chr(int(i,16))
	return plainText

if inputContent[0] == 'M':
	cipherText = inputContent[11:]
	outputContent = morseDecrypt(cipherText)
elif inputContent[0] == 'C':
	cipherText = inputContent[18:]
	outputContent = caesarDecrypt(cipherText)
elif inputContent[0] == 'H':
	cipherText = inputContent[4:]
	outputContent = hexDecrypt(cipherText)

outputStream = open(outputPath, "w")
outputStream.write(outputContent)
