import argparse, os

def Encrypted(Text):
	Encrypted_text= Text.split(':')[1]

	if Text.split(':')[0] == 'Caesar Cipher(+3)' :
		alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
		plaintext = ''
		for cipherTextChar in Encrypted_text.strip():
			if cipherTextChar == ' ':
				plaintext = plaintext + cipherTextChar
			else:
				alphabetPosition = 3
				while cipherTextChar != alphabet[alphabetPosition]:
					alphabetPosition +=1
				alphabetPosition = alphabetPosition - 3
				plaintext = plaintext + alphabet[alphabetPosition]
		print(plaintext)
		return plaintext

	elif Text.split(':')[0] == 'Morse Code':
		MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
	                    'C':'-.-.', 'D':'-..', 'E':'.',
	                    'F':'..-.', 'G':'--.', 'H':'....',
	                    'I':'..', 'J':'.---', 'K':'-.-',
	                    'L':'.-..', 'M':'--', 'N':'-.',
	                    'O':'---', 'P':'.--.', 'Q':'--.-',
	                    'R':'.-.', 'S':'...', 'T':'-',
	                    'U':'..-', 'V':'...-', 'W':'.--',
	                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
	                    '1':'.----', '2':'..---', '3':'...--',
	                    '4':'....-', '5':'.....', '6':'-....',
	                    '7':'--...', '8':'---..', '9':'----.',
	                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
	                    '?':'..--..', '/':'-..-.', '-':'-....-',
	                    '(':'-.--.', ')':'-.--.-', ' ':'/'}

		decrypt = { value: key for key,value in MORSE_CODE_DICT.items()}
		plaintext = ''
		if Encrypted_text == '/':
			plaintext = plaintext + ' '
		else:
			plaintext = ''.join(decrypt[i] for i in Encrypted_text.split() )
		
		print(plaintext.lower())
		return plaintext.lower()

	elif Text.split(':')[0] == 'Hex':
		_hex = Encrypted_text
		plaintext = ''
		if _hex == ' ' :
			plaintext += ' '
		else:
			to_bytes = bytes.fromhex(_hex)
			string = to_bytes.decode("ASCII")
			plaintext += string

		print(plaintext)
		return plaintext.lower()


parser = argparse.ArgumentParser(description = "decryption of 3 types")
parser.add_argument('input', help='the input directory')
parser.add_argument('output', help='the output directory')
args = parser.parse_args()


path = args.input
path_output = args.output

for file in os.listdir(path):
	with open(path+"/"+file, 'r') as f:
		with open(path_output + "/" + file.replace(".txt","_m46198.txt"),"w") as n:
			n.write(Encrypted(f.read()))
			
			
