import os
import argparse
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("put_in_file", help="enter a file")
	parser.add_argument("put_out_file", help="enter a file")
args = parser.parse_args()
input_file = args.put_in_file
for j in os.listdir(input_file):
	text_pos = j.find('.txt')
	input_file_heading = j[0:text_pos]
	file = open(f'{args.put_in_file}/{j}', 'r')
	transfer = []
	for line in file:
		line = line.rstrip()
	transfer.append(line)
	cipher_temp = transfer[0]
	cipher=cipher_temp.lower()
	cipher_type = None
	semicolon_position = cipher.find(':')
	main_cipher = cipher[semicolon_position+1:]
	decipher = ''


	# Cipher Type
	if cipher[0] == "m":
		cipher_type = "Morse Code"
	elif cipher[0] == "c":
		cipher_type = "Caesar's Cipher(+3)"
	elif cipher[0] == "h":
		cipher_type = "Hexadecimal"


	# Caesar's Cipher
	if cipher_type == "Caesar's Cipher(+3)":
		ciphertext=main_cipher
		plaintext=""
		alphabet="XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC".lower()
		ciphertextposition=0
		while ciphertextposition<len(ciphertext):
			ciphertextchar=ciphertext[ciphertextposition]
			alphabetposition=3
			if ciphertextchar != ' ':
				while ciphertextchar != alphabet[alphabetposition]:
					alphabetposition+=1
				alphabetposition = alphabetposition - 3
				plaintext = plaintext + alphabet[alphabetposition]
				ciphertextposition += 1
			else:
				plaintext = plaintext + ' '
				ciphertextposition += 1
		decipher = plaintext


	# Hexadecimal
	elif cipher_type == "Hexadecimal":
		cipherhex = main_cipher
		a = bytes.fromhex(cipherhex)
		b = a.decode("ASCII")
		decipher = b


	# Morse Code
	elif cipher_type == "Morse Code":
		cipher_morse = ".... --- .-- . ...- . .-. / ... --- .-.. ...- .. -. --. / -- --- .-. ... . / -.-. --- -.. . / -- .- -.-- / -... . / - .... . / -- --- ... - / -.. .. ..-. ..-. .. -.-. ..- .-.. -"
		morse_dict = {'....' : 'h', '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '}
		cipher_words = cipher_morse.split(' ')
		dict_words = morse_dict.keys()
		phrase=''
		word_number = 0
		for i in cipher_words:
			if i in dict_words:
				phrase += morse_dict[cipher_words[word_number]]
				word_number += 1
		decipher = phrase
	#print(decipher.lower())

	line = [decipher.lower()]
	with open(os.path.join(args.put_out_file, f'{input_file_heading}_b26193dm.txt'), 'w') as f:
		f.writelines(line)