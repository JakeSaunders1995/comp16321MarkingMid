import argparse 
import re

parser = argparse.ArgumentParser(description='encryption')
parser.add_argument('input', type=str, help='input file path')
parser.add_argument('output', type=str, help='output file path')
args = parser.parse_args()
def writeresult(outputpath):
	f = open(outputpath,'w')
	f.write(plaintext)
	f.close

f = open(args.input)
lines=f.read()
f.close


MorseCode = {'a':'.-', 'b':'-...',
				'c':'-.-.', 'd':'-..', 'e':'.',
				'f':'..-.', 'g':'--.', 'h':'....',
				'i':'..', 'j':'.---', 'k':'-.-',
				'l':'.-..', 'm':'--', 'n':'-.',
				'o':'---', 'p':'.--.', 'q':'--.-',
				'r':'.-.', 's':'...', 't':'-',
				'u':'..-', 'v':'...-', 'w':'.--',
				'x':'-..-', 'y':'-.--', 'z':'--..',
				'1':'.----', '2':'..---', '3':'...--',
				'4':'....-', '5':'.....', '6':'-....',
				'7':'--...', '8':'---..', '9':'----.',
				'0':'-----', '.':'.-.-.-', '?':'..--..',
				'!':'-.--.', '(':'-.--.', '@':'.--.-.',
				':':'---...', '=':'-...-', '-':'-....-',
				')':'-.--.-', '+':'.-.-.', ',':'--..--',
				"'":'.----.', '_':'..--.-', '$':'...-..-',
				';':'-.-.-.', '/':'-..-.', '"':'.-..-.',
				'&':'....'
				}


if re.match('hex',lines,flags=re.I):
	ciphertext=re.findall('\d+\D',lines)
	plaintext = ''
	ciphertextPosition = 0
	while (ciphertextPosition < len(ciphertext)):
		ciphertextChar = ciphertext[ciphertextPosition]
		plaintext += chr(int(ciphertextChar,16))
		ciphertextPosition += 1 
	print (plaintext)

	
elif re.match('caesar',lines,flags=re.I):
	ciphertext=re.findall('(?<=:).*$',lines)
	plaintext = ''
	alphabet = 'xyzabcdefghijklmnopqrstuvwxyzabc'
	ciphertextPosition = 0 
	while (ciphertextPosition < len(ciphertext[0])):
		ciphertextChar = ciphertext[0][ciphertextPosition]
		alphabetPosition = 3
		if ciphertextChar == ' ':
			plaintext += ' '
			ciphertextPosition+=1
		elif ciphertextChar in alphabet:	
			while ciphertextChar != alphabet[alphabetPosition]:
				alphabetPosition +=1

			alphabetPosition -= 3 
			plaintext += alphabet[alphabetPosition]
			ciphertextPosition+=1
		else:			
			plaintext += ciphertextChar
			ciphertextPosition+=1
	print(plaintext)

	
elif re.match('morse',lines,flags=re.I):
	ciphertext=re.findall('(?<=:).*$',lines)
	ciphertext[0] += ' '
	plaintext=''
	ciphertextChar=''
	i = 0
	while i < len(ciphertext[0]):
		if (ciphertext[0][i] ==' '):
			i +=1
			plaintext += list(MorseCode.keys())[list(MorseCode.values()).index(ciphertextChar)]
			ciphertextChar = ''
		elif (ciphertext[0][i] =='/'):
			i +=2
			plaintext += " "
		elif (ciphertext[0][i] != ' ' and '/'):
		# else:
			ciphertextChar += ciphertext[0][i]
			i+=1
	print(plaintext)
writeresult(args.output)



		

