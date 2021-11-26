import argparse
import os

# argparse
parser = argparse.ArgumentParser(description="Encryption")
parser.add_argument('DecryptIndir', type=str, help='Input dir for decrypt')
parser.add_argument('DecryptOutdir', type=str, help='Output dir for decrypt')

args, unknown = parser.parse_known_args()

path = os.path.abspath(args.DecryptIndir)
outputPath = os.path.abspath(args.DecryptOutdir)

for filename in os.listdir(path):
	if filename.endswith(".txt"):
		f = open(os.path.join(path, filename), 'r')
		ciphertext = f.read()
		# print(ciphertext)
		x = filename.replace(".txt","_y67506st.txt")
		outputFolder = os.path.join(outputPath, x)

		substringH = 'Hex:'
		substringC = 'Caesar Cipher(+3):'
		substringM = 'Morse Code:'

		if substringH in ciphertext:
			HexCipher = ciphertext[4:].replace(" ","")
			# print(HexCipher)
			HexPlain = bytes.fromhex(HexCipher).decode('utf-8')

			f = open(outputFolder, "w")
			f.write(
			HexPlain.lower()
			)
			f.close()		

		if substringC in ciphertext:
			CaesarCipher = ciphertext[18:]
			# print(CaesarCipher)

			CaesarAlpha = "abcdefghijklmnopqrstuvwxyz"
			CaesarPlain = ""

			for letter in CaesarCipher:
				if letter in CaesarAlpha:
					letter_index = (CaesarAlpha.find(letter)-3) % len(CaesarAlpha)
					CaesarPlain = CaesarPlain + CaesarAlpha[letter_index]
				else:
					CaesarPlain = CaesarPlain + letter

			f = open(outputFolder, "w")
			f.write(
			CaesarPlain.lower()
			)
			f.close()	

		if substringM in ciphertext:
			MorseCipher = ciphertext[11:]
			def morse(message):
				MorseEncrypt = {'A': '.-',     'B': '-...',   'C': '-.-.', 
								        'D': '-..',    'E': '.',      'F': '..-.',
								        'G': '--.',    'H': '....',   'I': '..',
								        'J': '.---',   'K': '-.-',    'L': '.-..',
								        'M': '--',     'N': '-.',     'O': '---',
								        'P': '.--.',   'Q': '--.-',   'R': '.-.',
								        'S': '...',    'T': '-',      'U': '..-',
								        'V': '...-',   'W': '.--',    'X': '-..-',
								        'Y': '-.--',   'Z': '--..',

								        '0': '-----',  '1': '.----',  '2': '..---',
								        '3': '...--',  '4': '....-',  '5': '.....',
								        '6': '-....',  '7': '--...',  '8': '---..',
								        '9': '----.', 

								        ',':'--..--', 	'.':'.-.-.-',	'?':'..--..',
								        '/':'-..-.', 		'-':'-....-',	'(':'-.--.', 
								        ')':'-.--.-',		' ':'/',			'@':'.--.-.',
								        '&':'.-...',		'+':'.-.-.',	'=':'-...-',
								        '"':'.-..-.',		'!':'-.-.--'
						       }
				MorseDecrypt = {value: key for key,value in MorseEncrypt.items()}
				
				if '-' in message:
					# message is Morse Code
					return ''.join(MorseDecrypt[i] for i in message.split(" "))
				# return print("Not Morse Code")

			f = open(outputFolder, "w")
			f.write(
			morse(MorseCipher).lower()
			)
			f.close()
		

   

