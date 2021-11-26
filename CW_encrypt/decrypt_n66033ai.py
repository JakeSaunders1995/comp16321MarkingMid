import os, argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('input')
	parser.add_argument('output')
	args = parser.parse_args()
	for file in os.listdir(args.input):
		filepath = os.path.join(args.input, file)
		encryption = extractData(filepath)
		for i in range(len(encryption)):
			if encryption[i] == ':':
				method = encryption[0:i]
				decryptedText = encryption[i+1:len(encryption)]
				break
			# end if
		# end for
		text = ''
		if method == "Hex":
			decryptedText = decryptedText.strip()
			decryptedText = decryptedText.replace(' ', '')
			for i in range(len(decryptedText) // 2):
				if hexToDec(decryptedText[i*2:(i+1)*2]) >= 65 and hexToDec(decryptedText[i*2:(i+1)*2]) <= 90:
					text += chr(hexToDec(decryptedText[i*2:(i+1)*2]) + 32)
				else:
					text += chr(hexToDec(decryptedText[i*2:(i+1)*2]))
				# end if
			# end for
		elif method == "Morse Code":
			letterCounter = ''
			for i in range(len(decryptedText)):
				if decryptedText[i] == ' ':
					if letterCounter == '': continue
					text += morseCode(letterCounter)
					letterCounter = ''
				elif decryptedText[i] == '/':
					text += ' '
				else:
					letterCounter += decryptedText[i]
				# end if
			# end for
			text += morseCode(decryptedText[len(decryptedText)-1])
		else:
			text = caesar(decryptedText)
		# end if
		result = outputName(file)
		result = os.path.join(args.output, result)
		f = open(result, 'w')
		f.write(text)
		f.close()
		print(text)
	# end for
# end def

def extractData(file):
	f = open(file, 'r')
	code = f.read()
	f.close()
	return code
# end def

def hexToDec(hex):
	decimal = 0
	for i in range(len(hex)):
		if hex[i] == 'a':
			decimal += 10 * (16**(len(hex)-i-1))
		elif hex[i] == 'b':
			decimal += 11 * (16**(len(hex)-i-1))
		elif hex[i] == 'c':
			decimal += 12 * (16**(len(hex)-i-1))
		elif hex[i] == 'd':
			decimal += 13 * (16**(len(hex)-i-1))
		elif hex[i] == 'e':
			decimal += 14 * (16**(len(hex)-i-1))
		elif hex[i] == 'f':
			decimal += 15 * (16**(len(hex)-i-1))
		else:
			decimal += int(hex[i]) * (16**(len(hex)-i-1))
		# end if
	# end for
	return decimal
# end def

def morseCode(letter):
	if letter == '.-':
		return 'a'
	elif letter == '-...':
		return 'b'
	elif letter == '-.-.':
		return 'c'
	elif letter == '-..':
		return 'd'
	elif letter == '.':
		return 'e'
	elif letter == '..-.':
		return 'f'
	elif letter == '--.':
		return 'g'
	elif letter == '....':
		return 'h'
	elif letter == '..':
		return 'i'
	elif letter == '.---':
		return 'j'
	elif letter == '-.-':
		return 'k'
	elif letter == '.-..':
		return 'l'
	elif letter == '--':
		return 'm'
	elif letter == '-.':
		return 'n'
	elif letter == '---':
		return 'o'
	elif letter == '.--.':
		return 'p'
	elif letter == '--.-':
		return 'q'
	elif letter == '.-.':
		return 'r'
	elif letter == '...':
		return 's'
	elif letter == '-':
		return 't'
	elif letter == '..-':
		return 'u'
	elif letter == '...-':
		return 'v'
	elif letter == '.--':
		return 'w'
	elif letter == '-..-':
		return 'x'
	elif letter == '-.--':
		return 'y'
	elif letter == '--..':
		return 'z'
	elif letter == '.----':
		return '1'
	elif letter == '..---':
		return '3'
	elif letter == '...--':
		return '3'
	elif letter == '....-':
		return '4'
	elif letter == '.....':
		return '5'
	elif letter == '-....':
		return '6'
	elif letter == '--...':
		return '7'
	elif letter == '---..':
		return '8'
	elif letter == '----.':
		return '9'
	elif letter == '-----':
		return '0'
	# end if
# end def

def caesar(cipherText):
	plainText = ""
	for i in range(len(cipherText) - 1):
		if ord(cipherText[i]) >= 68 and ord(cipherText[i]) <= 90:
			plainText = ord(cipherText[i]) + 29
		elif ord(cipherText[i]) >= 65 and ord(cipherText[i]) <= 67:
			plainText = ord(cipherText[i]) + 55
		elif ord(cipherText[i]) < 100 and ord(cipherText[i]) >= 97:
			plainText += chr(ord(cipherText[i]) + 23)
		elif cipherText[i] == ' ':
			plainText += ' '
		else:
			plainText += chr(ord(cipherText[i]) - 3)
		# end if
	# end for
	return plainText
# end def

def outputName(file):
	firstHalf = file[:-4]
	output = firstHalf + "_n66033ai.txt"
	return output
# end def

main()