import argparse	
import os


parser = argparse.ArgumentParser()
parser.add_argument("first")
parser.add_argument("last")
args = parser.parse_args()

files = os.scandir(args.first) 

if not os.path.isdir(args.last):
	os.mkdir(args.last)


for element in files:

	with open(element.path, 'r') as myfile:
	    cipher = myfile.read()
	    

	if cipher[0] == "H":
	  	hex1 = cipher[cipher.index(":")+1:]
	  	hex1 = hex1.replace(" ", "")
	  	cipher_hex = bytearray.fromhex(hex1)
	  	hexadecimal = cipher_hex.decode("ASCII")
	
	elif cipher[0] == "C":
		caesar1 = cipher[cipher.index(":")+1:]
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		caesar_temp_string = ""
		for x in caesar1:
			if x in alphabet:
				index = alphabet.find(x) 
				y = alphabet[index-3]
				caesar_temp_string += y
			else:
				caesar_temp_string += x
		
	elif cipher[0] == "M":
		morse1 = cipher[cipher.index(":")+1:]
		morse1 = morse1.split(" ")

		morse_dict = {'-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '/': " "}
		morse_temp_string = ""
		for x in morse1:
			morse_temp_string += morse_dict.get(x)

			

	output_name = element.name.split(".")[0]
	output_name = output_name + "_h18603tp.txt"

	os.path.join(args.last, output_name)
	with open(os.path.join(args.last, output_name), 'w+') as myfile:
		if cipher[0] == "H":
			myfile.write(hexadecimal)
		elif cipher[0] == "C":
			myfile.write(caesar_temp_string)
		elif cipher[0] == "M":
			myfile.write(morse_temp_string)
