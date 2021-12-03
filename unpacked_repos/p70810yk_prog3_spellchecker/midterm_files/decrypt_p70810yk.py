import sys
import os.path
import os
filenumber = ""
inputpath = sys.argv[1]
filelist = os.listdir(inputpath)
for file in filelist:
	f = open(inputpath+"/"+file)
	message = f.readline()

	morse_code_dict = {".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f","--.":"g","....":"h","..":"i",".---":"j","-.-":"k",".-..":"l","--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r","...":"s","-":"t","..-":"u","...-":"v",".--":"w","-..-":"x","-.--":"y","--..":"z","/":" "}

	def hex_decrpyt(message):
		decrypted_message = str()
		number_of_char = int((len(message) - 3) / 3)
		for x in range(number_of_char):
			encrypted_char = message[3*x+4:3*x+6]
			ASCII_char = int(encrypted_char,16)
			if ASCII_char > 64 and ASCII_char <91:
				ASCII_char +=32
			char = chr(ASCII_char)
			decrypted_message += char
		return(decrypted_message)

	def caesar_decrpyt(message):
		decrypted_message = str()
		number_of_char = int((len(message) - 18))
		for x in range(number_of_char):
			encrypted_char = message[x+18]
			encrypted_ASCII = ord(encrypted_char)
			if encrypted_char != " ":
				encrypted_ASCII -=3
				encrypted_char = chr(encrypted_ASCII)
			decrypted_message += str(encrypted_char)
		return(decrypted_message)

	def morse_decrpyt(message):
		decrypted_message = str()
		encrypted_code = message.split(":")
		encrypted_word_list = encrypted_code[1].split(" ")
		for x in encrypted_word_list:
			encrypted_word = morse_code_dict.get(x)
			decrypted_message += str(encrypted_word)
		return(decrypted_message)

	if message[0] == "H":
		decrypted_message = hex_decrpyt(message)
	elif message[0] == "C":
		decrypted_message = caesar_decrpyt(message)
	elif message[0] == "M" :
		decrypted_message = morse_decrpyt(message)

	outputpath = sys.argv[2]
	outputfile = file.split(".")
	output = open(outputpath+outputfile[0]+"_p70810yk.txt","x")
	output.write(decrypted_message)
	filenumber = ""
