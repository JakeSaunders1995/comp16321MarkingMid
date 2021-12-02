# - Imports -
import sys
from os import listdir
from os.path import isfile, join

# - Global inputs -
input_folder = sys.argv[1]
test_files = [file for file in listdir(input_folder) if isfile(join(input_folder, file)) and file[0] != '.']

# - Global dictionnary -
morse_to_eng = {
    '.-':'a', '-...':'b',
    '-.-.':'c', '-..':'d', '.':'e',
    '..-.':'f', '--.':'g', '....':'h',
    '..':'i', '.---':'j', '-.-':'k',
    '.-..':'l', '--':'m', '-.':'n',
    '---':'o', '.--.':'p', '--.-':'q',
    '.-.':'r', '...':'s', '-':'t',
    '..-':'u', '...-':'v', '.--':'w',
    '-..-':'x', '-.--':'y', '--..':'z',
    '.----':'1', '..---':'2', '...--':'3',
    '....-':'4', '.....':'5', '-....':'6',
    '--...':'7', '---..':'8', '----.':'9',
    '-----':'0', '--..--':',', '.-.-.-':'.',
    '..--..':'?', '-..-.':'/', '-....-':'-',
    '-.--.':'(', '-.--.-':')', '/' : ' '
}



# - Main functions -
def hexadecimal(text):
	# Recursion end condition:
	if len(text) == 2: return chr(int(text, 16)).lower()
	# Recursion call and instruction (addition):
	return chr(int(text[:2], 16)).lower() + hexadecimal(text[3:])

def morse(text):
	return "".join([morse_to_eng[code] for code in text.split()])

def ceasared_character(character, alphabet):
	return alphabet[(ord(character.lower()) % ord('a')) - 3]

def ceasar(text):
	alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
	final = ["".join([ceasared_character(letter, alphabet) if letter.lower() in alphabet else letter for letter in word]) for word in text.split()]
	return " ".join(final)

def answer(instruction):
	cut_index = instruction.index(':')
	details = {'algorithm' : instruction[:cut_index], 'sentence' : instruction[cut_index+1:]}
	if details['algorithm'] == 'Hex':
		return hexadecimal(details['sentence'])
	elif details['algorithm'] == 'Morse Code':
		return morse(details['sentence'])
	else:
		return ceasar(details['sentence'])



# - Outputs -
for file in test_files:
	input_file = open(f"{input_folder}/{file}")
	
	instruction = input_file.readline()
	decrypted = answer(instruction)

	output_folder = sys.argv[2]
	output_file = open(f"{output_folder}/{file[:-4]}_n61655sb.txt", "w")
	output_file.write(decrypted)

	input_file.close()
	output_file.close()

