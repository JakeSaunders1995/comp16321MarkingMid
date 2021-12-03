import sys
import os

def decrypt(filename):
	input_file = input_folder + "/" + filename
	input_file = open(input_file,"r")
	output_file = filename[:-4]
	output_file = output_file+"_V55941np.txt"
	new_output_file = output_folder + "/" + output_file
	output_file = open(new_output_file,"w+")
	data = input_file.readlines()
	data = data[0]
	algorithm = ""
	colon_present = False
	x = 0
	while colon_present == False:
		if data[x] != ":":
			algorithm = algorithm + data[x]
		else:
			colon_present = True
		x+= 1

	string = ""

	if algorithm == "Hex":
		hex_string = ""
		for i in range(4,len(data)-1,3):
			hex_string = hex_string + data[i:i+2]
		string = bytearray.fromhex(hex_string).decode() #inbuilt function to convert hex
		string = string.lower()

	elif algorithm == "Morse Code": #0 represents a dot, 1 represents a dash
		characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9',',','.','?','"',':',"'",'-','/','(',')']
		codes = ['01','1000','1010','100','0','0010','110','0000','00','0111','101','0100','11','10','111','0110','1101','010','000','1','001','0001','011','1001','1011','1100','11111','01111','00111','00011','00001','00000','10000','11000','11100','11110','110011','010101','001100','010010','111000','011110','100001','10010','10110','101101']
		binary_to_character = []
		for i in range(0,len(characters)): #creates a 2d array of morse code to their decrypted form
			temp = []
			temp.append(characters[i])
			temp.append(codes[i])
			binary_to_character.append(temp)
		binary_string = ""
		for i in range(11,len(data)): #this changes each . to 0 and - to 1
			if data[i] == ".":
				binary_string = binary_string + "0"
			elif data[i] == "-":
				binary_string =binary_string + "1"
			else:
				binary_string = binary_string + data[i]

		binary_string_arr = []
		temp = []
		temp_string = ""
		for i in binary_string: #creates a 2d array of words with the letters being the morse code inside them
			if i == "0" or i == "1":
				temp_string = temp_string + i
			elif i == " " and len(temp_string) >0:
				temp.append(temp_string)
				temp_string = ""
			elif i == "/":
				binary_string_arr.append(temp)
				temp = []
		temp.append(temp_string)
		binary_string_arr.append(temp)

		word = ""
		for coded_word in binary_string_arr: #decodes the morse code and adds it to a string
			for coded_letter in coded_word:
				for code in binary_to_character:
					if code[1] == coded_letter:
						word = word + code[0]
			string = string + word + " "
			word = ""
		string = string[:-1] #removes the space at the end

	else:
		caesar_shift = ""
		x = 14
		bracket_found = False
		while bracket_found == False: #finds the starting character for the cipher text and also the caesar shift value
			if data[x] != ")":
				caesar_shift = caesar_shift + data[x]
			elif data[x] == ")":
				bracket_found = True
				position = x
			x += 1
		caesar_shift = int(caesar_shift)
		reverse_caesar_shift = caesar_shift *-1 #converts the caesar shift into reverse to easily decode
		for i in range(position+2,len(data)): #converts each ciphertext character to decoded forms
			if data[i] in alphabet:
				character_ascii = ord(data[i])
				character_ascii += reverse_caesar_shift
				if 97 <= character_ascii <= 122: #if the converted ciphertext character isnt in the alphabet changes so it would be
					character = chr(character_ascii)
				elif character_ascii < 97:
					difference = 97 - character_ascii
					character = chr(123-difference)
				elif character_ascii > 122:
					difference = character_ascii -122
					character = chr(96+difference)
				string = string + character
			else:
				string = string + data[i]
	output_file.write(string)

input_folder = sys.argv[1]
output_folder = sys.argv[2]
try: #will make a folder if there isnt one
	os.mkdir(output_folder)
except OSError as error:
	pass

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
arr = os.listdir(input_folder)
for i in range(0,len(arr)):
	decrypt(arr[i])
	
#command i used to test ignore
#python3 decrypt_V55941np.py ~/PythonStuff/Python_Midterm/midterm_files/Example_inputs/Example_inputs_program2 ~/PythonStuff/Python_Midterm/midterm_files/program2_outputs
