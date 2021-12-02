import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("folder", type = str, nargs = "+")
args = parser.parse_args()
folders = args.folder
files = os.listdir(folders[0])

#Defining a dictionary for morse code:
morselegend_dict = {".-": 'a', "-...": 'b', "-.-.": 'c', "-..": 'd', ".": 'e', "..-.": 'f', "--.": 'g', "....": 'h', "..": 'i', ".---": 'j', "-.-": 'k', ".-..": 'l', "--": 'm', "-.": 'n', "---": 'o', ".--.": 'p', "--.-": 'q', ".-.": 'r', "...": 's', "-": 't', "..-": 'u', "...-": 'v', ".--": 'w', "-..-": 'x', "-.--": 'y', "--..": 'z', "/": " ", " ": "/"}

for file in files:
	f =open(folders[0] + "/" + file, 'r')

	input_Str = f.read()
	
	#Decoding Hex:

	#Checking if input is Hexadecimal in nature:
	if input_Str[0] == 'H':
		#Isolating relevant input:
		hex_inputStr = input_Str[4:]
		hex1 = bytes.fromhex(hex_inputStr)
		dec = hex1.decode("ASCII")
		print(dec)

	#Decoding Morse:
	#Checking if input is a Morse Code:
	elif input_Str[0] == "M":
		#Isolating relevant input
		morse_input = input_Str[11:]
		dec = ""
		split_morse = morse_input.split(' ')
	#[Mapping Morse letters to letters of the english alphabet using Dictionary "morselegend_dict"]
		for morse_code in split_morse:
				dec += morselegend_dict[morse_code]
		print(dec)

	#Decoding Caeser:
	elif input_Str[0] == "C":
		Caeser_Str = input_Str[18:]
		dec = ""
		Caeser_StrPosition = 0
		encrypt = "xyzabcdefghijklmnopqrstuvwxyz"
		len_str = len(Caeser_Str)
		dec += " "

		for a in range(0,len_str):
			char = Caeser_Str[a]
			if char ==" ":
				dec +=" "
				continue
			for b in range(3,len(encrypt)):
				if char == encrypt[b]:
					decryptchar = encrypt[b-3]
					dec+=decryptchar
				else:
					pass
			
		print(dec)

	

	f.close()
	ind = file.index(".")
	f_name = file[0:ind]
	o = open(folders[1] + "/" + f_name + '_j96158ap.txt', 'w')

	o.write(dec)

	o.close()














