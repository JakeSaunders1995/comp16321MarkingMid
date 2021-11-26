import sys
import os

#input1 = "/home/csimage/www/midterm_files"(5)"/midterm_files/Example_inputs/Example_inputs_program2"
#output1 = "/home/csimage/www/midterm_files"(5)"/midterm_files/Example_outputs/Example_outputs_program2"

input1 = sys.argv[1]
output1 = sys.argv[2]

dir_list = os.listdir(input1)
cwd = os.getcwd()
input1 = input1.replace(cwd+"/","")
output1 = output1.replace(cwd+"/","")

def encryption_method(input_file):
	if example_input[0] == "C":
		#print("We are using Caesar Cipher")
		return (decrypt_Caesar(example_input))

	elif example_input[0] == "H":
		#print("We are using Hexadecimal")
		return(decrypt_Hexadecimal(example_input))

	elif example_input[0] == "M":
		#print("We are using Morse Code")
		return(decrypt_MorseCode(example_input))

def decrypt_Caesar(input_file):
	alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
	ciphertext = example_input[18:len(example_input)]
	ciphertext = ciphertext.lower()
	#exw fdhvdu lv d olwwoh pruh gliilfxow hvshfldoob li brx gr lw lq d crr
	#print(ciphertext)
	plaintext = ""
	ciphertextPosition = 0
	while ciphertextPosition < len(ciphertext)-1:
		if ciphertext[ciphertextPosition] == " ":
			plaintext = plaintext + " "
			#print(plaintext)
			ciphertextPosition += 1
		else:	
			ciphertextChar = ciphertext[ciphertextPosition]
			#ASCIIValue = GetASCIIValue(ciphertextChar)
			alphabetPosition = 3
			while ciphertextChar != alphabet[alphabetPosition]:
				alphabetPosition += 1
				#print(alphabetPosition)
				#if alphabetPosition >= 31:
					#alphabetPosition = 0
			alphabetPosition -= 3
			#ASCIIValue = ord(ciphertextChar)
			#ASCIIValue_Cipher = ASCIIValue - 3
			#CharValue_Cipher = chr(ASCIIValue_Cipher)
			plaintext = plaintext + str(alphabet[alphabetPosition])
			#print(plaintext)
			#plaintext = plaintext + CharValue_Cipher
			ciphertextPosition += 1	
	return(plaintext)

def decrypt_Hexadecimal(input_file):
	ciphertext = example_input[4:len(example_input)]
	plaintext = bytearray.fromhex(ciphertext).decode()
	plaintext = plaintext.lower()
	return(plaintext)

def decrypt_MorseCode(input_file):
	MorseCode_Dictionary = {"...." : 'h', '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '}

	ciphertext_input = example_input[11:len(example_input)]
	ciphertext_input = ciphertext_input.lower()
	ciphertext_input += " "
	plaintext = ""
	ciphertext = ""
	for char in ciphertext_input:
		if char != " ":
			i=0
			ciphertext += char
		else:
			i +=1
			if i == 2:
				plaintext += " "
			else:
				plaintext += MorseCode_Dictionary.get(ciphertext)
				ciphertext = ""

	return(plaintext)

for files in range(len(dir_list)):
 	file_to_check = input1+"/"+dir_list[files]
 	file = open(file_to_check)
 	example_input = file.read()
 	file.close()
 	decrypted = encryption_method(example_input)
 	#print(decrypted)
 	output_file = dir_list[files].replace(".txt","_d52553je")
 	output_file = output_file+".txt"
 	file_to_write = output1+"/"+output_file
 	file = open(file_to_write, "w")
 	file.write(decrypted)
 	file.close()
