import argparse
import os

def encryptionType(cipher_text):
	type = ""
	for i in cipher_text:
		if i == ":":
			break
		else: 
			type += i
	if type == "Hex":
		hexadecimal(cipher_text)
	elif type == "Caesar Cipher(+3)":
		caesar(cipher_text)
	elif type == "Morse Code":
		morseCode(cipher_text)

def morseCode(cipher_text):
	cipher_text = cipher_text.replace("Morse Code:","")
	Morse_dictionary = {
    	".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
    	"....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
    	"---": "O", ".--．": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    	"..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",

    	"-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    	".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

    	".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
    	"-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
    	"..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
    	".--.-.": "@", ".-.-.": "+",
	}

	Morse_text = ""
	cipher_text = cipher_text.split()
	
	for i in cipher_text:
		results = Morse_dictionary.get(i, 0)
		Morse_text += str(results)

	for i in Morse_text:
		if 65<=ord(i)<=90:
			Morse_text = Morse_text.replace(i,chr(ord(i)+32))
		elif i == "0":
			Morse_text = Morse_text.replace("0"," ")

	f1.write(Morse_text)

def caesar(cipher_text):
	cipher_text = cipher_text.replace("Caesar Cipher(+3):","")
	decrypted_text = ""
	for i in cipher_text:
		if 68<=ord(i)<=90:
			decrypted_text += chr(ord(i)+32-3)
		elif 100<=ord(i)<=122:
			decrypted_text += chr(ord(i)-3)
		elif i == "c" or i == "C":
			decrypted_text += "z"
		elif i == "b" or i == "B":
			decrypted_text += "y"
		elif i == "a" or i == "A":
			decrypted_text += "x"
		elif i == " ":
			decrypted_text += i

	f1.write(decrypted_text)

def hexadecimal(cipher_text):
	cipher_text = cipher_text.replace("Hex:","")
	hex_text = str(bytearray.fromhex(cipher_text))
	hex_text = hex_text.replace("bytearray(b'","")
	hex_text = hex_text.replace("')","")

	for i in hex_text:
		if 65<=ord(i)<=90:
			hex_text = hex_text.replace(i,chr(ord(i)+32))
	
	f1.write(hex_text)

parser = argparse.ArgumentParser(description='input the txt files')
parser.add_argument("input_file",type=str)
parser.add_argument("output_file",type=str)
args = parser.parse_args()
input_path = args.input_file
output_path = args.output_file

os.chdir(input_path)
files = os.listdir(input_path)
files.sort()
file_count = 1
for file in files:
	with open(file,"r+") as f:
		content = f.readlines()
		f.close()
	cipher_text = content[0]
	
	os.chdir(output_path)
	file_name = "test_file" + str(file_count) +"_v79907sy.txt"
	with open(file_name, "w") as f1:
		final_text = encryptionType(cipher_text)
		f1.close()
	file_count += 1
	os.chdir(input_path)