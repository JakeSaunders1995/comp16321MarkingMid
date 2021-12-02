import sys
import os
input_folder = sys.argv[1]
output_folder= sys.argv[2]


def translate(parameter):
	thefirst_word=parameter.read(1)

	if thefirst_word=='H':
		while 1:

				information_inside=parameter.read()
				splitting=information_inside.partition(":")[2]
				in_bytes=bytes.fromhex(splitting)
				in_ascii=in_bytes.decode("ASCII")
				if not information_inside:
					break

				
				with open(output_file, 'w') as o:
					o.write(in_ascii.lower())

	if thefirst_word == 'C':
		while True:
			information_inside = parameter.read()
			splitting = information_inside.partition(":")[2]
			ciphertext = splitting
			plaintext = ""
			ciphertextPosition = 0

			while (ciphertextPosition < len(ciphertext)):
				ciphertextChar= ciphertext[ciphertextPosition]
				for idx, val in enumerate(ciphertextChar):
					if val.isalpha():
						if ciphertextChar in ("a", "b", "c"):
							Value_ACSII = ord(ciphertextChar)
							Value_ACSII = Value_ACSII + 23
							plaintext = plaintext + chr(Value_ACSII)
							ciphertextPosition = ciphertextPosition + 1
						else:
							Value_ACSII = ord(ciphertextChar)
							Value_ACSII = Value_ACSII - 3
							plaintext = plaintext + chr(Value_ACSII)
							ciphertextPosition = ciphertextPosition + 1

					else:
						plaintext = plaintext + val 
						ciphertextPosition = ciphertextPosition + 1
			

			if not information_inside:
				break 

			with open(output_file, "w") as f:
				f.write(plaintext.lower())



	if thefirst_word=='M':
		while 1:
			information_inside=parameter.read()
			splitting=information_inside.partition(":")[2]

			All_code = {
			    "A": ".-",
			    "B": "-...",
			    "C": "-.-.",
			    "D": "-..",
			    "E": ".",
			    "F": "..-.",
			    "G": "--.",
			    "H": "....",
			    "I": "..",
			    "J": ".---",
			    "K": "-.-",
			    "L": ".-..",
			    "M": "--",
			    "N": "-.",
			    "O": "---",
			    "P": ".--.",
			    "Q": "--.-",
			    "R": ".-.",
			    "S": "...",
			    "T": "-",
			    "U": "..-",
			    "V": "...-",
			    "W": ".--",
			    "X": "-..-",
			    "Y": "-.--",
			    "Z": "--..",
			    "1": ".----",
			    "2": "..---",
			    "3": "...--",
			    "4": "....-",
			    "5": ".....",
			    "6": "-....",
			    "7": "--...",
			    "8": "---..",
			    "9": "----.",
			    "0": "-----",
			    " ": "/"
			}

			def in_english(Parameter):
				blank = []
				for i in Parameter.split(' '):
					for english, morse in All_code.items():
						if morse == i:
							blank.append(english)
				return ''.join(blank)

			
			if not information_inside:
				break


			translating=in_english(splitting)

			with open(output_file, 'w') as o:
				o.write(translating.lower())

		




for filename in os.listdir(input_folder):
	if filename.endswith('.txt'):
		input_file=os.path.join(input_folder, filename)
		output_file=str(output_folder + "/" + filename[:10] + "_q89254rn" + filename[10:])
		with open(input_file, 'r') as i:
			files=i
			translate(files)
