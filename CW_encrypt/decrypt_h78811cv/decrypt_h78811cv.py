import sys, os

def get_contents(file):
	colon = file.find(":")
	contents = file[colon+1:len(file)]
	contents_list = contents.split()
	return contents_list

def hex(file, plaintext):
	i = 0 
	contents_list = get_contents(file)
	while i <= len(contents_list)-1:
		denary = int(contents_list[i],16)
		ascii_character = chr(denary)
		plaintext += ascii_character
		i += 1
	return plaintext

def caesar(file, alphabet, plaintext):
	n = 0
	contents_list = get_contents(file)
	while n <= len(contents_list)-1:
		i = 0
		while i <= len(contents_list[n])-1:
			if contents_list[n] in punctuation:
				plaintext += contents_list[n]
			else:
				ciphertext_char_location = alphabet.find(contents_list[n][i])
				plaintext_char_location = ciphertext_char_location - 3
				if plaintext_char_location == -1:
					plaintext_char = alphabet[plaintext_char_location:]
				elif plaintext_char_location < -1:
					plaintext_char = alphabet[plaintext_char_location:plaintext_char_location+1]
				else:
					plaintext_char = alphabet[plaintext_char_location]
				plaintext += plaintext_char
			i += 1

		plaintext += " " 
		n+=1
	return plaintext

def morseCode(file, plaintext, morse_code_dict):
	contents_list = get_contents(file)
	i = 0
	while i <= len(contents_list)-1:
		if contents_list[i] == "/":
			plaintext += " "
		else:
			plaintext += morse_code_dict[contents_list[i]]
		i += 1
	return plaintext

punctuation = "!():;{[]'},./?-"
alphabet = "abcdefghijklmnopqrstuvwxyz"
morse_code_dict = {
	'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f',
	'--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l',
	'--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r',
	'...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x',
	'-.--':'y', '--..':'z', '-----': '0', '.----':'1', '..---':'2',
	'...--':'3', '....-': '4', '.....':'5', '-....':'6', '--...':'7',
	'---..':'8', '----.':'9', '.-.-.-':'.', '--..--':',', '..--..':'?',
	'-.-.-.':';', '---...':':', '-....-':'-', '-..-.':'/', '.----.':"'",
	'.-..-.':'"', '-.--.':'(', '-.--.-': ')' 
}

input_directory = sys.argv[1]
file_list = os.listdir(input_directory)

n = 0
while n <= len(file_list)-1:

	plaintext = ""

	test_file1 = open(input_directory+"/"+file_list[n], "r")
	file = test_file1.read()
	test_file1.close()

	if file[0] == "H":
		plaintext = hex(file, plaintext)
	elif file[0] == "C":
		plaintext = caesar(file, alphabet, plaintext)
	elif file[0] == "M":
		plaintext = morseCode(file, plaintext, morse_code_dict)

	filename = str(file_list[n]).replace(".txt", "")
	ouput_directory = sys.argv[2]
	output_file = open(ouput_directory+"/"+filename+"_h78811cv.txt", "w")
	output_file.write(plaintext.lower())
	output_file.close()

	n += 1
