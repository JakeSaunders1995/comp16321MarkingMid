import os
import sys 

#Declaring variables and morse dictionary

folderIn = sys.argv[1]
folderOut = sys.argv[2]
file_number = 0
encrypt_list = []
current_file = 0

#morse dictionary from online
morsedictionary = {'A': '.-', 'B': '-...','C': '-.-.', 'D': '-..', 'E': '.','F': '..-.', 'G': '--.', 'H': '....','I': '..', 'J': '.---', 'K': '-.-','L': '.-..', 'M': '--', 'N': '-.','O': '---', 'P': '.--.', 'Q': '--.-','R': '.-.', 'S': '...', 'T': '-','U': '..-', 'V': '...-', 'W': '.--','X': '-..-', 'Y': '-.--', 'Z': '--..','1': '.----', '2': '..---', '3': '...--','4': '....-', '5': '.....', '6': '-....','7': '--...', '8': '---..', '9': '----.','0': '-----', ', ': '--..--', '.': '.-.-.-','?': '..--..', '/': '-..-.', '-': '-....-','(': '-.--.', ')': '-.--.-'}

#Inputting the folder with encrypted text
for filename in sorted(os.listdir(folderIn)):
	file_number += 1
	with open(os.path.join(folderIn, filename), 'r') as f:
		all_encrypt = f.read().rstrip()
		encrypt_list.append(all_encrypt)

#The decryptions
for string in encrypt_list:
	current_file += 1

	#Decrypting Hexadecimal
	if "Hex" in string:
		hexEncrypt = string.replace("Hex:", "")
		hexDecrypt = bytes.fromhex(hexEncrypt).decode('utf-8')
		hexDecrypt = hexDecrypt.lower()

		output_name = "test_file" + str(current_file) + "_b16225mz"
		output = open(folderOut+"/"+output_name+".txt", "w")
		output.write(hexDecrypt)

	#Decrypting Caesar Cipher	
	elif "Caesar Cipher" in string:
		caesarEncrypt = string.replace("Caesar Cipher(+3):", "")
		CaesarToText = ""
		for character in caesarEncrypt:
			if character == " ":
				CaesarToText += " "
			elif character.lower() < "d":
				CaesarToText += chr(ord(character) + 23)
			else:
				CaesarToText += chr(ord(character) - 3)

			output_name = "test_file" + str(current_file) + "_b16225mz"
			output = open(folderOut+"/"+output_name+".txt", "w")
			output.write(CaesarToText)  

	#Decrypting Morse Code	
	elif "Morse Code" in string:
		morseEncrypt = string.replace("Morse Code:", "")
		morseEncrypt = morseEncrypt.split()
		morseDecrypt = ""
		for morse in morseEncrypt:
			if morse in morsedictionary.values():
				morseDecrypt += (list(morsedictionary.keys())[list(morsedictionary.values()).index(morse)])
			elif morse == "/":
				morseDecrypt += " "
			morseDecrypt = morseDecrypt.lower()

			output_name = "test_file" + str(current_file) + "_b16225mz"
			output = open(folderOut+"/"+output_name+".txt", "w")
			output.write(morseDecrypt)










   












