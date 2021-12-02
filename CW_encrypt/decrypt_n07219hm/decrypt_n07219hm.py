from sys import argv
from os import listdir
#defines variables and global dictionaries

input_folder_path = argv[1]
output_folder_path = argv[2]

username = "n07219hm"

global caesar_dictionary
caesar_dictionary = {
	"d" : "a",
	"e" : "b",
	"f" : "c",
	"g" : "d",
	"h" : "e",
	"i" : "f",
	"j" : "g",
	"k" : "h",
	"l" : "i",
	"m" : "j",
	"n" : "k",
	"o" : "l",
	"p" : "m",
	"q" : "n",
	"r" : "o",
	"s" : "p",
	"t" : "q",
	"u" : "r",
	"v" : "s",
	"w" : "t",
	"x" : "u",
	"y" : "v",
	"z" : "w",
	"a" : "x",
	"b" : "y",
	"c" : "z",
}

global morse_dictionary
morse_dictionary = {
	'.-':'a', 
	'-...':'b',
    '-.-.':'c', 
    '-..':'d', 
    '.':'e',
    '..-.':'f', 
    '--.':'g', 
    '....':'h',
    '..':'i', 
    '.---':'j', 
    '-.-':'k',
    '.-..':'l', 
    '--':'m', 
    '-.':'n',
    '---':'o', 
    '.--.':'p', 
    '--.-':'q',
    '.-.':'r', 
    '...':'s', 
    '-':'t',
    '..-':'u', 
    '...-':'v', 
    '.--':'w',
    '-..-':'x', 
    '-.--':'y', 
    '--..':'z',
    '.----':'1', 
    '..---':'2', 
    '...--':'3',
    '....-':'4', 
    '.....':'5', 
    '-....':'6',
    '--...':'7', 
    '---..':'8', 
    '----.':'9',
    '-----':'0', 
    '--..--':',', 
    '.-.-.-':'.',
    '..--..':'?', 
    '-..-.':'/', 
    '-....-':'-',
    '-.--.':'(', 
    '-.--.-':')'
}


# Function takes input file path as input and reads the file and splits it into the algorithm name and the ciphertext 
def read_text_file(path):
	input_file = open(path,"r")
	input_file_string = input_file.read().lower()
	input_file.close()
	global list_of_split_string
	list_of_split_string = input_file_string.split(":")
	
# Function takes the output file path and the plaintext then writes it to the output file
def write_output_to_file(path,plaintext):
	output_file = open(path,"w")
	output_file.write(plaintext)
	output_file.close()


#decrypts hex
def hex_decrypt():
	hex_string = list_of_split_string[1]
	hex_string_bytes = bytes.fromhex(hex_string)
	hex_plaintext = hex_string_bytes.decode("ASCII").lower()
	return hex_plaintext


#decrypts caesar
def caesar_decrypt():
	caesar_string = list_of_split_string[1].lower()
	plaintext_list = []
	for character in caesar_string:
		if character in caesar_dictionary.keys():
			plaintext_list.append(caesar_dictionary[character])
		else:
			plaintext_list.append(character)
	
	caesar_plaintext = "".join(plaintext_list).lower()
	return caesar_plaintext


#decrypts morse code
def morse_decrypt():
	morse_string = list_of_split_string[1]
	morse_word_list = morse_string.split(" / ")
	
	plaintext_letter_list = []

	for i in range(0,len(morse_word_list)):
		
		morse_letter_list = morse_word_list[i].split(" ")
		
		for letter in morse_letter_list:
			plaintext_letter_list.append(morse_dictionary[letter])
		plaintext_letter_list.append(" ")
		
	morse_plaintext = "".join(plaintext_letter_list)
	return morse_plaintext



#Function identifies which encryption method has been used and calls the appropriate function
def which_encryption_method():
	
	if list_of_split_string[0] == "hex":
		
		return hex_decrypt()
	elif list_of_split_string[0] == "morse code":
		
		return morse_decrypt()
	elif list_of_split_string[0] == "caesar cipher(+3)":
		return caesar_decrypt()
	else:
		print("invalid algorithm")





#Looping through files
file_list = listdir(input_folder_path)
output_file_list = []
for file in file_list:
	output_file_list.append(file[:-4] + "_" + username + ".txt")

for i in range(0,len(file_list)):

	output_file_path = output_folder_path + output_file_list[i] 
	read_text_file(input_folder_path + file_list[i])
	#print(which_encryption_method())
	write_output_to_file(output_file_path, which_encryption_method())
	

