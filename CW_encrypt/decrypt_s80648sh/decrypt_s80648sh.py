import sys 
import re
import os

def decryption(input_file,output_folder):
	

	def get_message():

		file = open(input_file)
		message = file.readline()
		file.close()
		print(message)
		return message

	def determine_cipher(message):
		if message[0] == "Hex":
			cipher = 0
		elif "Caesar Cipher" in message[0]:
			cipher = 1
		else:
			cipher = 2
		return cipher

	def decrypt_hex(message):
		print("Decrypting Hex")
		print(message)
		formatted_message = message.replace(" ","")
		decrypted_message = bytearray.fromhex(formatted_message).decode()
		return decrypted_message
		
	def decrypt_caesar(full_message):
		steps = full_message[0].replace("Caesar Cipher","").replace("(","")
		steps = steps.replace(")","")
		steps = int(steps)

		encrypted = full_message[1]
		print(encrypted)
		decrypted = ""
		ASCII = []
		for char in encrypted:
			ASCII.append(ord(char))
		print(ASCII, "\n")

		new_ASCII = []
		for i in range(len(ASCII)):
			if ASCII[i] != 32: #If not equal to space
				new_ASCII.append(ASCII[i] - steps)
			else:
				new_ASCII.append(ASCII[i])
		
		print(new_ASCII)

		for char in new_ASCII:
			decrypted = decrypted + chr(char)
		return decrypted

	def decrypt_morse(message):
		letters = message.split(" ")
		decrypted_message = ""
		
		morse_values = { 
			'A': '.-',   'B': '-...',
	        'C': '-.-.', 'D': '-..', 
	        'E': '.',    'F': '..-.', 
	        'G': '--.',  'H': '....',
	        'I': '..',   'J': '.---', 
	        'K': '-.-',  'L': '.-..', 
	        'M': '--',   'N': '-.',
	        'O': '---',  'P': '.--.', 
	        'Q': '--.-', 'R': '.-.',
	        'S': '...',  'T': '-',
	        'U': '..-',  'V': '...-', 
	        'W': '.--',  'X': '-..-', 
	        'Y': '-.--', 'Z': '--..',
	        '1': '.----', '2':'..---', '3':'...--',
	        '4': '....-', '5':'.....', '6':'-....',
	        '7': '--...', '8':'---..', '9':'----.',
	        '0': '-----', ', ':'--..--', '.':'.-.-.-',
	        '?': '..--..', ' ': '/', #Space
	    }
	    
		for i in range (0,len(letters)):
			for name,code in morse_values.items():
				if code == letters[i]:
					decrypted_message = decrypted_message + name
					continue
		decrypted_message = decrypted_message.lower()
		return decrypted_message

	def output(decrypted_message):
		output_path = input_file.replace(".txt","")
		output_path = output_path.replace("./Example_inputs_program2","")
		output_path = output_path + "_s80648sh.txt"
		output_path = (output_folder + output_path).replace("//","/")

		file = open(output_path,"a")
		file.write(f"{decrypted_message}\n")
		file.close()

		


	message = get_message()
	split_message = message.split(":")
	cipher = determine_cipher(split_message)


	if cipher == 0:
		decrypted_message = decrypt_hex(split_message[1])
	elif cipher == 1:
		decrypted_message = decrypt_caesar(split_message)
	else:
		decrypted_message = decrypt_morse(split_message[1])

	output(decrypted_message)


input_folder = sys.argv[1]
output_folder= sys.argv[2]

input_files = os.listdir(input_folder)
input_files.sort()

print(input_files)

for i in range(0,len(input_files)):
	decryption(input_folder + "/" + input_files[i],output_folder)
