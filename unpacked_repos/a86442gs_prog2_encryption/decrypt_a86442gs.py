import sys
import os



input_directory = sys.argv[1]
file_list = os.listdir(input_directory)

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
					'(':'-.--.', ')':'-.--.-', " ":"/"}


n=0 
while n<= len(file_list)-1:
	plaintext=""

	test_file1= open(input_directory +"/" +file_list[n],"r")
	data = test_file1.read()
	test_file1.close()

	if data[0]== "C":
		a = "abcdefghijklmnopqrstuvwxyz "
		letter_to_index = dict(zip(a, range(len(a))))
		index_to_letter = dict(zip(range(len(a)), a))
		message = data.replace("Caesar Cipher(+3):", "")
		cipher=message
		def decrypt(cipher, shift=3):
			decrypted = ""

			for letter in cipher:
				try:
					number = (letter_to_index[letter] - shift) % len(letter_to_index)
					letter = index_to_letter[number]
					decrypted += letter

				except KeyError:
					pass

			return decrypted


		decrypted = decrypt(cipher, shift=3)
		decrypted1=decrypted.replace("y", "x")
		decrypted1=decrypted1.replace("z", "y")
		decrypted1=decrypted1.replace(" ","z")
		decrypted1=decrypted1.replace("x", " ")

		plaintext = decrypted1

	elif data[0]=="H":
		file = data.replace("Hex:", "")
		encryptAscii = bytearray.fromhex(file).decode()
		encryptAscii = encryptAscii.lower()
		plaintext = encryptAscii

	elif data[0]=="M":

		def decrypt(message):

			message += ' '

			decipher = ''
			citext = ''
			for letter in message:
				if (letter != ' '):
					i = 0
					citext += letter
				else:
					i += 1
					if i == 2 :
						decipher += ' '
					else:
						decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
						citext = ''

			return decipher


		message =data
		message1=message.replace("Morse Code:", "")
		result = decrypt(message1)
		plaintext =result.lower()



	filename =str(file_list[n]).replace(".txt", "")
	output_directory =sys.argv[2]
	output_file =open(output_directory +"/"+filename+"a86442gs.txt", "w")
	output_file.write(plaintext)
	output_file.close()

	n+=1